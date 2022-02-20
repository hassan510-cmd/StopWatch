from kivy.app import App
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.config import Config

from time import strftime


# Window.borderless = True
class ImageButton(ButtonBehavior, Image):
    pass


class StopwatchScreen(Screen):
    pass


class ClockScreen(Screen):
    pass


class MainApp(App):
    is_start = False
    sw_second = 0

    def update_time(self, nap):
        if self.is_start:
            self.sw_second += nap
        self.root.ids['clock_screen'].ids['time'].text = strftime(
            '[b]%H[/b]:%M:%S')
        m, s = divmod(self.sw_second, 60)
        self.root.ids['stopwatch_screen'].ids['stopwatch'].text = (
                    '%2d : %2d.[size=40]%2d[/size]' % (
            int(m), int(s), int(s * 100 % 1000)))

    def on_start(self):
        print(self.root_window.size[1])
        Clock.schedule_interval(self.update_time, 0)

    def go_forward(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'stopwatch_screen'

    def go_back(self):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'clock_screen'

    def start_stop(self):
        self.root.ids['stopwatch_screen'].ids[
            'start_stop'].text = 'start' if self.is_start else 'stop'
        self.is_start = not self.is_start

    def reset(self):
        if self.is_start:
            self.root.ids['stopwatch_screen'].ids['start_stop'].text = 'start'
            self.is_start = False
        self.sw_second = 0


if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    Window.clearcolor = get_color_from_hex('#121212')
    LabelBase.register(name='Robot', fn_regular='Roboto-Thin.ttf',
                       fn_bold='Roboto-Medium.ttf')

    MainApp().run()

