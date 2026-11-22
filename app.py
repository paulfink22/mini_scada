from interface.model.setup import Setup
from interface.model.connection import ModbusConnection

config_system: Setup=Setup()
config_system.setup_connection()
connection: ModbusConnection=ModbusConnection(config_system.connection_data["port"], config_system.connection_data["baudrate"], config_system.connection_data["byte_size"], config_system.connection_data["parity"], config_system.connection_data["stop_bits"], config_system.connection_data["timeout"], config_system.connection_data["id"])
if connection.get_data()==1:
	print("Connection failed")

