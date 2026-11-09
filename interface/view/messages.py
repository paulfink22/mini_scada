from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

class Message (Console):
	def __init__(self)-> None:
		super().__init__()
	def show_message(self, caption: str, message: str, fgColor: str, bgColor: str)-> None:
		header: str=f"[{fgColor} on {bgColor}]{caption}[/{fgColor} on {bgColor}]"
		content: str=f"[{bgColor} on {fgColor}]{message}[/{bgColor} on {fgColor}]"
		self.clear()
		panel: Panel=Panel(content, title=header, border_style=bgColor)
		self.print(panel)
	def show_prompt(self, caption: str, fgColor: str, bgColor: str)-> str:
		header: str=f"[{fgColor} on {bgColor}]{caption}[/{fgColor} on {bgColor}]"
		result: str=Prompt.ask(header)
		return result
	def show_confirm(self, caption: str, fgColor: str, bgColor: str)-> bool:
		header: str=f"[{fgColor} on {bgColor}]{caption}[/{fgColor} on {bgColor}]"
		result: bool=Confirm.ask(header)
		return result
