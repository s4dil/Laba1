s=[1,2,2,2,2,3,5,5,6,7,7,7,8,3]
print("Начальный массив: ",s)
dat4ik=False
for i in range(1,len(s)):
    try:
        if s[i]==s[i-1]:
            dat4ik=True
            continue
        else:
            if dat4ik==True:
                s.pop(i-1)
                dat4ik=False
            else:
                continue
    except:
        pass
print("Преобразованный массив: ",s)
a + b = Ничего
Типо добавлено очередоное изменение.
выаываав
