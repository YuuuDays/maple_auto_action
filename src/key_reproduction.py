import time, json
from pynput.keyboard import Controller, Key
from pathlib import Path

def play_record():
    """records フォルダから選んだJSONを再生する♡（先頭timeを0に補正）"""

    kb = Controller()

    BASE_DIR = Path(__file__).resolve().parent.parent
    RECORD_DIR = BASE_DIR / "records"

    json_files = sorted(RECORD_DIR.glob("*.json"))
    if not json_files:
        print("再生できる記録がないよ…♡")
        return

    # 一覧表示♡
    print("再生可能な記録一覧♡")
    for i, path in enumerate(json_files, start=1):
        print(f"[{i}] {path.name}")

    # ユーザ選択♡
    try:
        choice = int(input("\n番号を選んでね → "))
        json_path = json_files[choice - 1]
    except (ValueError, IndexError):
        print("番号が正しくないよ…♡")
        return

    print(f"選択されたファイル → {json_path.name}")
    print("再生開始♡")

    with open(json_path, encoding="utf-8") as f:
        events = json.load(f)

    if not events:
        print("中身が空だったよ…♡")
        return

    # ✅ 先頭イベントの time を 0 に補正♡
    first_time = float(events[0].get("time", 0.0))
    for e in events:
        t = float(e.get("time", 0.0))
        e["time"] = max(0.0, t - first_time)

    start = time.perf_counter()

    def str_to_key(key_str):
        if key_str is None:
            return None
        if isinstance(key_str, str) and len(key_str) == 1:
            return key_str
        try:
            return Key[key_str]
        except Exception:
            return None

    for e in events:
        target_time = float(e.get("time", 0.0))

        # 指定時刻まで待つ（補正後のタイミングで再現♡）
        while time.perf_counter() - start < target_time:
            pass

        k = str_to_key(e.get("key"))
        if k is None:
            continue

        etype = e.get("type")
        if etype == "press":
            kb.press(k)
        elif etype == "release":
            kb.release(k)
