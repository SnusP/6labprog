from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from datetime import datetime
from fpdf import FPDF
from kivy.uix.dropdown import DropDown
import gspread
class Application(App):
    def build(self):
        Window.clearcolor = (16 / 255, 71 / 255, 140 / 255, 0);
        self.grid = GridLayout(cols=2, padding=[30], spacing=10)
        self.noth1 = Label()
        self.label = Label(text="Введите данные", font_size=30)
        self.speed = TextInput(text = "Введите скорость")
        dropdown = DropDown()

        for ingrediant in ["g","kg","ton"]:
            btn = Button(text=ingrediant, size_hint_y=None, color="cyan",height = 25)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        self.trigger = Button(text="Выберите единицы измерения", background_color=(255, 207, 0, 200 / 255))
        self.trigger.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.trigger, 'text', x))

        dropdown1 = DropDown()

        for ingrediant in ["km\h", "km/s", "m/h","m/s"]:
            btn = Button(text=ingrediant, size_hint_y=None, color="cyan", height=25)
            btn.bind(on_release=lambda btn: dropdown1.select(btn.text))
            dropdown1.add_widget(btn)
        self.trigger1 = Button(text="Выберите единицы измерения", background_color=(255, 207, 0, 200 / 255))
        self.trigger1.bind(on_release=dropdown1.open)
        dropdown1.bind(on_select=lambda instance, x: setattr(self.trigger1, 'text', x))


        self.m = TextInput(text="Введите массу")
        self.filename = TextInput(text="Введите название файла")
        self.but = Button(text="Создать PDF", font_size=30, background_color=(255, 207, 0, 200 / 255),
                          on_press=self.go)
        self.grid.add_widget(self.label)
        self.grid.add_widget(self.noth1)
        self.grid.add_widget(self.m)
        self.grid.add_widget(self.trigger)

        self.grid.add_widget(self.speed)
        self.grid.add_widget(self.trigger1)
        self.grid.add_widget(self.filename)
        self.grid.add_widget(self.but)
        return self.grid
    def go(self,obj):
        print(self.trigger.text)
        google_table(self.m.text, self.speed.text, self.filename.text,self.trigger.text,self.trigger1.text)
def create_pdf(text,filename):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    for line in text:
        if len(line) == 0:
            pdf.ln()
        else:
            pdf.cell(0, 7, '   '.join(line), ln=1)
    pdf.output(f"{filename}.pdf", 'F')
def google_table(m, v, s,me,ve):
    sa = gspread.service_account(filename="token.json")
    sheet = sa.open("5task")
    worksheet = sheet.worksheet("pdf")
    worksheet.update('A1', s)
    worksheet.update('C4', me)
    worksheet.update('C5', ve)
    worksheet.update('C3', me+"*("+ve+")^2")
    worksheet.update('B1', datetime.today().strftime('%Y-%m-%d'))
    worksheet.update('B4', m)
    worksheet.update('B5', v)
    worksheet.update('B5', v)

    create_pdf(worksheet.get_all_values(), datetime.today().strftime('%Y-%m-%d') + ' - ' + s)
sa = gspread.service_account(filename="token.json")
sheet = sa.open("5task")
worksheet = sheet.worksheet("pdf")
if __name__ == "__main__":
    Application().run()
