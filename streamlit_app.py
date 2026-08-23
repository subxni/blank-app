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
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

.hero {
    padding: 3rem 2.8rem;
    border-radius: 24px;
    background: linear-gradient(135deg, #eef5ff, #f7f4ff);
    margin-bottom: 1.5rem;
}

.hero h1 {
    font-size: 3.1rem;
    line-height: 1.15;
    margin: 0 0 0.8rem 0;
    white-space: nowrap;
}

.hero p {
    font-size: 1.08rem;
    color: #475569;
    line-height: 1.7;
    margin-bottom: 0;
}

.kicker {
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.13em;
    color: #64748b;
    margin-bottom: 0.5rem;
}

.section {
    padding-top: 2.2rem;
    margin-top: 2rem;
    border-top: 1px solid #e5e7eb;
}

.section h2 {
    margin-top: 0.2rem;
    margin-bottom: 1rem;
}

p {
    line-height: 1.75;
}

.callout {
    padding: 1.2rem 1.35rem;
    background: #f8fafc;
    border-left: 4px solid #64748b;
    border-radius: 10px;
    margin: 1rem 0;
    line-height: 1.75;
}

.question {
    padding: 1.5rem;
    background: #f1f5f9;
    border-radius: 16px;
    margin: 1rem 0 1.2rem 0;
    text-align: center;
}

.question h3 {
    margin: 0;
    line-height: 1.5;
}

.flow {
    padding: 1.4rem;
    background: #f8fafc;
    border-radius: 16px;
    text-align: center;
    line-height: 2;
    margin: 1rem 0;
}

.card {
    padding: 1.3rem;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    min-height: 150px;
}

.lifecycle {
    padding: 1.7rem;
    background: #f8fafc;
    border-radius: 20px;
    text-align: center;
    margin: 1.2rem 0;
}

.lifecycle .step {
    display: inline-block;
    vertical-align: middle;
    width: 13%;
    min-width: 105px;
    margin: 0.25rem;
    padding: 0.8rem 0.4rem;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
}

.lifecycle .arrow {
    display: inline-block;
    font-size: 1.3rem;
    vertical-align: middle;
    margin: 0 0.15rem;
}

.step-title {
    font-weight: 800;
    margin-bottom: 0.35rem;
}

.step-text {
    font-size: 0.82rem;
    color: #64748b;
    line-height: 1.45;
}

.source-box {
    padding: 1.2rem 1.35rem;
    background: #f8fafc;
    border-radius: 12px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 실제 논문에서 확인한 데이터
# =========================================================

rate_data = pd.DataFrame({
    "단량체": ["NPMA", "BPMA", "PYMA", "TPMA"],
    "겉보기 중합 속도상수 (min⁻¹)": [
        3.93e-1,
        1.88e-1,
        1.17e-1,
        0.50e-1
    ]
})

conversion_data = pd.DataFrame({
    "볼밀링 시간 (min)": [5, 30],
    "NPMA 전환율 (%)": [83, 95]
})

force_data = pd.DataFrame({
    "고분자": ["PNPMA", "PPYMA"],
    "주사슬 신장 median Fmax (nN)": [5.92, 5.91],
    "곁가지 신장 median Fmax (nN)": [5.85, 5.81]
})

depoly_data = pd.DataFrame({
    "조건": [
        "정제된 PNPMA",
        "단량체 5 mol% 첨가",
        "단량체 20 mol% 첨가"
    ],
    "Mlim (kDa)": [4.4, 5.8, 7.7]
})


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="kicker">CHEMISTRY · SCIENCE WEB</div>

<h1>고분자를 만들면서 동시에 분해할 수 있을까?</h1>

<p>
전문적인 고분자 합성 연구를 화학 개념과 실제 연구 데이터,
다양한 시각적 매체를 활용하여 재구성한 과학 웹사이트입니다.
</p>

</div>
""", unsafe_allow_html=True)


st.info(
    "연세대학교 연세소식에서 소개된 연구를 출발점으로 원 연구 논문까지 "
    "확장하여 조사하고, 전문적인 화학 정보를 고등학생 독자가 이해하기 쉽도록 "
    "웹 콘텐츠로 재구성했습니다."
)


# =========================================================
# 01 연구 시작
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">01 · RESEARCH START</div>
<h2>연구 시작</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "연세대학교 연세소식에서 「김병수 교수팀, 쇠구슬로 만드는 친환경 고분자 "
    "합성 기술 개발」이라는 기사를 접했습니다. 기사에서는 쇠구슬을 이용한 "
    "볼밀링으로 용매 없이 고분자를 합성하고, 기계적 힘에 의한 분해와 원래 "
    "단량체로의 해중합까지 연결할 수 있는 연구를 소개하고 있었습니다. "
    "특히 고분자의 합성과 분해가 하나의 기계화학 반응에서 함께 연구된다는 "
    "점에 관심을 갖게 되어, 기사에서 소개된 내용을 원 연구 논문까지 "
    "확장하여 조사했습니다."
)

st.write(
    "원 논문에서는 방향족 치환기의 크기가 서로 다른 네 가지 메타크릴레이트 "
    "단량체를 비교하고, 기계화학적 ATRP에서 나타나는 중합 속도와 고분자 "
    "분해 경로를 분석했습니다. 또한 MALDI-ToF 질량분석과 CoGEF 계산을 "
    "활용하여 실제 실험에서 관찰된 절단 위치를 분자 수준에서 해석하고, "
    "해중합 과정까지 확인했습니다. 따라서 이 웹사이트에서는 기사에 "
    "간략하게 제시된 연구를 화학 개념, 실험 방법, 실제 데이터와 연결하여 "
    "하나의 흐름으로 재구성했습니다."
)

st.markdown("""
<div class="callout">

<b>기사 → 원 논문 → 정보 선별 → 시각적 재구성</b><br>
과학 기사에서 연구의 핵심 내용을 접한 뒤 원 논문을 통해 세부적인
실험 방법과 데이터를 확인하고, 이를 고등학생 독자가 이해하기 쉬운
웹 콘텐츠로 재구성했습니다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 02 연구 질문
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">02 · RESEARCH QUESTION</div>
<h2>연구 질문</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="question">
<h3>고분자를 만드는 과정에서<br>
동시에 분해가 일어날 수 있을까요?</h3>
</div>
""", unsafe_allow_html=True)

st.write(
    "일반적으로 고분자 합성과 분해는 서로 반대되는 과정으로 생각하기 "
    "쉽습니다. 그러나 기계화학적 ATRP에서는 반응이 진행되는 동안 "
    "기계적 힘이 고분자 사슬에 전달되기 때문에 고분자 사슬의 성장과 "
    "절단이 서로 경쟁할 수 있습니다. 연구진은 이러한 현상을 세 단계로 "
    "나누어 분석하고, 단순한 고분자 합성을 넘어 분해와 해중합까지 "
    "하나의 연구 흐름으로 살펴보았습니다."
)


# =========================================================
# 03 고분자의 생애주기
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">03 · POLYMER LIFECYCLE</div>
<h2>고분자의 생애주기</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "이 연구의 전체 흐름을 한눈에 볼 수 있도록 단량체의 출발부터 "
    "고분자의 합성, 기계적 분해, 해중합과 단량체 회수까지를 하나의 "
    "순환 구조로 표현했습니다."
)

st.markdown("""
<div class="lifecycle">

<div class="step">
<div class="step-title">① 단량체</div>
<div class="step-text">메타크릴레이트 기반<br>출발 물질</div>
</div>

<div class="arrow">→</div>

<div class="step">
<div class="step-title">② ATRP</div>
<div class="step-text">라디칼 중합을<br>정밀하게 제어</div>
</div>

<div class="arrow">→</div>

<div class="step">
<div class="step-title">③ 고분자</div>
<div class="step-text">반복 단위가 연결된<br>고분자 사슬 형성</div>
</div>

<div class="arrow">→</div>

<div class="step">
<div class="step-title">④ 기계적 힘</div>
<div class="step-text">볼밀링으로<br>에너지 전달</div>
</div>

<div class="arrow">→</div>

<div class="step">
<div class="step-title">⑤ 분해</div>
<div class="step-text">고분자 사슬의<br>기계적 절단</div>
</div>

<div class="arrow">→</div>

<div class="step">
<div class="step-title">⑥ 해중합</div>
<div class="step-text">단량체가 다시<br>생성될 수 있음</div>
</div>

<div class="arrow">↺</div>

<div class="step">
<div class="step-title">⑦ 단량체</div>
<div class="step-text">다시 출발 물질로<br>이어지는 순환</div>
</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 04 고분자와 단량체
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">04 · POLYMER CHEMISTRY</div>
<h2>어떤 고분자를 연구했을까요?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "연구진은 메타크릴레이트 골격에 서로 다른 방향족 치환기가 결합된 "
    "네 종류의 단량체를 직접 합성했습니다. 치환기의 크기와 구조가 "
    "달라지기 때문에 각 단량체의 반응성과 기계적 분해 거동을 비교할 "
    "수 있습니다."
)

monomers = pd.DataFrame({
    "약어": ["NPMA", "BPMA", "PYMA", "TPMA"],
    "단량체": [
        "2-naphthyl methacrylate",
        "4-biphenyl methacrylate",
        "1-pyrene methacrylate",
        "4-tritylphenyl methacrylate"
    ],
    "분자 부피 (Å³)": [
        219.46,
        228.19,
        268.40,
        389.44
    ]
})

st.dataframe(
    monomers,
    hide_index=True,
    use_container_width=True
)

st.write(
    "논문에서 계산된 분자 부피는 NPMA 219.46 Å³, BPMA 228.19 Å³, "
    "PYMA 268.40 Å³, TPMA 389.44 Å³입니다. 전체적으로 단량체 크기가 "
    "커질수록 중합 반응성이 낮아지는 경향이 나타났지만, PYMA는 이 "
    "경향에서 벗어났습니다. 연구진은 이러한 차이에 입체적 접근성뿐 "
    "아니라 방향족 고리 사이의 π–π stacking과 같은 분자 간 상호작용도 "
    "영향을 줄 수 있다고 해석했습니다."
)


# =========================================================
# 05 ATRP
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">05 · ATRP</div>
<h2>ATRP는 어떤 역할을 할까요?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "ATRP는 Atom Transfer Radical Polymerization의 약자로, "
    "전이금속 촉매를 이용하여 라디칼의 활성화와 비활성화를 조절하는 "
    "정밀 라디칼 중합법입니다. 이를 통해 고분자 사슬의 성장을 보다 "
    "제어된 방식으로 진행할 수 있습니다."
)

st.markdown("""
<div class="flow">

<b>비활성 상태</b>
&nbsp; → &nbsp;
<b>활성화</b>
&nbsp; → &nbsp;
<b>단량체 첨가와 사슬 성장</b>
&nbsp; → &nbsp;
<b>비활성화</b>

</div>
""", unsafe_allow_html=True)

st.write(
    "이번 연구에서는 ethyl 2-bromoisobutyrate를 개시제로, CuBr을 "
    "촉매로, PMDETA를 리간드로 사용했습니다. 이러한 ATRP 반응계를 "
    "용액이 아닌 기계화학 조건에 적용했다는 점이 연구의 중요한 "
    "특징입니다."
)


# =========================================================
# 06 기계화학
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">06 · MECHANOCHEMISTRY</div>
<h2>화학 반응에 기계적 힘을 이용한다면?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "기계화학은 외부에서 가해지는 기계적 힘을 이용해 화학 반응을 "
    "유도하는 분야입니다. 이 연구에서는 진동식 볼밀을 이용하여 "
    "반응물에 반복적인 충돌과 기계적 에너지를 전달했습니다. "
    "따라서 여기서 쇠구슬은 단순히 물질을 분쇄하는 도구가 아니라 "
    "고체 상태에서 화학 반응을 진행시키는 에너지 전달 수단입니다."
)

st.markdown("""
<div class="flow">

반응물 + ATRP 반응계
<br>↓<br>
⚙️ <b>볼밀링</b>
<br>↓<br>
충돌 · 기계적 에너지 전달
<br>↓<br>
<b>고체 상태 중합</b>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 07 실제 중합 데이터
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">07 · EXPERIMENTAL DATA</div>
<h2>단량체에 따라 중합 속도가 달라질까요?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "연구진은 각 단량체의 시간에 따른 전환율을 분석하고, "
    "ln([M]₀/[M]ₜ)를 시간에 대해 나타내어 겉보기 중합 속도상수 "
    "kp,app를 계산했습니다. 그 결과 네 단량체에서 서로 다른 "
    "중합 속도가 확인되었습니다."
)

rate_display = rate_data.copy()
rate_display["겉보기 중합 속도상수 (min⁻¹)"] = [
    "3.93 × 10⁻¹",
    "1.88 × 10⁻¹",
    "1.17 × 10⁻¹",
    "0.50 × 10⁻¹"
]

st.dataframe(
    rate_display,
    hide_index=True,
    use_container_width=True
)

st.bar_chart(
    rate_data.set_index("단량체"),
    y="겉보기 중합 속도상수 (min⁻¹)",
    height=350
)

st.write(
    "NPMA의 kp,app가 가장 높았고 TPMA가 가장 낮았습니다. 연구진은 "
    "전체적으로 단량체의 분자 크기가 커질수록 반응 부위에 접근하기 "
    "어려워지는 입체적 효과가 중합 속도를 낮추는 요인이라고 "
    "설명했습니다. 다만 PYMA의 경우 단순한 분자 크기만으로는 "
    "반응성을 완전히 설명할 수 없어 방향족 분자 사이의 상호작용도 "
    "고려할 필요가 있음을 제시했습니다."
)


# =========================================================
# 08 시간에 따른 전환율
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">08 · NMR DATA</div>
<h2>실제로 얼마나 중합되었을까요?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "대표적인 NPMA의 중합 과정은 ¹H NMR spectroscopy를 이용해 "
    "추적했습니다. 논문에 따르면 NPMA의 전환율은 볼밀링 5분 후 "
    "83%, 30분 후 95%에 도달했습니다. 전환율은 단량체와 고분자의 "
    "특정 신호를 비교하여 계산했습니다."
)

st.line_chart(
    conversion_data.set_index("볼밀링 시간 (min)"),
    y="NPMA 전환율 (%)",
    height=320
)

st.dataframe(
    conversion_data,
    hide_index=True,
    use_container_width=True
)


# =========================================================
# 09 합성과 분해의 경쟁
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">09 · PROPAGATION & DEGRADATION</div>
<h2>중합과 분해가 동시에 경쟁합니다</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "이 연구에서 중요한 개념은 중합과 분해가 서로 완전히 분리된 "
    "과정이 아니라는 점입니다. 반응 초기에는 단량체가 연결되면서 "
    "고분자 사슬이 성장하지만, 반응이 진행되면 기계적 힘에 의한 "
    "고분자 사슬의 절단도 증가합니다."
)

st.markdown("""
<div class="flow">

<b>Stage I</b> · 전파 우세
<br>
고분자 사슬이 성장합니다.
<br><br>
↓
<br><br>
<b>Stage II</b> · 전파 ↔ 분해
<br>
두 과정의 속도가 균형을 이루는 영역입니다.
<br><br>
↓
<br><br>
<b>Stage III</b> · 분해 우세
<br>
고분자 사슬의 절단이 우세해지면서 분자량이 감소합니다.

</div>
""", unsafe_allow_html=True)

st.write(
    "특히 주사슬의 C–C 결합이 동종분해(homolytic cleavage)를 받아 "
    "절단되면 더 짧은 고분자 사슬과 고분자 라디칼이 생성될 수 있습니다. "
    "따라서 반응 시간이 길어진다고 해서 고분자 분자량이 계속 증가하는 "
    "것은 아니며, 어느 시점부터는 분해가 우세해집니다."
)


# =========================================================
# 10 분해 위치
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">10 · CHAIN SCISSION</div>
<h2>고분자의 어디가 끊어질까요?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "연구진은 MALDI-ToF 분석을 통해 고분자의 서로 다른 위치에서 "
    "절단이 일어날 수 있음을 확인했습니다. 분석 대상에는 α-말단, "
    "ω-말단, 곁가지(pendant group), 그리고 고분자 주사슬(main chain)이 "
    "포함되었습니다."
)

st.markdown("""
<div class="flow">

<b>고분자 사슬</b>
<br><br>
α-말단 ｜ 곁가지 ｜ 주사슬 ｜ ω-말단
<br><br>
↓
<br>
기계적 힘에 의한 서로 다른 절단 경로

</div>
""", unsafe_allow_html=True)

st.write(
    "특히 치환기의 크기와 구조에 따라 분해 경로의 상대적인 비중이 "
    "달라졌습니다. 연세대 기사에서도 부피가 큰 치환기를 가진 "
    "고분자에서 주사슬보다 치환기 부위 절단이 상대적으로 우세하게 "
    "나타났다고 설명하고 있습니다. [oai_citation:2‡Yonsei News](https://news.yonsei.ac.kr/kr/academia/detail?bbSeq=35820)"
)


# =========================================================
# 11 계산화학
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">11 · COMPUTATIONAL CHEMISTRY</div>
<h2>실험 결과를 계산화학으로 다시 확인하다</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "실험에서 관찰된 절단 경로를 분자 수준에서 해석하기 위해 "
    "연구진은 CoGEF(Constrained Geometries simulate External Force) "
    "계산을 사용했습니다. CoGEF에서는 분자 구조의 특정 원자 사이 "
    "거리를 단계적으로 늘려 외부에서 힘이 가해지는 상황을 모사하고, "
    "그 과정에서 나타나는 힘의 변화를 분석합니다."
)

st.write(
    "PNPMA와 PPYMA의 주사슬을 신장했을 때의 median Fmax는 각각 "
    "5.92 nN과 5.91 nN으로 거의 같았습니다. 따라서 두 고분자의 "
    "분해 경로 차이를 단순히 주사슬 자체의 결합 강도 차이만으로 "
    "설명하기는 어렵습니다. 연구진은 실험적인 절단 빈도와 계산 결과를 "
    "함께 비교하여 분자 구조와 기계적 힘의 전달 방식을 해석했습니다."
)

st.dataframe(
    force_data,
    hide_index=True,
    use_container_width=True
)


# =========================================================
# 12 해중합
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">12 · DEPOLYMERIZATION</div>
<h2>분해의 끝에서 단량체를 다시 얻을 수 있을까요?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "이 연구는 단순히 고분자를 작은 조각으로 만드는 데서 끝나지 "
    "않습니다. 기계적 분해 과정에서 원래의 단량체로 되돌아가는 "
    "해중합(depolymerization)도 확인했습니다. PNPMA뿐 아니라 "
    "PPYMA에서도 해중합이 관찰되어 이러한 현상이 특정 고분자 하나에 "
    "한정되지 않을 가능성을 보여주었습니다."
)

st.markdown("""
<div class="flow">

<b>고분자</b>
<br>
↓
<br>
기계적 분해
<br>
↓
<br>
<b>해중합</b>
<br>
↓
<br>
<b>원래 단량체 생성</b>

</div>
""", unsafe_allow_html=True)

st.write(
    "또한 PNPMA의 분해 과정에서 잔류 단량체의 양을 달리했을 때 "
    "분해의 한계 분자량(Mlim)이 달라졌습니다. 정제된 PNPMA만 사용한 "
    "경우 Mlim은 4.4 kDa였고, 단량체를 5 mol% 첨가하면 5.8 kDa, "
    "20 mol% 첨가하면 7.7 kDa로 증가했습니다. 이는 생성된 단량체가 "
    "고분자 분해를 억제하는 방향으로 중합–해중합 평형에 영향을 줄 수 "
    "있음을 보여줍니다."
)

st.bar_chart(
    depoly_data.set_index("조건"),
    y="Mlim (kDa)",
    height=330
)


# =========================================================
# 13 연구의 의미
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">13 · SIGNIFICANCE</div>
<h2>이 연구가 보여주는 것은 무엇일까요?</h2>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>① 정밀 합성</h3>
    기계화학 조건에서도 ATRP를 이용하여
    기능성 메타크릴레이트 고분자를
    제어된 방식으로 합성했습니다.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>② 힘-유도 분해</h3>
    고분자의 구조에 따라 기계적 힘에 의해
    나타나는 절단 경로가 달라지는 현상을
    실험과 계산으로 분석했습니다.
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>③ 원료 회수 가능성</h3>
    고분자의 분해뿐 아니라 원래 단량체로
    되돌아가는 해중합까지 확인했습니다.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# 14 전문적인 연구를 웹 콘텐츠로
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">14 · MEDIA DESIGN</div>
<h2>전문적인 연구를 어떻게 웹 콘텐츠로 바꾸었는가?</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "이 웹사이트는 전문적인 연구 내용을 단순히 요약하여 옮긴 것이 "
    "아닙니다. 먼저 과학 기사에서 연구의 핵심 아이디어를 파악한 뒤 "
    "원 논문을 확인하여 기사에 생략된 실험 방법과 연구 데이터를 "
    "추가로 조사했습니다. 이후 정보의 성격에 따라 서로 다른 "
    "시각적 매체를 선택하여 웹페이지의 구조로 재배치했습니다."
)

media_data = pd.DataFrame({
    "연구 정보": [
        "연구의 배경과 질문",
        "고분자의 생애주기",
        "단량체 구조 비교",
        "중합 속도",
        "시간에 따른 전환율",
        "분해 단계",
        "분해 위치",
        "계산화학 결과",
        "해중합"
    ],
    "재구성한 매체": [
        "설명문 + 강조 박스",
        "순환형 과정도",
        "표",
        "표 + 막대그래프",
        "선그래프 + 표",
        "단계별 모식도",
        "구조 과정도",
        "수치 비교표",
        "과정도 + 막대그래프"
    ],
    "매체를 선택한 이유": [
        "연구의 맥락을 자연스럽게 전달하기 위해",
        "전체 연구 흐름을 한눈에 보여주기 위해",
        "분자 구조의 차이를 비교하기 위해",
        "수치의 크기 차이를 직관적으로 보여주기 위해",
        "시간에 따른 변화를 보여주기 위해",
        "반응의 순서를 명확하게 보여주기 위해",
        "서로 다른 절단 위치를 구분하기 위해",
        "계산 결과의 차이를 직접 비교하기 위해",
        "분해에서 원료 회수까지의 흐름을 보여주기 위해"
    ]
})

st.dataframe(
    media_data,
    hide_index=True,
    use_container_width=True
)

st.write(
    "예를 들어 중합 속도처럼 여러 물질의 수치를 비교해야 하는 "
    "정보에는 막대그래프를 사용하고, 시간에 따른 전환율 변화에는 "
    "선그래프를 사용했습니다. 반면 합성에서 분해와 해중합으로 "
    "이어지는 과정은 숫자보다 순서와 관계를 보여주는 것이 중요하기 "
    "때문에 과정 모식도로 표현했습니다. 이를 통해 같은 연구 정보를 "
    "하나의 표현 방식으로 반복하지 않고 정보의 특성에 맞는 매체로 "
    "변환했습니다."
)


# =========================================================
# 15 콘텐츠 제작 목적
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">15 · CONTENT PURPOSE</div>
<h2>콘텐츠 제작 목적</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="callout">

이 웹사이트의 목적은 전문적인 고분자 합성 연구를
<b>시각적 매체로 재구성한 과학 웹사이트</b>로 제작하는 것입니다.

<br><br>

주요 독자는 <b>고등학생</b>으로 설정했습니다. 따라서 ATRP,
기계화학, 중합 속도, 고분자 분해, 해중합과 같은 전문적인 개념을
그대로 나열하기보다 실제 연구에서 사용된 데이터와 연결하여
이해할 수 있도록 구성했습니다.

<br><br>

또한 과학 기사에서 접한 연구를 원 논문까지 확장하여 조사한 뒤,
연구의 핵심 정보를 표·그래프·과정 모식도·수치 강조·비교 카드 등
다양한 시각적 매체로 재구성했습니다.

<br><br>

이를 통해 전문적인 과학 정보를 단순화하는 데 그치지 않고,
정보의 구조와 관계가 드러나도록 표현 방식을 선택하여
독자가 연구의 흐름을 스스로 따라갈 수 있도록 하는 것을
목표로 했습니다.

</div>
""", unsafe_allow_html=True)


# =========================================================
# 16 연구 확인 자료
# =========================================================

st.markdown("""
<div class="section">
<div class="kicker">16 · SOURCES</div>
<h2>연구 확인 자료</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="source-box">

<b>① 과학 기사 — 연구를 처음 접한 자료</b><br>
연세대학교 연세소식, 「김병수 교수팀, 쇠구슬로 만드는 친환경 고분자 합성 기술 개발」, 2026.05.11<br>
연구의 배경과 기계화학적 고분자 합성·분해의 핵심 내용을 파악하는 데 활용했습니다.

<br><br>

<b>② 원 연구 논문 — 심화 조사 자료</b><br>
Kwon, G., Yim, D., Cha, S. et al.<br>
<i>Mechanochemical atom transfer radical polymerization unlocks functional methacrylate lifecycles of controlled synthesis, force-activated degradation, and depolymerization.</i><br>
Nature Communications 17, 5826 (2026).<br>
DOI: 10.1038/s41467-026-72346-3<br>
기사에서 소개된 연구의 실험 방법, 분석 방법, 수치 데이터와 분자 수준의 해석을 확인하는 데 활용했습니다.

<br><br>

<b>③ 정보 재구성</b><br>
기사와 원 논문에서 확인한 정보를 연구의 흐름에 따라 선별하고,
고등학생 독자를 대상으로 이해하기 쉬운 시각적 웹 콘텐츠로 재구성했습니다.

</div>
""", unsafe_allow_html=True)

st.markdown(
    "기사 원문: "
    "[연세대학교 연세소식](https://news.yonsei.ac.kr/kr/academia/detail?bbSeq=35820)"
)

st.markdown(
    "원 논문: "
    "[Nature Communications](https://www.nature.com/articles/s41467-026-72346-3)"
)

st.caption(
    "본 웹사이트는 공개된 과학 기사와 원 연구 논문을 바탕으로 "
    "연구 내용을 교육·과학 커뮤니케이션 목적에 맞게 재구성한 콘텐츠입니다."
)
