from pico2d import *

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
    if dirX > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    cursor.draw(cursorX, cursorY)
    update_canvas()
    frame = (frame + 1) % 8

def move():
    print('움직여야 해')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
cursorX, cursorY = 0, 0
points = []
frame = 0
dirX, dirY = 0, 0
hide_cursor()

while running:
    if points: # 배열이 비어있지 않다면
        move()

    draw()


    handle_events()

close_canvas()




