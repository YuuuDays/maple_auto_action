import lab_behind_the_closed_door_4,sekainohate_2_5_ren
import src.ren_action as test_ren
import src.key_input as key_input
import src.key_reproduction as key_rep

import time
from datetime import datetime, timedelta, timezone
from typing import Callable, Optional

#動きの記録
def action_record():
    key_input.record_keys()

#動きの再生
def action_reproduction():
    key_rep.play_record()

# 記録と再生の選択肢
def action_select():
    action: Optional[Callable[[], None]] = None
    print("記録と再生どちらにしますか")
    print("1:再生")
    print("2:記録")
    print("/n")

    choise = input().strip()

    #再生
    if choise == "1":
        action = action_reproduction
    #記録
    elif choise== "2":
        action = action_record
    else:
        print("1か2を入れてください")
        return
    
    assert action is not None  # ここで型を確定
    action()


def main():
    action_select()

    


def main_action():
    input_number = 0
    action: Optional[Callable[[], None]] = None
    #選択し
    print("\nどっちを起動する？")
    print("1:paradinを起動")
    print("2:ren")
    print("/n")

    choise = input("plz input number 1 or 2").strip()

    if choise == "1":
        action = lab_behind_the_closed_door_4.action_define
    elif choise== "2":
        action = sekainohate_2_5_ren.action_define
    else:
        print("1か2を入れてください")
        return
    
    assert action is not None  # ここで型を確定

    # プログラム起動時に「マクロ開始！」を表示し、その後に日本時間の現在時刻を表示
    JST = timezone(timedelta(hours=9), 'JST')
    print("マクロ開始！")
    print("現在時刻: ", datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S"))
    
    while True:
        action()

if __name__ == "__main__":
    main()