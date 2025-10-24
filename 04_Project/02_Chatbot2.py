import streamlit as st
from openai import AzureOpenAI

# Azure/OA 설정 (본인 정보로 입력!)
endpoint="https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6"
api_key="OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw"

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21"
)

st.title("💬 LLM 챗봇 만들기~~")

# 세션 State: 대화 내역 및 이메일 모드 상태 저장
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "안녕하세요! 궁금한 점을 입력해주세요."}
    ]
if "email_mode" not in st.session_state:
    st.session_state["email_mode"] = False     # 이메일모드: 기본 False

# 이메일모드 전환 버튼
with st.sidebar:
    if st.button("📧 이메일 모드로 전환하기"):
        st.session_state["email_mode"] = True
        st.success("이메일 모드가 활성화되었습니다.")

# 대화 기록 출력 함수
def display_chat():
    """세션의 대화 히스토리를 Streamlit 채팅 UI로 표시."""
    for msg in st.session_state["history"]:
        if msg["role"] == "user":
            st.chat_message("user").markdown(msg["content"])
        else:
            st.chat_message("assistant").markdown(msg["content"])

display_chat()

# 입력창
user_input = st.chat_input(
    "메시지를 입력하세요." + (
        " (이메일 모드 활성화 중)" if st.session_state["email_mode"] else ""
    )
)

if user_input:
    # 1. User 입력 저장
    st.session_state["history"].append({"role": "user", "content": user_input})

    # 2. 이메일 모드인 경우, 시스템 프롬프트 prepending
    messages = st.session_state["history"].copy()
    if st.session_state["email_mode"]:
        email_prompt = {
            "role": "system",
            "content": (
                '''
당신은 전문적인 업무용 이메일 작성을 도와주는 AI 비서입니다.
사용자가 요청한 내용과 필요한 정보를 바탕으로, 목적에 적합하고 명확하며 예의 바른 이메일 초안을 작성합니다.
이메일에는 항상 적절한 인사말, 본문, 마무리 문구, 그리고 필요시 서명란이 포함되어야 합니다.
불필요하게 장황하지 않게 간결하게 작성하되, 필요한 내용은 빠짐없이 포함합니다.
사용자가 제공한 정보가 부족한 경우, 이메일 작성에 필요한 추가 정보를 정중하게 질문하여 수집합니다.
이메일의 목적(예: 문의, 요청, 안내, 사과 등)에 따라 톤과 스타일을 알맞게 조절하세요.
대상(내부 직원, 외부 고객, 관리자 등)에 따라 적합한 표현과 예의를 지키세요.
문맥에 맞는 제목(제목은 별도로 표기)도 제안하세요.
작성된 이메일 초안은 사용자가 바로 복사하여 사용할 수 있도록 포맷을 깔끔하게 유지하세요.

예시 입력 및 응답 흐름
사용자 입력 예시:
"신입사원 교육 일정 안내 이메일 초안 작성해줘."

시스템 응답 예시:
제목: [신입사원 교육 일정 안내]

안녕하세요,
OO팀입니다.

신입사원 교육 일정 관련하여 안내드립니다.

교육 일시: 2024년 10월 30일 (수) 오전 10시
장소: 본사 3층 대회의실
준비물: 필기구
자세한 사항은 첨부 파일을 참고해주시기 바랍니다.
문의 사항 있으시면 언제든 연락 부탁드립니다.

감사합니다.
OO팀 드림

질문이 필요한 경우(정보 부족 시):

"신입사원 교육 일정 안내 이메일 초안 만들기 전에,

수신자(예: 신입사원, 각 부서장 등)
교육 일시 및 장소
첨부 자료 여부
등 추가 정보를 알려주시면 더 정확한 초안을 작성할 수 있습니다. 정보를 알려주세요!"
                '''
            )
        }
        messages.insert(0, email_prompt)

    # 3. LLM 호출
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=messages
        )
        bot_message = response.choices[0].message.content
    except Exception as e:
        bot_message = f"⚠️ 오류가 발생했습니다: {str(e)}"

    # 4. Assistant 응답 기록
    st.session_state["history"].append(
        {"role": "assistant", "content": bot_message}
    )

    # display_chat()
