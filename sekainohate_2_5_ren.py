from src import ren_action as a
import time
import random
from datetime import datetime, timedelta, timezone
import keyboard


#ren用
#========================
# メイン
#========================

start_time = time.time()

def action_define():
    # 左上2段目
    time.sleep(2)
    a.throw_oneThird_shuriken()

    a.which_one_n_attack()
    a.complex_random_delay()
    a.down_move()

    #左上1段目
    a.complex_random_delay()
    a.which_one_n_attack()
    a.complex_random_delay()
    a.down_move()

    #最下層
    a.complex_random_delay()
    a.no_meanig_select()
    a.n_attack()

    #1回移動
    a.mini_delay()
    a.right_move()
    a.n_attack()

    #2回移動
    a.mini_delay()
    a.right_move()
    a.which_one_n_attack()

    #3回移動
    a.complex_random_delay()
    a.right_move()
    a.n_attack()

    #上に行く準備
    keyboard.press('left')
    a.complex_random_delay()
    keyboard.release('left')
    a.complex_random_delay()

    a.up_move1()

    #右1段目
    a.complex_random_delay()
    a.which_one_n_attack()
    a.mini_delay()
    a.throw_oneThird_shuriken()

    a.complex_random_delay()

    #右2段目
    a.complex_random_delay()
    a.up_move1()

    a.n_attack()
    a.mini_delay()

    #折り返しいっぞ！
    a.complex_random_delay()
    a.down_move()

    #折り返し右1段
    a.complex_random_delay()
    a.throw_oneThird_shuriken()
    a.mini_delay()
    a.which_one_n_attack()
    a.mini_delay()
    a.down_move()

    #折り返し最下層
    a.complex_random_delay()
    a.n_attack()
    a.mini_delay()
    a.no_meanig_select()
    
    #左1回
    a.mini_delay()
    a.left_move()
    a.complex_random_delay()
    a.n_attack()

    #左2回
    a.complex_random_delay()
    a.left_move()
    a.complex_random_delay()
    a.n_attack()
    a.mini_delay()
    a.no_meanig_select()

    #左3回
    a.complex_random_delay()
    a.left_move()
    a.complex_random_delay()
    a.which_one_n_attack()
    a.mini_delay()
    #調整
    keyboard.press('right')
    a.mini_delay()
    keyboard.release('right')

    #左側1段目へ
    a.complex_random_delay()
    a.up_move1()
    a.mini_delay()
    a.n_attack()

    #左側2段目へ
    a.complex_random_delay()
    a.up_move1()
    a.mini_delay()
    a.which_one_n_attack()
    a.complex_random_delay()

    # 1周ごとに経過時間を表示
    elapsed = time.time() - start_time
    print(f"経過時間:{int(elapsed//60)}分({int(elapsed%60)}秒)")