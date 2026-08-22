import streamlit as st

st.set_page_config(page_title="RESILIA - Contacts Directory", page_icon="📞", layout="wide")

# Custom CSS for UI styling
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background-color: #FAF6F0;
            color: #111827;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        /* Hide standard Streamlit header and footer */
        #MainMenu, footer, header { visibility: hidden; }

        /* Card Container Styling */
        .contact-card {
            background-color: #FFFFFF;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .contact-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
        }

        .contact-icon {
            width: 42px;
            height: 42px;
            background-color: #EFF6FF;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
        }

        .contact-title {
            font-weight: 700;
            font-size: 1.05rem;
            color: #1F2937;
            margin: 0;
        }

        .contact-dept {
            font-size: 0.85rem;
            color: #6B7280;
            margin: 0;
        }

        .contact-person {
            font-size: 0.9rem;
            font-weight: 600;
            color: #374151;
            margin-top: 10px;
            margin-bottom: 2px;
        }

        .contact-phone {
            font-size: 0.88rem;
            color: #4B5563;
            margin-bottom: 15px;
        }

        /* Custom Soft Buttons */
        div.stButton > button {
            border-radius: 8px !important;
            font-weight: 600 !important;
        }

        /* Top Yellow Alert Box */
        .info-box {
            background-color: #FFFBEB;
            border: 1px solid #FDE68A;
            border-radius: 10px;
            padding: 14px 20px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        /* Top Red Emergency Alert Box */
        .emergency-box {
            background-color: #FEF2F2;
            border: 1px solid #FCA5A5;
            border-radius: 10px;
            padding: 14px 20px;
            color: #991B1B;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. TOP NAVIGATION BAR
# -----------------------------------------------------------------------------
nav_col1, nav_col2, nav_col3 = st.columns([1.5, 3, 1.8])

with nav_col1:
    if st.button("🛡️ RESILIA", key="brand_home"):
        try:
            st.switch_page("pages/maintenance.py")
        except Exception:
            st.switch_page("maintenance.py")
    st.caption("Building Intelligence for Safer Communities")

with nav_col2:
    search_input = st.text_input(
        "Search",
        placeholder="🔍 Search address or building...",
        label_visibility="collapsed"
    )

with nav_col3:
    c_help, c_notif, c_user = st.columns([1, 1.2, 1.8])
    with c_help:
        if st.button("❓ Help"):
            st.info("Support Center")
            
    with c_notif:
        if st.button("🔔 Notifications (3)"):
            try:
                st.switch_page("pages/notifications.py")
            except Exception:
                st.switch_page("notifications.py")
                
    with c_user:
        st.markdown("<div style='text-align: right;'><b>Admin User</b><br><small style='color: #6B7280;'>Authority</small></div>", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# 2. PAGE HEADER & ALERT BADGES
# -----------------------------------------------------------------------------
hdr_col1, hdr_col2, hdr_col3 = st.columns([2.5, 1.5, 2])

with hdr_col1:
    st.title("Contacts Directory")
    st.caption("Connect with the right authority for each building system")

with hdr_col2:
    st.markdown("""
        <div class="emergency-box">
            <b>📞 Emergency Contacts</b><br>
            <small>24/7 Support Service</small>
        </div>
    """, unsafe_allow_html=True)

with hdr_col3:
    st.markdown("""
        <div class="info-box">
            <span>ℹ️</span>
            <div>
                <b>Need Assistance?</b><br>
                <small style="color: #6B7280;">Choose a category to find the right contact person.</small>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 3. CONTACTS GRID DATA (3x3 Layout)
# -----------------------------------------------------------------------------
contacts_data = [
    {
        "icon": "💧",
        "title": "Water Management",
        "dept": "Dubai Municipality HQ",
        "address": "Al Wasl Rd, Dubai, UAE",
        "person": "Eng. Ahmed Al Mansoori",
        "phone": "+971 4 123 4567"
    },
    {
        "icon": "⚡",
        "title": "Electricity",
        "dept": "DEWA Headquarters",
        "address": "Al Ittihad Rd, Dubai, UAE",
        "person": "Eng. Fatima Al Zaabi",
        "phone": "+971 4 234 5678"
    },
    {
        "icon": "🏠",
        "title": "Roof Management",
        "dept": "Dubai Building Dept.",
        "address": "Business Bay, Dubai, UAE",
        "person": "Eng. Omar Hassan",
        "phone": "+971 4 345 6789"
    },
    {
        "icon": "🏗️",
        "title": "Structural Stability",
        "dept": "Trakhees - Structural Dept.",
        "address": "Port Saeed, Dubai, UAE",
        "person": "Eng. Salma Tariq",
        "phone": "+971 4 456 7890"
    },
    {
        "icon": "🌧️",
        "title": "Weather Related",
        "dept": "National Center of Meteorology",
        "address": "Al Barsha, Dubai, UAE",
        "person": "Dr. Khalid Al Nuaimi",
        "phone": "+971 4 567 8901"
    },
    {
        "icon": "🧱",
        "title": "Exterior Walls",
        "dept": "Dubai Municipality - Buildings",
        "address": "Al Wasl Rd, Dubai, UAE",
        "person": "Eng. Mariam Farid",
        "phone": "+971 4 678 9012"
    },
    {
        "icon": "🚰",
        "title": "Drainage Systems",
        "dept": "Dubai Municipality - Sewage Dept.",
        "address": "Umm Ramool, Dubai, UAE",
        "person": "Eng. Yousuf Ibrahim",
        "phone": "+971 4 789 0123"
    },
    {
        "icon": "🚪",
        "title": "Interior",
        "dept": "Dubai Municipality - Interior Dept.",
        "address": "Al Barsha, Dubai, UAE",
        "person": "Eng. Noor Al Hammadi",
        "phone": "+971 4 890 1234"
    },
    {
        "icon": "🛡️",
        "title": "Security",
        "dept": "Dubai Police - Community Safety",
        "address": "Al Kifaf, Dubai, UAE",
        "person": "Lt. Ahmed Bin Rashid",
        "phone": "+971 4 901 2345"
    }
]

# Helper function to render a card box
def render_contact_card(data, idx):
    st.markdown(f"""
        <div class="contact-card">
            <div class="contact-header">
                <div class="contact-icon">{data['icon']}</div>
                <div>
                    <p class="contact-title">{data['title']}</p>
                    <p class="contact-dept">{data['dept']}<br>{data['address']}</p>
                </div>
            </div>
            <p class="contact-person">{data['person']}</p>
            <p class="contact-phone">{data['phone']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    btn_c1, btn_c2 = st.columns([1.5, 1])
    with btn_c1:
        if st.button("👁️ More Help", key=f"help_{idx}", use_container_width=True):
            st.info(f"Detailed routing guide for {data['title']} authorities.")
    with btn_c2:
        if st.button("📞 Call", key="call_{idx}", use_container_width=True):
            st.success(f"Dialing {data['phone']}...")

# Render Grid Rows (3 Columns each)
for i in range(0, len(contacts_data), 3):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if i < len(contacts_data):
            render_contact_card(contacts_data[i], i)
            
    with col2:
        if i + 1 < len(contacts_data):
            render_contact_card(contacts_data[i+1], i+1)
            
    with col3:
        if i + 2 < len(contacts_data):
            render_contact_card(contacts_data[i+2], i+2)
            
    st.write("")

# Footer
st.divider()
st.caption("© 2026 RESILIA. All rights reserved. | About Us | How It Works | Privacy Policy | Terms of Use | Data Sources | Contact Us | License & Compliance")
