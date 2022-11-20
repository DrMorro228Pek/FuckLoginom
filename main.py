import pandas as pd
import numpy as np

#Подзадание 1
#df_1 = pd.read_csv('1.txt', sep=';', encoding="utf-8")
# df_1['Date'] = pd.to_datetime(df_1['Date'], format="%d.%m.%Y")
# ans_1 = df_1.groupby(df_1['Article'])['Date'].agg(['first', 'last']).reset_index()
#print(ans_1)

#Подзадание 2
# df_2_1 = pd.read_csv('1.txt', sep=';', encoding="utf-8")
# df_2_1 = df_2_1.groupby(df_2_1['Article']).agg({
#     'Count': 'sum',
#     'Cost': 'mean'
# }).reset_index()
# df_2_1['Value'] = df_2_1.apply(lambda row: ((row['Count'] - 1) * row['Cost']), axis=1)
# df_2_1 = df_2_1.apply(np.int64)
#
# df_2_2 = pd.read_csv('2.txt', sep=';', encoding="utf-8")
# df_2_3 = pd.merge(df_2_1, df_2_2, on='Article', how='inner')
# #TovSubgroup
# ans_2 = df_2_3.groupby(df_2_3['Подгруппа']).agg(
#     {
#         'Value': 'sum'
#     }
# )

#print(ans_2)

#Подзадание 3
# df_3 = pd.read_csv('1.txt', sep=';', encoding="utf-8")
#
# ans_3 = df_3.groupby(df_3['Article']).agg({
#     'Check': 'count'
# })
#
# labels = ['до 10', 'от 10 до 50', 'от 50 до 100', 'от 100 до 200', 'от 200 до 300', 'свыше 300']
# bins = [0, 10, 50, 100, 200, 300, 100000]
#
# ans_3['Интервал'] = pd.cut(ans_3.Check, bins, labels=labels)
# print(ans_3)

#Задание 2
#pd.set_option("display.max_rows", None)
# df_4 = pd.read_csv('3.txt', sep=';', encoding="utf-8")
# df_4['Квартал'] = pd.to_datetime(df_4['Квартал'], format="%d.%m.%Y")
# df_4.sort_values(by='Квартал')
#
# df_4_1 = df_4.groupby('Код Клиента')['Класс'].agg(['first', 'last']).reset_index()
# print(df_4_1)

#Задание 3
df_5 = pd.read_csv('4.txt', sep=';', encoding="utf-8")
df_5 = df_5.groupby('КЛИЕНТ_КОД', as_index=False).agg(['min', 'max', 'mean', 'sum']).reset_index()


pd.set_option('display.max_columns', None)
print(df_5)
