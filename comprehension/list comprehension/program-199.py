sales_list=[[2020,45000],
            [2021,50000],
            [2022,30000],
            [2023,43000],
            [2024,60000]]

sales_list1=[s for s in sales_list if s[1]<50000]
sales_list2=[s for s in sales_list if s[1]>=50000]

print(sales_list)
print(sales_list1)
print(sales_list2)
