import streamlit as st
import pandas as pd

# =========================================================
# 페이지 설정
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
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

.hero {
    padding: 4rem 3rem;
    border-radius: 28px;
    background: linear-gradient(135deg, #eef5ff, #f7f4ff);
    margin-bottom: 2rem;
}

.hero h1 {
    font-size: 3.3rem;
    line-height: 1.15;
    margin-bottom: 1rem;
    white-space: nowrap;
}

.hero p {
    font-size: 1.12rem;
    color: #475569;
    line-height: 1.8;
}

.kicker {
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.13em;
    color: #64748b;
}

.section {
    padding-top: 3rem;
    margin-top: 2.5rem;
    border-top: 1px solid #e5e7eb;
}

.callout {
    padding: 1.4rem;
    background: #f8fafc;
    border-left: 5px solid #64748b;
    border-radius: 12px;
    margin: 1.2rem 0;
    line-height: 1.85;
}

.question {
    padding: 1.8rem;
    background: #f1f5f9;
    border-radius: 18px;
    margin: 1.5rem 0;
    text-align: center;
}

.question h3 {
    margin-bottom: 0.5rem;
}

.flow {
    text-align: center;
    padding: 1.6rem;
    background: #f8fafc;
    border-radius: 16px;
    font-size: 1.08rem;
    line-height: 2.3;
    margin: 1.2rem 0;
}

.card {
    padding: 1.5rem;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    min-height: 170px;
}

.big-number {
    font-size: 2.5rem;
    font-weight: 800;
}

.source {
    font-size: 0.86rem;
    color: #64748b;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 데이터
# =========================================================

kinetics = pd.DataFrame({
    "단량체": ["NPMA", "BPMA", "PYMA", "TPMA"],
    "kp_app (min⁻¹)": [0.393, 0.188, 0.117, 0.050]
})

conversion = pd.DataFrame({
    "볼밀링 시간 (min)": [5, 30],
    "전환율 (%)": [83, 95]
})

scission = pd.DataFrame({
    "고분자": ["PNPMA", "PPYMA"],
    "ps/ms": [1.25, 4.57]
})

force_data = pd.DataFrame({
    "계산 항목": [
        "System-wide median Favg,max",
        "Main-chain elongation median Fmax"
    ],
    "PNPMA (nN)": [4.22, 5.92],
    "PPYMA (nN)": [4.06, 5.91]
})


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="kicker">
CHEMISTRY · SCIENCE WEB
</div>

<h1>고분자를 만들면서 동시에 분해할 수 있을까?</h1>

<p>
<b>ATRP × Mechanochemistry</b><br>
분자 구조와 기계적 힘은 고분자의 합성과 분해 경로를 어떻게 결정하는가?
</p>

</div>
""", unsafe_allow_html=True)

st.info(
    "기사에서 접한 최신 고분자 합성 연구를 출발점으로, "
    "논문의 핵심 개념과 연구 데이터를 선별하고 다양한 시각적 매체를 활용해 "
    "하나의 과학 웹사이트로 재구성했습니다."
)


# =========================================================
# 00 콘텐츠 제작 의도
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">00 · ABOUT THIS WEB</div>

<h2>이 웹사이트는 어떻게 만들어졌을까?</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
이 콘텐츠는 전문적인 화학 연구를 단순하게 요약하는 데서 그치지 않고,
연구의 핵심 질문과 실험 결과, 화학적 원리를 독자가 하나의 흐름으로
이해할 수 있도록 시각적 매체로 재구성한 과학 웹사이트이다.

먼저 과학 기사에서 소개된 '기계적 힘으로 고분자를 합성하고,
동시에 분해와 해중합까지 관찰한다'는 연구 내용에 관심을 갖고
원 연구 논문으로 내용을 확장하였다.

이후 논문에서 제시된 ATRP, 기계화학, 단량체 구조에 따른 반응성,
고분자 사슬의 절단, 계산화학적 분석 등의 내용을 선별하고,
이를 텍스트·표·막대그래프·선그래프·수치 강조·과정 모식도 등의
매체로 나누어 배치하였다.

주요 독자는 고등학생으로 설정하되, 전문적인 연구 내용을 지나치게
단순화하지 않고 핵심 화학 용어와 실제 연구 데이터를 함께 제시하는
방식으로 구성하였다.
""")

st.markdown("""
<div class="question">

<h3>콘텐츠의 핵심 목표</h3>

전문적인 고분자 합성 연구를

<br>

<b>읽고 → 선별하고 → 구조화하고 → 시각화하여</b>

<br>

고등학생 독자가 연구의 흐름과 화학적 의미를
스스로 따라갈 수 있는 과학 웹사이트로 재구성한다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 01 연구 시작
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">01 · RESEARCH START</div>

<h2>연구 시작</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
이 연구의 출발점은 '고분자를 어떻게 더 정밀하게 만들 것인가'라는
질문에서 한 단계 더 나아간다.

기존의 고분자 합성에서는 단량체를 연결하여 원하는 고분자를 만드는
과정이 중요하다. 그러나 합성된 고분자가 사용된 이후에는 다시
분해하거나 재활용하는 과정 역시 중요하다.

2026년 Nature Communications에 발표된 연구에서는
기계화학(mechanochemistry)과 원자 이동 라디칼 중합(ATRP)을 결합하여
고분자의 합성뿐 아니라 기계적 분해와 해중합까지 하나의 연구 흐름에서
살펴보았다.

특히 연구진은 방향족 곁가지의 크기가 서로 다른 네 가지
메타크릴레이트 단량체를 설계하여, 분자 구조의 차이가
중합 속도와 이후의 분해 경로에 어떤 차이를 만드는지 비교하였다.
""")

st.markdown("""
<div class="callout">

<b>기사에서 발견한 연구를 논문으로 확장하기</b><br><br>

과학 기사에서 접한 흥미로운 연구 내용을 단순히 전달하는 대신,
원 논문에서 연구 목적·실험 조건·측정 방법·수치 데이터를 확인하고
그중 독자에게 의미 있는 정보를 선별하여 웹 콘텐츠로 재구성하였다.

</div>
""", unsafe_allow_html=True)

st.caption(
    "연구의 실제 논문은 Kwon et al., Nature Communications, 2026에 게재되었다."
)


# =========================================================
# 02 연구 질문
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">02 · RESEARCH QUESTION</div>

<h2>연구자가 던진 질문</h2>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="question">

<h3>고분자를 만드는 과정에서<br>
동시에 분해가 일어난다면 어떻게 될까?</h3>

</div>
""", unsafe_allow_html=True)

st.write("""
일반적으로 중합은 단량체가 연결되어 고분자 사슬을 형성하는 과정으로,
분해는 이미 만들어진 고분자가 끊어지는 과정으로 생각하기 쉽다.

그러나 기계화학적 ATRP에서는 기계적 에너지가 반응계에 지속적으로
전달되기 때문에 고분자 사슬의 성장과 절단이 동시에 일어날 수 있다.

따라서 연구진은 단순히 '고분자가 만들어지는가'를 확인하는 것을 넘어,
중합 속도와 분해 속도의 경쟁, 분해가 일어나는 위치,
그리고 최종적으로 단량체가 다시 생성되는 해중합까지 조사하였다.
""")


# =========================================================
# 03 고분자
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">03 · POLYMER</div>

<h2>먼저, 고분자는 어떻게 만들어지는가?</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
고분자(polymer)는 작은 분자인 단량체(monomer)가 반복적으로 연결되어
형성되는 거대한 분자이다.

이번 연구에서는 메타크릴레이트 골격은 유지하면서 그 주변에 붙어 있는
방향족 곁가지의 크기를 달리한 네 종류의 단량체를 비교했다.
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
<br>
↓
<br>
중합
<br>
↓
<br>
<b>고분자 사슬</b>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 04 ATRP
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">04 · ATRP</div>

<h2>고분자의 성장을 조절하는 ATRP</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
ATRP는 Atom Transfer Radical Polymerization의 약자로,
전이금속 촉매를 이용하여 라디칼의 생성과 소멸을 조절하면서
고분자 사슬의 성장을 제어하는 정밀 라디칼 중합법이다.

이번 연구에서는 기계화학적 조건에서 ATRP를 구현하기 위해
개시제, 구리 촉매와 리간드를 이용하였다.
""")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">

    <h3>일반적인 라디칼 중합</h3>

    라디칼 생성<br>
    ↓<br>
    사슬 성장<br>
    ↓<br>
    종결

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">

    <h3>ATRP</h3>

    비활성 상태<br>
    ↓<br>
    활성화<br>
    ↓<br>
    단량체 첨가<br>
    ↓<br>
    비활성화

    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="callout">

<b>논문에서 사용한 주요 반응계</b><br><br>

개시제: ethyl 2-bromoisobutyrate<br>
촉매: CuBr<br>
리간드: PMDETA

</div>
""", unsafe_allow_html=True)


# =========================================================
# 05 기계화학
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">05 · MECHANOCHEMISTRY</div>

<h2>용액이 아니라 기계적 힘으로 반응을 일으킨다면?</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
기계화학은 열이나 빛과 같은 전통적인 에너지 공급 방식과 달리
기계적 에너지를 이용하여 화학적 변화를 유도하는 분야이다.

이 연구에서는 진동식 볼밀(ball mill)을 이용하여 반응물에
반복적인 충돌과 기계적 에너지를 전달했다.

즉, 이 연구에서 '볼밀'은 단순히 물질을 갈아주는 장치가 아니라
고체 상태 반응에 필요한 기계적 에너지를 공급하는 반응 도구로 사용된다.
""")

st.markdown("""
<div class="flow">

반응물 + ATRP 반응계

<br>
↓

⚙️ <b>진동식 볼밀</b>

<br>
↓

충돌 · 마찰 · 기계적 에너지 전달

<br>
↓

<b>고체 상태 중합</b>

</div>
""", unsafe_allow_html=True)

st.caption(
    "논문에서는 MM400 진동식 볼밀, 스테인리스강 용기와 두 개의 스테인리스강 볼을 사용했다."
)


# =========================================================
# 06 분자 구조
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">06 · MOLECULAR STRUCTURE</div>

<h2>곁가지의 크기가 달라지면 반응성도 달라질까?</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
연구진은 방향족 곁가지의 크기가 서로 다른 네 가지 단량체를 이용해
분자 구조와 기계화학적 중합 반응성 사이의 관계를 비교하였다.

이는 단순히 '어떤 단량체가 더 빨리 반응하는가'를 확인하는 것이 아니라,
분자 수준의 구조적 차이가 실제 고분자 합성 과정에 어떤 영향을 주는지를
살펴보기 위한 비교이다.
""")

st.markdown("""
<div class="flow">

<b>곁가지의 구조와 크기</b>

↓

반응 부위의 접근성 및 입체적 환경

↓

<b>단량체의 반응성 차이</b>

↓

<b>중합 속도 차이</b>

</div>
""")


# =========================================================
# 07 데이터
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">07 · DATA VISUALIZATION</div>

<h2>실제 연구 데이터를 그래프로 읽어보기</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
다음 그래프는 논문에서 제시된 네 단량체의 겉보기 중합 속도 상수
kp_app를 비교한 것이다.

표만 제시하는 대신 막대그래프로 변환하여 단량체 사이의 차이를
한눈에 비교할 수 있도록 구성하였다.
""")

st.bar_chart(
    kinetics.set_index("단량체"),
    y="kp_app (min⁻¹)",
    height=400
)

st.dataframe(
    kinetics,
    hide_index=True,
    use_container_width=True
)

st.markdown("""
<div class="callout">

<b>데이터에서 확인할 수 있는 경향</b><br><br>

NPMA → 0.393 min⁻¹<br>
BPMA → 0.188 min⁻¹<br>
PYMA → 0.117 min⁻¹<br>
TPMA → 0.050 min⁻¹

<br><br>

방향족 곁가지의 구조가 달라짐에 따라
기계화학적 ATRP에서 나타나는 중합 속도에도 차이가 나타났다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 08 합성과 분해의 경쟁
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">08 · COMPETING PROCESSES</div>

<h2>고분자의 생성과 분해는 동시에 일어날 수 있다</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
이 연구에서 중요한 점은 중합과 분해를 완전히 독립적인 과정으로
보지 않는다는 것이다.

볼밀링이 계속되는 동안 단량체가 연결되어 고분자 사슬이 성장하는
동시에, 기계적 힘에 의해 이미 형성된 고분자 사슬이 절단될 수도 있다.

따라서 반응 시간이 길어진다고 해서 고분자가 단순히 계속 증가한다고
볼 수 없으며, 중합과 분해의 상대적인 속도를 함께 고려해야 한다.
""")

st.markdown("""
<div class="flow">

<b>Stage I</b>
<br>
중합 우세

↓

<b>Stage II</b>
<br>
중합과 분해 경쟁

↓

<b>Stage III</b>
<br>
분해 우세

</div>
""", unsafe_allow_html=True)


# =========================================================
# 09 전환율
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">09 · EXPERIMENTAL DATA</div>

<h2>실제로 얼마나 중합되었을까?</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
대표적인 단량체인 NPMA의 중합 과정을 ¹H NMR로 추적한 결과,
볼밀링 5분 후 전환율은 83%, 30분 후에는 95%에 도달했다.

이 데이터를 선그래프로 재구성하여 시간에 따른 전환율 변화를
시각적으로 나타냈다.
""")

st.line_chart(
    conversion.set_index("볼밀링 시간 (min)"),
    y="전환율 (%)",
    height=350
)

st.dataframe(
    conversion,
    hide_index=True,
    use_container_width=True
)

st.caption(
    "전환율은 논문에서 ¹H NMR 피크 적분을 비교하여 산출하였다."
)


# =========================================================
# 10 고분자의 어디가 끊어지는가
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">10 · DEGRADATION</div>

<h2>고분자의 어디가 끊어질까?</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
기계적 힘이 고분자에 작용한다고 해서 모든 결합이 동일한 방식으로
끊어지는 것은 아니다.

연구진은 MALDI-ToF 질량분석과 계산화학적 분석 등을 이용하여
주사슬(main chain), 곁가지(pendant group), 말단(end group)에서
나타나는 절단을 구분하여 분석하였다.

특히 곁가지의 크기가 달라지면서 기계적 분해 경로에도 차이가
나타나는지를 확인하였다.
""")

st.bar_chart(
    scission.set_index("고분자"),
    y="ps/ms",
    height=350
)

st.dataframe(
    scission,
    hide_index=True,
    use_container_width=True
)

st.markdown("""
<div class="callout">

<b>Stage III의 ps/ms</b><br><br>

PNPMA → 1.25<br>
PPYMA → 4.57

<br><br>

ps/ms는 pendant-group scission과 main-chain scission의
상대적인 비율을 나타내는 값이다.

PPYMA에서 이 값이 더 크게 나타나
곁가지 절단의 상대적 비중이 더 높았음을 보여준다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 11 계산화학
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">11 · COMPUTATIONAL CHEMISTRY</div>

<h2>실험만으로 설명하기 어려운 부분을 계산으로 확인하다</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
연구진은 실험 결과를 분자 수준에서 해석하기 위해
CoGEF(constrained geometries simulate external force) 계산을 활용하였다.

이 계산은 외부에서 힘이 가해지는 상황을 모델링하여
분자 구조가 늘어나면서 어느 부분에서 힘이 집중되는지
분석하는 데 사용되었다.

즉, 실험에서 관찰된 '어디가 끊어지는가'라는 현상을
분자 수준의 힘의 전달과 연결해 해석한 것이다.
""")

st.dataframe(
    force_data,
    hide_index=True,
    use_container_width=True
)

st.markdown("""
<div class="callout">

PNPMA의 main-chain elongation median Fmax → <b>5.92 nN</b><br>
PPYMA의 main-chain elongation median Fmax → <b>5.91 nN</b>

<br><br>

두 값이 거의 비슷하다는 결과는
두 고분자의 분해 경로 차이를 단순한
'주사슬 자체의 강도 차이'만으로 설명하기 어렵다는 점을 보여준다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 12 해중합
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">12 · DEPOLYMERIZATION</div>

<h2>분해의 끝에는 다시 단량체가 나타난다</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
연구에서는 단순히 고분자의 분자량이 감소하는 현상뿐 아니라
분해 과정에서 원래의 단량체가 생성되는 해중합(depolymerization)도
관찰하였다.

대표적으로 PNPMA를 대상으로 한 분석에서
기계적 분해와 함께 NPMA가 생성되는 현상이 확인되었다.

따라서 연구에서 관찰되는 과정은 단순한 '고분자 파괴'보다
고분자의 합성에서 분해, 그리고 단량체 생성까지 이어지는
하나의 순환적 과정으로 이해할 수 있다.
""")

st.markdown("""
<div class="flow">

<b>NPMA</b>

↓

ATRP + 볼밀링

↓

<b>PNPMA</b>

↓

기계적 분해

↓

<b>해중합</b>

↓

<b>NPMA 생성</b>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.metric("Mn,GPC", "21.5 kDa")

with col2:
    st.metric("Đ", "1.25")


# =========================================================
# 13 연구의 의미
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">13 · SIGNIFICANCE</div>

<h2>이 연구가 보여주는 것</h2>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">

    <h3>① 합성</h3>

    기계화학적 조건에서
    ATRP를 이용해 고분자를 합성한다.

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">

    <h3>② 분해</h3>

    기계적 힘이 고분자 사슬에 작용하면서
    서로 다른 위치에서 절단이 일어난다.

    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">

    <h3>③ 해중합</h3>

    분해 과정에서 단량체가 생성되는
    해중합까지 관찰된다.

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 14 최종 메시지
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">14 · TAKEAWAY</div>

<h2>고분자의 '생애'를 하나의 흐름으로 바라보다</h2>

</div>
""", unsafe_allow_html=True)

st.write("""
이 연구의 핵심은 단순히 '볼밀로 고분자를 만들었다'는 것이 아니다.

정밀 중합법인 ATRP와 기계화학을 결합하여 고분자를 합성하고,
동시에 일어나는 기계적 분해를 분자 구조와 연결해 분석하며,
최종적으로 단량체가 다시 생성되는 해중합까지 관찰했다는 데 의미가 있다.

특히 네 종류의 방향족 메타크릴레이트를 비교함으로써
곁가지의 구조가 중합 반응성과 분해 경로에 영향을 줄 수 있음을
실험과 계산을 통해 살펴보았다.

따라서 고분자를 '한번 만들어지면 끝나는 물질'이 아니라
합성 → 구조 변화 → 분해 → 해중합으로 이어지는
하나의 화학적 생애주기로 바라볼 수 있다.
""")

st.markdown("""
<div class="flow">

<b>단량체</b>

↓

<b>ATRP 중합</b>

↓

<b>고분자 형성</b>

↓

<b>기계적 힘</b>

↓

<b>고분자 분해</b>

↓

<b>해중합</b>

↓

<b>단량체 생성</b>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 15 콘텐츠 제작 방식
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">15 · MEDIA DESIGN</div>

<h2>전문적인 연구를 어떻게 웹 콘텐츠로 바꾸었는가?</h2>

</div>
""", unsafe_allow_html=True)

media = pd.DataFrame({
    "연구 정보": [
        "연구 질문과 배경",
        "단량체 종류",
        "중합 속도 데이터",
        "시간에 따른 전환율",
        "분해 경로 데이터",
        "계산화학 결과",
        "합성 → 분해 → 해중합 과정"
    ],
    "사용한 매체": [
        "텍스트 + 강조 박스",
        "표",
        "막대그래프 + 표",
        "선그래프 + 표",
        "막대그래프 + 수치 강조",
        "비교 표 + 설명",
        "과정 모식도"
    ],
    "전달 목적": [
        "연구의 맥락 이해",
        "분자 구조 비교",
        "수치 차이의 직관적 비교",
        "시간에 따른 변화 파악",
        "분해 경로 비교",
        "실험과 계산의 연결",
        "전체 연구 흐름 파악"
    ]
})

st.dataframe(
    media,
    hide_index=True,
    use_container_width=True
)

st.write("""
이처럼 동일한 정보를 하나의 표현 방식으로 반복하지 않고,
정보의 성격에 따라 가장 적합한 매체를 선택하였다.

수치 비교에는 그래프와 표를 사용하고,
복잡한 반응 과정에는 단계별 모식도를 사용하며,
연구의 핵심 결론은 강조 박스와 핵심 수치로 제시하였다.

이를 통해 전문적인 연구 내용을 단순화하는 것이 아니라
정보의 구조를 시각적으로 재배치하여 독자의 이해를 돕도록 하였다.
""")


# =========================================================
# 16 콘텐츠 제작 목적
# =========================================================

st.markdown("""
<div class="section">

<div class="kicker">16 · CONTENT PURPOSE</div>

<h2>콘텐츠 제작 목적</h2>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout">

이 웹사이트는 전문적인 고분자 합성 연구의 내용을
<b>시각적 매체로 재구성한 과학 웹사이트</b>이다.

<br><br>

고등학생을 주요 독자로 설정하여 ATRP, 기계화학,
중합 속도, 고분자 분해, 해중합과 같은 전문 개념을
단순한 용어 설명에 그치지 않고 실제 연구 데이터와 연결하였다.

<br><br>

특히 기사에서 접한 연구를 원 논문으로 확장하여
핵심 정보를 선별하고, 이를 텍스트·표·그래프·과정 모식도·
수치 강조 등의 다양한 매체로 재구성함으로써
전문적인 과학 정보를 효과적으로 전달하는 것을 목표로 하였다.

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
### 핵심 연구 논문

Kwon, G., Yim, D., Cha, S. et al.

**Mechanochemical atom transfer radical polymerization unlocks
functional methacrylate lifecycles of controlled synthesis,
force-activated degradation, and depolymerization.**

*Nature Communications*, 17, 5826 (2026).

DOI: **10.1038/s41467-026-72346-3**

### 연구 확인 자료

Nature Communications 원문 및 PubMed 등
공개 학술 데이터베이스의 연구 정보를 참고하여 구성하였다.

### 콘텐츠 제작

기사에서 접한 연구를 출발점으로 원 연구의 내용을 확인하고,
고등학생 독자를 대상으로 핵심 개념과 연구 데이터를 선별한 뒤
다양한 시각적 매체를 활용해 과학 웹사이트 형태로 재구성하였다.
""")

st.caption(
    "Chemistry · Science Communication · Web-based Visual Content"
)
