from gtts import gTTS
import os

def loe_failist(x:str):
    with open(x,"r",encoding="utf-8-sig") as f:
        jarjend=[]
        for rida in f:
            jarjend.append(rida.strip()) 
        return jarjend 

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3") 
    os.system("heli.mp3")


def tolkimine(rus,est):
    sona=input("Kirjutage sõna, mida soovite tõlkida ")
    while sona.isdigit():
        sona=input("Kirjuta õige sõna")
    if sona not in rus and sona not in est:
        print("Seda sõna pole sõnastikus ")
        vale=input("Kas soovite selle sõna sõnaraamatusse lisada? (jah või ei) ").lower() 
        while vale not in ["jah","ei"]:
            vale=input("Kirjuta ainult jah või ei ") 
        if vale=="jah":
            if rustaht(sona)==True:
                rus.append(sona)
                tolke=input("Kirjutage sõna tõlge ") 
                while tolke.isdigit():
                    tolke=input("Kirjuta õige sõna ")
                est.append(tolke)
            else: 
                est.append(sona)
                tolke=input("Kirjutage sõna tõlge ") 
                while tolke.isdigit():
                    tolke=input("Kirjuta õige sõna ")
                rus.append(sona)
        else:
            print("Olgu, hüvasti")
    for i in range(len(rus)):
        if sona==rus[i]:
            print(f"{rus[i]} - {est[i]}")
            heli(est[i],"et")
        elif sona==est[i]:
            print(f"{est[i]} - {rus[i]}")
            heli(rus[i],"ru") 
    for i in range(len(rus)):
        rus[i]=rus[i]+"\n"
    with open('rus.txt',"w",encoding="utf-8-sig") as j:
        j.writelines(rus)
    for i in range(len(est)):
        est[i]=est[i]+"\n"
    with open('est.txt',"w",encoding="utf-8-sig") as j:
        j.writelines(est)

def rustaht(x:str):
    rusl=['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    rusl1=[x.upper() for x in rusl1] 
    rusl2=rusl1+rusl
    xa=list(x)
    for i in range(len(xa)):
        if xa[i] not in rusl2:
            return False
    return True

def esttaht(x:str):
    estl=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    estl1=[x.upper() for x in estl1] 
    estl2=estl+estl1
    xa=list(x)
    for i in range(len(xa)):
        if xa[i] not in estl2:
            return False
    return True

def paranda(fail1:str,fail2:str):
    rus=[] 
    est=[]
    f=open(fail1,'r',encoding="utf-8-sig")
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for line in f:
        est.append(line.strip()) 
    f.close()
    keel=input("Kas parandame vene või eesti sõnaraamatus? ").lower()
    while keel not in ["vene","eesti"]:
        keel=input("Kirjuta vene või eesti ")
    if keel=="vene":
        indv=input("Millist sõna soovite parandada? ")
        while indv not in rus:
            indv=input("Kirjutage õige sõna ")
        for i in range(len(rus)):
            if indv==rus[i]:
                ind=rus.index(indv) 
        parasona=input("Kirjutage parandatud sõna ")
        while parasona.isdigit():
            parasona=input("Kirjutage õige sõna ")
        rus[ind]=parasona
        for i in range(len(rus)):
            rus[i]=rus[i]+"\n"
        f=open(fail1,"w",encoding="utf-8-sig")
        f.writelines(rus)
        f.close()
    else:
        indv=input("Millist sõna soovite parandada? ")
        while indv not in est:
            indv=input("Kirjutage õige sõna ")
        for i in range(len(rus)):
            if indv==est[i]:
                ind=est.index(indv) 
        parasona=input("Kirjutage parandatud sõna ")
        while parasona.isdigit():
            parasona=input("Kirjutage õige sõna ")
        est[ind]=parasona
        for i in range(len(rus)):
            est[i]=est[i]+"\n"
        f=open(fail2,"w",encoding="utf-8-sig")
        f.writelines(est)
        f.close()

def harjutus(fail1:str,fail2:str):
    rus=[] 
    est=[]
    game=[] 
    a=[]
    v=0
    f=open(fail1,'r',encoding="utf-8-sig")
    for line in f:
        rus.append(line.strip())
    f.close()
    f=open(fail2,'r',encoding="utf-8-sig")
    for line in f:
        est.append(line.strip()) 
    f.close()
    num=int(input("Mitu korda soovite kontrollida? "))
    for i in num:
        keel=input("Mis keeles treenime? (vene või eesti) ").lower()
        while keel not in ["vene","eesti"]:
            keel=input("Kirjutage ainult vene või eesti ").lower() 
        if keel=="vene":
            rana=rus[num] 
            tolk=input(f"Mis on sõna {rana} tõlge? ") 
            if tolk==est[num]:
                game.append(f"{i+1} {keel} mäng - võit")
                print("Võit") 
                v+=1
            else:
                game.append(f"{i+1}, {keel} mäng - kaotus") 
                print("Kaotus")
        else:
            rana=est[num] 
            tolk=input(f"Mis on sõna {rana} tõlge? ") 
            if tolk==rus[num]:
                game.append(f"{i+1} {keel} mäng - võit")
                print("Võit")
                v+=1
            else:
                game.append(f"{i+1}, {keel} mäng - kaotus") 
                print("Kaotus")
        a.append(num)
    print(game)
    protsent=round((v/num*100),1)
    print(f"Võiduprotsent - {protsent}")

def salvesta(x:str,y:list):
    f=open(x,"w",encoding="utf-8-sig")
    for line in y:
        f.write(line+"\n")
    f.close()
