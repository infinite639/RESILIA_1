import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="RESILIA",
    page_icon="🛡️",
    layout="centered"
)

# Function to encode image to base64 for seamless HTML embedding
def get_image_base64(path):
    with open(image_1.png, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Convert logo image to base64 string
try:
    logo_base64 = get_image_base64("logo.png")
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="logo-img">'
except Exception:
    # Fallback placeholder icon if image isn't found
    logo_html = '<div class="logo-placeholder">🛡️</div>'

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

        /* Main container styling */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 5rem;
            text-align: center;
        }

        /* Header layout (Logo + Brand Name) */
        .brand-header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
            margin-bottom: 24px;
        }

        .logo-img {
            width: 55px;
            height: auto;
        }

        .brand-title {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: 2px;
            color: #111827;
            margin: 0;
            line-height: 1;
        }

        /* Red Divider Line */
        .divider {
            width: 45px;
            height: 3px;
            background-color: #D32F2F;
            margin: 0 auto 28px auto;
            border-radius: 2px;
        }

        /* Subtitle Text */
        .subtitle {
            font-size: 1.25rem;
            color: #2D3748;
            font-weight: 400;
            margin-bottom: 45px;
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

        /* Maintenance Button (Primary Solid Red) */
        div.row-widget.stButton:nth-child(1) > button {
            background-color: #CE3834 !important;
            color: white !important;
            border: none !important;
        }

        div.row-widget.stButton:nth-child(1) > button:hover {
            background-color: #B52D2A !important;
            box-shadow: 0 4px 12px rgba(206, 56, 52, 0.3);
        }

        /* Feedback Button (Secondary Outlined Red) */
        div.row-widget.stButton:nth-child(2) > button {
            background-color: transparent !important;
            color: #CE3834 !important;
            border: 1.5px solid #CE3834 !important;
        }

        div.row-widget.stButton:nth-child(2) > button:hover {
            background-color: rgba(206, 56, 52, 0.05) !important;
        }
    </style>
""", unsafe_allow_html=style_code if 'style_code' in locals() else "", unsafe_allow_html=True)

# Main Header & Title Section
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

# Centered Action Buttons
col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

with col2:
    if st.button("🏢 Maintenance", key="maint_btn"):
        st.success("Redirecting to Maintenance portal...")

with col4:
    if st.button("💬 Feedback", key="feed_btn"):
        st.info("Redirecting to Feedback form...")
