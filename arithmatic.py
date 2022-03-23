a=float(input("Введите сторону a: "))
b=float(input("Введите сторону b: "))
c=float(input("Введите сторону c: "))
p=(a+b+c) /2
s1=p*(p-a)*(p-b)*(p-c)
s=s1**(0.5)
print("Плошадь треугольника равна: ", s)