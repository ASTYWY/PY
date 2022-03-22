a1=int(input("a1 = "))
a2=int(input("a2 = "))
a3=int(input("a3 = "))
b1=int(input("b1 = "))
b2=int(input("b2 = "))
c3=(((a3*100)+(a2*10)+a3)+((b2*10)+b1))//100
c2=((((a3*100)+(a2*10)+a3)+((b2*10)+b1))%100)//10
c1=(a1+b1)%10
print("c1 = ", c1)
print("c2 = ", c2)
print("c3 = ", c3)