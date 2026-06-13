a = int(input("Tell your number :- "))

try:
    print(10/a)

except ZeroDivisionError:
    print("Sorry you cannot divide by 0 ")

finally :
    print("This will run in any situation. ")

print ("Ok I have done the division ")
