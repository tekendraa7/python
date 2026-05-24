l = [2,3,5,6,1,9,8]
l.sort()
print(l)
sum = 0
for i in l:
    sum = sum + i
print(sum)
print(f"The average is : {sum/len(l)}.")