import pyautogui
import keyboard

# keyboard 라이브러리 설치필요
# pip install keyboard
print("스페이스바를 누르면 현재 마우스 좌표가 출력됩니다.")
print("엔터를 누르면 프로그램이 종료됩니다.")

while True:
    if keyboard.is_pressed('space'):
        x, y = pyautogui.position()
        print(f"현재 마우스 좌표: ({x}, {y})")
        # 연속감지 방지 (스페이스바를 떼는 동안 대기)
        while keyboard.is_pressed('space'):
            pass
    if keyboard.is_pressed('enter'):
        print("프로그램을 종료합니다!")
        break