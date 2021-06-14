from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    new_drawer= ObjectProperty()

class Test(MDApp):
    def build(self):
        return Builder.load_file('tasker.kv')


Test().run()