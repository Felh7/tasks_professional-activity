from random import randint
stroka = str(input("введите сообщение: "))
word = str(input("введите ключ-слово: "))
n=6
m=6
a=[[0]*m for i in range(n)]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
alphint=["1","2","3","4","5","6","7","8","9",]
alphtable=["A","D","F","G","V","X"]
length = len(alphabet)
brackets = [[0]*m for k in range(n)]
# матрица рандомных значений
# матрица координат значений
for i in range (n):
    for j in range (m):
        index=randint(0,len(alphabet)-1)
        buff= alphabet.pop(index)
        brackets[i][j] = alphtable[i]+alphtable[j]
        a[i][j] = buff
        if length == 0:
            break
print("\n\nматрица алфавита")
for i in range(n):
    print("\n")
    for j in range(m):
        print(a[i][j], end = " ")
print("\n")


print("\nматрица клеток")
for i in range(n):
    print("\n")
    for j in range(m):
        print(brackets[i][j], end = " ")
print("\n")

spis=[]
k=[]
dict={}
count=0
chislo = 0
# заполнение списка буквами из слова-ключа
for x in word:
    if not x in spis:
        spis.append(x)
    else:
        x=x+alphint[chislo]
        spis.append(x)
        chislo+=1

values=[x for x in stroka if x != " "]

#замена элементов строки на элементы координат
for i in range (n):
    for j in range(m):
        for l in range(0, len(values)):
            if values[l] == a[i][j]:
                values[l] = brackets[i][j]
ran= len(word)
fin = []
for i in range (0,len(word)):
    for j in range (i, len(values), ran):
        x = values[j]
        k.append(x)
    if k is []:
        break
    else:
        dict[spis[i]] = k
        k = []

for c in (dict.keys()):
    print(c ,": ",dict[c])

print("\nсписок по слову")
for c in sorted(dict.keys()):
    print(c ,": ",dict[c])

count = 0
emergant =[]


while True:
    try:
        for i in sorted(dict):
            fin.append(dict[i][count])
        count+=1
    except IndexError:
        for i in dict:
            try:
                if dict[i][count]:
                    emergant.append(dict[i][count])
            except IndexError:
                break
        for i in reversed(emergant):
            fin.append(i)
        break


print("результат шифрвоки", fin)

'''
#расшифровка
finale = ""
kount = 0
fl = True

print("\nрасшифровка")
secretwor=word#str(input("введите секретное слово"))

matrix = a
secretword=[]
chislo=0

for x in secretwor:
    if not x in secretword and x !="":
        secretword.append(x)
    else:
        secretword.append(x+alphint[chislo])
        chislo+=1

shifred = [str(x) for x in secretword]
shifred  = sorted(shifred)
text = fin
k=[]
dict2 = {}
for i in range (0,len(secretword)):
    for j in range (i, len(text)-len(secretword), len(secretword)):
        x = text[j]
        k.append(x)

    if k is []:
        break
    else:
        dict2[shifred[i]] = k
        k = []
print("\n", "первый дикт", "\n")
for c in dict2.keys():
    print(c ,": ",dict2[c])

dictuncrypt = {}

for x in range (len(secretword)):
    dictuncrypt[secretword[x]] = dict2[secretword[x]]
print("\n", "второй дикт", "\n")

for c in dictuncrypt.keys():
    print(c ,": ",dictuncrypt[c])

vivod = ""
kount = 0
fl = True
while fl == True:
    for x in dictuncrypt.keys():
        try:
            vivod+=(dict[x][kount])
        except IndexError:
            fl = False

    kount+=1

result=""

for x in range(0, len(vivod)-1, 2):
    b = vivod[x]+vivod[x+1]
    for i in range(m):
        for j in range(n):
            if brackets[i][j] == b:

                result+=matrix[i][j]
print("\nрезультат расшифровки:",result)
'''
with open ("data.txt", "w") as file:
    for x in word:
        file.write(x)
    file.write('\n')
    for x in fin:
        file.write(x)
    file.write('\n')
    for i in range(m):
        for j in range (n):
            file.write(a[i][j])
    file.write('\n')
    for i in range(m):
        for j in range (n):
            file.write(brackets[i][j])