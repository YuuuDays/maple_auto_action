from src import paradin_action as a
import time
import random
from datetime import datetime, timedelta, timezone

#paradin用
#========================
# メイン
#========================

start_time = time.time()

def action_define():
    #　左上3段目
    time.sleep(2)
    a.time_60_attack()

    a.which_one_n_attack()
    a.complex_random_delay()
    a.down_move

    # 左上2段目
    a.complex_random_delay()
    a.which_one_n_attack()
    a.which_one_n_attack()
    a.complex_random_delay()
    a.down_move()

    # 左上1段目
    a.which_n_or_special()
    a.complex_random_delay()
    a.down_move()

    # # 最下層
    # complex_random_delay()
    # which_one_attack()
    # right_move()
    # special_attack()
    # complex_random_delay()
    # which_one_attack()
    # right_move()

    # # 右側
    # up_move1()
    # move_mini_delay()
    # keyboard.press('left')
    # time.sleep(0.4)
    # keyboard.release('left')

    # complex_random_delay()
    # which_one_attack()
    # complex_random_delay()

    # up_move1()
    # which_one_attack()
    # complex_random_delay()

    # # -----ここから折り返し

    # #　右上3段目
    # which_one_attack()
    # move_mini_delay()
    # down_move()

    # # 右上2段目
    # complex_random_delay()
    # which_one_attack()
    # complex_random_delay()
    # down_move()

    # #　一番下
    # complex_random_delay()
    # which_one_attack()
    # left_move()

    # if random.randint(0, 1) == 0:
    #     keyboard.press('space')
    #     time.sleep(0.5)
    #     keyboard.release('space')
    # else:
    #     keyboard.press('shift')
    #     time.sleep(0.5)
    #     keyboard.release('shift')
    # time.sleep(0.5)
    
    # special_attack()
    # which_one_attack()
    # left_move()

    # #上ります
    # mini_delay()
    # up_move1()

    # keyboard.press('right')
    # time.sleep(0.4)
    # keyboard.release('right')

    # move_mini_delay()
    # which_one_attack()
    # complex_random_delay()

    # up_move1()
    # which_one_attack()
    # complex_random_delay()

    # keyboard.press('d')

    # 1周ごとに経過時間を表示
    elapsed = time.time() - start_time
    print(f"経過時間:{int(elapsed//60)}分({int(elapsed%60)}秒)")