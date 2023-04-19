print("\nрасшифровка")
alphint=["1","2","3","4","5","6","7","8","9",]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]

m=n=6
matrix = [[0]*m for k in range(n)]
brackets = [[0]*m for c in range(n)]
with open ("data.txt", "r") as file:
    secret = file.readline()
    stroka= file.readline()
    for i in range (m):
        for j in range(n):
            matrix[i][j] =file.read(1)
    file.read(1)
    for k in range (m):
        for l in range(n):
            brackets[k][l] =file.read(2)
print(secret, stroka )
secretword=[]
chislo=0

for x in secret:
    if (not x in secretword) and x in alphabet:
        secretword.append(x)
    else:
        secretword.append(x+alphint[chislo])
        chislo+=1
secretword= secretword[:-1]

shifred = [str(x) for x in secretword]
shifred  = sorted(shifred)

k=[]
dict2 = {}
text = []
print(stroka)
for i in range (0, len(stroka),2):
    try:
        text.append(stroka[i]+stroka[i+1])
    except IndexError:
        break
print(text)
for i in range (0,len(secretword)):
    for j in range (i, len(text), len(secretword)):
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
emergant= []
while fl == True:
    for x in dictuncrypt.keys():
        try:
            vivod+=(dictuncrypt[x][kount])
        except IndexError:
            try:
                for i in sorted(dictuncrypt.keys()):
                    emergant.append(dictuncrypt[i][kount])
            except IndexError:
                for i in reversed(emergant):
                    vivod+=i
                pass
            fl = False
            break
    kount+=1
print(vivod)
result=""
for i in range (m):
    print(brackets[i])
for x in range(0, len(vivod), 2):
    b = vivod[x]+vivod[x+1]
    for i in range(m):
        for j in range(n):
            if brackets[i][j] == b:
                result+=matrix[i][j]
print("\nрезультат расшифровки:",result)