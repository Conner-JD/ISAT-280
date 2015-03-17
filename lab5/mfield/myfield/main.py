# File name: floatlayout.py

from kivy.lang import Builder 
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from kivy.utils import platform

class FloatLayoutWidget(FloatLayout):
	def __init__(self, *args, **kwargs):
		super(FloatLayoutWidget, self).__init__(*args, **kwargs)
		text1 = self.ids['button1']
		text2 = self.ids['label1']
		text1.text='Hello'
		text1.font_size=40
		text2.text='World!'

class FloatLayoutApp(App):
	title = 'Magnetic Sensor'
	def __init__(self, **kwargs):
		super(FloatLayoutApp,self).__init__(**kwargs)
		if platform() == 'android':
			from jnius import autoclass
			Hardware = autoclass('org.renpy.android.Hardware')
			self.hw = Hardware()
			self.hw.magneticFieldSensorEnable(False)
		else:
			self.hw = None

	def build(self):
		Clock.schedule_interval(self.update_compass,0.1)		
		return FloatLayoutWidget()

	def update_compass(self,*args):
		if self.hw is None:
			return
		cur = self.hw.magneticFieldSensorReading()
		hell = self.root.ids['label1']
		hell.font_size=35
		hell.text= str(cur)

	def on_pause(self):
		# when you are going on pause, don't forget to stop the $
		if self.hw is None:
			return
		self.hw.magneticFieldSensorEnable(False)
		return True

	def on_resume(self):
		# reactivate the sensor when you are back to the app
		if self.hw is None:
			return
		self.hw.magneticFieldSensorEnable(True)


if __name__=="__main__":
   FloatLayoutApp().run()
