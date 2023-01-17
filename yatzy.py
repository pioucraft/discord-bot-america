import random


a1 = random.randint(1,6)
a2 = random.randint(1,6)
a3 = random.randint(1,6)
a4 = random.randint(1,6)
a5 = random.randint(1,6)

b1 = random.randint(1,6)
b2 = random.randint(1,6)
b3 = random.randint(1,6)
b4 = random.randint(1,6)
b5 = random.randint(1,6)

point_A = 0
point_B = 0

print("Joueur A: ")
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print("")

print("Joueur B: ")
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

reponse_A = input("Joueuer A voulez-vous rejouer ?"
      "Si oui, dites les numéros à relancer sous cette forme : ex: 3, 5, 1"
      "Si non, appuyez sur 0. ")
if reponse_A == str(a1) + ", " + str(a2) + ", " + str(a3) + ", " + str(a4) + ", " + str(a5):
      a1 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a4 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a2) + ", " + str(a3) + ", " + str(a4):
      a1 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a4 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a2) + ", " + str(a3) + ", " + str(a5):
      a1 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a2) + ", " + str(a4) + ", " + str(a5):
      a1 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      a4 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a3) + ", " + str(a4) + ", " + str(a5):
      a1 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a4 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2) + ", " + str(a3) + ", " + str(a4) + ", " + str(a5):
      a4 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a3) + ", " + str(a4) + ", " + str(a5):
      a4 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2) + ", " + str(a4) + ", " + str(a5):
      a4 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2) + ", " + str(a3) + ", " + str(a5):
      a2 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2) + ", " + str(a3) + ", " + str(a4):
      a4 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a4) + ", " + str(a5):
      a4 = random.randint(1, 6)
      a1 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a3) + ", " + str(a5):
      a3 = random.randint(1, 6)
      a1 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a3) + ", " + str(a4):
      a4 = random.randint(1, 6)
      a1 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a2) + ", " + str(a5):
      a2 = random.randint(1, 6)
      a1 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a2) + ", " + str(a4):
      a4 = random.randint(1, 6)
      a1 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a2) + ", " + str(a3):
      a2 = random.randint(1, 6)
      a1 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a2):
      a1 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a3):
      a1 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a4):
      a1 = random.randint(1, 6)
      a4 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1) + ", " + str(a5):
      a1 = random.randint(1, 6)
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2) + ", " + str(a3):
      a3 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2) + ", " + str(a4):
      a4 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2) + ", " + str(a5):
      a5 = random.randint(1, 6)
      a2 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a3) + ", " + str(a4):
      a4 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a3) + ", " + str(a5):
      a5 = random.randint(1, 6)
      a3 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a4) + ", " + str(a5):
      a5 = random.randint(1, 6)
      a4 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a1):
      a1 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a2):
      a2 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a3):
      a3 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a4):
      a4 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == str(a5):
      a5 = random.randint(1, 6)
      print(a1)
      print(a2)
      print(a3)
      print(a4)
      print(a5)
elif reponse_A == "pair":
    elif str(a1) and str(a2) == 1:
        point_A += 2
    elif str(a1) and str(a3) == 1:
        point_A += 2
    elif str(a1) and str(a4) == 1:
        point_A += 2
    elif str(a1) and str(a5) == 1:
        point_A += 2
    elif str(a2) and str(a3) == 1:
        point_A += 2
    elif str(a2) and str(a4) == 1:
        point_A += 2
    elif str(a2) and str(a5) == 1:
        point_A += 2
    elif str(a3) and str(a4) == 1:
        point_A += 2
    elif str(a3) and str(a5) == 1:
        point_A += 2
    elif str(a4) and str(a5) == 1:
        point_A += 2
    elif str(a1) and str(a2) == 2:
    point_A += 2
    elif str(a1) and str(a3) == 2:
        point_A += 2
    elif str(a1) and str(a4) == 2:
        point_A += 2
    elif str(a1) and str(a5) == 2:
        point_A += 2
    elif str(a2) and str(a3) == 2:
        point_A += 2
    elif str(a2) and str(a4) == 2:
        point_A += 2
    elif str(a2) and str(a5) == 2:
        point_A += 2
    elif str(a3) and str(a4) == 2:
        point_A += 2
    elif str(a3) and str(a5) == 2:
        point_A += 2
    elif str(a4) and str(a5) == 2:
        point_A += 2
    elif str(a1) and str(a2) == 3:
        point_A += 2
    elif str(a1) and str(a3) == 3:
        point_A += 2
    elif str(a1) and str(a4) == 3:
        point_A += 2
    elif str(a1) and str(a5) == 3:
        point_A += 2
    elif str(a2) and str(a3) == 3:
        point_A += 2
    elif str(a2) and str(a4) == 3:
        point_A += 2
    elif str(a2) and str(a5) == 3:
        point_A += 2
    elif str(a3) and str(a4) == 3:
        point_A += 2
    elif str(a3) and str(a5) == 3:
        point_A += 2
    elif str(a4) and str(a5) == 3:
        point_A += 2
    elif str(a1) and str(a2) == 4:
        point_A += 2
    elif str(a1) and str(a3) == 4:
        point_A += 2
    elif str(a1) and str(a4) == 4:
        point_A += 2
    elif str(a1) and str(a5) == 4:
        point_A += 2
    elif str(a2) and str(a3) == 4:
        point_A += 2
    elif str(a2) and str(a4) == 4:
        point_A += 2
    elif str(a2) and str(a5) == 4:
        point_A += 2
    elif str(a3) and str(a4) == 4:
        point_A += 2
    elif str(a3) and str(a5) == 4:
        point_A += 2
    elif str(a4) and str(a5) == 4:
        point_A += 2
    elif str(a1) and str(a2) == 5:
        point_A += 2
    elif str(a1) and str(a3) == 5:
        point_A += 2
    elif str(a1) and str(a4) == 5:
        point_A += 2
    elif str(a1) and str(a5) == 5:
        point_A += 2
    elif str(a2) and str(a3) == 5:
        point_A += 2
    elif str(a2) and str(a4) == 5:
        point_A += 2
    elif str(a2) and str(a5) == 5:
        point_A += 2
    elif str(a3) and str(a4) == 5:
        point_A += 2
    elif str(a3) and str(a5) == 5:
        point_A += 2
    elif str(a4) and str(a5) == 5:
        point_A += 2
    elif str(a1) and str(a2) == 6:
        point_A += 2
    elif str(a1) and str(a3) == 6:
        point_A += 2
    elif str(a1) and str(a4) == 6:
        point_A += 2
    elif str(a1) and str(a5) == 6:
        point_A += 2
    elif str(a2) and str(a3) == 6:
        point_A += 2
    elif str(a2) and str(a4) == 6:
        point_A += 2
    elif str(a2) and str(a5) == 6:
        point_A += 2
    elif str(a3) and str(a4) == 6:
        point_A += 2
    elif str(a3) and str(a5) == 6:
        point_A += 2
    elif str(a4) and str(a5) == 6:
        point_A += 2
elif reponse_A == "un":
elif reponse_A == "deux":
elif reponse_A == "trois":
elif reponse_A == "quatre":
elif reponse_A == "cinq":
elif reponse_A == "six":



reponse_B = input("Joueuer B voulez-vous rejouer ?"
      "Si oui, dites les numéros à relancer sous cette forme : ex: 3, 5, 1"
      "Si non, appuyez sur 0. ")
if reponse_B == str(b1) + ", " + str(b2) + ", " + str(b3) + ", " + str(b4) + ", " + str(b5):
     b1 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     b4 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b2) + ", " + str(b3) + ", " + str(b4):
     b1 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     b4 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b2) + ", " + str(b3) + ", " + str(b5):
     b1 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b2) + ", " + str(b4) + ", " + str(b5):
     b1 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     b4 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b3) + ", " + str(b4) + ", " + str(b5):
     b1 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     b4 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2) + ", " + str(b3) + ", " + str(b4) + ", " + str(b5):
     b4 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b3) + ", " + str(b4) + ", " + str(b5):
     b4 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2) + ", " + str(b4) + ", " + str(b5):
     b4 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2) + ", " + str(b3) + ", " + str(b5):
     b2 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2) + ", " + str(b3) + ", " + str(b4):
     b4 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b4) + ", " + str(b5):
     b4 = random.randint(1, 6)
     b1 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b3) + ", " + str(b5):
     b3 = random.randint(1, 6)
     b1 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b3) + ", " + str(b4):
     b4 = random.randint(1, 6)
     b1 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b2) + ", " + str(b5):
     b2 = random.randint(1, 6)
     b1 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b2) + ", " + str(b4):
     b4 = random.randint(1, 6)
     b1 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b2) + ", " + str(b3):
     b2 = random.randint(1, 6)
     b1 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b2):
     b1 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b3):
     b1 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b4):
     b1 = random.randint(1, 6)
     b4 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1) + ", " + str(b5):
     b1 = random.randint(1, 6)
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2) + ", " + str(b3):
     b3 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2) + ", " + str(b4):
     b4 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2) + ", " + str(b5):
     b5 = random.randint(1, 6)
     b2 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b3) + ", " + str(b4):
     b4 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b3) + ", " + str(b5):
     b5 = random.randint(1, 6)
     b3 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b4) + ", " + str(b5):
     b5 = random.randint(1, 6)
     b4 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b1):
     b1 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b2):
     b2 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b3):
     b3 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b4):
     b4 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_B == str(b5):
     b5 = random.randint(1, 6)
     print(b1)
     print(b2)
     print(b3)
     print(b4)
     print(b5)
elif reponse_A == "pair":
    elif str(a1) and str(a2) == 1:
        point_A += 2
    elif str(a1) and str(a3) == 1:
        point_A += 2
    elif str(a1) and str(a4) == 1:
        point_A += 2
    elif str(a1) and str(a5) == 1:
        point_A += 2
    elif str(a2) and str(a3) == 1:
        point_A += 2
    elif str(a2) and str(a4) == 1:
        point_A += 2
    elif str(a2) and str(a5) == 1:
        point_A += 2
    elif str(a3) and str(a4) == 1:
        point_A += 2
    elif str(a3) and str(a5) == 1:
        point_A += 2
    elif str(a4) and str(a5) == 1:
        point_A += 2
    elif str(a1) and str(a2) == 2:
    point_A += 2
    elif str(a1) and str(a3) == 2:
        point_A += 2
    elif str(a1) and str(a4) == 2:
        point_A += 2
    elif str(a1) and str(a5) == 2:
        point_A += 2
    elif str(a2) and str(a3) == 2:
        point_A += 2
    elif str(a2) and str(a4) == 2:
        point_A += 2
    elif str(a2) and str(a5) == 2:
        point_A += 2
    elif str(a3) and str(a4) == 2:
        point_A += 2
    elif str(a3) and str(a5) == 2:
        point_A += 2
    elif str(a4) and str(a5) == 2:
        point_A += 2
    elif str(a1) and str(a2) == 3:
        point_A += 2
    elif str(a1) and str(a3) == 3:
        point_A += 2
    elif str(a1) and str(a4) == 3:
        point_A += 2
    elif str(a1) and str(a5) == 3:
        point_A += 2
    elif str(a2) and str(a3) == 3:
        point_A += 2
    elif str(a2) and str(a4) == 3:
        point_A += 2
    elif str(a2) and str(a5) == 3:
        point_A += 2
    elif str(a3) and str(a4) == 3:
        point_A += 2
    elif str(a3) and str(a5) == 3:
        point_A += 2
    elif str(a4) and str(a5) == 3:
        point_A += 2
    elif str(a1) and str(a2) == 4:
        point_A += 2
    elif str(a1) and str(a3) == 4:
        point_A += 2
    elif str(a1) and str(a4) == 4:
        point_A += 2
    elif str(a1) and str(a5) == 4:
        point_A += 2
    elif str(a2) and str(a3) == 4:
        point_A += 2
    elif str(a2) and str(a4) == 4:
        point_A += 2
    elif str(a2) and str(a5) == 4:
        point_A += 2
    elif str(a3) and str(a4) == 4:
        point_A += 2
    elif str(a3) and str(a5) == 4:
        point_A += 2
    elif str(a4) and str(a5) == 4:
        point_A += 2
    elif str(a1) and str(a2) == 5:
        point_A += 2
    elif str(a1) and str(a3) == 5:
        point_A += 2
    elif str(a1) and str(a4) == 5:
        point_A += 2
    elif str(a1) and str(a5) == 5:
        point_A += 2
    elif str(a2) and str(a3) == 5:
        point_A += 2
    elif str(a2) and str(a4) == 5:
        point_A += 2
    elif str(a2) and str(a5) == 5:
        point_A += 2
    elif str(a3) and str(a4) == 5:
        point_A += 2
    elif str(a3) and str(a5) == 5:
        point_A += 2
    elif str(a4) and str(a5) == 5:
        point_A += 2
    elif str(a1) and str(a2) == 6:
        point_A += 2
    elif str(a1) and str(a3) == 6:
        point_A += 2
    elif str(a1) and str(a4) == 6:
        point_A += 2
    elif str(a1) and str(a5) == 6:
        point_A += 2
    elif str(a2) and str(a3) == 6:
        point_A += 2
    elif str(a2) and str(a4) == 6:
        point_A += 2
    elif str(a2) and str(a5) == 6:
        point_A += 2
    elif str(a3) and str(a4) == 6:
        point_A += 2
    elif str(a3) and str(a5) == 6:
        point_A += 2
    elif str(a4) and str(a5) == 6:
        point_A += 2
#elif reponse_B == "0":
