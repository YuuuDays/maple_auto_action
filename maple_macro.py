import pyautogui
import keyboard
import time
import random
import numpy as np
from PIL import ImageGrab
import cv2

class MapleMacro:
    def __init__(self):
        # 人間らしい操作のための設定
        pyautogui.PAUSE = 0.1  # 基本待機時間
        pyautogui.FAILSAFE = True  # マウスを画面左上に移動で緊急停止
        
        # キー設定
        self.jump_key = 'alt'
        self.attack_key = 'ctrl'
        self.buff_key = '1'
        
        # 動作フラグ
        self.is_running = False
        
    def human_like_delay(self, min_delay=0.1, max_delay=0.3):
        """人間らしい待機時間を生成"""
        time.sleep(random.uniform(min_delay, max_delay))
    
    def human_like_mouse_move(self, x, y, duration=0.5):
        """人間らしいマウス移動"""
        # 現在のマウス位置
        current_x, current_y = pyautogui.position()
        
        # ベジェ曲線を使用して自然な動きを生成
        points = self._generate_bezier_curve(
            (current_x, current_y),
            (x, y),
            num_points=50
        )
        
        # 各ポイントを移動
        for point in points:
            pyautogui.moveTo(point[0], point[1], duration=duration/len(points))
            self.human_like_delay(0.01, 0.03)
    
    def _generate_bezier_curve(self, start, end, num_points=50):
        """ベジェ曲線を生成して自然なマウス移動を実現"""
        # 制御点をランダムに生成
        control1 = (
            start[0] + random.uniform(-100, 100),
            start[1] + random.uniform(-100, 100)
        )
        control2 = (
            end[0] + random.uniform(-100, 100),
            end[1] + random.uniform(-100, 100)
        )
        
        points = []
        for t in np.linspace(0, 1, num_points):
            # 3次ベジェ曲線の計算
            x = (1-t)**3 * start[0] + 3*(1-t)**2*t * control1[0] + 3*(1-t)*t**2 * control2[0] + t**3 * end[0]
            y = (1-t)**3 * start[1] + 3*(1-t)**2*t * control1[1] + 3*(1-t)*t**2 * control2[1] + t**3 * end[1]
            points.append((x, y))
        
        return points
    
    def press_key(self, key, duration=0.1):
        """キーを押す（人間らしい間隔で）"""
        pyautogui.keyDown(key)
        self.human_like_delay(duration, duration*1.5)
        pyautogui.keyUp(key)
    
    def start_macro(self):
        """マクロを開始"""
        self.is_running = True
        print("マクロを開始します...")
        
        try:
            while self.is_running:
                # 基本の攻撃パターン
                self.press_key(self.attack_key)
                self.human_like_delay(0.2, 0.4)
                
                # ランダムなジャンプ
                if random.random() < 0.3:  # 30%の確率でジャンプ
                    self.press_key(self.jump_key)
                    self.human_like_delay(0.3, 0.6)
                
                # バフの使用（5分に1回程度）
                if random.random() < 0.001:
                    self.press_key(self.buff_key)
                    self.human_like_delay(1.0, 2.0)
                
                # 完全にランダムな待機時間
                if random.random() < 0.1:  # 10%の確率で長めの待機
                    self.human_like_delay(1.0, 3.0)
                
        except KeyboardInterrupt:
            self.stop_macro()
    
    def stop_macro(self):
        """マクロを停止"""
        self.is_running = False
        print("マクロを停止しました")

if __name__ == "__main__":
    macro = MapleMacro()
    print("マクロを開始するには 'F2' を押してください")
    print("マクロを停止するには 'F3' を押してください")
    
    keyboard.add_hotkey('F2', macro.start_macro)
    keyboard.add_hotkey('F3', macro.stop_macro)
    
    keyboard.wait('esc')  # ESCキーでプログラム終了 