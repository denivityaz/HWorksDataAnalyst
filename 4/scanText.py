import re

text = "When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!"

# юзаем регулярное выражение с которым минуту назад познакомились
matches = re.findall(r'\((.*?)\)', text)

for match in matches:
    print(match)

# или find

start = text.find("(")
end = text.find(")")

if start != -1 and end != -1:
    result = text[start+1:end]
print('\n',result)