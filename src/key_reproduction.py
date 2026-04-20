import time, json, threading
from pynput.keyboard import Controller, Key, Listener
from pathlib import Path

LAST_USED_FILE = None  # play_record内で初期化

def _load_last_used(record_dir: Path) -> dict:
    path = record_dir / ".last_used.json"
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

def _save_last_used(record_dir: Path, last_used: dict, key: str) -> None:
    last_used[key] = time.time()
    path = record_dir / ".last_used.json"
    path.write_text(json.dumps(last_used, indent=2), encoding="utf-8")

PAUSE_KEY = Key.f8   # 一時停止/再開
STOP_KEY  = Key.f9   # 中止（任意）

def choose_from_list(items, title, show_name=lambda p: p.name, last_used_times=None):
    """番号固定で表示順だけ変わる選択ユーティリティ♡
    last_used_times: items と同じ長さの float リスト（0.0 = 未使用）
    """
    if not items:
        print("選べる項目がないよ…♡")
        return None

    # (元の番号, item) ペアに変換
    numbered = list(enumerate(items, start=1))

    if last_used_times:
        # 未使用を元番号順で先に、使用済みを使用時刻昇順で後に（最後に使ったものが一番下）
        def sort_key(pair):
            i, _ = pair
            t = last_used_times[i - 1]
            return (1, t) if t > 0 else (0, i)
        display_order = sorted(numbered, key=sort_key)
    else:
        display_order = numbered

    print(title)
    for i, it in display_order:
        print(f"[{i}] {show_name(it)}")

    # 番号 → item の逆引きマップ
    num_map = {i: it for i, it in numbered}
    try:
        choice = int(input("\n番号を選んでね → "))
        item = num_map.get(choice)
        if item is None:
            print("番号が正しくないよ…♡")
            return None
        return item
    except ValueError:
        print("番号が正しくないよ…♡")
        return None

def play_record():
    """records/配下のフォルダ→json を2段階で選んで再生♡"""

    kb = Controller()

    BASE_DIR = Path(__file__).resolve().parent.parent
    RECORD_DIR = BASE_DIR / "records"

    last_used = _load_last_used(RECORD_DIR)

    # --- 1段目：records直下のフォルダを選ぶ ---
    folders = sorted([p for p in RECORD_DIR.iterdir() if p.is_dir()])
    folder_times = [last_used.get(p.name, 0.0) for p in folders]

    folder = choose_from_list(
        folders,
        title="再生したいフォルダを選んでね♡",
        show_name=lambda p: p.name,
        last_used_times=folder_times,
    )
    if folder is None:
        return

    # --- 2段目：そのフォルダ内のjsonを選ぶ ---
    json_files = sorted(folder.glob("*.json"))
    file_times = [last_used.get(f"{folder.name}/{p.name}", 0.0) for p in json_files]

    json_path = choose_from_list(
        json_files,
        title=f"\n『{folder.name}』の中の記録一覧だよ♡",
        show_name=lambda p: p.name,
        last_used_times=file_times,
    )
    if json_path is None:
        return

    _save_last_used(RECORD_DIR, last_used, folder.name)
    _save_last_used(RECORD_DIR, last_used, f"{folder.name}/{json_path.name}")

    print(f"\n選択されたファイル → {folder.name}/{json_path.name}")
    print("再生開始♡（一時停止/再開: F8, 中止: F9）")

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

    pause_event = threading.Event()   # set() されている間は「停止中」
    stop_event = threading.Event()    # set() されたら中止

    def on_press(key):
        if key == PAUSE_KEY:
            if pause_event.is_set():
                pause_event.clear()
                print("▶ 再開♡")
            else:
                pause_event.set()
                print("⏸ 一時停止♡（F8で再開）")
        elif key == STOP_KEY:
            stop_event.set()
            pause_event.clear()
            print("⏹ 中止♡")

    listener = Listener(on_press=on_press)
    listener.start()

    start = time.perf_counter()
    paused_total = 0.0
    pause_started_at = None

    try:
        for e in events:
            if stop_event.is_set():
                break

            target_time = float(e.get("time", 0.0))

            while True:
                if stop_event.is_set():
                    break

                if pause_event.is_set():
                    if pause_started_at is None:
                        pause_started_at = time.perf_counter()
                    time.sleep(0.03)
                    continue
                else:
                    if pause_started_at is not None:
                        paused_total += (time.perf_counter() - pause_started_at)
                        pause_started_at = None

                elapsed = time.perf_counter() - start - paused_total
                if elapsed >= target_time:
                    break

                time.sleep(0.03)

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
