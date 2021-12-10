lijst= []
lijst2 = {

}
def nogiets():
    meer = input("wilt u nog meer op uw boodschappen lijst? y/n ").lower()
    if meer ==("n"):
        print(lijst2)
    elif meer == ("y"):
        boodschaplijst()
    else:
        print("sorry dat begrijp ik niet.")
        nogiets()

def boodschaplijst():
    boodschap = input('wat wilt u in uw boodschappenlijst hebben? ').lower()
    if boodschap in lijst2:     
        lijst2[boodschap] += 1
        nogiets()
    else:
        lijst2[boodschap]= 1
        nogiets()

boodschaplijst()
