filename = input("Enter file name: ")
filehand = open(filename)
lst = list()
for line in filehand:
    line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
