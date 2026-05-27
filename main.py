import streamlit as st
import time

# 1. 페이지 설정 (넓은 화면을 선호할 수 있으므로 layout을 자동으로 조절하도록 설정)
st.set_page_config(
    page_title="나만의 커스텀 여행 팜플렛 🗺️",
    page_icon="🎨",
    layout="wide"  # 4~5일 일정을 가로로 넓고 예쁘게 보기 위해 wide로 변경했습니다!
)

# 2. 팜플렛 테마를 위한 커스텀 CSS 스타일 정의
st.markdown("""
<style>
    /* 전체 팜플렛을 감싸는 카드 테두리 스타일 */
    .pamphlet-container {
        background-color: #FFFDF0; /* 따뜻한 크림색 배경 */
        border: 4px dashed #FFB5A7; /* 귀여운 핑크빛 점선 테두리 */
        padding: 25px;
        border-radius: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.08);
        margin-top: 10px;
        margin-bottom: 25px;
    }
    /* 팜플렛 내부 타이틀 */
    .pamphlet-title {
        text-align: center;
        color: #FF7096;
        font-family: 'Malgun Gothic', sans-serif;
        font-weight: bold;
        margin-bottom: 5px;
    }
    /* 하루 일정 카드 스타일 */
    .day-card {
        background-color: #FFFFFF;
        border: 1px solid #FEC5BB;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.04);
        text-align: center;
        margin-bottom: 15px; /* 모바일에서 세로로 정렬될 때를 위한 여백 */
    }
    .day-title {
        background-color: #FFE5EC;
        color: #FF7096;
        font-weight: bold;
        border-radius: 8px;
        padding: 5px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 3. 메인 화면 타이틀 및 소개
st.title("🎨 감성 가득! 맞춤 기간제 여행 팜플렛 ✈️")
st.write("당곡고 친구들 환영합니다! 이름, 나이, MBTI뿐만 아니라 **원하는 여행 기간(몇박 며칠)**까지 선택하여 나만의 맞춤형 3단~5단 접이식 팜플렛을 만들어 보세요! 💖")
st.write("---")

# 4. 여행지 데이터 정의 (각 여행지별 5일치 일정 풀세트 구비 완료!)
travel_options = {
    "NT": [  # 분석가형 (INTJ, INTP, ENTJ, ENTP)
        {
            "name": "영국 런던 🇬🇧",
            "concept": "지적 자극과 역사가 살아 숨 쉬는 탐구 여행",
            "image": "https://images.unsplash.com/photo-1513635269975-59663e0ca1ad?auto=format&fit=crop&w=800&q=80",
            "season": "🌤️ 5월 ~ 9월 (선선하고 해가 가장 긴 골든 시즌!)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "🏛️ 대영박물관 관람\n\n🎡 런던아이 야경 타기", "tip": "💡 박물관은 무료지만 온라인 예약은 필수예요!"},
                {"day": "Day 2 📅", "activity": "🛍️ 소호 거리 소품숍\n\n☕ 정통 애프터눈 티 체험", "tip": "💡 스콘에 클로티드 크림과 잼을 가득 발라요!"},
                {"day": "Day 3 📅", "activity": "🏰 타워브릿지 산책\n\n🎭 유명 뮤지컬 관람", "tip": "💡 당일 아침 '데이시트' 예매로 할인 노리기!"},
                {"day": "Day 4 📅", "activity": "🏰 윈저 성 근교 투어\n\n🍺 로컬 펍 피시앤칩스", "tip": "💡 영국의 펍 문화를 체험하며 기분을 내보세요!"},
                {"day": "Day 5 📅", "activity": "🌳 하이드 파크 자전거\n\n🛍️ 해러즈 백화점 쇼핑", "tip": "💡 백화점 식품관에서 예쁜 홍차 틴케이스 득템하기!"}
            ]
        },
        {
            "name": "미국 뉴욕 🇺🇸",
            "concept": "끊임없이 성장하는 트렌디하고 세련된 도시 여행",
            "image": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=800&q=80",
            "season": "🍂 9월 ~ 11월 (센트럴 파크 단풍이 그림 같은 가을!)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "🗽 자유의 여신상 페리\n\n🌳 센트럴 파크 산책", "tip": "💡 돗자리와 크림치즈 베이글을 포장해 가세요!"},
                {"day": "Day 2 📅", "activity": "🖼️ MoMA 현대미술관\n\n🍕 뉴욕 대표 화덕피자 맛보기", "tip": "💡 금요일 저녁 기부입장 혜택을 미리 확인해요!"},
                {"day": "Day 3 📅", "activity": "🏙️ 타임스퀘어 탐방\n\n🎷 정통 뉴욕 재즈바 공연", "tip": "💡 인기 재즈바는 최소 2주 전에 예약하세요!"},
                {"day": "Day 4 📅", "activity": "🌉 브루클린 브릿지 걷기\n\n📸 덤보 포토존 인생샷", "tip": "💡 해 질 무렵 브루클린 브릿지를 건너면 예술이에요!"},
                {"day": "Day 5 📅", "activity": "🎭 브로드웨이 연극 관람\n\n🛍️ 첼시 마켓 랍스터 먹방", "tip": "💡 타임스퀘어의 TKTS 부스에서 당일 할인 티켓을 노려보세요!"}
            ]
        }
    ],
    "NF": [  # 외교관형 (INFJ, INFP, ENFJ, ENFP)
        {
            "name": "아이슬란드 레이캬비크 🇮🇸",
            "concept": "동화 속 요정의 나라 같은 감성 가득 오로라 여행",
            "image": "https://images.unsplash.com/photo-1504893524553-ac55fce698be?auto=format&fit=crop&w=800&q=80",
            "season": "🌌 10월 ~ 3월 (밤이 길어 오로라를 관측하기 가장 좋은 시기!)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "🌊 블루라군 온천욕\n\n🧖‍♀️ 머드 마스크 팩 체험", "tip": "💡 머리카락이 상할 수 있으니 린스를 듬뿍 바르기!"},
                {"day": "Day 2 📅", "activity": "🧊 웅장한 폭포 관광\n\n🌋 치솟는 간헐천 감상", "tip": "💡 바람이 매우 불어 모자와 장갑은 필수입니다!"},
                {"day": "Day 3 📅", "activity": "🌌 코코아 마시며\n\n✨ 오로라 헌팅 투어 가기", "tip": "💡 오로라 예보 수치를 매시간 체크해 보세요!"},
                {"day": "Day 4 📅", "activity": "🧊 요쿨살론 빙하 호수\n\n🚶 검은 모래 해변 걷기", "tip": "💡 SF 영화 속에 들어온 듯한 신비로운 풍경을 감상하세요."},
                {"day": "Day 5 📅", "activity": "🌋 화산 동굴 탐험\n\n🪵 따뜻한 통나무집 스파", "tip": "💡 몸에 쌓인 모든 피로를 노곤하게 풀어내기!"}
            ]
        },
        {
            "name": "프랑스 파리 🇫🇷",
            "concept": "미술관과 길거리 빵 냄새에 취하는 낭만 예술 여행",
            "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
            "season": "🌸 4월 ~ 6월 (거리에 예쁜 꽃이 활짝 피는 봄날의 파리!)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "🗼 에펠탑 앞 잔디밭 피크닉\n\n🥐 바게트 & 치즈 먹방", "tip": "💡 빵집에 줄 선 현지인들을 따라 구매해 보세요!"},
                {"day": "Day 2 📅", "activity": "🎨 루브르/오르세 미술관\n\n🚢 센강 야경 크루즈", "tip": "💡 유람선은 일몰 직전에 타는 것이 가장 예쁩니다!"},
                {"day": "Day 3 📅", "activity": "🛍️ 샹젤리제 거리 쇼핑\n\n🧁 달콤한 마카롱 클래스", "tip": "💡 '라두레'나 '피에르 에르메'에서 원조를 맛보세요!"},
                {"day": "Day 4 📅", "activity": "🏰 화려한 베르사유 궁전\n\n🍽️ 정통 달팽이 요리", "tip": "💡 자전거를 대여해 베르사유 정원을 돌아보는 것을 추천해요!"},
                {"day": "Day 5 📅", "activity": "🎨 몽마르뜨 언덕 산책\n\n☕ 감성 카페 브런치", "tip": "💡 사랑해 벽 앞에서 예쁜 커플샷이나 우정샷 남기기!"}
            ]
        }
    ],
    "SJ": [  # 관리자형 (ISTJ, ISFJ, ESTJ, ESFJ)
        {
            "name": "일본 교토 🇯🇵",
            "concept": "고즈넉한 역사 속 질서와 평화를 찾는 전통 여행",
            "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=800&q=80",
            "season": "🌸 3월 ~ 4월 (화사한 벚꽃 엔딩) 혹은 🍁 11월 (붉은 단풍 시즌)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "⛩️ 후시미 이나리 신사\n\n🦊 여우 석상 길 산책", "tip": "💡 사람이 안 붐비는 오전 8시 이전에 가야 한적해요!"},
                {"day": "Day 2 📅", "activity": "🎋 아라시야마 대나무숲\n\n🍱 정갈한 수제 두부 정식", "tip": "💡 자전거를 빌려서 숲 뒤쪽 마을까지 가보세요!"},
                {"day": "Day 3 📅", "activity": "👘 일본 기모노 체험\n\n🍵 수제 녹차 디저트 시식", "tip": "💡 사진 작가처럼 소품(우산 등)을 함께 렌탈해 보세요!"},
                {"day": "Day 4 📅", "activity": "🏯 금빛 찬란 금각사\n\n🍜 청수사 앞 따뜻한 우동", "tip": "💡 연못에 비친 반짝이는 금각사 배경은 최고의 포토존!"},
                {"day": "Day 5 📅", "activity": "🏮 기온거리 밤 산책\n\n🍢 골목 야키토리 맛보기", "tip": "💡 밤 조명이 들어온 정겨운 전통 가옥 골목을 느껴보세요."}
            ]
        },
        {
            "name": "싱가포르 🇸🇬",
            "concept": "치안 좋고 깔끔해 계획대로 딱 맞는 안전 여행",
            "image": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=800&q=80",
            "season": "☀️ 2월 ~ 10월 (비가 적게 내려 도심을 걷기 쾌적한 시기!)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "🌳 슈퍼트리 쇼 감상\n\n🦀 싱가포르 칠리크랩", "tip": "💡 슈퍼트리 밑에 누워서 하늘의 조명쇼를 보세요!"},
                {"day": "Day 2 📅", "activity": "🎢 유니버설 스튜디오\n\n🏖️ 센토사 해변 액티비티", "tip": "💡 줄 서는 시간을 아껴주는 익스프레스 패스 추천!"},
                {"day": "Day 3 📅", "activity": "🛍️ 오차드 로드 쇼핑\n\n✈️ 창이공항 대형 폭포 관람", "tip": "💡 공항 내 '쥬얼창이' 폭포는 탑승 수속 전 필수!"},
                {"day": "Day 4 📅", "activity": "🦁 머라이언 파크 인생샷\n\n🍲 정통 바쿠테(갈비탕) 먹방", "tip": "💡 머라이언 동상이 물을 뿜는 입모양에 맞춰 웃긴 샷 남기기!"},
                {"day": "Day 5 📅", "activity": "🚢 마리나베이 리버크루즈\n\n🍹 야경 좋은 루프탑 바", "tip": "💡 무알콜 칵테일을 마시며 화려한 도시 레이저 쇼를 감상해요!"}
            ]
        }
    ],
    "SP": [  # 탐험가형 (ISTP, ISFP, ESTP, ESFP)
        {
            "name": "뉴질랜드 퀸스타운 🇳🇿",
            "concept": "온몸으로 짜릿한 스릴을 즐기는 야외 액티비티 여행",
            "image": "https://images.unsplash.com/photo-1589871973318-9ca1258faa5d?auto=format&fit=crop&w=800&q=80",
            "season": "☀️ 12월 ~ 2월 (자연을 즐기기 가장 따뜻한 남반구의 여름!)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "🚠 곤돌라 타고 올라가기\n\n🏎️ 스피드 만점 루지 타기", "tip": "💡 한 번 타면 너무 재밌으니 무조건 3회권 이상 끊기!"},
                {"day": "Day 2 📅", "activity": "🚢 밀포드 사운드 피오르드\n\n🐬 빙하 크루즈 & 돌고래 찾기", "tip": "💡 비가 올 때 폭포들이 더 웅장해져서 또 다른 매력이 있어요!"},
                {"day": "Day 3 📅", "activity": "🍔 줄 서서 먹는 퍼그버거\n\n🌌 호숫가에서 별자리 보기", "tip": "💡 밤 10시 이후 야외로 나가면 쏟아지는 은하수를 감상!"},
                {"day": "Day 4 📅", "activity": "🚤 짜릿한 샷오버 제트보트\n\n🍷 푸른 자연 속 와이너리 투어", "tip": "💡 물 위를 360도 회전하는 스릴 넘치는 보트를 타보세요!"},
                {"day": "Day 5 📅", "activity": "🏔️ 반지의 제왕 촬영지 탐험\n\n🐑 평화로운 목장 양떼 구경", "tip": "💡 영화 속 장엄한 판타지 세계가 현실로 눈앞에 펼쳐집니다."}
            ]
        },
        {
            "name": "미국 라스베이거스 🇺🇸",
            "concept": "눈부신 도심 화려함의 극치와 신나는 축제 여행",
            "image": "https://images.unsplash.com/photo-1522083165195-342750297f05?auto=format&fit=crop&w=800&q=80",
            "season": "🌸 3월 ~ 5월 / 🍂 9월 ~ 11월 (한낮에도 걷기에 날씨가 딱 좋습니다!)",
            "itinerary": [
                {"day": "Day 1 📅", "activity": "🏨 스트립 호텔 무료 쇼 구경\n\n⛲ 벨라지오 대형 분수 쇼", "tip": "💡 분수 쇼는 30분 간격으로 무료로 진행돼요!"},
                {"day": "Day 2 📅", "activity": "🚁 웅장한 그랜드 캐년\n\n📸 헬리콥터 투어 & 촬영", "tip": "💡 대자연의 스케일을 하늘 위에서 내려다보는 신비한 경험!"},
                {"day": "Day 3 📅", "activity": "🎡 하이롤러 대관람차 탑승\n\n🎪 태양의 서커스(O쇼) 관람", "tip": "💡 세계 최고 퀄리티 서커스는 최소 몇 주 전 매진 필수 예매!"},
                {"day": "Day 4 📅", "activity": "🎡 아찔한 타워 위 놀이기구\n\n🥩 호텔 럭셔리 뷔페 먹방", "tip": "💡 고공 빌딩 끝자락에서 공중으로 돌며 아드레날린을 느껴봐요!"},
                {"day": "Day 5 📅", "activity": "🌵 레드락 캐년 미니 하이킹\n\n🛍️ 프리미엄 아울렛 털기", "tip": "💡 라스베이거스는 쇼핑의 성지! 알찬 득템을 노려보세요."}
            ]
        }
    ]
}

# 5. 사용자 입력 섹션 (이름, 나이, 여행일수, MBTI)
col_input1, col_input2, col_input3 = st.columns(3)

with col_input1:
    user_name = st.text_input("🏷️ 나의 예쁜 이름 입력하기:", value="당곡이")
with col_input2:
    user_age = st.slider("🎂 내 나이 설정하기:", min_value=1, max_value=100, value=17)
with col_input3:
    # 🌟 "몇박며칠" 기간 선택 란 추가! 🌟
    user_duration = st.selectbox(
        "📆 원하는 여행 일정을 골라보세요:",
        options=["2박 3일 🌅", "3박 4일 ✈️", "4박 5일 🌴"],
        index=1  # 기본값: 3박 4일
    )

user_mbti = st.selectbox(
    "🔮 나의 MBTI를 선택해 주세요:",
    options=["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
)

# 6. 세션 상태(Session State) 설정 (데이터 유지용)
if "options" not in st.session_state:
    st.session_state.options = None
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None
if "user_name" not in st.session_state:
    st.session_state.user_name = "당곡이"
if "user_age" not in st.session_state:
    st.session_state.user_age = 17
if "user_duration" not in st.session_state:
    st.session_state.user_duration = "3박 4일 ✈️"

# 7. 여행지 분석 작동 버튼 클릭 시
if st.button("🚀 나만의 맞춤형 추천 여행지 보기!"):
    st.session_state.user_name = user_name
    st.session_state.user_age = user_age
    st.session_state.selected_mbti = user_mbti
    st.session_state.user_duration = user_duration
    
    # MBTI 그룹 판별 (NT / NF / SJ / SP)
    mbti_group = ""
    if "N" in user_mbti and "T" in user_mbti:
        mbti_group = "NT"
    elif "N" in user_mbti and "F" in user_mbti:
        mbti_group = "NF"
    elif "S" in user_mbti and "J" in user_mbti:
        mbti_group = "SJ"
    else:
        mbti_group = "SP"
        
    st.session_state.options = travel_options[mbti_group]
    
    with st.spinner("🎨 열심히 팜플렛을 그리고 있습니다... 조금만 기다려주세요! 🎨"):
        time.sleep(1.2)
    st.success("✨ 맞춤 후보지가 준비되었습니다! 아래에서 최종 목적지를 선택해 보세요!")

# 8. 후보지 선택 및 대망의 팜플렛 출력!
if st.session_state.options is not None:
    st.write("---")
    st.markdown(f"### 💌 {st.session_state.user_name}님({st.session_state.selected_mbti})만을 위해 준비된 후보")
    
    opt_names = [opt["name"] for opt in st.session_state.options]
    user_choice = st.radio(
        "👇 아래 도시 중 팜플렛으로 인쇄하고 싶은 최종 목적지를 골라주세요!",
        options=opt_names
    )
    
    # 선택된 목적지 데이터 가져오기
    chosen_data = next(opt for opt in st.session_state.options if opt["name"] == user_choice)
    
    st.write("---")
    st.balloons() # 축하 풍선 날리기 🎈
    
    # [팜플렛 출력 영역] HTML/CSS 스타일 컨테이너 시작
    st.markdown("<div class='pamphlet-container'>", unsafe_allow_html=True)
    
    # 팜플렛 타이틀
    st.markdown(f"<h2 class='pamphlet-title'>🎒 {st.session_state.user_name}님의 인생 팜플렛</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #888;'>✨ {st.session_state.selected_mbti} & {st.session_state.user_duration} 추천: <b>{chosen_data['name']}</b>편 ✨</p>", unsafe_allow_html=True)
    
    # 여행지 대표 이미지 출력
    st.image(chosen_data["image"], use_container_width=True, caption=f"📸 낭만이 살아 넘치는 아름다운 {chosen_data['name']}")
    
    # 여행 기본 설명 및 방문 시기
    st.write(f"🌈 **컨셉:** *\"{chosen_data['concept']}\"*")
    st.write(f"📅 **추천 방문 시기:** {chosen_data['season']}")
    
    # 나이 맞춤형 꿀팁 문구
    age = st.session_state.user_age
    if age < 20:
        st.info(f"🍼 **{age}세의 어린 날개들을 위한 가이드:** 어른들의 잔소리를 벗어나 스스로 부딪쳐 보는 여행! 국제 학생증을 챙겨 각종 티켓 할인을 꼭 받으세요! 💰")
    elif age < 30:
        st.info(f"🏃‍♀️ **{age}세의 튼튼한 다리를 지닌 청춘을 위한 가이드:** 두 발로 세상 곳곳을 정복해 보세요! 대중교통 자유이용권을 적극 추천합니다! 🗺️")
    else:
        st.info(f"☕ **{age}세의 힐링 탐색가를 위한 가이드:** 한두 개만 알차게 보는 여유로운 일정이 필요해요. 아름다운 노천카페에서 멍하니 커피를 즐기며 충전하세요. 💆")
    
    st.markdown("<h4 style='color: #FF7096; margin-top:20px;'>🗺️ 폴더블 일일 플랜북 </h4>", unsafe_allow_html=True)
    
    # 🌟 [선택 일수에 맞춘 파이썬 리스트 슬라이싱 기술 적용!] 🌟
    # 2박 3일 -> 3일치, 3박 4일 -> 4일치, 4박 5일 -> 5일치 데이터를 슬라이싱하여 추출합니다.
    if "2박" in st.session_state.user_duration:
        slice_days = 3
    elif "3박" in st.session_state.user_duration:
        slice_days = 4
    else:
        slice_days = 5
        
    # 사용자가 선택한 일수만큼 일정 리스트를 잘라냅니다! (정보 교과 탐구 포인트!)
    selected_itinerary = chosen_data['itinerary'][:slice_days]
    
    # 잘라낸 일수만큼 가로 단(Columns)을 동적으로 생성합니다.
    p_cols = st.columns(slice_days)
    
    # 동적 팜플렛 배치!
    for i, col in enumerate(p_cols):
        with col:
            st.markdown(f"""
            <div class="day-card">
                <div class="day-title">{selected_itinerary[i]['day']}</div>
                <p style='font-size: 13px; line-height: 1.4;'>{selected_itinerary[i]['activity'].replace('\n\n', '<br><b>⬇️</b><br>')}</p>
                <p style='font-size: 11px; color: #555; background-color:#FFF5F5; padding:5px; border-radius:5px;'>{selected_itinerary[i]['tip']}</p>
            </div>
            """, unsafe_allow_html=True)
        
    # [팜플렛 출력 영역] HTML/CSS 스타일 컨테이너 종료
    st.markdown("</div>", unsafe_allow_html=True)

# 9. 하단 가이드
st.write("---")
st.caption("🎈 당곡고등학교 정보 수업 실습을 위해 디자인된 AI 도우미 프로그램입니다. 친구들과 함께 멋지게 커스터마이징해 보세요!")
