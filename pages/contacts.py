import streamlit as st

st.set_page_config(page_title="RESILIA - Contacts Directory", page_icon="🛡️", layout="wide")

# Custom CSS matching exact visual proportions, colors, fonts, and inline element placements
st.markdown("""
    <style>
        .stApp {
            background-color: #FAF8F5;
            color: #111827;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        #MainMenu, footer, header { visibility: hidden; }

        /* Navigation Header */
        .nav-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #FFFFFF;
            padding: 12px 30px;
            border-bottom: 1px solid #E5E7EB;
            margin-bottom: 25px;
        }

        .search-box-container {
            display: flex;
            align-items: center;
            background-color: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            width: 480px;
            overflow: hidden;
        }

        .search-box-container input {
            border: none;
            background: transparent;
            padding: 10px 14px;
            width: 100%;
            font-size: 0.9rem;
            outline: none;
        }

        .search-box-btn {
            background-color: #FDE68A;
            border: none;
            padding: 10px 16px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Page Top Banner Badges */
        .emergency-banner {
            background-color: #FEF2F2;
            border: 1px solid #FEE2E2;
            border-radius: 12px;
            padding: 14px 18px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .assistance-banner {
            background-color: #FFFBEB;
            border: 1px solid #FEF3C7;
            border-radius: 12px;
            padding: 14px 18px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        /* Grid Contact Cards */
        .contact-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 20px 22px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
            height: 100%;
        }

        .card-top-row {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            margin-bottom: 16px;
        }

        .card-icon-title {
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }

        .card-icon-bg {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background-color: #EFF6FF;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            flex-shrink: 0;
        }

        .card-title-text {
            font-size: 1.05rem;
            font-weight: 700;
            color: #111827;
            margin: 0 0 2px 0;
        }

        .card-subtitle-text {
            font-size: 0.82rem;
            color: #6B7280;
            margin: 0;
            line-height: 1.35;
        }

        .person-name {
            font-size: 0.88rem;
            font-weight: 600;
            color: #374151;
            margin: 0 0 4px 0;
        }

        .phone-number {
            font-size: 0.88rem;
            color: #4B5563;
            margin: 0;
        }

        /* Streamlit native button overrides for absolute layout matching */
        div.stButton > button[key^="contact_btn_"] {
            background-color: #FDE68A !important;
            color: #111827 !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
            padding: 6px 16px !important;
            height: 38px !important;
        }

        div.stButton > button[key^="help_btn_"] {
            background-color: #FFFFFF !important;
            color: #374151 !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
            font-size: 0.85rem !important;
            height: 38px !important;
        }

        div.stButton > button[key^="call_btn_"] {
            background-color: #FFFFFF !important;
            color: #16A34A !important;
            border: 1px solid #DCFCE7 !important;
            border-radius: 8px !important;
            height: 38px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TOP NAVIGATION BAR
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="nav-container">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.6rem;">🛡️</span>
            <div>
                <span style="font-weight: 800; font-size: 1.3rem; letter-spacing: 0.5px;">RESILIA</span>
                <span style="font-size: 0.75rem; color: #6B7280; display: block; margin-top: -3px;">Building Intelligence for Safer Communities</span>
            </div>
        </div>
        <div class="search-box-container">
            <input type="text" placeholder="Search address or building..." />
            <button class="search-box-btn">🔍</button>
        </div>
        <div style="display: flex; align-items: center; gap: 24px;">
            <span style="font-size: 0.9rem; color: #374151; cursor: pointer;">❓ Help</span>
            <div style="position: relative; cursor: pointer;">
                <span style="font-size: 1.1rem;">🔔</span>
                <span style="position: absolute; top: -5px; right: -8px; background-color: #DC2626; color: white; border-radius: 50%; padding: 1px 5px; font-size: 0.65rem; font-weight: 700;">3</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="text-align: right;">
                    <span style="font-weight: 700; font-size: 0.88rem; display: block; color: #111827;">Admin User</span>
                    <span style="font-size: 0.75rem; color: #6B7280; display: block;">Authority</span>
                </div>
                <span style="font-size: 0.8rem; color: #6B7280;">▼</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PAGE HEADER & ASSISTANCE BADGES
# -----------------------------------------------------------------------------
h_col1, h_col2, h_col3 = st.columns([2.5, 1.3, 1.8])

with h_col1:
    st.markdown("<h2 style='margin: 0; font-weight: 800; font-size: 1.8rem;'>Contacts Directory</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size: 0.95rem; margin-top: 4px;'>Connect with the right authority for each building system</p>", unsafe_allow_html=True)

with h_col2:
    st.markdown("""
        <div class="emergency-banner">
            <span style="font-size: 1.4rem;">📞</span>
            <div>
                <span style="font-weight: 700; color: #DC2626; font-size: 0.88rem; display: block;">Emergency Contacts</span>
                <span style="font-size: 0.78rem; color: #6B7280;">24/7 Support</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with h_col3:
    st.markdown("""
        <div class="assistance-banner">
            <span style="font-size: 1.3rem;">ℹ️</span>
            <div>
                <span style="font-weight: 700; color: #111827; font-size: 0.88rem; display: block;">Need Assistance?</span>
                <span style="font-size: 0.78rem; color: #6B7280;">Choose a category to find the right contact person.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# CONTACTS DATA STRUCTURE (9 CARDS)
# -----------------------------------------------------------------------------
contacts = [
    {
        "icon": "💧", "bg": "#EFF6FF", "title": "Water Management",
        "dept": "Dubai Municipality HQ", "loc": "Al Wasl Rd, Dubai, UAE",
        "person": "Eng. Ahmed Al Mansoori", "phone": "+971 4 123 4567"
    },
    {
        "icon": "⚡", "bg": "#FEF3C7", "title": "Electricity",
        "dept": "DEWA Headquarters", "loc": "Al Ittihad Rd, Dubai, UAE",
        "person": "Eng. Fatima Al Zaabi", "phone": "+971 4 234 5678"
    },
    {
        "icon": "🏠", "bg": "#EFF6FF", "title": "Roof Management",
        "dept": "Dubai Building Dept.", "loc": "Business Bay, Dubai, UAE",
        "person": "Eng. Omar Hassan", "phone": "+971 4 345 6789"
    },
    {
        "icon": "🏗️", "bg": "#EFF6FF", "title": "Structural Stability",
        "dept": "Trakhees - Structural Dept.", "loc": "Port Saeed, Dubai, UAE",
        "person": "Eng. Salma Tariq", "phone": "+971 4 456 7890"
    },
    {
        "icon": "🌧️", "bg": "#F3F4F6", "title": "Weather Related",
        "dept": "National Center of Meteorology", "loc": "Al Barsha, Dubai, UAE",
        "person": "Dr. Khalid Al Nuaimi", "phone": "+971 4 567 8901"
    },
    {
        "icon": "🧱", "bg": "#FFEDD5", "title": "Exterior Walls",
        "dept": "Dubai Municipality - Buildings", "loc": "Al Wasl Rd, Dubai, UAE",
        "person": "Eng. Mariam Farid", "phone": "+971 4 678 9012"
    },
    {
        "icon": "🚰", "bg": "#FEE2E2", "title": "Drainage Systems",
        "dept": "Dubai Municipality - Sewage Dept.", "loc": "Umm Ramool, Dubai, UAE",
        "person": "Eng. Yousuf Ibrahim", "phone": "+971 4 789 0123"
    },
    {
        "icon": "🚪", "bg": "#DCFCE7", "title": "Interior",
        "dept": "Dubai Municipality - Interior Dept.", "loc": "Al Barsha, Dubai, UAE",
        "person": "Eng. Noor Al Hammadi", "phone": "+971 4 890 1234"
    },
    {
        "icon": "🛡️", "bg": "#F3F4F6", "title": "Security",
        "dept": "Dubai Police - Community Safety", "loc": "Al Kifaf, Dubai, UAE",
        "person": "Lt. Ahmed Bin Rashid", "phone": "+971 4 901 2345"
    }
]

# Function to render each card cleanly with dual-layer layout (HTML for Info, Streamlit Widgets for Actions)
def render_card(c, index):
    st.markdown(f"""
        <div class="contact-card">
            <div class="card-top-row">
                <div class="card-icon-title">
                    <div class="card-icon-bg" style="background-color: {c['bg']};">{c['icon']}</div>
                    <div>
                        <h4 class="card-title-text">{c['title']}</h4>
                        <p class="card-subtitle-text">{c['dept']}<br>{c['loc']}</p>
                    </div>
                </div>
                <span style="color: #9CA3AF; font-size: 0.8rem; cursor: pointer;">⌵</span>
            </div>
            <p class="person-name">{c['person']}</p>
            <p class="phone-number">{c['phone']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Action buttons positioned underneath card details to match layout structure
    btn_col1, btn_col2, btn_col3 = st.columns([2, 2.5, 1.2])
    with btn_col1:
        st.button("Contact", key=f"contact_btn_{index}")
    with btn_col2:
        st.button("👁️ More Help", key=f"help_btn_{index}", use_container_width=True)
    with btn_col3:
        st.button("📞", key=f"call_btn_{index}", use_container_width=True)

# -----------------------------------------------------------------------------
# 3x3 GRID DISPLAY
# -----------------------------------------------------------------------------
for row in range(0, 9, 3):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_card(contacts[row], row)
    with col2:
        render_card(contacts[row + 1], row + 1)
    with col3:
        render_card(contacts[row + 2], row + 2)
        
    st.write("")

# Footer
st.markdown("<hr style='margin-top: 40px; border-color: #E5E7EB;'>", unsafe_allow_html=True)
ft_col1, ft_col2 = st.columns([4, 1])
with ft_col1:
    st.caption("© 2026 RESILIA. All rights reserved.  |  About Us  |  How It Works  |  Privacy Policy  |  Terms of Use  |  Data Sources  |  Contact Us")
with ft_col2:
    st.markdown("<div style='text-align: right;'><small style='color: #6B7280;'>License & Compliance</small></div>", unsafe_allow_html=True)
