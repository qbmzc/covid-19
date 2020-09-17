import pandas as pd

file_path = '/data/Cong/2017.xlsx'
data = pd.read_excel(file_path, index_col=0)
data.to_csv('data.csv', encoding='utf-8')
