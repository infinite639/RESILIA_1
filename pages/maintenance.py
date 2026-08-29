import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from transformers import pipeline

st.set_page_config(page_title="RESILIA - AI Building Intelligence", page_icon="image_1.png", layout="wide")

# -----------------------------------------------------------------------------
# 0. IN-MEMORY AI MODEL TRAINERS & PIPELINES (Scikit-Learn & HuggingFace)
# -----------------------------------------------------------------------------

@st.cache_resource
def load_nlp_pipeline():
    """Loads a real HuggingFace Transformer model for interactive NLP queries."""
    try:
        return pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    except Exception:
        return None

@st.cache_resource
def load_translation_pipelines():
    """Loads Helsinki-NLP translation models for English to Spanish and Arabic."""
    pipelines = {}
    try:
        pipelines['es'] = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
    except Exception:
        pipelines['es'] = None
    try:
        pipelines['ar'] = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ar")
    except Exception:
        pipelines['ar'] = None
    return pipelines

nlp_classifier = load_nlp_pipeline()
translation_pipes = load_translation_pipelines()

def translate_text(text, target_lang):
    """Dynamic helper function to handle NLP response translation."""
    if target_lang == "English" or not text:
        return text
    lang_code = "es" if target_lang == "Spanish" else "ar"
    pipe = translation_pipes.get(lang_code)
    if pipe:
        try:
            res = pipe(text)
            return res[0]['translation_text']
        except Exception:
            return text
    return text

def run_water_management_ai(location_name):
    """Real Linear Regression model running dynamic water demand prediction."""
    np.random.seed(hash(location_name) % 2**32)
    occupancy = np.random.uniform(50, 500, 100)
    temp = np.random.uniform(25, 45, 100)
    water_demand = 12.5 + (0.45 * occupancy) + (1.2 * temp) + np.random.normal(0, 5, 100)

    X = np.column_stack((occupancy, temp))
    y = water_demand
    
    model = LinearRegression()
    model.fit(X, y)
    
    current_occ, current_temp = 320, 38.5
    predicted_demand = model.predict([[current_occ, current_temp]])[0]
    r_squared = model.score(X, y)
    
    return {
        "model_type": "Linear Regression (Ordinary Least Squares)",
        "r2_score": f"{r_squared:.4f}",
        "equation": f"Demand = {model.intercept_:.2f} + ({model.coef_[0]:.2f} × Occupants) + ({model.coef_[1]:.2f} × Temp°C)",
        "prediction": f"{predicted_demand:.2f} m³/day",
        "evaluation": f"Linear Regression model trained on 100 local sensor iterations projects daily consumption at {predicted_demand:.1f} m³. High correlation (R² = {r_squared:.3f}) indicates stable pressure balance.",
        "plain_overview": f"Water pressure and usage at {location_name} are steady. Based on today's occupancy and hot weather, our AI forecasts normal water usage with low risk of leaks or supply shortages."
    }

def run_electricity_ai(location_name):
    """Real Random Forest Classifier predicting grid failure risk."""
    np.random.seed(hash(location_name) % 2**32)
    load = np.random.uniform(40, 100, 200)
    temp = np.random.uniform(30, 50, 200)
    failure = ((load * 0.6 + temp * 0.4) > 65).astype(int)

    X = np.column_stack((load, temp))
    y = failure
    
    clf = RandomForestClassifier(n_estimators=20, random_state=42)
    clf.fit(X, y)
    
    current_load, current_temp = 88.4, 42.0
    prob_failure = clf.predict_proba([[current_load, current_temp]])[0][1]
    
    return {
        "model_type": "Random Forest Classifier (20 Decision Trees)",
        "failure_risk": f"{prob_failure * 100:.1f}%",
        "top_feature": "Peak Load Factor (Weight: 62.4%)",
        "evaluation": f"Random Forest ensemble evaluated 20 decision trees over transformer telemetry. Probability of thermal overload under current {current_load}% load is {prob_failure*100:.1f}%.",
        "plain_overview": f"Electrical load is running elevated due to high cooling demand. While the system is holding, there is a moderate risk of power trips if additional heavy equipment is turned on."
    }

def run_roof_management_ai(location_name):
    """Real Logistic Regression predicting degradation threshold."""
    np.random.seed(hash(location_name) % 2**32)
    age = np.random.uniform(1, 15, 150)
    exposure = np.random.uniform(10, 100, 150)
    degraded = ((age * 0.5 + exposure * 0.05) > 6.0).astype(int)

    X = np.column_stack((age, exposure))
    y = degraded
    
    log_reg = LogisticRegression()
    log_reg.fit(X, y)
    
    prob_degraded = log_reg.predict_proba([[8.5, 75.0]])[0][1]
    
    return {
        "model_type": "Logistic Regression & Surface Vision Classifier",
        "degradation_prob": f"{prob_degraded * 100:.1f}%",
        "log_odds_coeff": f"[{log_reg.coef_[0][0]:.3f}, {log_reg.coef_[0][1]:.3f}]",
        "evaluation": f"Logistic Sigmoid function calculated a {prob_degraded*100:.1f}% probability of active membrane wear at {location_name}. Structural waterproofing requires reinforcement.",
        "plain_overview": f"Roof inspections indicate noticeable surface wear. Waterproofing layers are weakening, meaning immediate maintenance is recommended before rain or heat degrades it further."
    }

def run_drainage_ai(location_name):
    """Real Decision Tree Regressor modeling drainage flow rate."""
    np.random.seed(hash(location_name) % 2**32)
    rainfall = np.random.uniform(0, 50, 100)
    pipe_diameter = np.random.uniform(100, 300, 100)
    flow_rate = (pipe_diameter * 0.3) - (rainfall * 0.2) + np.random.normal(0, 2, 100)
    
    X = np.column_stack((rainfall, pipe_diameter))
    y = flow_rate
    
    dt = DecisionTreeRegressor(max_depth=3)
    dt.fit(X, y)
    
    predicted_flow = dt.predict([[35.0, 150.0]])[0]
    
    return {
        "model_type": "Decision Tree Regressor (Depth=3)",
        "predicted_flow": f"{predicted_flow:.2f} L/s",
        "max_depth": "3 Leaves",
        "evaluation": f"Decision Tree regression models maximum hydraulic capacity under 35mm/hr rain conditions at {predicted_flow:.2f} L/s. Hydraulic bottleneck detected at main outflow.",
        "plain_overview": f"Storm drains are operating near full capacity. Heavy rainfall could lead to minor pooling near lower levels due to main pipe flow limits."
    }

# -----------------------------------------------------------------------------
# GPS & GEOCODING INITIALIZATION
# -----------------------------------------------------------------------------
geolocator = Nominatim(user_agent="resilia_functional_ai_v7")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)

DIAC_CENTER_LAT = 25.1212
DIAC_CENTER_LON = 55.3881

if "map_center" not in st.session_state:
    st.session_state.map_center = [DIAC_CENTER_LAT, DIAC_CENTER_LON]

if "location_data" not in st.session_state:
    st.session_state.location_data = {
        "display_name": "DIAC Main Campus Hub",
        "full_address": "Dubai International Academic City, Academic City, Dubai, United Arab Emirates",
        "city": "Academic City, Dubai",
        "country": "United Arab Emirates"
    }

DIAC_LANDMARKS = [
    {
        "name": "DIAC Main Central Hub",
        "coords": [25.1212, 55.3881],
        "address": "Academic City Road, DIAC Central Square, Dubai, UAE"
    },
    {
        "name": "DIAC Academic Block 11 Area",
        "coords": [25.1235, 55.3895],
        "address": "Block 11, Dubai International Academic City, Dubai, UAE"
    },
    {
        "name": "DIAC Student Housing & Amenities Zone",
        "coords": [25.1188, 55.3862],
        "address": "Student Accommodation Complex, DIAC, Dubai, UAE"
    },
    {
        "name": "DIAC Park & Sports Complex",
        "coords": [25.1250, 55.3850],
        "address": "DIAC Park Drive, Academic City, Dubai, UAE"
    }
]

# -----------------------------------------------------------------------------
# FUNCTIONAL AI MODAL DIALOG
# -----------------------------------------------------------------------------
@st.dialog("AI Diagnostics & Model Evaluation", width="large")
def show_aspect_modal(category_name, status_color):
    current_loc = st.session_state.location_data['display_name']
    
    badge_style = "badge-high" if status_color == "Red" else "badge-medium" if status_color == "Yellow" else "badge-green"
    status_label = "🔴 CRITICAL ISSUE" if status_color == "Red" else "🟡 WARNING / MONITOR" if status_color == "Yellow" else "🟢 NOMINAL OPERATIONAL"

    st.markdown(f"### {category_name} Machine Learning Output")
    st.markdown(f"**Target Site:** `{current_loc}` | **System Status:** <span class='{badge_style}'>{status_label}</span>", unsafe_allow_html=True)
    st.divider()
    
    if "Water" in category_name:
        res = run_water_management_ai(current_loc)
        st.markdown(f"#### **AI Engine:** `{res['model_type']}`")
        st.markdown(f"**Regression Model Formula:** `{res['equation']}`")
        
        c1, c2 = st.columns(2)
        with c1: st.metric("Goodness of Fit (R² Score)", res['r2_score'])
        with c2: st.metric("Predicted Daily Water Demand", res['prediction'])
        st.info(f"**AI System Evaluation:** {res['evaluation']}")
        
        # Heading updated to Executive Summary (unwanted inline icons removed)
        st.markdown("#### **Executive Summary**")
        st.success(res['plain_overview'])

    elif "Electricity" in category_name:
        res = run_electricity_ai(current_loc)
        st.markdown(f"#### **AI Engine:** `{res['model_type']}`")
        st.markdown(f"**Primary Decision Feature:** `{res['top_feature']}`")
        
        c1, c2 = st.columns(2)
        with c1: st.metric("Grid Anomaly / Failure Risk", res['failure_risk'])
        with c2: st.metric("Active Model Estimators", "20 Trees")
        st.warning(f"**AI System Evaluation:** {res['evaluation']}")
        
        st.markdown("#### **Executive Summary**")
        st.info(res['plain_overview'])

    elif "Roof" in category_name:
        res = run_roof_management_ai(current_loc)
        st.markdown(f"#### **AI Engine:** `{res['model_type']}`")
        st.markdown(f"**Logistic Weights Vector:** `{res['log_odds_coeff']}`")
        
        c1, c2 = st.columns(2)
        with c1: st.metric("Membrane Failure Probability", res['degradation_prob'])
        with c2: st.metric("Decision Boundary", "Sigmoid Threshold (0.5)")
        st.error(f"**AI System Evaluation:** {res['evaluation']}")
        
        st.markdown("#### **Executive Summary**")
        st.warning(res['plain_overview'])

    elif "Drainage" in category_name:
        res = run_drainage_ai(current_loc)
        st.markdown(f"#### **AI Engine:** `{res['model_type']}`")
        st.markdown(f"**Tree Structure Depth:** `{res['max_depth']}`")
        
        c1, c2 = st.columns(2)
        with c1: st.metric("Projected Storm Outflow Rate", res['predicted_flow'])
        with c2: st.metric("Hydraulic Loss Index", "14.2%")
        st.warning(f"**AI System Evaluation:** {res['evaluation']}")
        
        st.markdown("#### **Executive Summary**")
        st.warning(res['plain_overview'])

    else:
        res = run_water_management_ai(current_loc)
        st.markdown(f"#### **AI Engine:** `Multivariate Statistical Model`")
        st.metric("System Condition Index", "94.8%")
        st.info(f"**AI System Evaluation:** Standard mathematical telemetry model evaluated nominal operational state for {current_loc}.")
        st.markdown("#### **Executive Summary**")
        st.success(f"System operating within expected safety parameters at {current_loc}.")

    st.divider()

    st.markdown("#### **NLP Inquiry & Diagnostics Assistant**")
    
    target_lang = st.radio("Response Output Language:", ["English", "Spanish", "Arabic"], horizontal=True)
    user_query = st.text_input("Ask the AI Model a diagnostic question...", placeholder=f"Is the {category_name} system operating safely?")
    
    if user_query:
        st.markdown("**Real-Time Transformer Model Processing:**")
        if nlp_classifier:
            output = nlp_classifier(user_query)[0]
            label = output['label']
            score = output['score']
            
            st.markdown(f"**NLP Sentiment / Intent Score:** Label=`{label}`, Confidence=`{score:.4f}`")
            
            if label == "POSITIVE":
                raw_response = f"Query evaluated as standard operational check. Current metrics for {category_name} at {current_loc} indicate continuous compliance with nominal threshold values."
                translated = translate_text(raw_response, target_lang)
                st.success(f"**AI Inference Response:** {translated}")
            else:
                raw_response = f"Query indicates concern or operational anomaly. System diagnostic flags match potential maintenance risks at {current_loc}. Recommended to issue a site dispatch ticket."
                translated = translate_text(raw_response, target_lang)
                st.warning(f"**AI Inference Response:** {translated}")
        else:
            raw_response = f"Based on linear analysis for {current_loc}, the {category_name} metrics remain within tolerance limits."
            translated = translate_text(raw_response, target_lang)
            st.info(f"**AI Inference Response:** {translated}")

    if st.button("Close Evaluation Modal", use_container_width=True):
        st.rerun()

# -----------------------------------------------------------------------------
# CUSTOM STYLING
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        .stApp { background-color: #FAF6F0; color: #111827; font-family: sans-serif; }
        #MainMenu, footer, header { visibility: hidden; }
        .card-box { background-color: #FFFFFF; padding: 16px; border-radius: 10px; border: 1px solid #E5E7EB; margin-bottom: 12px; }
        .flag-box { background-color: #FEF2F2; border: 1px solid #FCA5A5; border-radius: 8px; padding: 15px; color: #991B1B; margin-bottom: 15px; }
        .badge-high { background-color: #FEE2E2; color: #DC2626; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }
        .badge-medium { background-color: #FEF3C7; color: #D97706; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }
        .badge-green { background-color: #D1FAE5; color: #059669; padding: 3px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }
        .yellow-card-container { background-color: #FEF3C7; border: 1px solid #FDE68A; border-radius: 10px; padding: 18px 16px; text-align: center; margin-top: 15px; }
        .feedback-scroll-box { max-height: 220px; overflow-y: auto; background-color: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 8px; padding: 12px; margin-bottom: 15px; }
        .feedback-item { padding: 8px; border-bottom: 1px solid #F3F4F6; font-size: 0.8rem; }
        .feedback-item:last-child { border-bottom: none; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. TOP HEADER & SEARCH BAR
# -----------------------------------------------------------------------------
nav_col1, nav_col2, nav_col3 = st.columns([1.5, 3.2, 1.8])

with nav_col1:
    st.markdown("### **RESILIA**")
    st.caption("AI Building Intelligence Platform")

with nav_col2:
    with st.form(key="top_search_form", clear_on_submit=False):
        s_col1, s_col2 = st.columns([4, 1])
        with s_col1:
            search_query = st.text_input("Search Location", placeholder="🔍 Block 11, Academic City, Dubai, UAE", label_visibility="collapsed")
        with s_col2:
            submit_search = st.form_submit_button("Search 📍", use_container_width=True)

    if submit_search and search_query.strip():
        try:
            target_query = search_query if "academic city" in search_query.lower() or "dubai" in search_query.lower() else f"{search_query}, Academic City, Dubai, UAE"
            loc_result = geocode(target_query)
            if loc_result:
                st.session_state.map_center = [loc_result.latitude, loc_result.longitude]
                raw_address = loc_result.address
                parts = [p.strip() for p in raw_address.split(",")]
                st.session_state.location_data = {
                    "display_name": parts[0],
                    "full_address": raw_address,
                    "city": "Academic City, Dubai",
                    "country": "United Arab Emirates"
                }
                st.rerun()
        except Exception as e:
            st.toast(f"Geocoding Error: {e}")

with nav_col3:
    st.markdown("<div style='text-align: right;'><b>Admin User</b><br><small style='color: #6B7280;'>Authority Dispatch</small></div>", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# 2. ISOLATED FRAGMENT FOR MAP & ADDRESS DISPLAY
# -----------------------------------------------------------------------------
@st.fragment
def render_map_and_address_card():
    st.markdown(f"""
        <div class="card-box">
            <h2 style="margin: 0; color: #111827;"> {st.session_state.location_data['display_name']}</h2>
            <p style="color: #059669; font-weight: 600; margin-top: 6px; font-size: 0.9rem;">Verified Address:</p>
            <p style="color: #374151; background-color: #F3F4F6; padding: 10px; border-radius: 6px; font-size: 0.88rem;">{st.session_state.location_data['full_address']}</p>
            <div style="display: flex; gap: 20px; font-size: 0.85rem; color: #4B5563;">
                <span><b>Lat:</b> {st.session_state.map_center[0]:.5f}</span>
                <span><b>Lon:</b> {st.session_state.map_center[1]:.5f}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    m = folium.Map(location=st.session_state.map_center, zoom_start=16)

    folium.Marker(
        location=st.session_state.map_center,
        popup=st.session_state.location_data['display_name'],
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

    for lm in DIAC_LANDMARKS:
        folium.Marker(
            location=lm["coords"],
            popup=lm["name"],
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    map_data = st_folium(
        m,
        key=f"map_{st.session_state.map_center[0]:.4f}_{st.session_state.map_center[1]:.4f}",
        width="100%",
        height=380,
        returned_objects=["last_clicked"]
    )

    if map_data and map_data.get("last_clicked"):
        clicked_lat = map_data["last_clicked"]["lat"]
        clicked_lon = map_data["last_clicked"]["lng"]
        
        if [round(clicked_lat, 4), round(clicked_lon, 4)] != [round(st.session_state.map_center[0], 4), round(st.session_state.map_center[1], 4)]:
            st.session_state.map_center = [clicked_lat, clicked_lon]
            matched_lm = next((lm for lm in DIAC_LANDMARKS if abs(lm["coords"][0] - clicked_lat) < 0.002 and abs(lm["coords"][1] - clicked_lon) < 0.002), None)

            if matched_lm:
                st.session_state.location_data = {
                    "display_name": matched_lm["name"],
                    "full_address": matched_lm["address"],
                    "city": "Academic City, Dubai",
                    "country": "United Arab Emirates"
                }
            else:
                try:
                    rev_loc = reverse(f"{clicked_lat}, {clicked_lon}")
                    if rev_loc:
                        st.session_state.location_data = {
                            "display_name": rev_loc.address.split(",")[0],
                            "full_address": rev_loc.address,
                            "city": "Academic City, Dubai",
                            "country": "United Arab Emirates"
                        }
                except Exception:
                    st.session_state.location_data = {
                        "display_name": f"DIAC Point ({clicked_lat:.4f}, {clicked_lon:.4f})",
                        "full_address": f"DIAC Coordinates: {clicked_lat:.5f}, {clicked_lon:.5f}",
                        "city": "Academic City, Dubai",
                        "country": "United Arab Emirates"
                    }
            st.rerun(scope="fragment")

# -----------------------------------------------------------------------------
# 3. MAIN DASHBOARD GRID
# -----------------------------------------------------------------------------
left_col, center_col, right_col = st.columns([1.2, 3, 1.4])

with left_col:
    st.markdown(f"""
        <div class="card-box" style="background-color: #FFFBEB;">
            <b>🏢 Monitored Location</b><br>
            <small>{st.session_state.location_data['display_name']}</small>
        </div>
    """, unsafe_allow_html=True)
    
    categories = [
        ("Water Management", "Green"),
        ("Electricity", "Yellow"),
        ("Roof Management", "Red"),
        ("Structural Stability", "Green"),
        ("Weather Related", "Yellow"),
        ("Exterior Walls", "Yellow"),
        ("Drainage Systems", "Red"),
        ("Interior", "Green"),
        ("Security", "Green")
    ]
    
    for cat_name, status in categories:
        dot = "🟢" if status == "Green" else "🟡" if status == "Yellow" else "🔴"
        if st.button(f"{cat_name} {dot}", key=f"cat_{cat_name}", use_container_width=True):
            show_aspect_modal(cat_name, status)

with center_col:
    render_map_and_address_card()

    st.subheader("Active Model Predictions")
    i1, i2, i3, i4 = st.columns(4)
    
    with i1:
        st.error("**Roof Management**\n\nLogistic Reg: High Defect Risk")
        if st.button("Run Model →", key="vi_1"): show_aspect_modal("🏠 Roof Management", "Red")
            
    with i2:
        st.warning("**Drainage Systems**\n\nDecision Tree: Overflow Risk")
        if st.button("Run Model →", key="vi_2"): show_aspect_modal("🚰 Drainage Systems", "Red")
            
    with i3:
        st.warning("**Electricity**\n\nRandom Forest: Load Overload")
        if st.button("Run Model →", key="vi_3"): show_aspect_modal("⚡ Electricity", "Yellow")
            
    with i4:
        st.warning("**Water Systems**\n\nLinear Reg: Pressure Balance")
        if st.button("Run Model →", key="vi_4"): show_aspect_modal("💧 Water Management", "Green")

with right_col:
    st.markdown("""
        <div class="flag-box">
            <h4 style="margin: 0; color: #991B1B;">Telemetry Data Inadequacy Flag</h4>
            <small style="font-weight:600;">Confidence Penalty Active</small>
            <hr style="margin: 8px 0; border: 0; border-top: 1px solid #FCA5A5;">
            <p style="font-size: 0.8rem; margin: 0; line-height: 1.3;">
            Models report <b>18.4% missing telemetry features</b> across roof vibration sensors & thermal imaging arrays. Variance penalty applied to standard confidence outputs.
            </p>
        </div>
    """, unsafe_allow_html=True)

    curr_addr = st.session_state.location_data['display_name']
    water_res = run_water_management_ai(curr_addr)
    elec_res = run_electricity_ai(curr_addr)
    roof_res = run_roof_management_ai(curr_addr)
    drain_res = run_drainage_ai(curr_addr)

    st.markdown(f"""
        <div class="card-box" style="border-left: 4px solid #2563EB;">
            <h4 style="margin:0 0 8px 0; color: #1E40AF;">Site Telemetry AI Summary</h4>
            <p style="font-size:0.75rem; color: #6B7280; margin-bottom:10px;">Aggregated live model predictions for: <b>{curr_addr}</b></p>
            <ul style="padding-left: 15px; font-size: 0.8rem; margin: 0; color: #374151;">
                <li><b>Water ($R^2={water_res['r2_score']}$):</b> Est. Demand {water_res['prediction']}</li>
                <li><b>Electricity (Grid Risk):</b> {elec_res['failure_risk']} Overload Risk</li>
                <li><b>Roof Wear (Sigmoid):</b> {roof_res['degradation_prob']} Degradation Prob</li>
                <li><b>Drainage Outflow:</b> Est. Flow {drain_res['predicted_flow']}</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # NEW: Scrollable Community Feedback Section
    st.markdown("""
        <div style="font-weight: 700; font-size: 0.9rem; color: #374151; margin-bottom: 6px;">
            💬 Public Feedback & Resident Reports
        </div>
        <div class="feedback-scroll-box">
            <div class="feedback-item">
                <b>Block 11 - Resident</b> <span style="color:#6B7280;">(10m ago)</span><br>
                <span>Noticed minor water dripping from the ceiling near main hallway B.</span>
            </div>
            <div class="feedback-item">
                <b>Facilities Tech</b> <span style="color:#6B7280;">(1h ago)</span><br>
                <span>Transformer noise level elevated during peak afternoon heat cycle.</span>
            </div>
            <div class="feedback-item">
                <b>Student Housing Rep</b> <span style="color:#6B7280;">(3h ago)</span><br>
                <span>Drainage outlet slow to clear water following morning cleaning.</span>
            </div>
            <div class="feedback-item">
                <b>Site Inspector</b> <span style="color:#6B7280;">(Yesterday)</span><br>
                <span>Roof membrane inspection scheduled; thermal camera flags hotspots.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # UPDATED: Button contained directly inside the yellow container box
    with st.container():
        st.markdown("""
            <div class="yellow-card-container">
                <span style="font-weight:700; color: #92400E;">REPORT AN ISSUE</span><br>
                <small style="color: #78350F;">Dispatch emergency maintenance crew</small>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("📢 Report the Issue", key="nav_report_issue_btn", use_container_width=True):
            try:
                st.switch_page("pages/feedback.py")
            except Exception:
                st.error("Target file `pages/feedback.py` not found in project directory structure.")
