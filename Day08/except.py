a = int(input("Tell your number :- "))

try:
    print(10/a)

except ZeroDivisionError:
    print("Sorry you cannot divide by 0 ")

print ("Ok I have done the division ")