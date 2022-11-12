import re

log = 'july 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'
index = log.index('[')
print(log[index+1:index+6])

result = re.search(r'aza', 'plaza')
print(result)

# simple regular expression
print(re.search(r'^x', 'xenon'))
print(re.search(r'p.ng', 'penguin'))
print(re.search(r'p.ng', 'clapping'))
print(re.search(r'p.ng', 'sponge'))

print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))

# wildcards and character classes
print(re.search(r'[Pp]ython', 'Python'))
print(re.search(r'[a-z]way', 'The end of the highway'))
print(re.search(r'[a-z]way', 'What a way to go'))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloudy'))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud9'))

print(re.search(r'[^a-zA-Z]', 'This is a sentence with spaces.'))
print(re.search(r'[^a-zA-Z ]', 'This is a sentence with spaces.'))

print(re.search(r'cat|dog', 'I like cats.'))
print(re.search(r'cat|dog', 'I like dogs.'))
print(re.search(r'cat|dog', 'I like both cats and dogs.'))

print(re.findall(r'cat|dog', 'I like both cats and dogs.'))

#repetition qualifiers
print(re.search(r'Py.*n', 'Pygmalion'))
print(re.search(r'Py.*n', 'Python Programming'))

print(re.search(r'Py[a-z]*n', 'Pythons Programming'))
print(re.search(r'Py[a-z]*n', 'Pyn'))

print(re.search(r'o+l+', 'goldfish'))
print(re.search(r'o+l+', 'woolly'))
print(re.search(r'o+l+', 'boil'))

print(re.search(r'p?each', 'To each their own'))
print(re.search(r'p?each', 'I like peaches'))

print(re.search(r'[a-zA-Z0-9]{6}', 'abcdef'))
print(re.findall(r'[a-zA-Z0-9]{6}', 'a ghost'))
print(re.findall(r'\b[a-zA-Z]{5}\b', 'I really like strawberries'))
print(re.findall(r'\w{5,10}', 'I really like strawberries'))
print(re.findall(r'\w{5,}', 'I really like strawberries'))
print(re.findall(r'\b\w{5}\b', 'Australia is a country and continent surrounded by the Indian and Pacific oceans.'))

# escape characters
print(re.search(r'.com', 'welcome'))
print(re.search(r'\.com', 'welcome'))
print(re.search(r'\.com', 'mydomain.com'))

print(re.search(r'\w*', 'This is an example'))
print(re.search(r'\w*', 'And_this_is_another'))

print(re.search(r'A.*a', 'Argentina'))
print(re.search(r'A.*a', 'Azerbaijan'))
print(re.search(r'A.*a$', 'Azerbaijan'))
print(re.search(r'A.*a$', 'Australia'))

pattern = r"^[a-zAA_Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable name"))
print(re.search(pattern, "my-variable1"))
print(re.search(pattern, "2my-variable1"))

# capturing groups

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result.groups())
print(result[0])
print(result[1])
print('{} {}'.format(result[2], result[1]))

def rearrangements(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return '{} {}'.format(result[2], result[1])

rearrangements('Lovelace, Ada')

# PID using regular expressions
log = 'july 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

r = re.searcg(regex, 'A completely different string that also has numbers [34567]')
print(r[1])

r = re.search(regex, '99 elephants in a [cage]')
print(r[1])

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ''
    return result[1]

extract_pid('99 elephants in a [cage]')

# splitting and replacing

re.split(r"[.?!]", "One sentence. Another one? And the last one!")
re.split(r"([.?!])", "One sentence. Another one? And the last one!", maxsplit=1)

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for youaaaa@eample.com")
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")















