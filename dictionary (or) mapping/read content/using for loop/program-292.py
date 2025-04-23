sales={2019:45000,
       2020:65000,
       2021:90000,
       2022:75000,
       2023:85000,
       2024:98000}

total=0

for year in sales:
    s=sales[year]
    total=total+s
    print(f'{year}--->{s}')

print(f'Total Sales {total}')
