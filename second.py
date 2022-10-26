with open('file_for_second_task.txt', 'r', encoding = 'utf-8') as data:
    infa = data.read()
    count1 = 1 #С однерки начинаем
    res = ''
    for i in range(len(infa)-1):
        if infa[i] == infa[i+1]: #Если совпадает этот индекс и следующий 
            count1=count1+1 #Прибавляем каунт
        else:
            res = res + str(count1) + infa[i] #Если не совпадает - в строчку добавляем каунт
            # и само значение
            count1 = 1 #Возвращаем значение каждый раз
    if count1 > 1 or (infa[len(infa)-2] != infa[-1]):#Если каунт у элемента больше 1 или
         # предпоследний элемент не равен последнему элементу
         res = res + str(count1) + infa[-1] #Напечатай каунт и последний элемент
         #это для последнего элемента, если он один
    print(res)