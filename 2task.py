from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from datetime import datetime
from fpdf import FPDF
import gspread
class Application(App):
    def build(self):
        Window.clearcolor = (16 / 255, 71 / 255, 140 / 255, 0);
        self.grid = GridLayout(cols=1, padding=[30], spacing=10)

        self.label = Label(text="Введите данные", font_size=30)
        self.speed = TextInput(text = "Введите скорость")
        self.m = TextInput(text="Введите массу")
        self.filename = TextInput(text="Введите название файла")
        self.but = Button(text="Создать PDF", font_size=30, background_color=(255, 207, 0, 200 / 255),
                          on_press=self.go)
        self.grid.add_widget(self.label)
        self.grid.add_widget(self.m)
        self.grid.add_widget(self.filename)
        self.grid.add_widget(self.speed)
        self.grid.add_widget(self.but)
        return self.grid
    def go(self,obj):
        google_table(self.m.text, self.speed.text, self.filename.text)
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
def google_table(m, v, s):
    sa = gspread.service_account(filename="token.json")
    sheet = sa.open("5task")
    worksheet = sheet.worksheet("pdf")
    worksheet.update('A1', s)
    worksheet.update('B1', datetime.today().strftime('%Y-%m-%d'))
    worksheet.update('B4', m)
    worksheet.update('B5', v)

    create_pdf(worksheet.get_all_values(), datetime.today().strftime('%Y-%m-%d') + ' - ' + s)
sa = gspread.service_account(filename="token.json")
sheet = sa.open("5task")
worksheet = sheet.worksheet("pdf")
if __name__ == "__main__":
    Application().run()

