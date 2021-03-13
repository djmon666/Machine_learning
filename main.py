from mlnumbers import classifyNumbers, storeNumbers
from mlmodel import trainModel, checkModel





API_KEY="23efcea0-842f-11eb-94af-bda5504cb1aacc63fa83-36ed-45bf-97b9-16bb85d27fea"


# -------------------------------------------------------
# CHECK IF THE MACHINE LEARNING MODEL IS READY TO USE
# -------------------------------------------------------

# you can use this to check if your machine learning model
# has finished training 

status = checkModel(API_KEY)
print (status)



# -------------------------------------------------------
# USE YOUR MACHINE LEARNING MODEL TO RECOGNIZE NUMBERS 
# -------------------------------------------------------

# CHANGE THIS to the data that you want your 
# machine learning model to classify
'''
data1 = "PLAYER"
data2 = "PLAYER"
data3 = "EMPTY"
data4 = "OPPONENT"
data5 = "OPPONENT"
data6 = "PLAYER"
data7 = "PLAYER"
data8 = "PLAYER"
data9 = "PLAYER"

test_data = [ data1, data2, data3, data4, data5, data6, data7, data8, data9 ]

#demo = classifyNumbers(API_KEY, test_data)

#label = demo["class_name"]
#confidence = demo["confidence"]

# CHANGE THIS to do something different with the result
#print ("result: '%s' with %d%% confidence" % (label, confidence))
'''



# -------------------------------------------------------
# ADD TRAINING EXAMPLES TO YOUR MACHINE LEARNING PROJECT
# -------------------------------------------------------

# CHANGE THIS to the data that you want to add 
# to your project training data
'''
data1 = "OPPONENT"
data2 = "OPPONENT"
data3 = "EMPTY"
data4 = "EMPTY"
data5 = "EMPTY"
data6 = "PLAYER"
data7 = "PLAYER"
data8 = "OPPONENT"
data9 = "PLAYER"

training_data = [ data1, data2, data3, data4, data5, data6, data7, data8, data9 ]


# CHANGE THIS to the training bucket to add the
# training example to
training_label = "top_right"

# remove the comment on the next line to use this 
#storeNumbers(API_KEY, training_data, training_label)
'''



# -------------------------------------------------------
# TRAIN A NEW MACHINE LEARNING MODEL
# -------------------------------------------------------

# after collecting new training examples, you can use 
# to train a new machine learning model 

# remove the comment on the next line to use this 
#trainModel(API_KEY)


import random
def menu():
    print ("Menu")
    print ("1. Jugar")
    print ("2. Entrenar")
    print ("3. Estadístiques")
    print ("4. Sortir")
    pos =input("Tria opció:")
    while not(int(pos)>=1 and int(pos)<=4):
        print ("Opció incorrecta")
        pos = input("Tria opció:")
    return pos
    

def drawBoard(l,n):
    if len(l)!=9:
        print ("Error! Panell mal fet!")
    else:
        print ("Torn número:",n)
        print ("============")
        print ("   "+"|"+"   "+"|"+"   ")
        print (" " + l[0] + " " + "|" +" " + l[1] + " " +  "|" +" " + l[2] + " ")
        print ("   "+"|"+"   "+"|"+"   ")
        print ("------------")
        print ("   "+"|"+"   "+"|"+"   ")
        print (" " + l[3] + " " + "|" +" " + l[4] + " " +  "|" +" " + l[5] + " ")
        print ("   "+"|"+"   "+"|"+"   ")
        print ("------------")
        print ("   "+"|"+"   "+"|"+"   ")
        print (" " + l[6] + " " + "|" +" " + l[7] + " " +  "|" +" " + l[8] + " ")
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
    if jug == "Player":
      jug = "Jugador"
    else :
      jug = "Màquina"
    print (jug,"ocupa la posició",n)
    l[n]=lletra
    return l

def isAWonPlay(l,i):
    if l[1]==i and l[4]==i and l[7]==i or l[0]==i and l[3]==i and l[6]==i or l[2]==i and l[5]==i and l[8]==i or l[6]==i and l[7]==i and l[8]==i or l[3]==i and l[4]==i and l[5]==i or l[0]==i and l[1]==i and l[2]==i or l[0]==i and l[4]==i and l[8]==i or l[2]==i and l[4]==i and l[6]==i:
        return True
    else:
        return False
def data_form(l,player):
  result=[]
  for e in l:
    if e == player[0]:
      result.append("PLAYER")
    elif e == player[1]:
      result.append("OPPONENT")
    else:
      result.append("EMPTY")
  return result
def data_rec(s):
  if s == "top_left":
    return 0
  elif s == "top_middle":
    return 1
  elif s == "top_right":
    return 2
  elif s == "middle_left":
    return 3
  elif s == "middle_middle":
    return 4
  elif s == "middle_right":
    return 5
  elif s == "bottom_left":
    return 6
  elif s == "bottom_middle":
    return 7
  elif s == "bottom_right":
    return 8
  else:
    return "ERROR"
def data_send(s):
  if s == 0:
    return "top_left"
  elif s == 1:
    return "top_middle"
  elif s == 2:
    return "top_right"
  elif s == 3:
    return "middle_left"
  elif s == 4:
    return "middle_middle"
  elif s == 5:
    return "middle_right"
  elif s == 6:
    return "bottom_left"
  elif s == 7:
    return "bottom_middle"
  elif s == 8:
    return "bottom_right"
  else:
    return "ERROR"
  '''
def randomPlay(l):
    if not (" " in l):
        return -1
    else:
        r=random.randint(0,len(l)-1)
        while l[r]!=" ":
            r=random.randint(0,len(l)-1)
    
        return r
  '''
def randomPlay(l,player):
    if not (" " in l):
        return -1
    else:
        test_data= data_form(l,player)
        #print (test_data)
        demo = classifyNumbers(API_KEY, test_data)
        label = demo["class_name"]
        times=0
        while not isAFreeSpace(l,data_rec(label))and times<3:
          test_data= data_form(l,player)
          #print (test_data)
          demo = classifyNumbers(API_KEY, test_data)
          label = demo["class_name"]
          #print (label)
          #print (data_rec(label))
          times +=1
        if times==3:
          r=random.randint(0,len(l)-1)
          while l[r]!=" ":
            r=random.randint(0,len(l)-1)
          print("Posició Random")
          return r
        else:
          return data_rec(label)
    

        
        
def play(l):
    t=input("Tria posició per jugar (0-8)")
    while t not in "012345678" or not isAFreeSpace(l,int(t)):
        print ("Ho sentim, aquesta posició no és vàlida.")
        t=input("Tria posició per jugar (0-8)")
    return int(t)


def chooseLetterPlayer():
    u=input("Tria entre la X o la O: ")
    while u not in "XO" or len(u)!=1 :
        print ("Ho sento. La lletra entrada no és vàlida.")
        u=input("Tria entre la X o la O: ")
    p="X"
    if p not in u:
        p="X"
    else:
        p="O"
    i=u
    a=[i,p]
    return a

def playAgain():
    u=input("Vols jugar una altra vegada? (y / n)")
    while u not in "yn":
        print ("Ho sento. La opció no és vàlida")
        u=input("Vols jugar una altra vegada? (y / n)")
    if u in "y":
        return True
    else:
        return False
    
def startBoard():
    return [" "," "," "," "," "," "," "," "," "]
def statistics(wg, lg, tg):
    suma=wg+lg+tg
    print ("Estadístiques:")
    print ("- Nombre de jocs jugats:",suma)
    print ("- Nombre de jocs guanyats:",wg)
    print ("- Nombre de jocs perduts:",lg)
    print ("- Nombre de jocs empatats:",tg)
    
   
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
            panell=[] 
            panell=t.copy()
            #print ( "Aquest és l'enviament:",panell)
            Play=play(t)
            t=applyPlay(ip,t,cosa,Play)
            drawBoard(t,i)
            if train:
              print("Entrenem la màquina amb aquestes posicions: ",panell)
              storeNumbers(API_KEY, data_form(panell,p),data_send(Play) )
            if isAWonPlay(t,cosa):
                print ("Felicitats, has guanyat. Entrenarem a la màquina amb els resultats")
                storeNumbers(API_KEY, data_form(panell,p),data_send(Play) )
                trainModel(API_KEY)
                result=1
            elif fullBoard(t):
                print ("wow has empatat, has jugat fatal! :>")
                result=0
            else:
                ip="Computer"
                cosa=p[1]
                i=i+1
        else:
            Play=randomPlay(t,p)
            t=applyPlay(ip,t,cosa,Play)
            drawBoard(t,i)
            if isAWonPlay(t,cosa):
                print ("Sembla que la intel·ligència Artificial t'ha guanyat.")
                result=2
            elif fullBoard(t):
                print ("wow has empatat, has jugat fatal! Impresionant! :>")
                result=0
            else:
                ip="Player"
                cosa=p[0]
                i=i+1
    return result
print ("Aquest és el joc del 3 en ratlla:")
wg=0

lg=0

tg=0

op = int(menu())
while op!=4:
  train= False
  if op==1:
    g=game()
    if g==1:
      wg+=1
    elif g==2:
      lg+=1
    else:
      tg+=1
  elif op==2:
    train= True
    print(status)
    g=game()
    if g==1:
      wg+=1
    elif g==2:
      lg+=1
    else:
      tg+=1
  elif op==3:
    statistics(wg,lg,tg)
  else:
    print ("Opció incorrecta!")
  op = int(menu())
print ("Gràcies per jugar")