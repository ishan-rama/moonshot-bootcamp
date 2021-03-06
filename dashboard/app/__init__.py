
from kivy.app import App
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp
from pyrsistent import v

from .view import MainWindow


class MainApp(App):
    colors = QueryDict()
    colors.primary = rgba("#2D9CDB")
    colors.secondary = rgba("#16213E")
    colors.success = rgba("#1FC98E")
    colors.warning = rgba("#F2C94C")
    colors.danger = rgba("#EB5757")

    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)

    fonts.heading = 'assets/fonts//Roboto/Roboto-Bold.ttf'
    fonts.subheading = 'assets/fonts/Roboto/Roboto-Regular.ttf'
    fonts.body = 'assets/fonts/Roboto/Roboto-Light.ttf'

    def build(self):
        return MainWindow()
