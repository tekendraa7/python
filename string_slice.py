a = 'Hello, World!'
print(a[1:5:1]) # slicing with start index, end index and step
print(a[1:5]) # slicing with start index and end index, step is default
print(a[1:]) # slicing with start index, end index is default
print(a[:5]) # slicing with end index, start index is default
print(a[::2]) # slicing with step, start and end index are default
print(a[::-1]) # slicing with negative step to reverse the string