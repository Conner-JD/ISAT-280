from jnius import autoclass
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

PythonActivity = autoclass('org.renpy.android.PythonActivity')
activity = PythonActivity.mActivity

Activity=autoclass('android.app.Activity')
vibrator = activity.getSystemService(Activity.VIBRATOR_SERVICE)
conn_mgr = autoclass('android.net.ConnectivityManager')

class FloatLayoutWidget(Widget):
	def __init__(self, **kwargs):
		super(FloatLayoutWidget,self).__init__(**kwargs)
		layout = FloatLayout(size=(300, 300))

class AndroidApp(App):
	#def build(self):
	#	vibrator.vibrate(1000)

	def __init__(self, **kwargs):
		super(AndroidApp,self).__init__(**kwargs)

	def build(self, *args, **kwargs):
		print "I am here."
		return FloatLayoutWidget()

	def check_connectivity(self):
		self.con_mgr = activity.getSystemService(Activity.CONNECTIVITY_SERVICE)
		self.conn = self.con_mgr.getNetworkInfo(conn_mgr.TYPE_WIFI).isConnectedOrConnecting()

		if self.conn:
			print "it's up"
			return "it's up"
		else:
			print 'it is down'
			return "it's down"

if __name__=="__main__":
	AndroidApp().run()
