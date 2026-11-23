from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
import time

class ModbusConnection (ModbusSerialClient):
	def __init__(self, port: str, baudrate: int, bytesize: int, parity: str, stopbits: int, timeout: int, device_id: int)->None:
		super().__init__(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits, timeout=timeout)
		self.device_id: int=device_id
		self.is_connected: bool=False
	def get_holding_registers(self)->list:
		pass
	def check_connection(self, timeout: int)->bool:
		if self.connected:
			return True
		self.close()
		time.sleep(timeout)
		try:
			return bool(self.connect())
		except (OSError, ModbusException):
			self.close()
	def get_data(self)->int:
		result: int=0
		if self.check_connection(2):
			self.get_holding_registers()
		else:
			return 1
		return result
