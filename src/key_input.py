import time, json
from typing import Optional
from pynput import keyboard

events: list[dict[str, object]] = []
start_time = time.perf_counter()
listener: Optional[keyboard.Listener] = None

def now() -> float:
    return round(time.perf_counter() - start_time, 4)

def key_to_str(key) -> str | None:
    if key is None:
        return None
    return getattr(key, "char", None) or getattr(key, "name", None)

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
        with open("record.json", "w", encoding="utf-8") as f:
            json.dump(events, f, indent=2, ensure_ascii=False)
        if listener:
            listener.stop()
        return

def record_keys() -> None:
    print("録画するよ")
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
