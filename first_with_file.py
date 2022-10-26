with open('text.txt', 'r', encoding = 'utf-8') as slova:
    nashi_slova = slova.read()
    print(nashi_slova)
    words = nashi_slova.split()
    result = ''
for i in range(len(words)):
    if not 'абв' in words[i]:
        result +=words[i]+ ' '
print(result)
