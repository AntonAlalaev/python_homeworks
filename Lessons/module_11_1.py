import requests
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt


# данные о заболеваемости ковид во владимирской области
# https://hubofdata.ru/dataset/6a4fe582-dc18-4c19-ba32-e27c67f135e9/resource/8d87b4c0-cdf3-47a5-947a-9bc1d46e864b/download/1.csv
# https://hubofdata.ru/dataset/vladimir_covid-19

URL = "https://hubofdata.ru/dataset/6a4fe582-dc18-4c19-ba32-e27c67f135e9/resource/8d87b4c0-cdf3-47a5-947a-9bc1d46e864b/download/1.csv"
response = requests.get(URL)

# Добавление newline=None чтобы корректно понимать конец строки во всех environments и вот здесь как раз и возникает
# проблема с кодировками. т.к. строка не имеет кодировки и пишет каждый символ двумя байтами
# как это побороть я пока не понял
data = StringIO(response.text, newline=None)
# Читаем данные из CSV в DataFrame указывая кодировку
# Попробовал множество возможных кодировок, но так и не добился нормальных значений (cp1251, cp866)
# В файле, когда его скачиваю кодировка вроде utf-8, но все равно какие-то кракозябры выходят
# Может из-за того что в Linux и надо какие-то другие шрифты использовать
df = pd.read_csv(data, sep=';', index_col=0, header=1, encoding='utf-8')


# конвертируем в числовые типы данных, ошибочные данные будут сконвертированы в NaN
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Убираем все нечисловые значения NaN
df = df.dropna()

print (df)

# Строим линейный график для каждой строки в наборе данных
plt.figure(figsize=(10, 6))
for index, row in df.iterrows():
    plt.plot(row.index, row.values)



plt.title('Статистика заболевания КОВИД в Владимирской области')
plt.xlabel('Даты ')
plt.ylabel('Количество заболевших')
# можно скрыть, т.к. так и не понял какая кодировка
plt.legend(df.index)
plt.grid(True) # Add grid lines
plt.show()
