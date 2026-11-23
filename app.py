from interface.model.setup import Setup
from interface.model.connection import ModbusConnection
from interface.view.messages import Message

main_messages: Message=Message()

config_system: Setup=Setup()
config_system.setup_connection()
connection: ModbusConnection=ModbusConnection(config_system.connection_data["port"], config_system.connection_data["baudrate"], config_system.connection_data["byte_size"], config_system.connection_data["parity"], config_system.connection_data["stop_bits"], config_system.connection_data["timeout"], config_system.connection_data["id"])
if connection.get_data()==1:
	main_messages.show_message("ERROR", "Device disconnected!", "red", "white")

