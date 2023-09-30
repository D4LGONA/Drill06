from pico2d import *
from math import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')


def handle_events():
    global running, cursorX, cursorY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursorX, cursorY = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            points.append([event.x, TUK_HEIGHT - 1 - event.y])

def draw():
    global points, frame, x, y, cursorX, cursorY
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if points:
        for i in points:
            cursor.draw(i[0], i[1])
    if state == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    
    cursor.draw(cursorX, cursorY)
    update_canvas()
    frame = (frame + 1) % 8

def move():
    global x, y, routes
    x, y = routes[0][0], routes[0][1]
    routes.remove(routes[0])

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
cursorX, cursorY = 0, 0
points = []
routes = []
frame = 0
state = 0
hide_cursor()

while running:
    if points: # 배열이 비어있지 않다면
        if not routes:
            if x < points[0][0]: state = 0
            else: state = 1
            x1, y1 = x, y
            x2, y2 = points[0][0], points[0][1]
            distance = sqrt((x1-x2) ** 2 + (y1-y2) **2)
            for i in range(0, int(distance) + 1, 1):
                t = i / int(distance)
                routes.append([(1-t) * x1 + t * x2 , (1-t) * y1 + t * y2])
            routes.append([x2, y2])
        move()
        if int(points[0][0]) == int(x) and int(points[0][1]) == int(y):
            points.remove(points[0])
            routes.clear()

    draw()
    handle_events()

close_canvas()




