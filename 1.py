nm=[]
sm=[]
cla=[]
poi=[]
ioi=[]
ioi1=[]
in1=[]
in2=[]
itog=[]
ghgh=[]
jkjk=[]
spis=[]
hjhjj=[]
from random import randint
with open ("names.txt", "r",encoding="utf-8") as f:
    for line in f:
        ioi.append(line)
    for i in range(50):
        in1.append(randint(0,50))
    for k in in1:
        nm.append(ioi[k])
with open ("surnames.txt", "r",encoding="utf-8") as ff:
    for line in ff:
        ioi1.append(line)
    for i in range(50):
        in2.append(randint(0,50))
    for k in in2:
        sm.append(ioi1[k])
for i in range(50):
    cla.append(randint(9,11))
for i in range(50):
    poi.append(randint(0,1000000))
with open("result.txt", "w",encoding="utf-8") as fff:
    for line in range(50):
        ghgh.append(f"{poi[line]}\n")
        jkjk.append(f"{poi[line]}\n")
print(ghgh)
ghgh=[line.rstrip() for line in ghgh]
jkjk.sort()
jkjk=[line.rstrip() for line in jkjk]
jhh=jkjk[47]
jhh1=jkjk[48]
jhh2=jkjk[49]
index=ghgh.index(jhh)
index1=ghgh.index(jhh1)
index2=ghgh.index(jhh2)
spis.append(index)
spis.append(index1)
spis.append(index2)
with open("result.txt", "a",encoding="utf-8") as ffff:
    for line in range(50):
        itog.append(f"{sm[line].strip()} {nm[line].strip()} {cla[line]} Класс:{poi[line]}-Балл(а/ов)\n\n")
    for line in itog:
        ffff.writelines(line)
    for line in spis:
        hjhjj.append(f"{cla[line]} Класс:{poi[line]}-Наивысший Балл\n\n")
    for line in hjhjj:
        ffff.writelines(line)