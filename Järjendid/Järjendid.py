
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

c=2**3
print(c)