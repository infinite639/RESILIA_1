import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="RESILIA",
    page_icon="🛡️",
    layout="centered"
)

# -----------------------------------------------------------------------------
# ANNOTATION 1: SESSION STATE INITIALIZATION FOR LIVE FEEDBACK SYNC
# Stores feedback entries shared across pages/feedback.py and homepage.py
# -----------------------------------------------------------------------------
if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = [
        {
            "user": "Resident",
            "date": "Aug 22, 2026",
            "text": "Water leaking from ceiling during heavy rain near main entrance.",
            "priority": "High Priority",
            "building": "Building A17",
            "issue_type": "Water Management"
        },
        {
            "user": "Faculty Member",
            "date": "Aug 20, 2026",
            "text": "Drainage backup observed in lower basement parking garage.",
            "priority": "Medium Priority",
            "building": "Building B04",
            "issue_type": "Drainage Systems"
        },
        {
            "user": "Student Delegate",
            "date": "Aug 19, 2026",
            "text": "Elevator door sensor glitch on the 3rd floor wing B.",
            "priority": "Medium Priority",
            "building": "Building C02",
            "issue_type": "Interior"
        },
        {
            "user": "Property Manager",
            "date": "Aug 15, 2026",
            "text": "Exterior wall tile hairline cracks along north wall.",
            "priority": "Low Priority",
            "building": "Building A17",
            "issue_type": "Exterior Walls"
        }
    ]

# Function to encode image to base64 for HTML embedding
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Convert logo image to base64 string
try:
    logo_base64 = get_image_base64("image_1.png")
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="logo-img">'
except FileNotFoundError:
    logo_html = '<div class="logo-placeholder" style="font-size: 4rem;">🛡️</div>'

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #FAF6F0;
            color: #1A1A1A;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 2rem;
            text-align: center;
            width: 100%;
        }

        .brand-header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 24px;
            width: 100%;
        }

        .logo-img {
            width: 90px;
            height: auto;
            display: block;
        }

        .brand-title {
            font-size: 4rem;
            font-weight: 800;
            letter-spacing: 2px;
            color: #111827;
            margin: 0;
            line-height: 1;
        }

        .divider {
            width: 50px;
            height: 3px;
            background-color: #FF6F61;
            margin: 0 auto 28px auto;
            border-radius: 2px;
        }

        .subtitle {
            font-size: 1.25rem;
            color: #2D3748;
            font-weight: 400;
            margin-bottom: 30px;
            line-height: 1.5;
            text-align: center;
        }

        /* Standard Navigation Button Styles */
        div.stButton > button {
            width: 100%;
            height: 52px;
            border-radius: 8px;
            font-size: 1.05rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }

        div.row-widget.stButton:nth-child(1) > button {
            background-color: #bf3e32 !important;
            color: white !important;
            border: none !important;
        }

        div.row-widget.stButton:nth-child(1) > button:hover {
            background-color: #E05547 !important;
            box-shadow: 0 4px 12px rgba(255, 111, 97, 0.35);
        }

        div.row-widget.stButton:nth-child(2) > button {
            background-color: transparent !important;
            color: #bf3e32 !important;
            border: 2px solid #FF6F61 !important;
        }

        div.row-widget.stButton:nth-child(2) > button:hover {
            background-color: rgba(255, 111, 97, 0.08) !important;
        }

        /* -------------------------------------------------------------------------
           ANNOTATION 2: FIXED HEIGHT SCROLLABLE CONTAINER FOR FEEDBACK CARDS
           Restricts height to 280px and adds a vertical scrollbar.
           ------------------------------------------------------------------------- */
        .scroll-box {
            max-height: 280px;
            overflow-y: scroll;
            padding-right: 10px;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            background-color: #FAF6F0;
            padding: 12px;
        }

        .scroll-box::-webkit-scrollbar {
            width: 7px;
        }

        .scroll-box::-webkit-scrollbar-thumb {
            background-color: #CBD5E1;
            border-radius: 4px;
        }

        .feedback-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 10px;
            padding: 14px;
            margin-bottom: 10px;
            text-align: left;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }

        .badge-high {
            background-color: #FEE2E2;
            color: #991B1B;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 700;
        }

        .badge-medium {
            background-color: #FEF3C7;
            color: #92400E;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 700;
        }

        /* -------------------------------------------------------------------------
           ANNOTATION 3: YELLOW BOX OVERRIDE FOR REPORT ISSUE BUTTON
           ------------------------------------------------------------------------- */
        div.stButton > button[key="yellow_report_btn"] {
            background-color: #F59E0B !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            height: 48px !important;
        }

        div.stButton > button[key="yellow_report_btn"]:hover {
            background-color: #D97706 !important;
            box-shadow: 0 4px 10px rgba(245, 158, 11, 0.3) !important;
        }
    </style>
""", unsafe_allow_html=True)

# Main Header & Subtitle Section
st.markdown(f"""
    <div class="main-container">
        <div class="brand-header">
            {logo_html}
            <h1 class="brand-title">RESILIA</h1>
        </div>
        <div class="divider"></div>
        <p class="subtitle">*An AI powered building maintenance<br>and resilience system.</p>
    </div>
""", unsafe_allow_html=True)

# Action Buttons Grid
col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 2])

with col2:
    if st.button("🏢 Maintenance", key="maint_btn"):
        try:
            st.switch_page("pages/maintenance.py")
        except Exception:
            st.switch_page("maintenance.py")

with col4:
    if st.button("💬 Feedback", key="feed_btn"):
        try:
            st.switch_page("pages/feedback.py")
        except Exception:
            st.switch_page("feedback.py")

st.write("")

# -----------------------------------------------------------------------------
# ANNOTATION 4: YELLOW CATEGORY BOX CONTAINING "REPORT THE ISSUE" BUTTON
# -----------------------------------------------------------------------------
y_box_col1, y_box_col2 = st.columns([3, 1.3])

with y_box_col1:
    st.markdown("""
        <div style="background-color: #FEF3C7; border: 1.5px solid #FCD34D; border-radius: 12px; padding: 14px 18px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.6rem;">⚠️</span>
                <div>
                    <strong style="color: #92400E; font-size: 1.05rem;">Need to Report a Hazard?</strong><br>
                    <span style="color: #78350F; font-size: 0.88rem;">Submit infrastructural issues directly to emergency management.</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with y_box_col2:
    if st.button("📢 Report the Issue", key="yellow_report_btn", use_container_width=True):
        try:
            st.switch_page("pages/feedback.py")
        except Exception:
            st.switch_page("feedback.py")

# -----------------------------------------------------------------------------
# ANNOTATION 5: SCROLLABLE FEEDBACK SECTION (COMPILED HTML BLOCK)
# Prevents page extension by containing all feedback items inside an inline scroll container.
# -----------------------------------------------------------------------------
st.markdown("<h3 style='text-align: center; font-weight: 700; color: #111827; margin-top: 30px; margin-bottom: 12px;'>📢 Community Feedback Stream</h3>", unsafe_allow_html=True)

if not st.session_state.feedback_list:
    st.info("No feedback records submitted yet.")
else:
    # Build complete HTML string for the scrollbox to avoid auto-closing tags
    feedback_html = '<div class="scroll-box">'
    
    for item in st.session_state.feedback_list:
        priority_label = item.get("priority", "Low Priority")
        badge_class = "badge-high" if ("High" in priority_label or "Critical" in priority_label) else "badge-medium"
        
        feedback_html += f"""
            <div class="feedback-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="color: #111827; font-size: 0.95rem;">{item['user']}</strong>
                    <span style="font-size: 0.8rem; color: #6B7280;">{item['date']}</span>
                </div>
                <p style="font-size: 0.88rem; color: #374151; margin: 8px 0; line-height: 1.4;">
                    {item['text']}
                </p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.8rem; color: #6B7280;">📍 <b>{item.get('building', 'General')}</b> — {item.get('issue_type', 'General')}</span>
                    <span class="{badge_class}">{priority_label}</span>
                </div>
            </div>
        """
        
    feedback_html += '</div>'
    
    # Render entire scroll box in one single call
    st.markdown(feedback_html, unsafe_allow_html=True)
