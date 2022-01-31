import random

maxgame = 28
mprok = 2
repeat = 1000
insgesamt = 0
maxcards = 0
mincards = 60
def runde():
    global maxgame
    global mprok
    global insgesamt
    global maxcards
    global mincards
    team1 = 0
    team2 = 0
    kartengebraucht = 0
    while team1 < maxgame and  team1 < maxgame:
        karte = random.randint(0,1)+2
        if random.randint(0,2) >= 1:
            team1 += karte

        karte = random.randint(0,1) + 2
        if random.randint(0,2) >= 1:
            team2 += karte

        kartengebraucht += 2
        if team1 == team2:
            if random.randint(0,1):
                team1 -= 1

            else:
                team2 -= 1

    ereignis = random.randint(0, 11)

    if ereignis == 0:
        team1 += 2
    elif ereignis == 1:
        team2 += 2
    elif ereignis == 2:
        team2 -= 1
    elif ereignis == 3:
        team2 -= 1
    elif ereignis == 9:
        team2 += 4
    elif ereignis == 10:
        team2 += 4
    insgesamt += kartengebraucht
    if kartengebraucht > maxcards:
        maxcards = kartengebraucht
    if kartengebraucht < mincards:
        mincards = kartengebraucht
    print("Team1: " + str(team1) + " Team2: " + str(team2))
for x in range(repeat):
    runde()

print("-Karten Gesamt: " + str(insgesamt/repeat))
print("-Zeit Normal: " + str((insgesamt*2)/repeat)+" Minuten")
print("Zeit Schnell: " + str((insgesamt*1.5)/repeat)+" Minuten")
print("Zeit Langsam: " + str((insgesamt*3)/repeat)+" Minuten")
print("Längstes Spiel "+str(maxcards)+" Karten")
print("Kürzestes Spiel "+str(mincards)+" Karten")
