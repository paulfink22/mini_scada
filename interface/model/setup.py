from interface.view.messages import Message

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
	def set_port(self)-> str:
		port: str=str()
		caption: str="Порт"
		content: str="""
Введите порт.
-В системе Windows это СОМn,
-в Linux dev/ttyUSBn, 
где n номер порта по порядку.
ВНИМАНИЕ! Порт не может быть числом!
"""
		content_confirm: str="""Введено числовое значение!
		Повторить (у) или принять СОМ3 по умолчанию?"""
		while True:
			self.show_message(caption, content, "white", "blue")
			port=self.show_prompt("Порт:", "white", "blue")
			if self.verify_int(port):
				if self.show_confirm(content_confirm, "white", "red"):
					continue
				else:
					port=self.connection_data["port"]
					break
			if self.show_confirm("Сохранить ввод?", "blue", "white"):
				break
		return port

	def input_settings(self)-> None:
		self.connection_data["port"]=self.set_port()
		self.connection_data["parity"]=self.show_prompt("Parity (even/odd/none):", "white", "blue")
		self.connection_data["baudrate"]=self.show_prompt("Baudrate (9600/19200/38400/57600):", "white", "blue")
		self.connection_data["byte_size"]=self.show_prompt("Byte size (7/8):", "white", "blue")
		self.connection_data["stop_bits"]=self.show_prompt("Stop bits:", "white", "blue")
	def setup_connection(self)-> dict:
		self.show_wellcome()
		if not self.default_settings():
			self.input_settings()
		return self.connection_data
