import gspread
import matplotlib.pyplot as plt
from datetime import datetime


def autoregress(data, dates):
    b = coeff(data)
    a = sum(data) / len(data) * (1 - b)
    forecast = []
    for i in data:
        forecast.append(a + b * i)

    fig, ax = plt.subplots()
    ax.plot(dates, data)
    ax.plot(dates, forecast,'o--')
    plt.show()
    print("________")


def coeff(data):
    y1 = sum(data[1:]) / len(data[1:])
    y2 = sum(data[:-1]) / len(data[:-1])
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for i in range(1, len(data)):
        numerator += (data[i] - y1) * (data[i - 1] - y2)
        denominator1 += (data[i] - y1) ** 2
        denominator2 += (data[i - 1] - y2) ** 2
    return numerator / (denominator1 * denominator2) ** 0.5


def start():
    sa = gspread.service_account(filename="token.json")
    sheet = sa.open("5task")
    worksheet = sheet.worksheet("kurs")

    dates = list(map(lambda o: datetime.strptime(o, '%d.%m.%Y'), worksheet.col_values(1)))
    y = list(map(lambda o: float(o.replace(',', '.')), worksheet.col_values(2)))
    autoregress(y, dates)

    dates = list(map(lambda o: datetime.strptime(o, '%d.%m.%Y'), worksheet.col_values(4)))
    y = list(map(lambda o: float(o.replace(',', '.')), worksheet.col_values(5)))
    autoregress(y, dates)


start()
