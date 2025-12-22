import time, json
from typing import Optional
from pynput import keyboard
from datetime import datetime
from pathlib import Path

events: list[dict[str, object]] = []
start_time = time.perf_counter()
listener: Optional[keyboard.Listener] = None

# 保存先ディレクトリ（なければ作る♡）
BASE_DIR = Path(__file__).resolve().parent.parent
RECORD_DIR = BASE_DIR / "records"
RECORD_DIR.mkdir(exist_ok=True)

def now() -> float:
    return round(time.perf_counter() - start_time, 4)

def key_to_str(key) -> str | None:
    if key is None:
        return None
    return getattr(key, "char", None) or getattr(key, "name", None)

def make_filename() -> Path:
    """
    record_YYYY-MM-DD_HH-MM-SS.json
    みたいな名前を作る♡
    """
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return RECORD_DIR / f"record_{ts}.json"

def on_press(key) -> None:
    events.append({
        "time": now(),
        "type": "press",
        "key": key_to_str(key),
    })

def on_release(key) -> None:
    events.append({
        "time": now(),
        "type": "release",
        "key": key_to_str(key),
    })

    if key == keyboard.Key.esc:
        path = make_filename()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(events, f, indent=2, ensure_ascii=False)

        print(f"保存したよ♡ → {path.name}")

        if listener:
            listener.stop()
        return

def record_keys() -> None:
    print("録画するよ♡（ESCで保存して終了）")
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
