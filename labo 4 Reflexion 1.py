from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.popup import Popup


def fahrenheit2celsius(tf):
    return (tf - 32) * 5/9


def celsius2fahrenheit(tc):
    return ((9/5) * tc) + 32


class temperaturechanger(App):
    def build(self):
        self.title = 'Temperature Converter 0.1'
        self.__celsius = TextInput()
        butplus = Button(text='to f')
        butplus.bind(on_press=self._toF)
        grid = GridLayout(rows=2, cols=3)
        grid.add_widget(Label(text='Celsius'))
        grid.add_widget(self.__celsius)
        grid.add_widget(butplus)

        self.__fahrenheit = TextInput()
        butmoins = Button(text='to c')
        butmoins.bind(on_press=self._toC)
        grid.add_widget(Label(text='Fahrenheit'))
        grid.add_widget(self.__fahrenheit)
        grid.add_widget(butmoins)

        return grid

    @property
    def celsius(self):
        self.__celsius

    @property
    def fahrenheit(self):
        self.__fahrenheit

    def _toF(self,source):
        c = self.__celsius.text
        try:
            celsius = float(c)
            tempff = celsius2fahrenheit(celsius)
            self.__fahrenheit.text = str(tempff)
        except:
            popup = Popup(title="Attention", content=Label(text="La température est invalide."))
            popup.open()
            Clock.schedule_once(lambda d: popup.dismiss(), 3)

    def _toC(self,source):
        f = self.__fahrenheit.text
        try:
            fahrenheit = float(f)
            tempfc = fahrenheit2celsius(fahrenheit)
            self.__celsius.text = str(tempfc)
        except:
            popup = Popup(title="Attention", content=Label(text="La température est invalide."))
            popup.open()
            Clock.schedule_once(lambda d: popup.dismiss(), 3)


Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '100')


temperaturechanger().run()
