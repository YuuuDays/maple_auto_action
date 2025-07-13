import keyboard
import time
import random

# ===================================
#ディレイ
# ===================================
# より複雑なランダムディレイ関数
def complex_random_delay():
    base_delay = random.uniform(0.2, 0.4)
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
    time.sleep(0.8)

    # cキーを確実に2回押す
    keyboard.press('c')
    mini_delay()  # 少し長めに押す
    keyboard.release('c')
    mini_delay()  # 間隔を空ける
    
    keyboard.press('c')
    mini_delay()  # 少し長めに押す
    keyboard.release('c')
    time.sleep(0.8)

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
    time.sleep(0.8)

    keyboard.release('left')
    complex_random_delay()

#========================
# メイン
#========================
def action_define():
    #　左側

    #　左上3段目
    which_one_attack()
    move_mini_delay()
    down_move()

    # 左上2段目
    complex_random_delay()
    which_one_attack()
    complex_random_delay()
    down_move()

    # 最下層
    complex_random_delay()
    which_one_attack()
    right_move()
    print("最下層右移動")
    complex_random_delay()
    which_one_attack()
    right_move()
    print("最下層右移動")
    # 右側
    up_move1()
    keyboard.send('left')

    complex_random_delay()
    which_one_attack()
    complex_random_delay()

    up_move1()
    which_one_attack()
    complex_random_delay()

    # -----ここから折り返し









