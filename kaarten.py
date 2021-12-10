import random
x=['kaart 1','kaart 2','kaart 3','kaart 4','kaart 5','kaart 6','kaart 7']
harten = ["harten koning", "harten vrouw", "harten boer", 'harten 10', 'harten 9', 'harten 8', 'harten 7', 'harten 6', 'harten 5', 'harten 4', 'harten 3', 'harten 2', 'harten aas']
klaveren=['klaveren koning', 'klaverenvrouw', 'klaveren boer', 'klaveren 10', 'klaveren 9', 'klaveren 8','klaveren 7','klaveren 6', 'klaveren 5', 'klaveren 4', 'klaveren 3', 'klaveren 2', 'klaveren aas']
schoppen=['schoppen koning','schoppen vrouw', 'schoppen boer', 'schoppen 10', 'schoppen 9', 'schoppen 8', 'schoppen 7', 'schoppen 6', 'schoppen 5', 'schoppen 4','schoppen 3','schoppen 2', 'schoppen aas']
ruiten=['ruiten koning','ruiten vrouw', 'ruiten boer', 'ruiten 10', 'ruiten 9','ruiten 8', 'ruiten 7','ruiten 6','ruiten 5','ruiten 4','ruiten 3','ruiten 2','ruiten aas']
deck = harten + klaveren + schoppen + ruiten +['joker','joker']

for itemA, itemB in zip(x, random.choices(deck, k = 7)):
    print(itemA + ":", itemB)
    deck.remove(itemB)
print('deck[47 kaarten]: ', deck)
