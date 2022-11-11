import csv

f = open('test.csv', 'r')
test = csv.reader(f)
for row in test:
    name, phone, role = row
    print('Name: {}, Phone: {}, Role: {}'.format(name, phone, role))
    
    
f.close()

hosts = [['workstation.local', '192.168.1'], ['workstation.local', '192.168.1'], ['workstation.local', '192.168.1']]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts
    

