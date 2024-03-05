"""
Collaborator: Justin Myshrall
Date: 2/28/2024
Title: Madlibs
"""
def madlib1():

    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous Person: ")

    madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. \
    Stay hydrated and {verb2} like you are {famous_person}!"

    print(madlib)

def madlib2():

    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    bird = input("Type of bird: ")
    room = input("Room in the house: ")
    verb1 = input("Verb (past tense): ")    
    verb2 = input("Verb: ")
    name = input("Relatives name: ")
    noun1 = input("Noun: ")
    liquid = input("A liquid: ")
    verb3 = input("Verb with -ing: ")
    body = input("Part of body plural: ")
    noun2 = input("Plural noun: ")
    verb4 = input("Verb with -ing: ")
    noun3 = input("Noun: ")


    madlib = f"It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs. \
    I {verb1} down the stairs to see if I could help {verb2} the dinner. My mom said, 'see if {name} needs a fresh {noun1}.' \
    So I carried a tray of glasses full of {liquid} into the {verb3} room. When I got there, I couldn't believe my {body}! \
    There were {noun2} {verb4} on the {noun3}!"

    print(madlib)

def main ():

    madlib1()
    madlib2()

main()
