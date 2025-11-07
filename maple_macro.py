import keyboard
import time
import random

# =============================
# keyboardモジュールの主な使い方まとめ
# keyboard.press(key)      : 指定したキーを押しっぱなしにする
# keyboard.release(key)    : 指定したキーを離す
# keyboard.send(key)       : 指定したキーを一度だけ押す
# keyboard.add_hotkey('esc', func) : 指定キーで関数を呼び出す
# =============================

# --- 設定 ---
MOVE_KEYS = ['left', 'right', 'up', 'down']  # 移動キー
ATTACK_KEYS = ['q', '2']  # 攻撃キー（例：a, s）
PERIODIC_KEYS = ['1', '2']  # 定期的に押したいキー（例：バフ等）

# --- ディレイ（マクロ対策） ---
def random_delay():
    """0.2～1.0秒のランダムディレイ"""
    delay = random.uniform(0.2, 1.0)
    time.sleep(delay)

# --- 移動 ---
def move(key):
    """方向キーで移動（ディレイ付き）"""
    if key in MOVE_KEYS:
        keyboard.press(key)
        random_delay()
        keyboard.release(key)

# --- 攻撃 ---
def attack(key):
    """攻撃キーを押す（ディレイ付き）"""
    if key in ATTACK_KEYS:
        keyboard.press(key)
        random_delay()
        keyboard.release(key)

# --- 定期的なキー押下 ---
def periodic_key_press(start_time, interval_sec=180):
    """
    プログラム開始からinterval_secごとにPERIODIC_KEYSを順に押す
    例：interval_sec=180なら3分ごと
    """
    now = time.time()
    if int(now - start_time) % interval_sec == 0:
        for key in PERIODIC_KEYS:
            keyboard.send(key)
            print(f"{key} を定期的に押しました")
            time.sleep(0.1)  # 連打防止

# --- ランダム要素の例 ---
def random_action():
    """ランダムで移動か攻撃を実行"""
    if random.random() < 0.5:
        move(random.choice(MOVE_KEYS))
    else:
        attack(random.choice(ATTACK_KEYS))

# --- メイン実行枠組み ---
def main_macro():
    print("マクロ開始！ESCで停止")
    is_running = True
    start_time = time.time()

    def stop_macro():
        nonlocal is_running
        print("マクロを停止します")
        is_running = False

    keyboard.add_hotkey('esc', stop_macro)

    try:
        while is_running:
            # ここに自分のロジックを書く
            random_action()  # ランダム行動例
            periodic_key_press(start_time, interval_sec=180)  # 3分ごとにバフ等
            time.sleep(0.1)  # CPU負荷軽減
    finally:
        print("終了しました")

if __name__ == "__main__":
    print("F1でマクロ開始、ESCで停止")
    keyboard.add_hotkey('f1', main_macro)
    # keyboard.add_hotkey('esc', stop_macro)
    keyboard.wait()  # 何かキーが押されるまで待機（ESCでstop_macroが呼ばれる） 