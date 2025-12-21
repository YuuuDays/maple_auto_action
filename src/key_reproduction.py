import time, json
from pynput.keyboard import Controller, Key
from pathlib import Path

def play_record():
    """record.json を読み込んでキー操作を再生する♡"""

    kb = Controller()

    BASE_DIR = Path(__file__).resolve().parent.parent
    json_path = BASE_DIR / "record.json"

    with open(json_path, encoding="utf-8") as f:
        events = json.load(f)

    start = time.perf_counter()

    def str_to_key(key_str):
        if key_str is None:
            return None
        if len(key_str) == 1:
            return key_str
        try:
            return Key[key_str]
        except KeyError:
            return None

    for e in events:
        # 指定時刻まで待つ（元の入力タイミング再現♡）
        while time.perf_counter() - start < e["time"]:
            pass

        k = str_to_key(e.get("key"))
        if k is None:
            continue

        if e["type"] == "press":
            kb.press(k)
        elif e["type"] == "release":
            kb.release(k)
