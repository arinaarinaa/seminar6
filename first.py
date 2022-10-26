# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

strochka = input('Введите вашу строчку - \n')
massive_slov = strochka.split()
print(massive_slov)
result = ''
for i in range(len(massive_slov)):
    if not 'абв' in massive_slov[i]:
        result +=massive_slov[i]+ ' '
print(result)
