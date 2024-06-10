#a
import csv
from pathlib import Path

file_route = Path('.') / 'dataset' /'area_protegida.csv'
def calc_value(data):
     value = sum(int(x[13]) for x in data)/len(data)
     return value
def my_function(data, value, *args):
     sub_data = filter(lambda x: int(x[8]) in args and int(x[13])<value, data)
     return list(sub_data)
with open(file_route, "r", encoding="utf-8") as data_set:
     reader = csv.reader(data_set)
     header, data = next(reader), list(reader)

value_data = calc_value(data)
result1 = my_function(data,value_data, 1, 2)
result2 = my_function(data, value_data, 3)
print(len(result1))
print(f"\n****\n{len(result2)}")

