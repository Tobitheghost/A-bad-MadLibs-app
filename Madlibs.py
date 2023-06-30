import random


def Be_Kind_adLib():
    Noun1 = input("Enter a Noun")
    Noun2 = input("Enter a Plural Noun")
    Noun3 = input("Enter Another Noun")
    Place = input("Enter A Place")
    Adjective = input("Enter an Adjective")
    Noun4 = input("Enter your final Noun")

    print("Be kind to your " + str(Noun1) + "-footed " + str(Noun2))
    print("For a duck may be somebody`s " + str(Noun3) + ",")
    print("Be kind to your " + str(Noun3) + "in " + str(Place))
    print("Where the weather is always " + str(Adjective) + ".")
    print("You may think that this is the " + str(Noun4) + ",")
    print("Well it is.")

def Letter_From_Camp_adLib():
    Relative1 = input("Enter a Relative")
    Adjective1 = input("Enter an Adjective")
    if Adjective1.find("a") == 0:
        global letterA
        letterA = "an"
    if Adjective1.find("e") == 0:
        letterA = "an"
    if Adjective1.find("i") == 0:
        letterA = "an"
    if Adjective1.find("o") == 0:
        letterA = "an"
    if Adjective1.find("u") == 0:
        letterA = "an"
    else:
        letterA = "a"
    Adjective2 = input("Enter another Adjective")
    Adjective3 = input("Enter yet another Adjective")
    Name1 = input("Enter a Name of someone in the room")
    Adjective4 = input("Enter your final Adjective")
    Adjective5 = input("I lied, enter another Adjective")
    Verb1 = input("Enter an Verb")
    Body = input("Enter a body part")
    Verb2 = input("Enter another Verb")
    Noun1 = input("Enter a Noun")
    Noun2 = input("Enter another Noun")
    Adverb = input("Enter an Adverb")
    Verb3 = input("Enter another Verb")
    Verb4 = input("Enter one more Verb, I promise")
    Relative2 = input("Enter another Relative")
    Name2= input("Enter another name of someone in the room")

    print("Dear " + str(Relative1) + ",")
    print("I am having " + str(letterA) + " " + str(Adjective1) + " time at camp. The counselor is " + str(Adjective2))
    print("and the food is " + str(Adjective3) + ". I met " + str(Name1) + " and we became " + str(Adjective4))
    print("friends. Unfortunately, " + str(Name1) + " is " + str(Adjective5) + " and I " + str(Verb1) + " my " + str(Body) + " so")
    print("we couldn`t go " + str(Verb2) + " like everybody else. I need more " + str(Noun1) + " and a")
    print(str(Noun2) + " sharpener, so please " + str(Adverb) + " " + str(Verb3) + " more when you " + str(Verb4) + " back.")
    print("Your " + str(Relative2) + ",")
    print(str(Name2))

def Romeo_and_Juliet():
    Noun1 = input("Enter a Noun")
    Place = input("Enter a Place")
    Noun2 = input("Enter another Noun")
    Noun3 = input("Enter ANOTHER NOUN")
    Noun4 = input("ANOTHER NOUN DAMNIT")
    Adjective1 = input("Enter an Adjective")
    Verb1 = input("Enter a Verb")
    Number = input("Enter A Number")
    Adjective = input("Enter an Adjective")
    Body = input("Enter a Body part")
    Verb2 = input("Enter another Verb")

    print("Two " + str(Noun1) + ", both alike in dignity,")
    print("In fair " + str(Place) + ", where we lay our scene,")
    print("From ancient " + str(Noun2) + " break to new mutiny,")
    print("Where civil blood makes civil hands unclean.")
    print("From forth the fatal loins of these two foes")
    print("A pair of star-cross`d " + str(Noun3) + " take their life;")
    print("Whole misadventure piteous overthrows")
    print("Do with their " + str(Noun4) + " bury their parents` strife.")
    print("The fearful passage of their " + str(Adjective1) + " love,")
    print("And the continuance of their parents` rage,")
    print("Which, but their children`s end, nought could " + str(Verb1) + ",")
    print("Is now the " + str(Number) + " hours` traffic of our stage;")
    print("The which if you with " + str(Adjective) + str(Body) + " attend,")
    print("What here shall " + str(Verb2) + ", our toil shall strive to mend. ")

list = [Be_Kind_adLib, Letter_From_Camp_adLib, Romeo_and_Juliet]
value = random.choice(list)
value()


