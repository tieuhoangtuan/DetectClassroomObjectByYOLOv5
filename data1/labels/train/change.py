import os

files = []
# Add the path of txt folder
path = "D:\\CNPMNC\\whiteboard\\valid\\labels\\"
for i in os.listdir(path):
    if i.endswith('.txt'):
        files.append(path+i)
        print(i)

for item in files:
    # define an empty list
    file_data = []

    # open file and read the content in a list
    with open(item, 'r') as myfile:
        for line in myfile:
            # remove linebreak which is the last character of the string
            currentLine = line[:-1]
            data = currentLine.split(" ")
            # add item to the list
            file_data.append(data)
    
    # Decrease the first number in any line by one
    for i in file_data:
        if i[0].isdigit():
            temp = float(i[0]) + 3
            i[0] = str(int(temp))

    # Write back to the file
    f = open(item, 'w')
    for i in file_data:
        res = ""
        for j in i:
            res += j + " "
        f.write(res)
        f.write("\n")
    f.close()