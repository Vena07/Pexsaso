import random
import time

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
    for i in range(100):
        print(" ")
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
    kolo = 1
    while kolo ==1:
        kolo -= 1
        choice=[]
        choice1 = []
        
        Pole() 
        
        cislo = True
        pismeno = True
        vyber = True
        
        print(" ")
        print("Player 1:")
        for i in range(2):
            vyber = True
            cislo = True
            pismeno = True
            while vyber == True:
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
                        if A1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

                elif volba1 == 2:
                    if volba2 == "A":
                        if A2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

                elif volba1 == 3:
                    if volba2 == "A":
                        if A3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

                elif volba1 == 4:
                    if volba2 == "A":
                        if A4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

        
            if volba1 == 1:
                if volba2 == "A":
                    A1 = A1save
                    choice.append(A1save)
                    choice1.append("A1")
                elif volba2 == "B":
                    B1 = B1save
                    choice.append(B1save)
                    choice1.append("B1")
                elif volba2 == "C":
                    C1 = C1save
                    choice.append(C1save)
                    choice1.append("C1")
                elif volba2 == "D":
                    D1 = D1save
                    choice.append(D1save)
                    choice1.append("D1")

            elif volba1 == 2:
                if volba2 == "A":
                    A2 = A2save
                    choice.append(A2save)
                    choice1.append("A2")
                elif volba2 == "B":
                    B2 = B2save
                    choice.append(B2save)
                    choice1.append("B2")
                elif volba2 == "C":
                    C2 = C2save
                    choice.append(C2save)
                    choice1.append("C2")
                elif volba2 == "D":
                    D2 = D2save
                    choice.append(D2save)
                    choice1.append("D2")

            elif volba1 == 3:
                if volba2 == "A":
                    A3 = A3save
                    choice.append(A3save)
                    choice1.append("A3")
                elif volba2 == "B":
                    B3 = B3save
                    choice.append(B3save)
                    choice1.append("B3")
                elif volba2 == "C":
                    C3 = C3save
                    choice.append(C3save)
                    choice1.append("C3")
                elif volba2 == "D":
                    D3 = D3save
                    choice.append(D3save)
                    choice1.append("D3")

            elif volba1 == 4:
                if volba2 == "A":
                    A4 = A4save
                    choice.append(A4save)
                    choice1.append("A4")
                elif volba2 == "B":
                    B4 = B4save
                    choice.append(B4save)
                    choice1.append("B4")
                elif volba2 == "C":
                    C4 = C4save
                    choice.append(C4save)
                    choice1.append("C4")
                elif volba2 == "D":
                    D4 = D4save
                    choice.append(D4save)
                    choice1.append("D4")


        
        if choice[0] == choice[1]:
            Pole()
            kolo += 1
            score1 += 1 
            print(" ")
            print("Gratuluji, našli jste stejné políčka!!")
        else:
            Pole()
            print(" ")
            print("Bouhžle se políčka neschodují.")
            print("Zapamatujte si nově zobrazená políčka , zanedlouho opět zmizí")
        
            if choice1[0] == "A1":
                A1 = "  " 
            elif choice1[0] == "B1":
                B1 = "  "
            elif choice1[0] == "C1":
                C1 = "  "      
            elif choice1[0] == "D1":
                D1 = "  "

            elif choice1[0] == "A2":
                A2 = "  "
            elif choice1[0] == "B2":
                B2 = "  "
            elif choice1[0] == "C2":
                C2 = "  "
            elif choice1[0] == "D2":
                D2 = "  "

            elif choice1[0] == "A3":
                A3 = "  "
            elif choice1[0] == "B3":
                B3 = "  "
            elif choice1[0] == "C3":
                C3 = "  "
            elif choice1[0] == "D3":
                D3 = "  "

            elif choice1[0] == "A4":
                A4 = "  "
            elif choice1[0] == "B4":
                B4 = "  "
            elif choice1[0] == "C4":
                C4 = "  "
            elif choice1[0] == "D4":
                D4 = "  "
            
            if choice1[1] == "A1":
                A1 = "  " 
            elif choice1[1] == "B1":
                B1 = "  "
            elif choice1[1] == "C1":
                C1 = "  "      
            elif choice1[1] == "D1":
                D1 = "  "

            elif choice1[1] == "A2":
                A2 = "  "
            elif choice1[1] == "B2":
                B2 = "  "
            elif choice1[1] == "C2":
                C2 = "  "
            elif choice1[1] == "D2":
                D2 = "  "

            elif choice1[1] == "A3":
                A3 = "  "
            elif choice1[1] == "B3":
                B3 = "  "
            elif choice1[1] == "C3":
                C3 = "  "
            elif choice1[1] == "D3":
                D3 = "  "

            elif choice1[1] == "A4":
                A4 = "  "
            elif choice1[1] == "B4":
                B4 = "  "
            elif choice1[1] == "C4":
                C4 = "  "
            elif choice1[1] == "D4":
                D4 = "  "


        
        
        
        
        
        time.sleep(5)        

        if score1 + score2 == 8:
            end=True
            
            Pole()
            
            print("Konec hry!! Všechna stejná pole byla oběvena! Gratuliji výherci")
            
    kolo = 1
    while kolo ==1:
        kolo -= 1
        choice=[]
        choice1 = []
        
        Pole() 
        
        cislo = True
        pismeno = True
        vyber = True
        
        print(" ")
        print("Player 2:")
        for i in range(2):
            vyber = True
            cislo = True
            pismeno = True
            while vyber == True:
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
                        if A1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D1 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

                elif volba1 == 2:
                    if volba2 == "A":
                        if A2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D2 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

                elif volba1 == 3:
                    if volba2 == "A":
                        if A3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D3 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

                elif volba1 == 4:
                    if volba2 == "A":
                        if A4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "B":
                        if B4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "C":
                        if C4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True
                    elif volba2 == "D":
                        if D4 == "  ":
                            vyber = False
                        else:
                            print("Vybrali jste už dávno nalezené políčko, vyberte jiné")
                            cislo = True
                            pismeno = True

        
            if volba1 == 1:
                if volba2 == "A":
                    A1 = A1save
                    choice.append(A1save)
                    choice1.append("A1")
                elif volba2 == "B":
                    B1 = B1save
                    choice.append(B1save)
                    choice1.append("B1")
                elif volba2 == "C":
                    C1 = C1save
                    choice.append(C1save)
                    choice1.append("C1")
                elif volba2 == "D":
                    D1 = D1save
                    choice.append(D1save)
                    choice1.append("D1")

            elif volba1 == 2:
                if volba2 == "A":
                    A2 = A2save
                    choice.append(A2save)
                    choice1.append("A2")
                elif volba2 == "B":
                    B2 = B2save
                    choice.append(B2save)
                    choice1.append("B2")
                elif volba2 == "C":
                    C2 = C2save
                    choice.append(C2save)
                    choice1.append("C2")
                elif volba2 == "D":
                    D2 = D2save
                    choice.append(D2save)
                    choice1.append("D2")

            elif volba1 == 3:
                if volba2 == "A":
                    A3 = A3save
                    choice.append(A3save)
                    choice1.append("A3")
                elif volba2 == "B":
                    B3 = B3save
                    choice.append(B3save)
                    choice1.append("B3")
                elif volba2 == "C":
                    C3 = C3save
                    choice.append(C3save)
                    choice1.append("C3")
                elif volba2 == "D":
                    D3 = D3save
                    choice.append(D3save)
                    choice1.append("D3")

            elif volba1 == 4:
                if volba2 == "A":
                    A4 = A4save
                    choice.append(A4save)
                    choice1.append("A4")
                elif volba2 == "B":
                    B4 = B4save
                    choice.append(B4save)
                    choice1.append("B4")
                elif volba2 == "C":
                    C4 = C4save
                    choice.append(C4save)
                    choice1.append("C4")
                elif volba2 == "D":
                    D4 = D4save
                    choice.append(D4save)
                    choice1.append("D4")


        
        if choice[0] == choice[1]:
            Pole()
            kolo += 1
            score2 += 1 
            print(" ")
            print("Gratuluji, našli jste stejné políčka!!")
        else:
            Pole()
            print(" ")
            print("Bouhžle se políčka neschodují.")
            print("Zapamatujte si nově zobrazená políčka , zanedlouho opět zmizí")
        
            if choice1[0] == "A1":
                A1 = "  " 
            elif choice1[0] == "B1":
                B1 = "  "
            elif choice1[0] == "C1":
                C1 = "  "      
            elif choice1[0] == "D1":
                D1 = "  "

            elif choice1[0] == "A2":
                A2 = "  "
            elif choice1[0] == "B2":
                B2 = "  "
            elif choice1[0] == "C2":
                C2 = "  "
            elif choice1[0] == "D2":
                D2 = "  "

            elif choice1[0] == "A3":
                A3 = "  "
            elif choice1[0] == "B3":
                B3 = "  "
            elif choice1[0] == "C3":
                C3 = "  "
            elif choice1[0] == "D3":
                D3 = "  "

            elif choice1[0] == "A4":
                A4 = "  "
            elif choice1[0] == "B4":
                B4 = "  "
            elif choice1[0] == "C4":
                C4 = "  "
            elif choice1[0] == "D4":
                D4 = "  "
            
            if choice1[1] == "A1":
                A1 = "  " 
            elif choice1[1] == "B1":
                B1 = "  "
            elif choice1[1] == "C1":
                C1 = "  "      
            elif choice1[1] == "D1":
                D1 = "  "

            elif choice1[1] == "A2":
                A2 = "  "
            elif choice1[1] == "B2":
                B2 = "  "
            elif choice1[1] == "C2":
                C2 = "  "
            elif choice1[1] == "D2":
                D2 = "  "

            elif choice1[1] == "A3":
                A3 = "  "
            elif choice1[1] == "B3":
                B3 = "  "
            elif choice1[1] == "C3":
                C3 = "  "
            elif choice1[1] == "D3":
                D3 = "  "

            elif choice1[1] == "A4":
                A4 = "  "
            elif choice1[1] == "B4":
                B4 = "  "
            elif choice1[1] == "C4":
                C4 = "  "
            elif choice1[1] == "D4":
                D4 = "  "


        
        
        
        
        
        time.sleep(5)        

        if score1 + score2 == 8:
            end=True
            
            Pole()
            
            print("Konec hry!! Všechna stejná pole byla oběvena! Gratuliji výherci")
        




    
    