from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.utils import platform
from plyer import gps

class FloatLayoutWidget(FloatLayout):
	def __init__(self, *args, **kwargs):
		super(FloatLayoutWidget, self).__init__(*args, **kwargs)

		text1 = self.ids['button1']
		text2 = self.ids['label1']
		text3 = self.ids['label2']

		text1.text='Hello'
		text1.font_size=40
		text2.text='World!'
		text3.text= 'I am waiting!'

class FloatLayoutApp(App):

	title = 'gps'
	gps_location = StringProperty()

	def __init__(self, **kwargs):
		super(FloatLayoutApp,self).__init__(**kwargs)
                self.gps=gps
                self.gps.configure(on_location=self.on_locations)

	def on_locations(self, **kwargs):
		self.gps_location = 'lat:{lat}\nlon: {lon}'.format(**kwargs)


	def build(self):
		return FloatLayoutWidget()

	def change_button_text(self,*args, **kwargs):
		text1=self.root.ids['button1']
		text2=self.root.ids['label1']

		if text1.text=='Hello':
			text1.text='World!'
			text2.text='Hello'
		else:
			text1.text='Hello'
			text2.text='World!'
 
if __name__=="__main__":
   FloatLayoutApp().run()
