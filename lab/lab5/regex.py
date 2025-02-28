import re

#task 1
txt = input()

x = re.search('a.*b', txt)

print(x)

#task 2
txt = input()

x = re.search('a.{1}b', txt)
y = re.search('a.{2}b', txt)

if re.search('a.{1}b', txt):
    print(x)
elif re.search('a.{2}b', txt):
    print(y)
else:
    print("Error")

#task 3
txt = 'wgeerger_egregerignerio'

x = re.findall(r"[a-z]+_[a-z]+", txt)

if x:
    print(x)
else:
    print("No match")

#task 4
txt = 'WFIWFNWFRoerjoiernwif'

x = re.findall('[A-Z]{1}[a-z]+', txt)

print(x)

#task 5
txt = 'wkgmwrgiuageoigjoijwfb'

x = re.search('a.*b$', txt)

print(x)

#task 6
txt = 'nernnero imerimer,ofnrmer.wpomermpr'

x = re.sub('[ .,]', ';', txt)

print(x)

#task 7
txt = 'hello_world'
txt2 = txt.upper()

camel = ''

i = 0

while(i != len(txt)):
    if txt[i] == '_':
        camel += txt[i] + txt2[i+1]
        i += 2
    else:
        camel += txt[i]
        i += 1

camel = re.sub('_', '', camel)

print(camel)

#task 8
txt = 'HelloWorld'

x = re.findall('[A-Z][^A-Z]*', txt)

print(x)

#task 9

str = "HelloWorld"

x = re.sub(r"([A-Z])", r" \1", str)

print(x)

#task 10
camel = 'HelloWorld'

snake = re.sub(r"([A-Z])", r" \1", camel)

snake = snake.lower()
snake = snake.strip()

snake = re.sub(r'\s', '_', snake)

print(snake)
