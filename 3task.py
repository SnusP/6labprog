from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from datetime import datetime
from fpdf import FPDF
import gspread,os,glob,webbrowser,PyPDF2
class Application(App):
    def build(self):
        Window.clearcolor = (16 / 255, 71 / 255, 140 / 255, 0);
        self.grid = GridLayout(cols=1, padding=[30], spacing=10)
        self.grid.add_widget(Label(text = "Выберете файл для открытия",font_size = 30))
        global a,i,buttons
        os.chdir('C:/Users/SnusP/PycharmProjects/prog2.1/Lab-6')
        for i in glob.glob("*.pdf"):
            a.append(i)
        print(a)
        for i in a:
            global c
            self.add_button(i)
        return self.grid
    def go(self,a):
        global flag
        if flag == True:
            return webbrowser.open(a)
    def add_button(self,i):
        global flag
        flag = False
        c = Button(text=f"{str(i.split(' - ')[1:])}", font_size=30, background_color=(255, 207, 0, 200 / 255),
                   on_press=lambda x: self.go(i))

        flag = True
        print(a)
        self.grid.add_widget(c)
    def openpdf(self,a):
        return webbrowser.open_new(a)
buttons = []
a = []

if __name__ == "__main__":
    Application().run()