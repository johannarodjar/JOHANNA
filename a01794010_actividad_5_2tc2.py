# -*- coding: utf-8 -*-
"""A01794010 actividad 5.2TC2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sa9tZHhqCHDnJaPfMPMyIDjDkSOoaHG1
"""

import sys
import pandas as pd
import json
import time

df1 = pd.read_json("/content/TC1.ProductList.json")
df2 = pd.read_json("/content/TC2.Sales.json")

print(f"Columns in df1: {df1.columns.tolist()}")
print(f"Columns in df2: {df2.columns.tolist()}")

def calculate_total_sales(df1, df2):
    merged_df = pd.merge(df1, df2, left_on='title', right_on='Product', how='left')
    merged_df['total_cost'] = merged_df['Quantity'] * merged_df['price']

    total_sales_cost = merged_df['total_cost'].sum()
    return total_sales_cost


total_cost = calculate_total_sales(df1, df2)


print(f"Total sales cost: ${total_cost:.2f}")


with open("/content/SalesResults.txt", "w") as file:
    file.write(f"Total sales cost: ${total_cost:.2f}")

output_file_path = "/content/SalesResults.txt"

# Escribir el resultado en el archivo de texto
with open(output_file_path, "w") as file:
    file.write(f"Total sales cost: ${total_cost:.2f}\n")

print(f"El resultado se ha guardado en {output_file_path}")