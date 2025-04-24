sales_dict={2020:45000,
            2021:54000,
            2022:67000,
            2023:85000,
            2024:35000}


print(sales_dict)
sales_dict1={year:sales for year,sales in sales_dict.items()
             if sales<50000}
print(sales_dict1)
sales_dict2={year:sales for year,sales in sales_dict.items()
             if sales>=50000}
print(sales_dict2)
