import pyautogui
import time


# '시작년도 클릭 좌표 (예: 100 200): 
start_year_pos = (940,767)
# 시작월 클릭 좌표 (예: 120 200):
start_month_pos = (1074,759)
# '종료년도 클릭 좌표 (예: 100 300)
end_year_pos = (1272,766)
# 종료월 클릭 좌표 (예: 120 300):
end_month_pos = (1394,766)
# '검색버튼 좌표 (예: 200 400):
search_btn_pos = (1441,1032)
# 엑셀 다운로드 버튼 좌표 (예: 300 500):
excel_btn_pos = (1519,1100)

def year_click(year):
    # 1. 시작년도 클릭 → 년도 입력(2025) → 엔터
    pyautogui.click(start_year_pos) # 클릭
    pyautogui.write(year) # 키보드 입력? # 문자열을 입력
    pyautogui.press('enter') # 키보드 입력
    time.sleep(0.2)

    # 3. 종료년도 클릭 → 년도 입력(2025) → 엔터
    pyautogui.click(end_year_pos)
    pyautogui.write(year)
    pyautogui.press('enter')
    time.sleep(0.2)

def month_click(start_m, end_m):
    # 2. 시작월 클릭 → 월 입력(01) → 엔터
    pyautogui.click(start_month_pos)
    pyautogui.write(start_m)
    pyautogui.press('enter')
    time.sleep(0.2)

    # 4. 종료월 클릭 → 월 입력(06) → 엔터
    pyautogui.click(end_month_pos)
    pyautogui.write(end_m)
    pyautogui.press('enter')
    time.sleep(0.2)

def download():
    # 5. 검색버튼 클릭 → 5초 이상 대기
    pyautogui.click(search_btn_pos)
    time.sleep(5)

    # 6. 엑셀파일 다운로드 클릭 → 1초 대기 → 엔터
    pyautogui.click(excel_btn_pos)
    time.sleep(1)
    pyautogui.press('enter')

# 반복하고 싶은 년도
years = ['2023','2024','2025']

# month
month_pair = [('01','06'), ('07','12')]

for year in years:
    # 클릭 좌표를 미리 입력 (예: input을 통해 직접 지정)
    print('각 버튼의 좌표를 마우스로 확인해서 아래에 입력하세요!')

    time.sleep(3) # 준비 시간 (예: 마우스를 움직일 시간)
    
    # year 설정
    year_click(year)

    # month 설정
    for start_m, end_m in month_pair:
        
        month_click(start_m, end_m)

        download()


print('매크로 작업이 완료되었습니다!')
