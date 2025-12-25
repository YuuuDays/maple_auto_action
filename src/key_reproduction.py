import time, json, threading
from pynput.keyboard import Controller, Key, Listener
from pathlib import Path

PAUSE_KEY = Key.f8   # 一時停止/再開
STOP_KEY  = Key.f9   # 中止（任意）

def play_record():
    """records フォルダから選んだJSONを再生（先頭time補正 + 一時停止/再開）"""

    kb = Controller()

    BASE_DIR = Path(__file__).resolve().parent.parent
    RECORD_DIR = BASE_DIR / "records"

    json_files = sorted(RECORD_DIR.glob("*.json"))
    if not json_files:
        print("再生できる記録がないよ…♡")
        return

    print("再生可能な記録一覧♡")
    for i, path in enumerate(json_files, start=1):
        print(f"[{i}] {path.name}")

    try:
        choice = int(input("\n番号を選んでね → "))
        json_path = json_files[choice - 1]
    except (ValueError, IndexError):
        print("番号が正しくないよ…♡")
        return

    print(f"選択されたファイル → {json_path.name}")
    print(f"再生開始♡（一時停止/再開: F8, 中止: F9）")

    with open(json_path, encoding="utf-8") as f:
        events = json.load(f)

    if not events:
        print("中身が空だったよ…♡")
        return

    # --- 先頭timeを0に補正 ---
    first_time = float(events[0].get("time", 0.0))
    for e in events:
        t = float(e.get("time", 0.0))
        e["time"] = max(0.0, t - first_time)

    def str_to_key(key_str):
        if key_str is None:
            return None
        if isinstance(key_str, str) and len(key_str) == 1:
            return key_str
        try:
            return Key[key_str]
        except Exception:
            return None

    # --- 一時停止/中止フラグ（スレッド安全♡） ---
    pause_event = threading.Event()   # set() されている間は「停止中」
    stop_event = threading.Event()    # set() されたら中止

    def on_press(key):
        # F8でトグル（一時停止/再開）
        if key == PAUSE_KEY:
            if pause_event.is_set():
                pause_event.clear()
                print("▶ 再開♡")
            else:
                pause_event.set()
                print("⏸ 一時停止♡（F8で再開）")

        # F9で中止
        elif key == STOP_KEY:
            stop_event.set()
            pause_event.clear()  # 停止中でも抜けられるように
            print("⏹ 中止♡")

    # 監視用リスナー（別スレッド）
    listener = Listener(on_press=on_press)
    listener.start()

    # --- 再生本体 ---
    start = time.perf_counter()
    paused_total = 0.0          # 停止していた合計時間
    pause_started_at = None     # 停止開始時刻

    try:
        for e in events:
            if stop_event.is_set():
                break

            target_time = float(e.get("time", 0.0))

            # 目標時刻まで待つ（途中で一時停止したら補正する♡）
            while True:
                if stop_event.is_set():
                    break

                # 一時停止中はここで待つ
                if pause_event.is_set():
                    if pause_started_at is None:
                        pause_started_at = time.perf_counter()
                    time.sleep(0.01)
                    continue
                else:
                    # 停止から復帰した瞬間、停止時間を加算
                    if pause_started_at is not None:
                        paused_total += (time.perf_counter() - pause_started_at)
                        pause_started_at = None

                elapsed = time.perf_counter() - start - paused_total
                if elapsed >= target_time:
                    break

                # CPU爆食い防止♡（精度はそこそこ維持）
                time.sleep(0.001)

            if stop_event.is_set():
                break

            k = str_to_key(e.get("key"))
            if k is None:
                continue

            etype = e.get("type")
            if etype == "press":
                kb.press(k)
            elif etype == "release":
                kb.release(k)

    finally:
        listener.stop()

    if stop_event.is_set():
        print("再生を中止したよ…♡")
    else:
        print("再生おわり♡")
