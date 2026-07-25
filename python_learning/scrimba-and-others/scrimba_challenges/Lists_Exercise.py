sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = sales_w1 + sales_w2

extra_day = int(input("Sales on extra day: "))
sales.append(extra_day)
sales.sort()

print(f'Your profit on your best day was ${max(sales)*1.5}')
print(f'Your profit on your worst day was ${min(sales)*1.5}')
print(f'Your total profit was ${sum(sales)*1.5}')
