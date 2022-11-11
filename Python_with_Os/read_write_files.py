file = open('tst.txt')
print('Read line',file.readline())
print('Read file',file.read())

file.close()

with open('tst.txt') as file:
    print('Read line',file.readline())
    print('Read file',file.read())
    
with open('tst.txt') as file:
    for line in file:
        print(line.strip().upper())
        
with open('tst.txt') as file:
    lines = file.readlines()
    lines.sort()
    print(lines)
    
with open('tst.txt','w') as file:
    file.write('Hello World')
    