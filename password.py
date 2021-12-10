import string, random

def generator(Length):
    global special,password

    special = '@#$%_?'
    upperamount = random.randrange(2,6)
    randomnum = random.randrange(4,7)
    loweramount  = Length - (upperamount + randomnum + 3)
    password = []

    password += (random.choices(string.ascii_uppercase, k = upperamount))
    password += (random.choices(string.digits, k = randomnum))
    password += (random.choices(string.ascii_lowercase, k = loweramount)) 
    password += (random.choices(special, k = 3))
    random.shuffle(password)
    checknum()

def checknum():
    for character in password[:3]:
        if character.isnumeric():
            generator(24)
    else:
        checkspecial()

def checkspecial():
    if special in password[0]  and special in password[-1]:
        generator(24)


generator(24)

print(*password, sep="")