from kivy.app import App
from kivy.core.audio import SoundLoader 

class HelloWorldApp(App):
    flag= False
    def play_music(self):
        if HelloWorldApp.flag is False or self.sound.status is 'stop':
            self.sound=SoundLoader.load('Jesse_Cook-Dance_Of_Spring.ogg')
            self.sound.play()
            HelloWorldApp.flag=True

    def stop_music(self):
        self.sound.stop()
        self.root.text="Ready to Play Again"

    def control_volume(self,volume):
        if self.sound.state is 'play':
            self.sound.volume=volume

    def control_volume(self,volume):
        if self.sound.state is 'play':
            self.sound.volume=volume

if __name__ == "__main__":
	HelloWorldApp().run()
	


