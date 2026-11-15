from interface.view.messages import Message

def check_loop(func):
	def wrapper(*arg, **kwarg):
		while True:
			if func(arg[0]):
				if arg[0].show_confirm("Сохранить изменения?", "blue", "white"):
					break
	return wrapper

class Setup (Message):
	def __init__(self)-> None:
		super().__init__()
		self.connection_data: dict=dict()
		self.connection_data["baudrate"]: int=9600
		self.connection_data["parity"]: str="even"
		self.connection_data["port"]: str="dev/ttyUSB0"
		self.connection_data["byte_size"]: int=8
		self.connection_data["stop_bits"]: int=1
		self.connection_data["timeout"]: int=5
		self.connection_data["id"]: int=10
	def show_wellcome(self)-> None:
		caption: str="Панель мониторинга КНС КАТУНЬ 1.0"
		content: str="Чтобы приступить к работе, настройте необходимые параметры соединения\nили примите по умолчанию"
		self.show_message(caption, content, "white", "red")
	def default_settings(self)-> bool:
		result: bool=False
		caption: str="Принять настройки по умолчанию?"
		if self.show_confirm(caption, "white", "blue"):
			result=True
		return result
	def verify_int(self, value: int)-> bool:
		is_integer: bool=True
		try:
			int(value)
		except ValueError:
			is_integer=False
		finally:
			return is_integer
	@check_loop
	def set_port(self)-> bool:
		default_values: list[str]=["COM1", "COM2", "COM3", "/dev/ttyUSB0", "/dev/ttyUSB0", "/dev/ttyUSB2", "/dev/ttyUSB3", "/dev/ttyUSB4"]
		result: bool=False
		port: str=str()
		caption: str="Порт"
		content: str="""
Введите порт.
-В системе Windows это СОМn,
-в Linux /dev/ttyUSBn, 
где n номер порта по порядку.
ВНИМАНИЕ! Порт не может быть числом!
"""
		content_error: str="""Введено false значение!
		Повторить (n) или принять СОМ3 по умолчанию? (y)"""
		self.show_message(caption, content, "white", "blue")
		port=self.show_prompt("Порт:", "white", "blue")
		if port in default_values:
			self.connection_data["port"]=port
			result=True
		else:
			if self.show_confirm(content_error, "white", "red"):
				result=True
		return result

	@check_loop
	def set_parity(self)->bool:
		default_values: list[str]=["none", "even", "odd"]
		result: bool=False
		caption: str="Введите чётность"
		content: str="""
Введите чётность, которая указана
в настройках контроллера.
ВНИМАНИЕ! Чётность не может быть числом и имеет следующие значения:
- none
- even
- odd
"""
		content_error: str="Введено неверное значение. Повторить (n) или принять значение EVEN по умолчанию (у) "
		self.show_message(caption, content, "white", "blue")
		port: str=self.show_prompt("Чётность:", "white", "blue")
		if port in default_values:
			self.connection_data["parity"]=port
			result=True
		else:
			if self.show_confirm(content_error, "white", "red"):
				result=True
		return result

	@check_loop
	def set_baudrate(self)->bool:
		default_values: list[int]=[1200, 2400, 4800, 9600, 19200, 38400, 57600]
		result: bool=False
		caption: str="Количесво бод"
		content: str="""
Введите корректное количество бод, указанное в настройках контроллера.
Стандартные значения бод:
- 1200;
- 2400;
- 4800;
- 9600(рекомендуется);
- 19200;
- 38400;
- 57600.
"""
		content_error:str ="Введено неверное значение. Повторить (n) или принять 9600 по умолчанию (y) "
		self.show_message(caption, content, "white", "blue")
		baudrate: str=self.show_prompt("Количество бод ", "white", "blue")
		if baudrate in default_values:
			self.connection_data["baudrate"]=baudrate
			result=True
		else:
			if self.show_confirm(content_error, "white", "red"):
				result=True
		return result

	def input_settings(self)-> None:
		self.set_port(self)
		self.set_parity(self)
		self.set_baudrate(self)

	def setup_connection(self)-> dict:
		self.show_wellcome()
		if not self.default_settings():
			self.input_settings()
		return self.connection_data
