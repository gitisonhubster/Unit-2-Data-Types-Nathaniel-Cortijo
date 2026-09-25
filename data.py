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
def divide(x,y):
    return(x/y)

x = int(input("gimme a number"))
if divide(x,2) == float:
    print("odd")
elif divide(x,2) == int:
    print("even")