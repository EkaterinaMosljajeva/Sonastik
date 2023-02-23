from moodul import *
laused=[]
while True:
    est=open('est.txt','r',encoding="utf-8-sig")
    rus=open('rus.txt','r',encoding="utf-8-sig")
    menu=int(input("1-Vaata sõnastikku\n2-Sõnade tõlkimine\n3-Tekst helisse\n4-Parandage viga sõnastikus\n5-Harjutus\n"))
    if menu==0:
        break
    elif menu==1:
        laused=loe_failist("est.txt")
        for line in laused:
            print(line)
        print()
        laused=loe_failist("rus.txt")
        for line in laused:
            print(line)
    elif menu==2:
        tolkimine(rus,est)
    elif menu==3:
        text=""
        for line in laused:
            text=text+" "+line 
        heli(text,"et")
    elif menu==4:
        paranda("rus.txt","est.txt")
    elif menu==5:
        harjutus("rus.txt","est.txt")

