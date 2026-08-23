import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# 기본 설정
# =========================================================
st.set_page_config(
    page_title="고분자를 만들면서 동시에 분해할 수 있을까?",
    page_icon="🧪",
    layout="wide"
)

# =========================================================
# 디자인
# =========================================================
st.markdown("""
<style>
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

.hero {
    padding: 3.5rem 3rem;
    border-radius: 25px;
    background: linear-gradient(135deg, #eef5ff, #f7f4ff);
    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 3.2rem;
    line-height: 1.15;
}

.hero p {
    font-size: 1.15rem;
    color: #475569;
}

.section {
    padding-top: 2.5rem;
    margin-top: 2rem;
    border-top: 1px solid #e5e7eb;
}

.kicker {
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #64748b;
}

.callout {
    padding: 1.2rem;
    background: #f8fafc;
    border-left: 5px solid #64748b;
    border-radius: 10px;
    margin: 1rem 0;
}

.flow {
    text-align: center;
    padding: 1.5rem;
    background: #f8fafc;
    border-radius: 15px;
    font-size: 1.1rem;
    line-height: 2;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 데이터
# =========================================================

# 논문에 보고된 apparent propagation rate constant
kinetics = pd.DataFrame({
    "Monomer": ["NPMA", "BPMA", "PYMA", "TPMA"],
    "kp_app": [0.393, 0.188, 0.117, 0.050]
})

# 논문 본문에 제시된 NPMA conversion
conversion = pd.DataFrame({
    "Time": [5, 30],
    "Conversion": [83, 95]
})

# Stage III scission ratio
scission = pd.DataFrame({
    "Polymer": ["PNPMA", "PPYMA"],
    "ps/ms": [1.25, 4.57]
})


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="kicker">
CHEMISTRY · SCIENCE NEWS · 2026
</div>

<h1>
고분자를 만들면서<br>
동시에 분해할 수 있을까?
</h1>

<p>
<b>ATRP × Mechanochemistry</b><br>
분자 구조와 기계적 힘은 고분자의 생성과 분해를 어떻게 결정하는가?
</p>

</div>
""", unsafe_allow_html=True)


st.info(
    "이 웹페이지는 2026년 Nature Communications에 게재된 "
    "기계화학적 ATRP 연구를 고등학생 독자가 이해할 수 있도록 "
    "화학 개념과 실제 연구 데이터를 시각적으로 재구성한 콘텐츠입니다."
)


# =========================================================
# 01 연구 소개
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">01 · RESEARCH</div>
<h2>연구를 만나다</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
고분자는 작은 분자인 단량체가 반복적으로 연결되면서 만들어진다.
그렇다면 만들어진 고분자를 필요할 때 다시 작은 분자로 되돌릴 수 있을까?

연세대학교 연구진은 기계화학(mechanochemistry)과
원자 이동 라디칼 중합(ATRP)을 결합하여
메타크릴레이트 계열 고분자의 합성, 기계적 분해 및
해중합을 하나의 연구 흐름에서 조사했다.
""")

st.markdown("""
<div class="callout">

<b>핵심 질문</b>

<br><br>

분자 구조와 기계적 힘은
고분자의 생성과 분해 경로에 어떤 영향을 줄까?

</div>
""", unsafe_allow_html=True)


# =========================================================
# 02 고분자
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">02 · POLYMER</div>
<h2>고분자는 어떻게 만들어질까?</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
단량체(monomer)가 반복적으로 연결되는 중합(polymerization)을 통해
긴 고분자 사슬이 만들어진다.

이번 연구에서는 방향족 치환기의 구조가 다른
메타크릴레이트 단량체를 비교하였다.
""")

monomers = pd.DataFrame({
    "약어": ["NPMA", "BPMA", "PYMA", "TPMA"],
    "단량체": [
        "2-naphthyl methacrylate",
        "4-biphenyl methacrylate",
        "1-pyrene methacrylate",
        "4-tritylphenyl methacrylate"
    ]
})

st.dataframe(
    monomers,
    hide_index=True,
    use_container_width=True
)

st.markdown("""
<div class="flow">

<b>단량체</b>
&nbsp;&nbsp;→&nbsp;&nbsp;
중합
&nbsp;&nbsp;→&nbsp;&nbsp;
<b>고분자 사슬</b>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 03 ATRP
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">03 · ATRP</div>
<h2>고분자의 성장을 조절하는 ATRP</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
ATRP(Atom Transfer Radical Polymerization)는
전이금속 촉매를 이용해 고분자 사슬 말단의 라디칼 상태를
활성화와 비활성화 사이에서 조절하는 정밀 라디칼 중합법이다.
""")

col1, col2 = st.columns(2)

with col1:

    st.subheader("일반적인 라디칼 중합")

    st.markdown("""
    ### 라디칼 생성
    ↓
    ### 사슬 성장
    ↓
    ### 종결
    """)

with col2:

    st.subheader("ATRP")

    st.markdown("""
    ### 비활성
    ↓
    ### 활성화
    ↓
    ### 단량체 첨가
    ↓
    ### 비활성화
    """)

st.markdown("""
<div class="callout">

<b>이번 연구의 ATRP 반응계</b><br><br>

개시제: ethyl 2-bromoisobutyrate<br>
촉매: CuBr<br>
리간드: PMDETA

</div>
""", unsafe_allow_html=True)


# =========================================================
# 04 기계화학
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">04 · MECHANOCHEMISTRY</div>
<h2>용매 대신 기계적 힘을 이용하다</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
기계화학은 기계적 에너지를 이용하여 화학반응을 유도하거나
변화시키는 분야이다.

연구진은 진동식 볼밀(ball mill)을 이용하여
반응물에 기계적 에너지를 전달하였다.
""")

st.markdown("""
<div class="flow">

반응물 + ATRP 반응계

<br>

↓

<br>

⚙️ <b>볼밀링</b>

<br>

↓

<br>

충돌·마찰에 의한 기계적 에너지

<br>

↓

<br>

<b>고분자 합성</b>

</div>
""", unsafe_allow_html=True)

st.caption(
    "연구에서는 MM400 진동식 볼밀을 사용하고 아르곤 분위기에서 반응을 진행하였다."
)


# =========================================================
# 05 중합속도 데이터
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">05 · DATA</div>
<h2>분자 구조가 중합 속도를 바꿀까?</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
연구진은 서로 다른 방향족 치환기를 가진 네 단량체의
겉보기 중합 속도 상수 kp_app를 비교하였다.
""")

fig = px.bar(
    kinetics,
    x="Monomer",
    y="kp_app",
    text="kp_app",
    labels={
        "Monomer": "단량체",
        "kp_app": "kp_app (min⁻¹)"
    },
    title="단량체별 겉보기 중합 속도 상수"
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig.update_layout(
    showlegend=False,
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("""
<div class="callout">

<b>연구 결과</b><br><br>

NPMA: 0.393 min⁻¹<br>
BPMA: 0.188 min⁻¹<br>
PYMA: 0.117 min⁻¹<br>
TPMA: 0.050 min⁻¹

<br><br>

단량체의 구조에 따라 중합 속도에 차이가 나타났다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 06 왜 다른가
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">06 · INTERPRETATION</div>
<h2>왜 중합 속도가 달라질까?</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
치환기의 크기와 구조는 반응 부위 주변의 입체적 환경과
분자 사이의 상호작용 등에 영향을 줄 수 있다.

따라서 같은 메타크릴레이트 골격을 가진 단량체라도
기계화학적 ATRP에서 동일한 반응성을 나타낸다고 볼 수 없다.
""")

st.markdown("""
<div class="flow">

<b>치환기 구조</b>

↓

반응 부위의 환경 및 분자 간 상호작용

↓

<b>반응성 차이</b>

↓

<b>중합 속도 차이</b>

</div>
""", unsafe_allow_html=True)

st.warning(
    "주의: '치환기가 클수록 무조건 중합 속도가 느려진다'고 단순화하면 안 된다. "
    "각 치환기의 구조적 특성을 함께 고려해야 한다."
)


# =========================================================
# 07 합성과 분해
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">07 · LIFECYCLE</div>
<h2>고분자는 만들어진 뒤 어떻게 될까?</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
볼밀링이 계속되면서 고분자의 생성뿐 아니라
기계적 분해도 중요해진다.

연구에서는 중합과 분해가 시간에 따라 경쟁하는
세 단계의 거동을 제시하였다.
""")

st.markdown("""
<div class="flow">

<b>Stage I</b>
중합 우세

↓

<b>Stage II</b>
중합과 분해 경쟁

↓

<b>Stage III</b>
분해 우세

</div>
""", unsafe_allow_html=True)


# =========================================================
# 08 전환율
# =========================================================

st.subheader("NPMA 중합의 전환율")

conversion_fig = px.line(
    conversion,
    x="Time",
    y="Conversion",
    markers=True,
    text="Conversion",
    labels={
        "Time": "볼밀링 시간 (min)",
        "Conversion": "전환율 (%)"
    }
)

conversion_fig.update_traces(
    textposition="top center"
)

conversion_fig.update_layout(
    height=400
)

st.plotly_chart(
    conversion_fig,
    use_container_width=True
)

st.caption(
    "논문 본문에 제시된 대표값: 5분 83%, 30분 95%."
)


# =========================================================
# 09 절단 위치
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">09 · SCISSION</div>
<h2>고분자의 어디가 끊어질까?</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
연구진은 기계적 분해 과정에서
주사슬(main chain) 절단과
pendant group(곁가지) 절단을 구분하여 분석하였다.

Stage III에서는 두 절단 경로의 상대적인 정도를
ps/ms 값으로 비교하였다.
""")

scission_fig = px.bar(
    scission,
    x="Polymer",
    y="ps/ms",
    text="ps/ms",
    labels={
        "Polymer": "고분자",
        "ps/ms": "pendant-group scission / main-chain scission"
    },
    title="Stage III의 절단 경로 비교"
)

scission_fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

scission_fig.update_layout(
    showlegend=False,
    height=400
)

st.plotly_chart(
    scission_fig,
    use_container_width=True
)

st.markdown("""
<div class="callout">

PNPMA → ps/ms = <b>1.25</b><br>
PPYMA → ps/ms = <b>4.57</b>

<br><br>

PPYMA에서는 pendant-group 절단이
main-chain 절단에 비해 상대적으로 더 두드러졌다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 10 CoGEF
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">10 · COMPUTATIONAL CHEMISTRY</div>
<h2>계산화학으로 힘의 전달을 들여다보다</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
연구진은 CoGEF
(constrained geometries simulate external force)
계산을 이용하여 외부 힘이 고분자 구조에 작용할 때
결합이 어떻게 반응하는지 분석하였다.
""")

force_data = pd.DataFrame({
    "항목": [
        "System-wide median Favg,max",
        "Main-chain elongation median Fmax"
    ],
    "PNPMA (nN)": [4.22, 5.92],
    "PPYMA (nN)": [4.06, 5.91]
})

st.dataframe(
    force_data,
    hide_index=True,
    use_container_width=True
)

st.markdown("""
<div class="callout">

PNPMA와 PPYMA의 주사슬을 늘리는 계산에서
median Fmax가 각각 <b>5.92 nN</b>과 <b>5.91 nN</b>으로
거의 같았다.

<br><br>

따라서 두 고분자의 분해 경로 차이를
단순히 '주사슬 자체가 더 약하기 때문'이라고만
설명하기는 어렵다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 11 해중합
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">11 · DEPOLYMERIZATION</div>
<h2>고분자를 다시 단량체로?</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
연구진은 PNPMA를 대상으로 기계적 분해와 해중합을 조사하였다.

5분간 볼밀링하여 합성한 PNPMA의
GPC 기준 수평균분자량 Mn,GPC는 21.5 kDa,
분산도 Đ는 1.25였다.

기계적 분해가 진행된 뒤에는
NPMA가 생성물로 확인되었다.
""")

st.markdown("""
<div class="flow">

<b>NPMA</b>

↓

ATRP + 볼밀링

↓

<b>PNPMA</b>

↓

기계적 분해 · 해중합

↓

<b>NPMA</b>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.metric("Mn,GPC", "21.5 kDa")

with col2:
    st.metric("Đ", "1.25")


# =========================================================
# 12 최종
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">12 · TAKEAWAY</div>
<h2>고분자의 '생애'를 설계한다</h2>
</div>
""", unsafe_allow_html=True)

st.write("""
이 연구의 의미는 단순히 용매 없이 고분자를 만들었다는 데 있지 않다.

정밀 중합법인 ATRP와 기계화학을 결합하고,
분자 구조에 따른 중합 속도와 기계적 분해 경로를 분석함으로써
고분자의 합성부터 분해와 해중합까지를 하나의
'분자 생애' 관점에서 살펴볼 수 있다는 점에 의미가 있다.
""")

st.markdown("""
<div class="flow">

<b>단량체</b>

↓

<b>정밀 중합</b>

↓

<b>고분자</b>

↓

<b>기계적 힘</b>

↓

<b>분해</b>

↓

<b>해중합</b>

↓

<b>단량체</b>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 출처
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">SOURCES</div>
<h2>출처 및 참고문헌</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 핵심 논문

Kwon, G., Yim, D., Cha, S. et al.  
**Mechanochemical atom transfer radical polymerization unlocks functional
methacrylate lifecycles of controlled synthesis, force-activated degradation,
and depolymerization.**  
*Nature Communications* (2026).  
DOI: **10.1038/s41467-026-72346-3**

### 연구 소개 기사

연세대학교 연구팀 연구 소개 기사, 2026.

---

### 웹페이지 제작 목적

전문적인 고분자 합성 연구의 핵심 개념과 실제 연구 데이터를
텍스트뿐 아니라 그래프, 표, 과정 모식도 등의 시각적 매체로
재구성하여 고등학생 독자가 연구의 흐름과 화학적 의미를
단계적으로 이해할 수 있도록 구성하였다.
""")

st.caption("Science communication project · Chemistry")
