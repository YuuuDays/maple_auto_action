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
def attack():
    keyboard.press('q')
    complex_random_delay()
    keyboard.release('q')

def attack_2():
    keyboard.press('w')
    complex_random_delay()
    keyboard.release('w')

# 攻撃どっちだ～
def which_one_attack():
    complex_random_delay()
    if random.randint(0, 1) == 0:
        attack()
    else:
        attack_2()
    complex_random_delay()

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

#========================
# 行動定義
#========================
MOVE_KEYS = ['left', 'right', 'up', 'down']  # 移動キー

#下移動
def down_move():
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

# #上移動_2
# def up_move2():
#     move_mini_delay()
#     keyboard.send('kanji')

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

#========================
# メイン
#========================
# プログラム起動時に「マクロ開始！」を表示し、その後に日本時間の現在時刻を表示
JST = timezone(timedelta(hours=9), 'JST')
print("マクロ開始！")
print("現在時刻: ", datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S"))

start_time = time.time()

def action_define():
    #　左側

    #　左上3段目
    keyboard.press('6')
    which_one_attack()
    move_mini_delay()
    down_move()

    # 左上2段目
    complex_random_delay()
    which_one_attack()
    complex_random_delay()
    down_move()

    if random.randint(0, 1) == 0:
        keyboard.press('2')
        time.sleep(0.5)
        keyboard.press('1')
    else:
        keyboard.press('F12')
        time.sleep(0.5)
        keyboard.press('space')
    time.sleep(0.5)
    # 最下層
    complex_random_delay()
    which_one_attack()
    right_move()
    special_attack()
    complex_random_delay()
    which_one_attack()
    right_move()

    # 右側
    up_move1()
    move_mini_delay()
    keyboard.press('left')
    time.sleep(0.4)
    keyboard.release('left')

    complex_random_delay()
    which_one_attack()
    complex_random_delay()

    up_move1()
    which_one_attack()
    complex_random_delay()

    # -----ここから折り返し

    #　右上3段目
    which_one_attack()
    move_mini_delay()
    down_move()

    # 右上2段目
    complex_random_delay()
    which_one_attack()
    complex_random_delay()
    down_move()

    #　一番下
    complex_random_delay()
    which_one_attack()
    left_move()

    if random.randint(0, 1) == 0:
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
    else:
        keyboard.press('shift')
        time.sleep(0.5)
        keyboard.release('shift')
    time.sleep(0.5)
    
    special_attack()
    which_one_attack()
    left_move()

    #上ります
    mini_delay()
    up_move1()

    keyboard.press('right')
    time.sleep(0.4)
    keyboard.release('right')

    move_mini_delay()
    which_one_attack()
    complex_random_delay()

    up_move1()
    which_one_attack()
    complex_random_delay()

    keyboard.press('d')

    # 1周ごとに経過時間を表示
    elapsed = time.time() - start_time
    print(f"経過時間:{int(elapsed//60)}分({int(elapsed%60)}秒)")
