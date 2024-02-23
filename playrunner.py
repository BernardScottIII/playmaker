import inquirer
import playbook
import os
import drawplay

sorted_playbook = list[list[playbook.Play]]([])
unique_formations = list[playbook.Formation]([])

def add_new_formation(formation):
    if not formation in unique_formations:
        unique_formations.append(formation)
        sorted_playbook.append(list[playbook.Play]([]))
    return

def create_playbook():
    with open("playbook.txt", "r") as plays:
        for play in plays:
            info = play.split(",")
            formation = info[0]
            personel = info[1:5]
            motion = info[5]
            shift = info[6]
            routes = info[7:11]
            pivots = info[11:15]
            w0_go_right = info[15] == "True\n"
            add_new_formation(formation)
            new_play = playbook.Play(formation, motion, shift, personel, routes, pivots, w0_go_right)
            sorted_playbook[unique_formations.index(formation)].append(new_play)
    return

def comp_list_by_elements(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def are_equal(a:list, b:list):
    if len(a) != len(b):
        return False
    else:
        return comp_list_by_elements(a, b)

def display_by_formation(formation, personel):
    for play in sorted_playbook[unique_formations.index(formation)]:
        if are_equal(play.get_personel_names(), personel):
            print("Found Valid Play!")
            drawplay.draw_play(play)
    return

create_playbook()

down = ""
while down != "Exit":
    os.system("cls")
    down = inquirer.list_input("Down Number", choices=["First", "Second", "Third", "Fourth", "Exit"])
    os.system("cls")

    personel = []
    while len(personel) < 4 and down != "Exit":
        personel = inquirer.checkbox("Personel", choices=["Devin Perry", "Keith Juros", "Bernard Scott", "Ben Trexler", "Chris Santiago"])

    os.system("cls")

    if down == "First":
        display_by_formation("T Formation", personel)
    elif down == "Second":
        display_by_formation("I Formation", personel)
    elif down == "Third":
        display_by_formation("Spread", personel)
    elif down == "Fourth":
        print("Punt")
    
    if down != "Exit":
        down = inquirer.list_input("Options", choices=["Go Back", "Exit"])