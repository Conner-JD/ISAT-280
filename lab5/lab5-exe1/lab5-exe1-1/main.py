
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty

from plyer import vibrator

Builder.load_string('''
#:import vibrator plyer.vibrator
<VibrationInterface>:
    orientation: 'vertical'
    Label:
        size_hint_y: None
        height: sp(40)
        text: 'vibrator exists: ' + str(vibrator.exists())
    Button:
        text: 'vibrate 10s'
        on_release: vibrator.vibrate(10)
    Button:
        text: 'vibrate 1s'
        on_release: vibrator.vibrate(1)
    Button:
        text: 'vibrate 0.1s'
        on_release: vibrator.vibrate(0.1)
    Button:
        text: 'cancel vibration'
        on_release: vibrator.cancel()
    TextInput:
        id: ti
        text: '0.5,0.5,1,2,0.1,0.1,0.1,0.1,0.1,0.1'
    Button:
        text: 'vibrate pattern'
        on_release:
            vibrator.pattern([float(n) for n in ti.text.split(',')],repeat=5)

''')


class VibrationInterface(BoxLayout):
    pass


class VibrationApp(App):
    
    title = 'Vibrator'

    def __init__(self, **kwargs):
        super(VibrationApp,self).__init__(**kwargs)

    def build(self):
        return VibrationInterface()

    def on_pause(self):
        return True


if __name__ == "__main__":
    VibrationApp().run()
