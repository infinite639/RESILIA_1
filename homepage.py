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
# Initializes the shared 'feedback_list' in st.session_state if it doesn't exist yet.
# When a user submits a form on pages/feedback.py, it prepends to this exact list.
# -----------------------------------------------------------------------------
if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = [
        {
            "user": "Resident",
            "date": "Aug 22, 2026",
            "text": "Water leaking from ceiling during heavy rain near entrance.",
            "priority": "High Priority",
            "building": "Building A17",
            "issue_type": "Water Management"
        },
        {
            "user": "Faculty Member",
            "date": "Aug 20, 2026",
            "text": "Drainage backup observed in lower basement parking.",
            "priority": "Medium Priority",
            "building": "Building B04",
            "issue_type": "Drainage Systems"
        }
    ]

# Function to encode image to base64 for HTML embedding
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Convert logo image to base64 string using your GitHub filename
try:
    logo_base64 = get_image_base64("image_1.png")
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="logo-img">'
except FileNotFoundError:
    # Fallback shield if the file name isn't found
    logo_html = '<div class="logo-placeholder" style="font-size: 4rem;">🛡️</div>'

# Custom CSS for styling
st.markdown("""
    <style>
        /* Base page background */
        .stApp {
            background-color: #FAF6F0;
            color: #1A1A1A;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Hide standard Streamlit chrome */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Main container layout - Center everything vertically & horizontally */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 3rem;
            text-align: center;
            width: 100%;
        }

        /* Header layout (Logo + Brand Name centered together) */
        .brand-header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-bottom: 24px;
            width: 100%;
        }

        /* Increased Logo Size */
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

        /* Red Divider Line */
        .divider {
            width: 50px;
            height: 3px;
            background-color: #FF6F61;
            margin: 0 auto 28px auto;
            border-radius: 2px;
        }

        /* Subtitle Text */
        .subtitle {
            font-size: 1.25rem;
            color: #2D3748;
            font-weight: 400;
            margin-bottom: 40px;
            line-height: 1.5;
            text-align: center;
        }

        /* Custom Button Styles */
        div.stButton > button {
            width: 100%;
            height: 52px;
            border-radius: 8px;
            font-size: 1.05rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }

        /* Maintenance Button (Coral Red Solid) */
        div.row-widget.stButton:nth-child(1) > button {
            background-color: #bf3e32 !important;
            color: white !important;
            border: none !important;
        }

        div.row-widget.stButton:nth-child(1) > button:hover {
            background-color: #E05547 !important;
            box-shadow: 0 4px 12px rgba(255, 111, 97, 0.35);
        }

        /* Feedback Button (Coral Red Outlined) */
        div.row-widget.stButton:nth-child(2) > button {
            background-color: transparent !important;
            color: #bf3e32 !important;
            border: 2px solid #FF6F61 !important;
        }

        div.row-widget.stButton:nth-child(2) > button:hover {
            background-color: rgba(255, 111, 97, 0.08) !important;
        }

        /* ANNOTATION 2: CARD STYLING FOR RECENT FEEDBACK DISPLAY */
        .feedback-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            text-align: left;
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

# Perfectly Centered Action Buttons
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

# -----------------------------------------------------------------------------
# ANNOTATION 3: RECENT FEEDBACK STREAM DISPLAY
# Reads st.session_state.feedback_list dynamically and renders all feedback cards.
# Any form submitted on pages/feedback.py instantly populates at the top here.
# -----------------------------------------------------------------------------
st.write("")
st.write("")
st.markdown("<hr style='border: 0; height: 1px; background: #E5E7EB; margin: 30px 0 20px 0;'>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-weight: 700; color: #111827; margin-bottom: 16px;'>📢 Recent Community Feedback</h3>", unsafe_allow_html=True)

if not st.session_state.feedback_list:
    st.info("No feedback records available yet.")
else:
    for item in st.session_state.feedback_list:
        priority_label = item.get("priority", "Low Priority")
        badge_class = "badge-high" if ("High" in priority_label or "Critical" in priority_label) else "badge-medium"
        
        st.markdown(f"""
            <div class="feedback-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 700; color: #111827; font-size: 0.95rem;">{item['user']}</span>
                    <span style="font-size: 0.8rem; color: #6B7280;">{item['date']}</span>
                </div>
                <p style="font-size: 0.88rem; color: #374151; margin: 8px 0 10px 0; line-height: 1.4;">
                    {item['text']}
                </p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.8rem; color: #6B7280;">📍 <b>{item.get('building', 'General')}</b> — {item.get('issue_type', 'General')}</span>
                    <span class="{badge_class}">{priority_label}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
