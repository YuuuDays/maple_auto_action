import lab_behind_the_closed_door_4
import time
from datetime import datetime, timedelta, timezone

def main():
    # プログラム起動時に「マクロ開始！」を表示し、その後に日本時間の現在時刻を表示
    JST = timezone(timedelta(hours=9), 'JST')
    print("マクロ開始！")
    print("現在時刻: ", datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S"))
    
    lab_behind_the_closed_door_4.action_define()







if __name__ == "__main__":
    main()