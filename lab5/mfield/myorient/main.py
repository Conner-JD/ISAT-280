from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
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
                text2.font_size=50

class FloatLayoutApp(App):

	title = 'orientation'

	def __init__(self, **kwargs):
		super(FloatLayoutApp,self).__init__(**kwargs)
		if platform() == 'android':
			from jnius import autoclass
			Hardware = autoclass('org.renpy.android.Hardware')
			self.hw = Hardware()
			self.hw.orientationSensorEnable(True)
		else:
			self.hw = None
			print "I'm here!"


	def build(self):
		Clock.schedule_interval(self.check_orientation,0.5)		
		return FloatLayoutWidget()

	def check_orientation(self,dt):
		if self.hw is None:
			return
		cur = self.hw.orientationSensorReading()
		hell = self.root.ids['label1']
		hell.font_size=30
		hell.text= str(cur)


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
