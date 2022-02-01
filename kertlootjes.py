import random

namen =[]
namen2 = []

aantalmensen = int(input('Hoeveel mensen wilt u toevoegen? '))
namen + namen2
for y in range(aantalmensen):
    l = input('Wie wilt u toevoegen? ')
    namen.append(l)
    namen2.append(l)
    
def dubbleu():
    dub2 = 0
    print('=======================')
    for x in range(aantalmensen):
        print(namen[dub2],"heeft", namen2[dub2])  
        dub2+=1

def mix():
    random.shuffle(namen)
    random.shuffle(namen2)
    check()

dub = 0
def check():
    global dub
    for x in range(aantalmensen):
        if namen[dub] == namen2[dub]:
            dub+=1
            mix()
    else:
        dubbleu()

mix()
