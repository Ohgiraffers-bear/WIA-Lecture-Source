import streamlit as st
import random
import time

restaurants = [
    "사이길 곱창",
    "가마솥 백반",
    "경상도쭈꾸미",
    "명동칼국수",
    "농부의밥상",
    "홍대돼지집",
    "육풍한우",
    "참설렁탕",
    "창원중국집",
    "팔선반점",
    "도야돈까스",
    "오코노미야끼",
    "김밥천국(성산점)",
    "무교동낙지",
    "신선설농탕",
    "테라로사 카페&레스토랑",
    "빅버거",
    "마마스키친",
    "카페 드롭탑",
    "앙쥬베이커리"
]

st.markdown(
    """
    <style>
    body {
        background-color: #e3f2fd;
    }
    .stApp {
        background-color: #e3f2fd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("창원 현대위아 근처 랜덤 회식장소 추천기")

st.write(
    """
    아래 버튼을 클릭하면 20개 맛집 리스트 중에서 랜덤으로 하나를 추천해줍니다.
    회식 장소 고민 끝!  
    """
)

if st.button("오늘의 랜덤 회식장소 추천받기!"):
    placeholder = st.empty()
    spin_names = random.sample(restaurants, len(restaurants))  # 음식점 이름 섞기
    for i in range(30):   # 3초 동안 0.1초마다 한 번씩 이름 바뀜
        name = random.choice(spin_names)
        placeholder.markdown(
            f"<h2 style='text-align: center; color: #FFB300;'>{name}</h2>", 
            unsafe_allow_html=True
        )
        time.sleep(0.1)

    selected = random.choice(restaurants)

    placeholder.markdown(
        f"<h2 style='text-align: center; color: #32CD32;'>🎉 오늘의 추천 회식 장소는:<br><b>{selected}</b> 입니다! 🎉</h2>", 
        unsafe_allow_html=True
    )
    st.balloons()   # <-- 풍선 효과 여기!


st.markdown("-----")
st.subheader("전체 맛집 리스트")
st.write(restaurants)

