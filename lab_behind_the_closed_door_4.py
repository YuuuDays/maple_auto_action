from src import paradin_action as a
import time
import random
from datetime import datetime, timedelta, timezone
import keyboard


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

    # 最下層へ
    a.which_one_n_attack()
    a.complex_random_delay()
    a.which_one_n_attack()
    a.down_move()
    
    # 一番下へついた&移動！
    a.complex_random_delay()
    a.which_one_n_attack()
    a.complex_random_delay()
    a.which_one_n_attack()

    a.right_move()
    a.complex_random_delay()
    a.special_attack()
    a.right_move()
    a.right_move()
    a.fake_action()
    
    
    # 右上に行こう!(位置調整)
    a.complex_random_delay()
    a.which_one_n_attack()
    a.little_turn_left_move()
    a.little_turn_left_move()
    a.complex_random_delay()
    a.up_move1()

    #右1段目
    a.complex_random_delay()
    a.which_n_or_special()
    a.complex_random_delay()
    a.which_n_or_special()
    a.complex_random_delay()
    a.up_move1()
    a.complex_random_delay()

    # 右2段目
    a.which_n_or_special()
    a.which_n_or_special()
    a.complex_random_delay()
    a.up_move1()

    # 右3段目
    a.complex_random_delay()
    a.which_n_or_special()
    a.complex_random_delay()
    a.special_attack()

    if random.randint(0,1) == 0:
        a.spaider_attack()
    else:
        keyboard.send('space')
    
    # ダメ押し用(上に移動できてない場合)
    a.up_move2()
    a.fake_action2()
    a.which_one_n_attack()
    a.which_one_n_attack()
    a.move_mini_delay()
    a.time_60_attack()
    # # -----ここから折り返し

    #降ります4回
    for i in range(4):
        a.complex_random_delay()
        a.down_move()
        a.complex_random_delay()

        if random.randint(0,1) == 0:
            a.special_attack()
            a.fake_action()
        else:
            a.which_one_n_attack()
        a.complex_random_delay()
        if random.randint(0,1) == 0:
            a.special_attack()
        else:
            a.which_one_n_attack()
        
        a.complex_random_delay()


    #また一番下についたので左まで移動
    a.complex_random_delay()
    a.which_one_n_attack()
    a.complex_random_delay()
    a.which_one_n_attack()

    a.left_move()
    a.complex_random_delay()
    a.special_attack()
    a.left_move()
    a.left_move()
    a.fake_action()

    #上るための位置調整
    if random.randint(0,1) == 0:
        a.special_attack()
    else:
        a.which_one_n_attack()

    a.complex_random_delay()
    a.which_one_n_attack()
    a.little_turn_right_move()
    a.little_turn_right_move()
    a.complex_random_delay()
    
    # 無理やり修正するか...
    keyboard.press('left')
    for f in range(7):
        a.move_mini_delay()
    a.which_one_n_attack()
    keyboard.release('left')

    a.little_turn_right_move()
    a.complex_random_delay()
    a.little_turn_right_move()
    a.complex_random_delay()
    a.up_move2()
    a.complex_random_delay()
    
    #めんどいので一番上までgo
    if random.randint(0,1) == 0:
        a.special_attack()
    else:
        a.which_one_n_attack()
    
    a.which_one_n_attack()
    a.complex_random_delay()
    a.up_move2()

    

    # 1周ごとに経過時間を表示
    elapsed = time.time() - start_time
    print(f"経過時間:{int(elapsed//60)}分({int(elapsed%60)}秒)")