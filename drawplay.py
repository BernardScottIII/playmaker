from PIL import Image, ImageDraw
from playbook import Play

# x-axis constants
WIDE_LEFT = 150
WIDE_RIGHT = 810
OUT_LEFT = 300
OUT_RIGHT = 660
TIGHT_LEFT = 430
TIGHT_RIGHT = 530
MIDDLE = 480

# y-axis constants
FIVE_YARD_LINE = 312
TEN_YARDS_LINE = 130
LOS = 493

# other constants
OFF_LOS_DELTA = 20
ONE_YARD = 36

# player constants
QB = (MIDDLE, LOS + (3 * ONE_YARD))
W0 = (MIDDLE, LOS)

def draw_players(im, W1, W2):
    pen = ImageDraw.Draw(im)
    radius = 20
    pen.ellipse((QB[0]-radius, QB[1]-radius, QB[0]+radius, QB[1]+radius), fill="red")
    pen.ellipse((W0[0]-radius, W0[1]-radius, W0[0]+radius, W0[1]+radius), fill="yellow")
    pen.ellipse((W1[0]-radius, W1[1]-radius, W1[0]+radius, W1[1]+radius), fill="yellow")
    pen.ellipse((W2[0]-radius, W2[1]-radius, W2[0]+radius, W2[1]+radius), fill="yellow")

def transform_cord(cord):
    return LOS - (cord * ONE_YARD)

def route_to_dir(WR, pivot, route, goingRight):
    flip = 1
    if goingRight:
        flip = -1
    pivot_pxl = transform_cord(pivot)
    if route in [1,5]: return [WR[0] - 3 * ONE_YARD * flip, pivot_pxl]
    elif route in [2,8]: return [WR[0] + ONE_YARD * flip, pivot_pxl - ONE_YARD]
    elif route == 3: return [WR[0] - ONE_YARD * flip, pivot_pxl + ONE_YARD]
    elif route == 4: return [WR[0] + ONE_YARD * flip, pivot_pxl + ONE_YARD]
    elif route == 6: return [WR[0] + ONE_YARD * flip, pivot_pxl]
    elif route == 7: return [WR[0] - ONE_YARD * flip, pivot_pxl - ONE_YARD]
    elif route == 9: return [WR[0], pivot_pxl - ONE_YARD]
    else: return [0,0]

def collect_route_points(WR, pivot, route, goingLeft):
    result = []
    result.extend(WR)
    result.extend([WR[0], transform_cord(pivot)])
    result.extend(route_to_dir(WR, pivot, route, goingLeft))
    return result


def draw_routes(im, play:Play, W1, W2):
    pen = ImageDraw.Draw(im)
    routes = play.get_routes()
    pivots = play.get_pivots()
    W0_points = collect_route_points(W0, pivots[1], routes[1], play.get_w0_go_right())
    W1_points = collect_route_points(W1, pivots[2], routes[2], False)
    W2_points = collect_route_points(W2, pivots[3], routes[3], True)
    
    pen.line(W0_points, fill="red", width=5)
    pen.line(W1_points, fill="red", width=5)
    pen.line(W2_points, fill="red", width=5)

def draw_play(play:Play):
    im = Image.open("field.png")
    W1 = ()
    W2 = ()
    if play.get_formation() == "T Formation":
        W1 = (TIGHT_LEFT, LOS)
        W2 = (TIGHT_RIGHT, LOS)
    elif play.get_formation() == "I Formation":
        W1 = (OUT_LEFT, LOS)
        W2 = (OUT_RIGHT, LOS)
    elif play.get_formation() == "Spread":
        W1 = (WIDE_LEFT, LOS)
        W2 = (WIDE_RIGHT, LOS)
    draw_players(im, W1, W2)
    draw_routes(im, play, W1, W2)
    im.show()  

# im = Image.open("field.png")
# pen = ImageDraw.Draw(im)
# pen.ellipse((460, 475, 500, 515), fill="yellow")
# pen.ellipse((460, 565, 500, 605), fill="red")
# pen.ellipse((410, 475, 450, 515), fill="teal")
# pen.ellipse((280, 475, 320, 515), fill="green")
# pen.ellipse((130, 475, 170, 515), fill="purple")
# pen.ellipse((510, 495, 550, 535), fill="cyan")
# pen.ellipse((640, 495, 680, 535), fill="orange")
# pen.ellipse((790, 495, 830, 535), fill="blue")
# pen.line((150,495,150,130, 380, 200), fill="red", width=5)
# pen.polygon((375,190,395,200,375,210), fill="white")
# pen.line((0,LOS,900,LOS), fill="yellow")
# im.show()
# im.save("template.png")