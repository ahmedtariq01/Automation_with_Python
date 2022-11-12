import re

log = 'july 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'
index = log.index('[')
print(log[index+1:index+6])

result = re.search(r'aza', 'plaza')
print(result)
print(re.search(r'^x', 'xenon'))
print(re.search(r'p.ng', 'penguin'))
print(re.search(r'p.ng', 'clapping'))
print(re.search(r'p.ng', 'sponge'))
print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))