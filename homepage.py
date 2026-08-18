import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="RESILIA",
    page_icon="🛡️",
    layout="centered"
)

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
        st.success("Redirecting to Maintenance...")
        st.swtich_page("pages/maintenance.py")

with col4:
    if st.button("💬 Feedback", key="feed_btn"):
        st.info("Redirecting to Feedback...")


