from pymodbus.client import ModbusSerialClient

class ModbusConnection (ModbusSerialClient):
	def __init__(self, _port: str, _baudrate: int, bytesize: int, parity: str, stopbits: int, timeout: int, device_id: int)->None:
		super().__init__(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits, timeout=timeout)
		self.device_id: int=device_id
	def test_connection(self)->int:
		pass
