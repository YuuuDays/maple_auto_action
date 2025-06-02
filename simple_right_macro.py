# =============================
# keyboardモジュールの主な使い方まとめ
#
# keyboard.press(key)      : 指定したキーを押しっぱなしにする
# keyboard.release(key)    : 指定したキーを離す
# keyboard.write(text)     : 文字列をタイプする（人が打つような動作）
# keyboard.send(key)       : 指定したキーを一度だけ押す（押してすぐ離す）
# keyboard.add_hotkey('esc', func) : 指定キーで関数を呼び出す（ホットキー登録）
# keyboard.is_pressed(key) : 指定キーが押されているか判定（True/False）
# keyboard.wait(key)       : 指定キーが押されるまで待機
#
# 例：
#   keyboard.press('a')
#   keyboard.release('a')
#   keyboard.write('hello')
#   keyboard.send('space')
#   keyboard.add_hotkey('esc', stop_macro)
#   if keyboard.is_pressed('shift'): ...
#   keyboard.wait('enter')
# =============================

import keyboard
import time
import random
import another_action as actions  # モジュール名を変更してインポート
is_running = False  # グローバルで管理

""""""""""""""""""""""""""""""""
# 関数定義
""""""""""""""""""""""""""""""""
#移動専用ミニマムディレク
def move_mini_delay():
    delay = random.uniform(0.4, 0.6)
    time.sleep(delay)

# 0.2-0.5秒のランダムディレイ
def mini_delay():
    delay = random.uniform(0.2, 0.4)
    time.sleep(delay)

# 0.2-1.0秒のランダムディレイ
def random_delay():
    delay = random.uniform(0.2, 1.0)
    time.sleep(delay)

# 1.0-1.8秒のランダムディレイ
def random_long_delay():
    delay = random.uniform(1.0, 1.8)
    time.sleep(delay)

# 1.8-2.5秒のランダムディレイ
def random_super_long_delay():
    delay = random.uniform(1.8, 2.5)
    time.sleep(delay)

"""
移動系(ワープ付き)
"""
# 上移動
def move_up():
    keyboard.press('w')
    keyboard.press('up')
    random_delay()
    keyboard.release('up')
    keyboard.release('w')
    random_delay()

# 下移動
def move_down():
    keyboard.press('w')
    keyboard.press('down')
    random_delay()
    keyboard.release('down')
    keyboard.release('w')
    random_delay()

# 左移動
def move_left():
    keyboard.press('w')
    keyboard.press('left')
    move_mini_delay()
    keyboard.release('left')
    keyboard.release('w')
    if random_number() %2 == 0:
        keyboard.press('left')
        keyboard.release('left')
    move_mini_delay()

# 右移動
def move_right():
    keyboard.press('w')
    keyboard.press('right')
    move_mini_delay()
    keyboard.release('right')
    keyboard.release('w')
    if random_number() %2 == 0:
        keyboard.press('right')
        keyboard.release('right')
    move_mini_delay()

#　通常降りる動作
def nomal_down():
    keyboard.press('c')
    keyboard.press('down')
    random_delay()
    keyboard.release('down')
    keyboard.release('c')
    random_delay()

"""
# 攻撃
"""
def attack():
    #3回数
    for i in range(4):
        keyboard.send('q')
        mini_delay()
        if random_number() %2 == 0:
            keyboard.send('q')
            mini_delay()

    #ランダム三回目
    if random_number() %2 == 0:
        keyboard.press('q')
        random_delay()
        keyboard.release('q')
    

def attack_2():
    for i in range(2):
        keyboard.press('2')
        random_long_delay()
        keyboard.release('2')


def tengu_attack():
    random_delay()
    keyboard.press('3')
    mini_delay()
    keyboard.release('3')

"""
#ランダムな数値を返すだけの関数
"""
def random_number():
    return random.randint(0, 100)

""""""""""""""""""""""""""""""""
# メインマクロ
""""""""""""""""""""""""""""""""
def stop_macro():
    global is_running
    print("マクロを停止します")
    is_running = False

def main_macro():
    global is_running
    # 時間経過スキル記録用
    start_time = time.time()
    """
    # 置きスキル(石)
    """
    last_okiishi_skill_time = time.time()
    intaval_okiishi_skill = 180
    """
    巻き込む蛇みたいな全体スキル
    """
    last_snake_skill_time = time.time()    
    intaval_snake_skill = 90


    if is_running:
        print("すでにマクロが動作中です")
        return
    print("マクロ開始！ESCで停止")
    is_running = True
    start_time = time.time()
    # 場所位置修正変数
    position_counter = 0
    try:
        while is_running:
            
            now = time.time()
            # 現在の時間
            elapsed_sec = int(now - start_time)
            elapsed_min = elapsed_sec // 60
            print(f"経過時間: 秒単位={elapsed_sec}, 分単位={elapsed_min}")


            # 巻き込む蛇みたいな全体スキル
            if now - last_snake_skill_time >= intaval_snake_skill:
                keyboard.press('7')
                random_delay()
                keyboard.release('7')
                last_snake_skill_time = now
                print("巻き込む蛇みたいな全体スキル設置！")
            
            """
            #自分で定義したロジック
            """
            #action_define()
            another_action()
            position_counter += 1
            # 場所位置修正
            if position_counter == 12:
                position_counter = 0
                keyboard.press('left')
                move_mini_delay()
                keyboard.release('left')
                move_mini_delay()
                keyboard.send('9')
                print("報告  :12回移動したので左へ位置修正!")
                print("スキル:大天狗出現!")
                
            
            # 置きスキル(石)
            if now - last_okiishi_skill_time >= intaval_okiishi_skill:
                keyboard.press('shift')
                random_delay()
                keyboard.release('shift')
                last_okiishi_skill_time = now
                print("置きスキル(石)設置！")
    finally:
        print("終了しました")

# 行動の定義
def action_define():
    #一段目
    #　化け物追加
    if random_number() %2 == 0:
        keyboard.press('4')
        random_delay()
        keyboard.release('4')
    else:
        keyboard.press('0')
        random_delay()
        keyboard.release('0')

    if random_number() %2 == 0: # 一段目初手攻撃
        attack()
    else:
        attack_2()
    move_right()
    attack()
    move_left()
    
    #二段目
    random_long_delay()
    move_up()
    if random_number() %2 == 0: # 一段目初手攻撃
        attack()
    else:
        attack_2()
    move_left()
    attack()
    move_right()
    #天狗攻撃
    if random_number() %2 == 0:
        tengu_attack()
    
    #三段目
    move_up()
    if random_number() %2 == 0: # 一段目初手攻撃
        attack()
    else:
        attack_2()
    random_delay()
    move_right()
    attack()
    move_left()
    # 2段下に降りる
    if random_number() %2 == 0:
        move_down()
        random_long_delay()
        move_down()
    else:
        nomal_down()
        random_long_delay()
        nomal_down()
    #一番下にいるので右を見る
    keyboard.send('right')
    random_delay()
    # 必要ならここでバフかける
    if random_number() %2 == 0:
        keyboard.press('a')
        random_delay()
        keyboard.release('a')

def another_action():
    
    #　化け物追加
    if random_number() %2 == 0:
        keyboard.press('4')
        mini_delay()
        keyboard.release('4')
    else:
        keyboard.press('0')
        random_delay()
        keyboard.release('0')

    # 天狗攻撃いっぞ！
    # 1段目
    attack_2()
    actions.move_right()  # 新しいモジュール名で呼び出し
    attack_2()
    actions.move_left()   # 新しいモジュール名で呼び出し
    attack()
    move_mini_delay()
    move_up()   #上に移動

    # 2段目
    keyboard.send('left')#左を見る
    attack_2()
    move_mini_delay()
    actions.move_left()
    if random_number() %2 == 0:
        attack()
    else:
        attack_2()
    move_mini_delay()
    actions.move_right()
    move_mini_delay()
    keyboard.send('3')  #大天狗出し
    move_up()

    # 3段目
    keyboard.send('right')#右を見る
    attack()
    move_mini_delay()
    actions.move_right()
    move_mini_delay()
    attack_2()
    move_mini_delay()
    actions.move_left()
    
    #　降りる
    random_long_delay()
    actions.move_down()
    random_long_delay()
    attack_2()
    random_long_delay()
    actions.move_down()
    mini_delay()

    # バフかけ
    if random_number() %2 == 0:
        keyboard.send('a')
        mini_delay()
        # ゴミ(ペット)に餌
        if random_number() %2 == 0:
            keyboard.send('F11')
    else:
        keyboard.send('s')
        mini_delay()

    
    

    

if __name__ == "__main__":
    print("F1でマクロ開始、ESCで停止")
    keyboard.add_hotkey('f1', main_macro)
    keyboard.add_hotkey('esc', stop_macro)
    keyboard.wait()  # 何かキーが押されるまで待機（ESCでstop_macroが呼ばれる） 
