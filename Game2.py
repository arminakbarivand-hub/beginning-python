import random

def valid (x):
    try:
        x =int(x)
    except ValueError:
        print ("meghdar vared shode eshtebah ast lotfan adad sahih vared konid")
        return False
    return True 


def Game ():
    number= random.randint(1,1000)
    while True:
        x = int(input("yek adad az 1 ta 1000 entekhab konid"))
        if valid(x)==True : 
            if x < number : 
                int(x= input("adad vared shode kochak bod"))
                if valid(x) == False  :
                    continue 
            if x > number : 
                int(x= input("adad vared shode bozorg bod"))
                if valid(x) == False  :
                    continue 
            else : 
                print("mashti dorost gofti")  
                break
        else : continue

Game()            