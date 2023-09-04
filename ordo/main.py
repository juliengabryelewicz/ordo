from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.logger import Logger
from kivy.lang import Builder

from functools import partial
import os.path
import os

from plugin import PluginList
from check import check_install

plugin_directories = [
    os.path.normpath('plugins')
]


class OrdoBox(BoxLayout):
    def __init__(self, **kwargs):
        super(OrdoBox, self).__init__(**kwargs)
        self.orientation="horizontal"
        self.bind(minimum_height=self.setter('height'))
        self.plugins_list=PluginList(plugin_directories)
        self.plugins_list.find_plugins()
        self.sm = ScreenManager()
        self.parameters = JsonStore("parameters/ordo.json")

        self.config_screen()

        menu = GridLayout(cols=1, spacing=1, size_hint_y=None)
        menu.bind(minimum_height=menu.setter('height'))
        for plugin in self.parameters.get("plugins"):
            if plugin in self.plugins_list._plugins:
                Builder.load_file("plugins/"+plugin+"/"+plugin+".kv")
                plugin_object = self.plugins_list._plugins[plugin].plugin_class
                main_screen = plugin_object.get_main_screen()
                for screen in plugin_object.get_screens():
                    self.sm.add_widget(screen)
                btn = Button(text=self.plugins_list._plugins[plugin].name, size_hint_y=None, height=40)
                btn.bind(on_press=partial(self.change_screen, main_screen.name))
                menu.add_widget(btn)
            else:
                Logger.info('plugin '+plugin+' not found')

        scroll = ScrollView(pos_hint={'top':1},size_hint=(0.2, None), size=(self.parameters.get("width"), self.parameters.get("height")))
        scroll.add_widget(menu)
        self.add_widget(scroll)
        self.add_widget(self.sm)

    def change_screen(self,screen,instance):
        self.sm.current=str(screen)

    def config_screen(self):
        Config.set('graphics','show_cursor',self.parameters.get("show_cursor"))
        Config.set('graphics', 'resizable', self.parameters.get("resizable"))
        Config.set('graphics', 'fullscreen', self.parameters.get("fullscreen"))
        Config.set('graphics', 'width', self.parameters.get("width"))
        Config.set('graphics', 'height', self.parameters.get("height"))
        Config.write()

class Ordo(App):
    def build(self):
        return OrdoBox()

if __name__ == "__main__":
    Ordo().run()