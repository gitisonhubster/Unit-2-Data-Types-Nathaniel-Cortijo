""" x = 3
y = float(3)
print(x,y)


 """



""" origninal_price=int((input("how much are you paying?")))
Tip_amount=int((input("what percent are you tiping")))
print("Original Price:" , origninal_price)
print("Tip:" , Tip_amount)
print("Total:" , origninal_price+(origninal_price*(Tip_amount/100))) """


""" 


values = [1,2.23,5,7,2,30,15] """
""" print(values)
for i in values:
    print(i) """
""" print(values[0])
print(values[6]) """


""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """


""" x = input("gimme a sentence")
y = len(x.split( ))
print(y) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct") 
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """


""" x = str(float(input("gimme a number"))/2)
even = ".0"
odd = ".5"
if even in x:
    print("even")
elif odd in x:
    print("odd") """

""" x = int(input("gimme a number"))
if x % 2 == 0:
    print("even")
else:
    print("odd") """

""" Tip_amount = 0
origninal_price=int((input("How much are you paying?")))
service_quality=input("How good was your service?")
if service_quality == "bad" :
    Tip_amount = 0
elif service_quality == "okay" :
    Tip_amount = 15
elif service_quality == "good" :
    Tip_amount = 20
elif service_quality == "great" :
    Tip_amount = 25
print("Original Price: $" , origninal_price)
print("Tip:" , Tip_amount,"%")
print("Total: $" , origninal_price+(origninal_price*(Tip_amount/100))) """

def factor(x):
    factors = []
    for i in int(x):
        if x % i == 0:
            factors.append(i)
    return(factors)

y = float(input("number you want to factor"))
print(factor(y))
