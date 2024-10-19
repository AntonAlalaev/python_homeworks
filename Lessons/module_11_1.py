import requests
from io import StringIO # чтобы преобразовать данные из потока строки как из файла
import pandas as pd
import matplotlib.pyplot as plt

# данные о заболеваемости ковид во владимирской области
# https://hubofdata.ru/dataset/6a4fe582-dc18-4c19-ba32-e27c67f135e9/resource/8d87b4c0-cdf3-47a5-947a-9bc1d46e864b/download/1.csv
# https://hubofdata.ru/dataset/vladimir_covid-19

URL = "https://hubofdata.ru/dataset/6a4fe582-dc18-4c19-ba32-e27c67f135e9/resource/8d87b4c0-cdf3-47a5-947a-9bc1d46e864b/download/1.csv"
response = requests.get(URL)

data = response.content

# Считываем данные csv в кодировке UTF-8, без этого очень долго не мог добиться нормального отображения заголовок строк
df = pd.read_csv(StringIO(data.decode('utf-8')), sep=';', index_col=0, header=1)


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
plt.legend(df.index)
plt.grid(True) # Add grid lines
plt.show()
