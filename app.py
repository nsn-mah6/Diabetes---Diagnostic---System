import joblib
import pandas as pd
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="D",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --ink: #17222d;
        --muted: #687887;
        --teal: #087f8c;
        --teal-dark: #075762;
        --mint: #e4f5f1;
        --cream: #f7fbf9;
        --line: #d8e5e3;
        --coral: #df684e;
    }

    .stApp {
        background: radial-gradient(circle at 8% 8%, #d8f0eb 0, transparent 28%),
                    radial-gradient(circle at 94% 18%, #fff0d8 0, transparent 22%),
                    var(--cream);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    .block-container {
        max-width: 1100px;
        padding: 3rem 2rem 4rem;
    }

    h1, h2, h3 {
        color: var(--ink) !important;
        font-family: 'Space Grotesk', sans-serif !important;
        letter-spacing: 0 !important;
    }

    .hero {
        animation: rise-in 700ms ease both;
        margin: 0 auto 2.1rem;
        max-width: 820px;
        text-align: center;
    }

    .eyebrow {
        color: var(--teal);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
    }

    .hero h1 {
        font-size: clamp(2.25rem, 6vw, 4.6rem);
        line-height: 0.98;
        margin: 0.65rem 0 1rem;
    }

    .hero p {
        color: var(--muted);
        font-size: 1.05rem;
        line-height: 1.65;
        margin: 0 auto;
        max-width: 590px;
    }

    .form-shell {
        animation: rise-in 800ms 120ms ease both;
        padding: 0.5rem 0;
    }

    div[data-testid="stForm"] {
        border: 0 !important;
        padding: 0 !important;
    }

    .section-label {
        color: var(--ink);
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .section-help {
        color: var(--muted);
        font-size: 0.88rem;
        margin-bottom: 1.2rem;
    }

    label, .stNumberInput label, .stSelectbox label {
        color: var(--ink) !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="input"], div[data-baseweb="select"] > div {
        background: #ffffff !important;
        border-color: var(--line) !important;
        border-radius: 10px !important;
        box-shadow: 0 3px 12px rgba(33, 74, 77, 0.04);
        transition: border-color 180ms ease, box-shadow 180ms ease, transform 180ms ease;
    }

    div[data-testid="stNumberInput"] {
        animation: field-in 550ms ease both;
    }

    div[data-testid="stNumberInput"]:hover div[data-baseweb="input"] {
        border-color: #9bcac7 !important;
        box-shadow: 0 7px 18px rgba(33, 74, 77, 0.09);
        transform: translateY(-2px);
    }

    div[data-baseweb="input"] input {
        color: var(--ink) !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"] > div:focus-within {
        border-color: var(--teal) !important;
        box-shadow: 0 0 0 3px rgba(8, 127, 140, 0.12) !important;
        transform: translateY(-1px);
    }

    .stFormSubmitButton button {
        background: var(--teal) !important;
        border: 0 !important;
        border-radius: 10px !important;
        color: white !important;
        font-weight: 700 !important;
        min-height: 3rem;
        transition: background 180ms ease, transform 180ms ease, box-shadow 180ms ease;
        width: 100%;
    }

    .stFormSubmitButton button:hover {
        background: var(--teal-dark) !important;
        box-shadow: 0 8px 18px rgba(8, 127, 140, 0.22);
        transform: translateY(-2px);
    }

    .result {
        animation: result-in 500ms ease both;
        border-left: 5px solid var(--teal);
        border-radius: 12px;
        margin-top: 1.5rem;
        padding: 1.25rem 1.4rem;
    }

    .result.positive {
        background: #fff1ed;
        border-left-color: var(--coral);
    }

    .result.negative {
        background: var(--mint);
    }

    .result-kicker {
        color: var(--muted);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .result-title {
        color: var(--ink);
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 0.25rem;
    }

    .result-note {
        color: var(--muted);
        font-size: 0.9rem;
        margin-top: 0.3rem;
    }

    .footer-note {
        color: var(--muted);
        font-size: 0.78rem;
        margin-top: 2rem;
        text-align: center;
    }

    @keyframes rise-in {
        from { opacity: 0; transform: translateY(18px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes result-in {
        from { opacity: 0; transform: scale(0.98) translateY(8px); }
        to { opacity: 1; transform: scale(1) translateY(0); }
    }

    @keyframes field-in {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    div[data-testid="stNumberInput"]:nth-child(1) { animation-delay: 80ms; }
    div[data-testid="stNumberInput"]:nth-child(2) { animation-delay: 140ms; }
    div[data-testid="stNumberInput"]:nth-child(3) { animation-delay: 200ms; }
    div[data-testid="stNumberInput"]:nth-child(4) { animation-delay: 260ms; }
    div[data-testid="stNumberInput"]:nth-child(5) { animation-delay: 320ms; }

    @media (max-width: 640px) {
        .block-container { padding: 2rem 1rem 3rem; }
        .hero { margin-bottom: 1.5rem; }
        .hero h1 { font-size: 2.65rem; }
        .hero p { font-size: 0.95rem; }
        .form-shell { padding: 0.25rem 0; }
        .stNumberInput, .stSelectbox { margin-bottom: 0.35rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

MODEL_PATH = "artifact/best_diabetes_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.markdown(
    """
    <header class="hero">
        <div class="eyebrow">Diabetes screening support</div>
        <h1>Diabetes Risk Assessment</h1>
        <p>Enter the patient's clinical measurements to receive a model-based diabetes risk prediction. This tool is for educational screening and does not replace a medical diagnosis.</p>
    </header>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="form-shell">', unsafe_allow_html=True)

# --------------------------------------------------
# Input Form
# --------------------------------------------------

with st.form("diabetes_form"):

    st.markdown('<div class="section-label">Patient health information</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-help">Enter the most recent available measurements for the patient.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=1,
            help="Number of pregnancies. Use 0 if not applicable.",
        )

        glucose = st.number_input(
            "Glucose (mg/dL)",
            min_value=0,
            max_value=400,
            value=120,
            help="Plasma glucose concentration.",
        )

        blood_pressure = st.number_input(
            "Blood pressure (mm Hg)",
            min_value=0,
            max_value=250,
            value=70,
            help="Diastolic blood pressure in mm Hg.",
        )

        skin_thickness = st.number_input(
            "Skin thickness (mm)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=0.1,
            help="Triceps skin fold thickness in mm.",
        )

        insulin = st.number_input(
            "Insulin (mu U/mL)",
            min_value=0.0,
            max_value=1000.0,
            value=80.0,
            step=0.1,
            help="Two-hour serum insulin level.",
        )

    with col2:

        age = st.number_input(
            "Age (years)",
            min_value=1,
            max_value=120,
            value=30,
        )

        bmi = st.number_input(
            "BMI (kg/m²)",
            min_value=0.0,
            max_value=80.0,
            value=25.0,
            step=0.1,
        )

        diabetes_pedigree_function = st.number_input(
            "Diabetes pedigree score",
            min_value=0.0,
            max_value=3.0,
            value=0.5,
            step=0.01,
            help="A family-history based diabetes score.",
        )

    submitted = st.form_submit_button(
        "Predict diabetes risk"
    )

st.markdown('</section>', unsafe_allow_html=True)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if submitted:

    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [diabetes_pedigree_function],
        "Age": [age],
    })

    try:

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.markdown(
                '<div class="result positive"><div class="result-title">Higher diabetes risk indicated</div></div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="result negative"><div class="result-title">Lower diabetes risk indicated</div></div>',
                unsafe_allow_html=True,
            )

    except (KeyError, TypeError, ValueError) as e:

        st.error(
            f"Prediction failed. Please check the model "
            f"input features.\n\nError: {e}"
        )
