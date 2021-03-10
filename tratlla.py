import random
def drawBoard(l,n):
    if len(l)!=9:
        print ("Error! Board badly designed!")
    else:
        print ("Turn number:",n)
        print ("============")
        print ("   "+"|"+"   "+"|"+"   ")
        print (" " + l[6] + " " + "|" +" " + l[7] + " " +  "|" +" " + l[8] + " ")
        print ("   "+"|"+"   "+"|"+"   ")
        print ("------------")
        print ("   "+"|"+"   "+"|"+"   ")
        print (" " + l[3] + " " + "|" +" " + l[4] + " " +  "|" +" " + l[5] + " ")
        print ("   "+"|"+"   "+"|"+"   ")
        print ("------------")
        print ("   "+"|"+"   "+"|"+"   ")
        print (" " + l[0] + " " + "|" +" " + l[1] + " " +  "|" +" " + l[2] + " ")
        print ("   "+"|"+"   "+"|"+"   ")
        print ("============")
   

def chooseInitialPlayer():
    t=random.randint(0,1)
    if t==1:
        return "Player"
    else:
        return "Computer" 

    
    
def isAFreeSpace(l,n):
    if len(l)>n:
        if l[n]==" ":
            return True
        else:
            return False
    else:
        return False
'''      
def fullBoard(l):
    for s in l:
        if s in " ":
            return False
        else: 
            return True
'''  
def fullBoard(l):
  for s in l:
    if s == " ":
      return False
  return True     
def applyPlay(jug,l,lletra,n):
    print (jug,"ocupies position",n)
    l[n]=lletra
    return l

def isAWonPlay(l,i):
    if l[1]==i and l[4]==i and l[7]==i or l[0]==i and l[3]==i and l[6]==i or l[2]==i and l[5]==i and l[8]==i or l[6]==i and l[7]==i and l[8]==i or l[3]==i and l[4]==i and l[5]==i or l[0]==i and l[1]==i and l[2]==i or l[0]==i and l[4]==i and l[8]==i or l[2]==i and l[4]==i and l[6]==i:
        return True
    else:
        return False


def randomPlay(l):
    if not (" " in l):
        return -1
    else:
        r=random.randint(0,len(l)-1)
        while l[r]!=" ":
            r=random.randint(0,len(l)-1)
    
        return r
    

        
        
def play(l):
    t=input("Choose position to play (0-8)")
    while t not in "012345678" or not isAFreeSpace(l,int(t)):
        print ("We are sorry. This position is not valid.")
        t=input("Choose position to play (0-8)")
    return int(t)


def chooseLetterPlayer():
    u=input("Choose between X or O: ")
    while u not in "XO":
        print ("We are sorry. This letter is not valid.")
        u=input("Choose between X or O: ")
    p="X"
    if p not in u:
        p="X"
    else:
        p="O"
    i=u
    a=[i,p]
    return a

def playAgain():
    u=input("Do you want to play another game? (y / n)")
    while u not in "yn":
        print ("We are sorry. This option is not valid.")
        u=input("Do you want to play another game? (y / n)")
    if u in "y":
        return True
    else:
        return False
    
def startBoard():
    return [" "," "," "," "," "," "," "," "," "]
    
    
def game():
    t=startBoard()
    p=chooseLetterPlayer()
    ip=chooseInitialPlayer()
    i=1
    if ip=="Computer":
        cosa=p[1]
    else:
        cosa=p[0]
    drawBoard(t,i)
    while not isAWonPlay(t,cosa) and not fullBoard(t):
        if ip=="Player":
            Play=play(t)
            t=applyPlay(ip,t,cosa,Play)
            drawBoard(t,i)
            if isAWonPlay(t,cosa):
                print ("Falicitats has guanyat a una maquina amb una inteligencia basicament random! Segur que totom et guanyara ;D")
                result=0
            elif fullBoard(t):
                print ("wow has empatat, has jugat fatal! Impresionant! :>")
                result=1
            else:
                ip="Computer"
                cosa=p[1]
                i=i+1
        else:
            Play=randomPlay(t)
            t=applyPlay(ip,t,cosa,Play)
            drawBoard(t,i)
            if isAWonPlay(t,cosa):
                print ("Falicitats has perdut contra una maquina amb inteligencia random! Ves a jugar MINECRAFT millor.")
                result=2
            elif fullBoard(t):
                print ("wow has empatat, has jugat fatal! Impresionant! :>")
                result=1
            else:
                ip="Player"
                cosa=p[0]
                i=i+1
    return result
#game()