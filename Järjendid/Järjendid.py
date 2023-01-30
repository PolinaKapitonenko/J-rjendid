
from abc import ABC
from ctypes import DllGetClassObject


spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Programmerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список")
    print("2-склеить списки\n3-добавть букву на i -позицию")
    print("4-удалить элемент")
    valik=int(input())
    if valik==1:
        a=input("Введи букву ")
        slovo_list.append(a)
        print(f"Добавить {a} новый список", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить")
        i=int(input("Введи номер позиции, которую хочешь добавить букву"))
        slovo_list.insert(i-1,a) #0,1,2...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить")
        slovo_list.remove(a)
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить: ")
        n=slovo_list.count(a)
    if n>0:
        for i in range(n):
            slovo_list.remove(a)
    else:
         print("Искомой буквы нет")
         print(slovo_list) 

        
#2
spisok=[]
print("Выбери более понравившейся вариант от 1 до 6")
while True:
    print("1-слова большими")
    print("2-слова маленькими")
    print("3-Разбиение строки по разделителю ")
    print("4-Переводит первый символ строки в верхний регистр, а все остальные внижний ")
    print("5-Переводит символы нижнего регистра в верхний, а верхнего – в нижний")
    print("6-Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний")
    print("7-КОНЕЦ")
    pan_Am=float(input())
    if pan_Am==1:
        a=input("Введи букву/слово: ")
        print(a.upper())
        print(f"Добавили {a} ",список)
    elif pan_Am==2:
        b=input("Введи букву: ")
        print(b.lower())
        print(f"Добавили {b} ",список)
    elif pan_Am==3:
        s=input("Введи букву: ")
        print(s.split())
        print(f"Добавили {s} ",список)
    elif pan_Am==4:
        c=input("Введи букву: ")
        print(c.capitalize())
        print(f"Добавили {c} ",список)
    elif pan_Am==5:
        v=input("Введи букву: ")
        print(v.swapcase())
        print(f"Добавили {v} ",список)
    elif pan_Am==6:
        b=input("Введи букву: ")
        print(b.title())
        print(f"Добавили {b} ",список)
    elif pan_Am==7:
        break


#3
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список")
    print("2-склеить списки\n3-добавить букву на i-позицию")
    print("4-удалить элемент")
    print("5-очистить список")
    print("6-развернуть список")
    print("7-возвращает колтчество элементов со значением x")
    valik=int(input())
    if valik==1:
        a=input("введи букву")
        slovo_list.append(a)
        print(f"Добавили {a}  новый список", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=(input("Введи букву, которую хочешь добавить "))
        i=int(input("Ввкди номер позии, куда хочешь добавить букву 0,"))
        slovo_list.insert(i=1,a) #0,1,2,3...
        print(slovo_list)
    elif valik==4:
        a=(input("Введи букву, которую хочешь удалить "))
        a=a.lower()
        listcopy_list=[]
        for t in (slovo_list):
            listcopy_list.append(t.lower())
        n=listcopy_list.count(a)
        if n>0:
            for i in range(n):
                listcopy_list.remove(a)
        else:
            print("Искомой буквы нет")
        print(listcopy_list)
    elif valik==5:
        slovo_list.clear()
    elif valik==6:
        slovo_list.reverse()
        

