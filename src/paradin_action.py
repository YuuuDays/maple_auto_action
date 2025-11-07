import keyboard
import time
import random
from datetime import datetime, timedelta, timezone

# ===================================
#ディレイ
# ===================================
# より複雑なランダムディレイ関数
def complex_random_delay():
    base_delay = random.uniform(0.2, 0.6)
    variation = random.uniform(-0.1, 0.1)
    delay = base_delay + variation
    time.sleep(delay)  # 実際に待機する

#移動専用ミニマムディレク
def move_mini_delay():
    delay = random.uniform(0.4, 0.6)
    time.sleep(delay)

# 0.1~0.3秒のディレイ
def mini_delay():
    delay = random.uniform(0.1, 0.3)
    time.sleep(delay)

def aisatsu():
    print("hellooo")
#========================
#攻撃定義
#========================
def n_attack():
    keyboard.press('q')
    complex_random_delay()
    keyboard.release('q')

def n_attack2():
    keyboard.press('w')
    complex_random_delay()
    keyboard.release('w')

# 攻撃どっちだ～
def which_one_n_attack():
    complex_random_delay()
    if random.randint(0, 1) == 0:
        n_attack()
    else:
        n_attack2()
    complex_random_delay()

# 60秒に一回
def time_60_attack():
    keyboard.press('m')
    complex_random_delay()
    keyboard.release('m')

def spaider_attack():
    move_mini_delay()
    keyboard.send('6')
    
#　追尾ハンマーかアタックハンマー
def special_attack():
    complex_random_delay()
    if random.randint(0, 1) == 0:
        keyboard.press('space')
        move_mini_delay()
        keyboard.release('space')
    else:
        keyboard.press('shift')
        move_mini_delay()
        keyboard.release('shift')
    
# 通常攻撃かスペシャル攻撃か
def which_n_or_special():
    complex_random_delay()
    if random.randint(0, 1) == 0:
        special_attack()
    else:
        which_one_n_attack()
# fake
def fake_action():
    time.sleep(0.5)
    if random.randint(0, 1) == 0:
        keyboard.send('1')
    else:
        keyboard.send('F12')
        time.sleep(0.5)
        keyboard.send('F12')
    time.sleep(0.5)

def fake_action2():
    time.sleep(0.5)
    if random.randint(0, 1) == 0:
        keyboard.send('d')
    else:
        keyboard.send('end')
    time.sleep(0.5)

#========================
# 行動定義
#========================
MOVE_KEYS = ['left', 'right', 'up', 'down']  # 移動キー

#下移動
def down_move():
    complex_random_delay()
    complex_random_delay()
    keyboard.press('down')
    keyboard.press('c')
    move_mini_delay()
    keyboard.release('down')
    keyboard.release('c')
    complex_random_delay()

#上移動_1
def up_move1():
    keyboard.press('e')
    move_mini_delay()
    keyboard.release('e')
    complex_random_delay()

#上移動2
def up_move2():
    keyboard.press(41)
    move_mini_delay()
    keyboard.release(41)
    complex_random_delay()

# 右移動
def right_move():
    complex_random_delay()
    
    # 右キーを押す
    keyboard.press('right')
    move_mini_delay()

    # cキーを確実に2回押す
    keyboard.press('c')
    mini_delay()  # 少し長めに押す
    keyboard.release('c')
    mini_delay()  # 間隔を空ける
    
    keyboard.press('c')
    mini_delay()  # 少し長めに押す
    keyboard.release('c')
    move_mini_delay()
    move_mini_delay()

    # 右キーを離す
    keyboard.release('right')
    complex_random_delay()

# 若干の右移動
def little_turn_right_move():
    complex_random_delay()

    keyboard.press('right')
    complex_random_delay()
    keyboard.release('right')

    move_mini_delay()

# 若干の左移動
def little_turn_left_move():
    complex_random_delay()

    keyboard.press('left')
    complex_random_delay()
    keyboard.release('left')

    move_mini_delay()
# 左移動
def left_move():
    complex_random_delay()

    keyboard.press('left')

    # cキーを確実に2回押す
    keyboard.press('c')
    mini_delay()  # 少し長めに押す
    keyboard.release('c')
    mini_delay()  # 間隔を空ける
    
    keyboard.press('c')
    mini_delay()  # 少し長めに押す
    keyboard.release('c')
    move_mini_delay()
    move_mini_delay()

    keyboard.release('left')
    complex_random_delay()


