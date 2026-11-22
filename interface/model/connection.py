from pymodbus.client import ModbusSerialClient

class ModbusConnection (ModbusSerialClient):
	def __init__(self, port: str, baudrate: int, bytesize: int, parity: str, stopbits: int, timeout: int, device_id: int)->None:
		super().__init__(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits, timeout=timeout)
		self.device_id: int=device_id
		self.is_connected: bool=False
	def get_holding_registers(self)->list:
		pass
	def get_data(self)->int:
		result: int=0
		if not self.connected:
			if self.is_connected:
				self.is_connected=False
			if self.connect():
				self.is_connected=True
			else:
				result=1
		return result
