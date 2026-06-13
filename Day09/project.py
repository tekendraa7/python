from pathlib import Path

def readfileandfolder():
    path = Path ('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i + 1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name : ")
        p = Path(name)
        with open(p, "w") as fs:
            data = input("What you want to write in this file: ")
            fs.write(data)
        print("FILE CREATED SUCCESSFULLY.")
    except Exception as err:
        print(f"An erroe occured as {err}")    

print("Press 1 for create a file. ")
print("Press 2 for read a file. ")
print("Press 3 for update a file. ")
print("Press 4 for delete a file. ")

check = int(input("Please tell your response: "))

if check ==1:
    createfile()