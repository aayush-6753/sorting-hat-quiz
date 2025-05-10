gryffindor=0
slytherin=0
ravenclaw=0
hufflepuff=0

q1 = int(input("What quality do you value most in a friend? 1)loyality 2)bravery 3)ambition 4)intelligence "))
if q1 == 1:
    hufflepuff += 1
elif q1 == 2:
    gryffindor += 1
elif q1 == 3:
    slytherin += 1
elif q1 == 4:
    ravenclaw += 1
else:
    print("the sorting hat has spoken, you are getting expelled")
    exit() 

q2 = int(input("If you were in a difficult situation, what would you rely on? 1)my brain 2)my gut/instincts 3)my connections 4)my patience "))
if q2 == 1:
    ravenclaw += 1
elif q2 == 2:
    gryffindor += 1
elif q2 == 3:
    slytherin += 1
elif q2 == 4:
    hufflepuff += 1
else:
    print("the sorting hat has spoken, you are getting expelled") 
    exit()

q3 = int(input("Pick a magical creature you like most 1)phoenix 2)basilik 3)hippogriff 4)niffler "))
if q3 == 1:
    gryffindor += 1
elif q3 == 2:
    slytherin += 1
elif q3 == 3:
    ravenclaw += 1
elif q3 == 4:
    hufflepuff += 1
else:
    print("the sorting hat has spoken, you are getting expelled")
    exit()

q4 = int(input("Which career would you prefer? 1) auror 2)minister of magic 3)professor at hogwarts 4)healer at st. mungo's "))
if q4 == 1:
    gryffindor += 1
elif q4 == 2:
    slytherin += 1
elif q4 == 3:
    ravenclaw += 1
elif q4 == 4:
    hufflepuff += 1
else:
    print("the sorting hat has spoken, you are getting expelled")
    exit()

q5 = int(input("Choose a Hogwarts subject 1)defence against dark magic 2)potions 3)astronomy 4)herbology "))
if q5 == 1:
    gryffindor += 1
elif q5 == 2:
    slytherin += 1  
elif q5 == 3:
    hufflepuff += 1
elif q5 == 4:
    ravenclaw += 1
else:
    print("the sorting hat has spoken, you are getting expelled")
    exit()

q6 = int(input("What’s most important to you? 1)justice 2)power 3)knowledge 4)compassion "))
if q6 == 1:
    gryffindor += 1
elif q6 == 2:
    slytherin += 1
elif q6 == 3:
    ravenclaw += 1
elif q6 == 4:
    hufflepuff += 1
else:
    print("the sorting hat has spoken, you are getting expelled")
    exit()

q7 = int(input("How do you respond to failure? 1)learn from it and adapt 2)keep pushing. never give up 3)find a new path to success 4)support others stay calm "))
if q7 == 1:
    ravenclaw += 1
elif q7 == 2:
    gryffindor += 1
elif q7 == 3:
    slytherin += 1
elif q7 == 4:
    hufflepuff += 1
else:
    print("the sorting hat has spoken, you are getting expelled")
    exit()


houses = {
    "Gryffindor": gryffindor,
    "Slytherin": slytherin,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff
}

chosen_house = max(houses, key=houses.get)


print(f"\n🧙 The Sorting Hat has spoken... You belong in {chosen_house}!")