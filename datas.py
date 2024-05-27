#Hello 

file_name = "text1.txt"

with open(file_name, "r") as file:
    print(file.name)
    print(file.mode)
    print(file.closed)

    # print(file.read(15))
    # print(file.read(10)) 

    print(file.readline())
    print(file.tell())

print(file.closed)