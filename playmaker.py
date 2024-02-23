import inquirer
from playbook import Formation, Play
from PIL import Image

formations = list[Formation]([])

with open("formations.txt", "r") as file:
    for lineup in file:
        info = lineup.split(",")
        print(info)
        w1_los_status = info[2] == "True"
        w2_los_status = info[4] == "True\n"
        formations.append(Formation(info[0], info[1], w1_los_status, info[3], w2_los_status))

formation = ""

def refresh_options():
    options = []
    for lineup in formations:
        options.append(lineup.get_name())

    options.append("Add New Formation")
    options.append("Exit")
    return options

def save_formation(info:list):
    formation = ""
    for item in info:
        formation += item + ","
    with open("formations.txt", "a") as file:
        file.write(formation[:-1] + "\n")

def save_play(play:Play):
    with open("playbook.txt", "a+") as file:
        personel = play.get_personel_names()
        routes = play.get_routes()
        pivots = play.get_pivots()
        file.write(f"{play.get_formation()},{personel[0]},{personel[1]},{personel[2]},{personel[3]},{play.get_motion()},{play.get_shift()},{routes[0]},{routes[1]},{routes[2]},{routes[3]},{pivots[0]},{pivots[1]},{pivots[2]},{pivots[3]},{play.get_w0_go_right()}\n")

def add_formation():
    formation_name = input("Enter formation name:")
    w1_lineup = inquirer.list_input("W1 Alignment", choices=["TIGHT", "OUT", "WIDE"])
    w1_los = inquirer.list_input("Is W1 on LOS?", choices=[True, False])
    w2_lineup = inquirer.list_input("W2 Alignment", choices=["TIGHT", "OUT", "WIDE"])
    w2_los = inquirer.list_input("Is W2 on LOS?", choices=[True, False])

    formations.append(Formation(formation_name, w1_lineup, w1_los, w2_lineup, w2_los))

    if inquirer.list_input("Save New Formation?", choices=[True, False]):
        save_formation([formation_name, w1_lineup, str(w1_los), w2_lineup, str(w2_los)])

def create_play(formation:Formation):
    route_options = ["Flat", "Sland", "Comeback", "Curl", "Out", "Drag", "Corner", "Post", "Fly"]
    player_options = []
    with open("roster.txt", "r") as file:
        for line in file:
            player_options.append(line[:-1])

    qb = inquirer.list_input("Select QB", choices = player_options)
    player_options.remove(qb)
    w0 = inquirer.list_input("Select W0", choices = player_options)
    player_options.remove(w0)
    w0_route = route_options.index(inquirer.list_input("Choose W0 Route", choices = route_options))+1
    w0_pivot = input("Enter W0 Pivot Distance:")
    w0_dir = inquirer.list_input("Direction W0 runs", choices = ["Left", "Right"]) == "Right"
    w1 = inquirer.list_input("Select W1", choices = player_options)
    player_options.remove(w1)
    w1_route = route_options.index(inquirer.list_input("Choose W1 Route", choices = route_options))+1
    w1_pivot = input("Enter W1 Pivot Distance:")
    w2 = inquirer.list_input("Select W2", choices = player_options)
    player_options.remove(w2)
    w2_route = route_options.index(inquirer.list_input("Choose W2 Route", choices = route_options))+1
    w2_pivot = input("Enter W2 Pivot Distance:")

    if inquirer.list_input("Save New Play?", choices=[True, False]):
        save_play(Play(formation, "NO", "NO", [qb, w0, w1, w2], [-1, w0_route, w1_route, w2_route], [-1, w0_pivot, w1_pivot, w2_pivot], w0_dir))

while formation != "Exit":

    formation = inquirer.list_input("Select Formation", choices=refresh_options())

    if formation == "Add New Formation":
        add_formation()
        continue
    elif formation != "Exit":
        create_play(formation)
        print("Exit program before starting playrunner.py")
