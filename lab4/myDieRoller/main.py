from kivy.app import App
from kivy.uix.widget import Widget

class DieRoller(Widget):
	pass

class DieRollerApp(App):
	def build(self):
		return DieRoller()

if __name__ == "__main__":
	DieRollerApp().run()
