a=input()
year=int(a[6:10])
print(f'{2021-year}\n',end='')
sex=int(a[16])
if sex%2==0:
    print('female')
else:
    print('male')