var = True
chim = False
phy = False
math = False
inf = False
while not chim:
    chim = int(input())
    if not (0<=chim<=20):
        chim = False

while not phy:       
    phy = int(input())
while not math:
    math = int(input())
while not info:
    info = int(input())

moyenne = (chim*3+phy*4+math*2+info*2)/11
    




