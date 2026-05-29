import streamlit as st

# 1. 앱 제목 및 설정
st.set_page_config(page_title="디지털 자판기", page_icon="🥤", layout="centered")
st.title("🥤 미니 디지털 자판기")
st.write("원하는 음료를 선택하고 금액을 입력해주세요!")

# 2. 자판기 상품 데이터 (메뉴 및 가격)
menu = {
    "콜라 🥤": 1500,
    "사이다 🍏": 1400,
    "이온음료 ⚡": 1600,
    "생수 💧": 1000,
    "커피 ☕": 2000
}

# 세션 상태(Session State) 초기화 -> 구매 후 잔액이나 상태를 유지하기 위함
if "wallet" not in st.session_state:
    st.session_state.wallet = 0

# 화면을 두 개의 열(Column)로 분할
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 메뉴판")
    # 표 형태로 메뉴와 가격 보여주기
    for item, price in menu.items():
        st.write(f"**{item}** : {price:,}원")

with col2:
    st.subheader("🪙 금액 투입 및 선택")
    
    # 3. 돈 투입받기
    insert_money = st.number_input("돈을 넣어주세요 (원)", min_value=0, step=100, value=0)
    
    # '금액 투입' 버튼 클릭 시 지갑에 금액 추가
    if st.button("금액 투입하기"):
        st.session_state.wallet += insert_money
        st.rerun() # 화면 새로고침하여 잔액 반영
        
    st.info(f"현재 투입된 총 금액: **{st.session_state.wallet:,}원**")


# 4. 음료 선택 및 구매 버튼
st.subheader("🛍️ 음료 구매")
selected_item = st.selectbox("구매할 음료를 선택하세요", list(menu.keys()))
price = menu[selected_item]

if st.button(f"{selected_item} 구매하기 ({price:,}원)"):
    if st.session_state.wallet >= price:
        # 잔액 차감
        st.session_state.wallet -= price
        st.success(f"🎉 {selected_item}이(가) 나왔습니다! 맛있게 드세요!")
        st.balloons() # 축하 효과🎈
        st.info(f"남은 잔돈: **{st.session_state.wallet:,}원**")
    else:
        st.error(f"❌ 금액이 부족합니다! {price - st.session_state.wallet:,}원이 더 필요합니다.")

# 5. 잔돈 반환 기능
if st.session_state.wallet > 0:
    if st.button("잔돈 반환받기 🪙"):
        st.warning(f"🪙 잔돈 {st.session_state.wallet:,}원이 반환되었습니다.")
        st.session_state.wallet = 0
        st.rerun()