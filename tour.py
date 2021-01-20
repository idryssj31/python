from random import *


# Petite précision si le joueur na plus d'argent il ne peut pas avancé
#exemple il lui reste 2€ case 5 il fait 3 aux dés et la prochaine case est une soustraction alors game over il termine avec -1€ case 5 l'adittion des cases ne ceux fait que si il a minimun 1€.
#Bonne correction

def gameplay():

    

    # On définie les joueurs ainsi que leurs argents.
    player1 = randint(1,10)
    player2 = randint(1,10)

    # On définie les deux dés dé à 6 face .
    dé1 = randint(1,3)
    dé2 = randint(1,3)

    #système de case
    case = randint(1,5)

    # Le résultat des deux dé.
    dé3 = dé1 + dé2

    #l'emplacement de la case.
    nbrcase = dé3

    # Resultat de l adition argent et dé
    résultat1 = player1 + dé3




    # case qui soustrait ou ajoute
    if case > 3:
        #dans ceux cas la soustrait
        résultat1 = player1 - dé3
        print("le joueur1 a ",player1, "€ sur lui il lance les deux dés et fait",dé3,"cepandant il est sur une case qui soustrait ainsi il lui reste plus que",résultat1, "€ il termine le tour sur la case",nbrcase,)
        
        if résultat1 < 1:
            print("le player1 termine le jeux avec ",résultat1,"€ en poche sur la case",nbrcase)
            
        
                    
    else:
        #dans ceux cas la ajoute
        print("le joueur1 a",player1, "€ sur lui il lance les deux dés et fait",dé3,"dorénavant il à",résultat1, "€ il termine le tour sur la case",nbrcase,)
    

        if résultat1 > 0:
            
            while résultat1 > 0:
                

                #nouvelle valeur du joueur apres le premier tour
                player1 = résultat1
                #print(résultat1,player1,)

                #système de case
                case = randint(1,5)

                # On définie les deux dés dé à 6 face .
                dé1 = randint(1,3)
                dé2 = randint(1,3)
                # Le résultat des deux dé.
                dé3 = dé1 + dé2

                

                # case qui soustrait ou ajoute
                if case > 3:

                    #dans ceux cas la soustrait
                    résultat1 = player1 - dé3
                    print("Le joueur1 a ",player1, "€ sur lui il lance les deux dés et fait",dé3,"cepandant il est sur une case qui soustrait ainsi il lui reste plus que",résultat1, "€ il termine le tour sur la case",nbrcase+dé3,)
                    
                    if résultat1 < 1:
                        print("Le player1 termine le jeux avec  ",résultat1,"€ en poche sur la case",nbrcase+dé3,)
                    

                else:
                    
                    #dans ceux cas la ajoute
                    print("Le joueur1 a",player1, "€ sur lui il lance les deux dés et fait",dé3,"dorénavant il à",résultat1, "€ il termine le tour sur la case",nbrcase+dé3,)
                    #print(player1,résultat1)



#joueur 2


    # On définie les deux dés dé à 6 face .
    dé11 = randint(1,3)
    dé22 = randint(1,3)

    #système de case
    casee = randint(1,5)

    # Le résultat des deux dé.
    dé33 = dé11 + dé22

    #l'emplacement de la case.
    nbrcases = dé33

    # Resultat de l adition argent et dé
    résultat11 = player2 + dé33




    # case qui soustrait ou ajoute
    if casee > 3:
        #dans ceux cas la soustrait
        résultat11 = player2 - dé33
        print("le joueur2 a ",player2, "€ sur lui il lance les deux dés et fait",dé33,"cepandant il est sur une case qui soustrait ainsi il lui reste plus que",résultat11, "€ il termine le tour sur la case",nbrcases,)
            
        if résultat11 < 1:
            print("le player2 termine le jeux avec ",résultat11,"€ en poche sur la case",nbrcases)
            
            
                        
    else:
        #dans ceux cas la ajoute
        print("le joueur2 a",player2, "€ sur lui il lance les deux dés et fait",dé33,"dorénavant il à",résultat11, "€ il termine le tour sur la case",nbrcases,)
        

        if résultat11 > 0:
                
            while résultat11 > 0:
                    

                #nouvelle valeur du joueur apres le premier tour
                player11 = résultat11
                #print(résultat1,player1,)

                #système de case
                casee = randint(1,5)

                # On définie les deux dés dé à 6 face .
                dé11 = randint(1,3)
                dé22 = randint(1,3)
                # Le résultat des deux dé.
                dé33 = dé11 + dé22

                    

                # case qui soustrait ou ajoute
                if casee > 3:

                    #dans ceux cas la soustrait
                    résultat11 = player11 - dé33
                    print("Le joueur2 a ",player11, "€ sur lui il lance les deux dés et fait",dé33,"cepandant il est sur une case qui soustrait ainsi il lui reste plus que",résultat11, "€ il termine le tour sur la case",nbrcases+dé33,)
                        
                    if résultat11 < 1:
                        print("Le player2 termine le jeux avec  ",résultat11,"€ en poche sur la case",nbrcases+dé33,)
                        
                            

                else:
                        
                    #dans ceux cas la ajoute
                    print("Le joueur2 a",player11, "€ sur lui il lance les deux dés et fait",dé33,"dorénavant il à",résultat11, "€ il termine le tour sur la case",nbrcases+dé33,)
                    #print(player1,résultat1)
     
    if nbrcase > nbrcases:
        print("le joueur2 à gagné")
    else:
        print("le joueur1 à gagné")

gameplay()