data = []
file_name = input("Provide a name of a file of data ")

try:
	fh = open(file_name,'r')
except IOError:
	print('Cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
finally:
	fh.close()
 

gradesData = []
if data:
    for student in data:
        print(student)
        try:
            name = student[:-1]
            grades = int(student[-1])
            gradesData.append([name, [grades]])
        except ValueError:
            gradesData.append([student[0:], []])
