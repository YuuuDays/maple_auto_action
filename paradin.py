import keyboard
import time
import random
from gekisen_nishi import *
# import pyautogui  # 必要に応じてコメントアウトを外す

# =============================
# keyboardモジュールの主な使い方まとめ
# keyboard.press(key)      : 指定したキーを押しっぱなしにする
# keyboard.release(key)    : 指定したキーを離す
# keyboard.send(key)       : 指定したキーを一度だけ押す
# keyboard.add_hotkey('esc', func) : 指定キーで関数を呼び出す
# =============================

# ===================
# 初期化
# ===================
is_running = False  # グローバルで管理

# メイン処理#メイン処理



# ====================================================================
#起動
def main_macro():
    global is_running
    is_running = True
    print("マクロを開始します")
    while is_running:
        #ここに処理を入れる↓
        time.sleep(0.1)
        gekisen_nishi_action()

        # action_define()

# 停止
def stop_macro():
    global is_running
    print("ESCキーが押されました！マクロを停止します")
    is_running = False

# 強制終了
def force_stop():
    global is_running
    print("Ctrl+Cで強制終了します")
    is_running = False
    import sys
    sys.exit()

# デバッグ用：ESCキーが押されたかテスト
def test_esc():
    print("ESCキーが認識されました！")

# 初期動作
if __name__ == "__main__":
    print("1でマクロ開始、ESCまたはF12で停止、Ctrl+Cで強制終了")
    keyboard.add_hotkey('1', main_macro)
    keyboard.add_hotkey('esc', stop_macro)
    keyboard.add_hotkey('f12', stop_macro)  # 代替キー
    keyboard.add_hotkey('ctrl+c', force_stop)  # 強制終了
    keyboard.add_hotkey('esc', test_esc)  # デバッグ用
    print("ESCキーのホットキーを登録しました")
    keyboard.wait()  # 何かキーが押されるまで待機

