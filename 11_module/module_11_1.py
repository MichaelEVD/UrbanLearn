import numpy as np

bmas_1m = np.arange(10)   # создание одномерного массива

b2 = [[x, x+2] for x in range(8)]
bmas_2m = np.array(b2)   # создание двумерного массива

b3 = [[x, x+2, x+3] for x in range(8)]
bmas_3m = np.array(b3)   # создание трехмерного массива

bmas_3m_trans = bmas_3m.T   # транспонирование трехмерного массива
bmas_2m_trans = bmas_2m.T   # транспонирование двумерного массива

print(bmas_1m)
print(bmas_2m)
print(bmas_3m)
print(bmas_3m_trans)
print(bmas_2m_trans)

bmas_1m.resize(2, 5)  # изменение размера исходного массива
print(bmas_1m)

from PIL import Image, ImageFont, ImageDraw, ImageFilter

image = Image.open('./image/winter_kurort.jpg')  # открытие изображения
image.show()
idraw = ImageDraw.Draw(image)
text = 'Курорт "Абзаково"'
font = ImageFont.truetype("arial.ttf", size=35)   # нанесение текста на изображение
idraw.text((20, 20), text, font=font)
image.show()
wb_image = image.convert('L')   # конвертация изображения в чернобелый цвет
wb_image.show()
rz_image = image.resize((400, 400))   # изменение размера изображения
rz_image.show()
sh_image = image.filter(ImageFilter.SHARPEN)   # увеличение резкости изображения
sh_image.show()

import pandas as pd

data = {'product_name': ['snb_boots', 'snb_bindings', 'helmet', 'snb_pants', 'snowboard'],
        'price': [30000, 20000, 15000, 10000, 60000]
        }
df = pd.DataFrame(data, index=[x for x in range(1, 6)])   # создание DataFrame
print(df)
max_price_eqip = df['price'].max()   # определение максимального значения
print(max_price_eqip)
min_price_eqip = df['price'].min()  # определение минимального значения
print(min_price_eqip)
df.to_csv('./image/snb_equip.csv', index=False)   # запись данных в файл csv
df.to_json("./image/snb_equip.json")         # запись данных в файл json(в виде пары ключ-значение)
a = df.shape   # определение количества столбцов и строк соответственно
print(a)