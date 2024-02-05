import random

print("Pexsaso")
znak1 = ":)"
znak2 = ":("
znak3 = ":O"
znak4 = ":D"
znak5 = ":/"
znak6 = ":|"
znak7 = ":*"
znak8 = ":3"
znak9 = ":)"
znak10 = ":("
znak11 = ":O"
znak12 = ":D"
znak13 = ":/"
znak14 = ":|"
znak15 = ":*"
znak16 = ":3"



znaky1= [znak1 , znak2 , znak3 , znak4 , znak5, znak6, znak7, znak8, znak9 , znak10 , znak11 , znak12 , znak13, znak14, znak15, znak15]


znak = str(random.choice(znaky1))
A1 = znak
znaky1.remove(znak)


znak = str(random.choice(znaky1))
A2 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
A3 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
A4 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
B1 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
B2 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
B3 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
B4 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
C1 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
C2 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
C3 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
C4 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
D1 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
D2 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
D3 = znak
znaky1.remove(znak)

znak = str(random.choice(znaky1))
D4 = znak
znaky1.remove(znak)


A1save = A1
A2save = A2
A3save = A3
A4save = A4

B1save = B1
B2save = B2
B3save = B3
B4save = B4

C1save = C1
C2save = C2
C3save = C3
C4save = C4

D1save = D1
D2save = D2
D3save = D3
D4save = D4




A1 = "  "
A2 = "  "
A3 = "  "
A4 = "  "

B1 = "  "
B2 = "  "
B3 = "  "
B4 = "  "

C1 = "  "
C2 = "  "
C3 = "  "
C4 = "  "

D1 = "  "
D2 = "  "
D3 = "  "
D4 = "  "

score1= 0
score2=0
int(score1)
int(score2)

end=False
cislo = True



def Pole():    
    print(f"   ║ 1  ║ 2  ║ 3  ║ 4  ║")
    print(f"═══╬════╬════╬════╬════╣")
    print(f" A ║ {A1} ║ {A2} ║ {A3} ║ {A4} ║")
    print(f"═══╬════╬════╬════╬════╣")
    print(f" B ║ {B1} ║ {B2} ║ {B3} ║ {B4} ║")
    print(f"═══╬════╬════╬════╬════╣")
    print(f" C ║ {C1} ║ {C2} ║ {C3} ║ {C4} ║")
    print(f"═══╬════╬════╬════╬════╣")
    print(f" D ║ {D1} ║ {D2} ║ {D3} ║ {D4} ║")
    print(f"═══╩════╩════╬════╩════╝")
    print(f"Player1 : {score1}  ║Player2 : {score2}  ")


while end == False:
    Pole()
    
    cislo = True
    pismeno = True
    
    print(" ")
    print("Player 1:")
    for i in range(2):
        while cislo == True:
            volba1=int(input("Zvolte číslici 1 - 4 :"))
            if volba1 < 1 or volba1 >4:
                print("Zadlai jste špatnou možnost")
            else:
                cislo=False
        
        while pismeno == True:
            volba2=str(input("Zvolte písmenko A - D (velký písmo):"))
            if volba2 == "A" or volba2=="B" or volba2 == "C" or volba2=="D":
                pismeno= False
            else:
                print("Zadlai jste špatnou možnost")
        
        if volba1 == 1:
            if volba2 == "A":
                A1 = A1save
            elif volba2 == "B":
                B1 = B1save
            elif volba2 == "C":
                C1 = C1save
            elif volba2 == "D":        
                D1 = D1save
        
        elif volba1 == 2:
            
            if volba2 == "A":
                A2 = A2save
            elif volba2 == "B":
                B2 = B2save
            elif volba2 == "C":
                C2 = C2save
            elif volba2 == "D":        
                D2 = D2save              
        
        elif volba1 == 3:
            
            if volba2 == "A":
                A3 = A3save
            elif volba2 == "B":
                B3 = B3save
            elif volba2 == "C":
                C3 = C3save
            elif volba2 == "D":        
                D3 = D3save         
        
        elif volba1 == 4:       
            
            if volba2 == "A":
                A4 = A4save
            elif volba2 == "B":
                B4 = B4save
            elif volba2 == "C":
                C4 = C4save
            elif volba2 == "D":        
                D4 = D4save


    




    
    