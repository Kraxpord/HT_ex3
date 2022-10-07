n = int(input("Введіть число1->"))
p = int(input("Введіть число2->"))
if n>p:
    g = n
    n = p
    p = g
elif n%7==0:
    n +=7
while n < p:
    print(f"{n}")
    n+=7
else:
    print('робота цикла завершина')
    print('робота програми завершина')