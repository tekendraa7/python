l = [12, 3, 4, 6, 19, 30, 45, 7]
largest = l[0]
index = 0
for i in range(len(l)):
    print(l[i])
    if l[i] > largest:
        largest = l[i]
        index = i
print(f"The largest number is {largest} at index {index}. ")