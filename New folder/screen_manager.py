from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
#from screen_manager import * 
from kivy.core.window import Window
from kivy.uix.image import Image
import time


class MainApp(MDApp):
    def build(self):
      Window.size = (375, 667)
      self.theme_cls.theme_style = "Light"
      self.theme_cls.primary_palette = "Teal"
      self.theme_cls.primary_hue = "500"

      return Builder.load_file("new.kv")

class ScreenMain(Screen):
  pass

class ScreenInstruction(Screen):
  pass

class ScreenRecent(Screen):
  pass

class ScreenAbout(Screen):
  pass

class ScreenConsole(Screen):
  pass

class WindowManager(ScreenManager):
  pass

if __name__ == '__main__':
    MainApp().run()