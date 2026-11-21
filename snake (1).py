import random
import curses
HEAD = '@'   # شكل راس الثعبان
BODY = 'o'   # شكل جسم الثعبان
FOOD = '*'   # شكل الأكل
screen = curses.initscr()
curses.curs_set(0)
screen_hight, screen_width = screen.getmaxyx()

window = curses.newwin(screen_hight, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

snk_x = screen_width // 4
snk_y = screen_hight // 2

snake = [[snk_y, snk_x],
         [snk_y, snk_x - 1],
         [snk_y, snk_x - 2]]

food = [screen_hight // 2, screen_width // 2]
window.addch(food[0], food[1], FOOD)

for i, part in enumerate(snake):
    window.addch(part[0], part[1], HEAD if i == 0 else BODY)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if (snake[0][0] in [0, screen_hight - 1] or
            snake[0][1] in [0, screen_width - 1] or
            snake[0] in snake[1:]):
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)
    window.addch(snake[1][0], snake[1][1], BODY)  # الراس القديمة تبقى جسم

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screen_hight - 2),
                random.randint(1, screen_width - 2)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], FOOD)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    try:
        window.addch(snake[0][0], snake[0][1], HEAD)
    except curses.error:
        pass
