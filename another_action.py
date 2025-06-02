import random
import time
import keyboard
# 0.2-1.0秒のランダムディレイ
def random_delay():
    delay = random.uniform(0.2, 1.0)
    time.sleep(delay)

#移動専用ミニマムディレク
def move_mini_delay():
    delay = random.uniform(0.2, 0.4)
    time.sleep(delay)

def down_delay():
    delay = random.uniform(0.5, 0.8)
    time.sleep(delay)

"""
移動系(ワープ付き)
"""

# 上移動
def move_up():
    keyboard.press('up')
    keyboard.press('w')
    move_mini_delay()
    keyboard.release('w')
    keyboard.release('up')


# 下移動
def move_down():
    keyboard.press('down')
    keyboard.press('w')
    down_delay()
    keyboard.release('w')
    keyboard.release('down')


# 左移動
def move_left():
    keyboard.press('w')
    keyboard.press('left')
    move_mini_delay()
    keyboard.release('left')
    keyboard.release('w')
    

# 右移動
def move_right():
    keyboard.press('w')
    keyboard.press('right')
    move_mini_delay()
    keyboard.release('right')
    keyboard.release('w')
    

#　通常降りる動作
def nomal_down():
    keyboard.press('c')
    keyboard.press('down')
    random_delay()
    keyboard.release('down')
    keyboard.release('c')
    random_delay()

