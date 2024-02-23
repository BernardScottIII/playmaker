class Play:
    def __init__(self, play_formation:str, play_motion:str, play_shift:str, play_personel:list, play_routes:list, play_pivots:list, play_w0_go_right:bool):
        self.formation = play_formation
        self.motion = play_motion
        self.shift = play_shift
        self.w0_go_right = play_w0_go_right
        self.routes = []
        self.pivots = []
        self.personel = []
        self.personel_names = []
        positions = ["QB", "W0", "W1", "W2"]
        for i in range(len(play_pivots)):
            self.routes.append(int(play_routes[i]))
            self.pivots.append(int(play_pivots[i]))
            self.personel.append(Player(play_personel[i], positions[i]))
            self.personel_names.append(play_personel[i])

    def __repr__(self):
        return f"{self.formation},\nWith {self.personel}:\nmotion {self.motion}"
    
    def get_formation(self):
        return self.formation
    
    def get_motion(self):
        return self.motion
    
    def get_routes(self):
        return self.routes
    
    def get_personel(self):
        return self.personel
    
    def get_personel_names(self):
        return self.personel_names
    
    def get_shift(self):
        return self.shift
    
    def get_pivots(self):
        return self.pivots
    
    def get_w0_go_right(self):
        return self.w0_go_right

class Player:
    def __init__(self, player_name, player_pos):
        self.name = player_name
        self.pos = player_pos

    def get_name(self):
        return self.name
    
    def get_pos(self):
        return self.pos

    def __repr__(self):
        return f"{self.name} ({self.pos})"
    
class Formation:
    def __init__(self, formation_name, formation_w1_loc, formation_w1_on_los, formation_w2_loc, formation_w2_on_los):
        self.name = formation_name
        self.w1_loc = formation_w1_loc
        self.w2_loc = formation_w2_loc
        self.w1_on_los = formation_w1_on_los
        self.w2_on_los = formation_w2_on_los

    def get_name(self):
        return self.name

    def get_w1_loc(self):
        return self.w1_loc
    
    def get_w2_loc(self):
        return self.w2_loc
    
    def w1_is_on_los(self):
        return self.w1_on_los
    
    def w1_is_on_los(self):
        return self.w2_on_los
