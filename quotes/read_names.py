import linecache

def simplecount(filename):
    lines = 0
    for line in open(filename):
        lines += 1
    return lines

fileLength = simplecount('names and nums.txt')
i = 1
nameNPhone = []
while i <= fileLength:
	particular_line = linecache.getline('names and nums.txt', i)
	phone = particular_line.split(":",1)[1]
	name = particular_line.split(":", -1)[0]
	nameNPhone.append([name, phone])
	i+=1

print(nameNPhone)