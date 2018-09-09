'''import fileinput
input_list = []

for line in fileinput.input():
    input_list.append(line)'''
    
input_list1 = open("file 2.txt","r")

input_list = []
for line in input_list1.readlines():
    input_list.append(line)


courses = input_list[1:input_list.index('Students\n')]

students = input_list[input_list.index('Students\n')+1:input_list.index('Grades\n')]

grades = input_list[input_list.index('Grades\n')+1:-1]

grades2 = []
for line in grades:
    j = line.split("~")
    grades2.append(j)
    
students2 = []
for line in students:
    j = line.split("~")
    students2.append(j)
    
final_list = []
for i in students2:
    final_list.append([i[0], i[1][:-1], '0'])
    
#print(final_list)
    
for i in grades2:
    for j in students2:
        for k in final_list:
            if i[3] == j[0] == k[0]:
                if i[4] == "A\n":
                    k[2] += '1'
                elif i[4] == "AB\n":
                    k[2] += "2"
                elif i[4] == "B\n":
                    k[2] += "3"
                elif i[4] == "BC\n":
                    k[2] += "4"
                elif i[4] == "C\n":
                    k[2] += "5"
                elif i[4] == "CD\n":
                    k[2] += "6"
                elif i[4] == "D\n":
                    k[2] += "7"
                    
                    
for l in final_list:
    c = list(l[2])
    sum = 0
    for i in c:
        if i == '1':
            sum += 10
        elif i == '2':
            sum += 9
        elif i == '3':
            sum += 8
        elif i == '4':
            sum += 7
        elif i == '5':
            sum += 6
        elif i == '6':
            sum += 5
        elif i == '7':
            sum += 4
    try:
        l[2] = sum/(len(l[2])-1)
    except ZeroDivisionError:
        l[2] = 0
        
for l in final_list:
    l[2] = round(l[2],2)
        
        
for l in final_list:
    l[2] = str(l[2]) + "\n"
    
final_list2 = []
for l in final_list:
    final_list2.append("~".join([l[0],l[1],l[2][:-1]]))
    
final_list2.sort()  
        
for l in final_list2:
    print(l)
    
a = open("graded_list 2.txt",'w')

for l in final_list2:
    a.write(l + "\n")
    
a.close()

a = open("graded_list 2.txt",'r')

a.readlines()