import streamlit as st

st.set_page_config(page_title="RESILIA - Contacts Directory", page_icon="image_1.png", layout="wide")

# -----------------------------------------------------------------------------
# 1. POP-UP MODALS (MORE HELP & CALLING)
# -----------------------------------------------------------------------------
@st.dialog("Officer Profile & Authority Details")
def show_more_help_modal(data):
    st.markdown(f"### {data['icon']} {data['title']}")
    st.caption(f"Assigned Authority: **{data['dept']}**")
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Contact Person:**\n{data['person']}")
        st.write(f"**Direct Extension:**\n{data['phone']}")
    with col2:
        st.write(f"**Office Location:**\n{data['loc']}")
        st.write(f"**Operating Hours:**\n{data['hours']}")

    st.info(f"**Emergency Response Window:** {data['response_time']}\n\nFor official escalations, submit a formal request via the main RESILIA dashboard.")
    
    if st.button("Close Directory Card", use_container_width=True):
        st.rerun()

@st.dialog("Establishing Connection...")
def show_calling_modal(data):
    st.markdown(f"<h3 style='text-align: center; color: #16A34A;'>📞 Calling {data['person']}...</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.1rem;'><b>{data['phone']}</b><br><small style='color: #6B7280;'>{data['dept']} — {data['loc']}</small></p>", unsafe_allow_html=True)
    st.divider()
    
    st.warning("Call session initialized via Secure VoIP Gateway. Please ensure microphone permissions are granted.")
    
    if st.button("End Call", use_container_width=True):
        st.rerun()

# -----------------------------------------------------------------------------
# 2. GLOBAL CSS STYLING (FIXED CARD SIZING & ENCLOSED BUTTONS)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #FAF8F5;
            color: #111827;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        #MainMenu, footer, header { visibility: hidden; }

        /* Unified Fixed-Size Card Container */
        .card-container {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
            min-height: 290px;
            max-height: 290px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .card-header-flex {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
        }

        .card-icon-title {
            display: flex;
            align-items: flex-start;
            gap: 12px;
        }

        .card-icon-bg {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
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
            line-height: 1.3;
        }

        .person-name {
            font-size: 0.88rem;
            font-weight: 600;
            color: #374151;
            margin: 12px 0 2px 0;
        }

        .phone-number {
            font-size: 0.88rem;
            color: #4B5563;
            margin: 0 0 14px 0;
        }

        /* Top Banner Badges */
        .emergency-banner {
            background-color: #FEF2F2;
            border: 1px solid #FEE2E2;
            border-radius: 12px;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .assistance-banner {
            background-color: #FFFBEB;
            border: 1px solid #FEF3C7;
            border-radius: 12px;
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        /* Button Customizations */
        div.stButton > button[key^="contact_btn_"] {
            background-color: #FDE68A !important;
            color: #111827 !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
            height: 38px !important;
        }

        div.stButton > button[key^="help_btn_"] {
            background-color: #F3F4F6 !important; /* Light Grayish Shade */
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
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. TOP NAVIGATION BAR (WITH SEARCH SYNC & NOTIFICATIONS PAGE SWITCH)
# -----------------------------------------------------------------------------
nav_col1, nav_col2, nav_col3 = st.columns([1.5, 3, 1.8])

with nav_col1:
    if st.button("RESILIA", key="nav_home_brand"):
        try:
            st.switch_page("pages/maintenance.py")
        except Exception:
            st.switch_page("maintenance.py")
    st.caption("Building Intelligence for Safer Communities")

with nav_col2:
    search_query = st.text_input(
        "Search",
        placeholder="🔍 Search address or building...",
        label_visibility="collapsed"
    )
    if search_query:
        st.toast(f"Searching building database for: '{search_query}'...")

with nav_col3:
    c_help, c_notif, c_user = st.columns([1, 1.3, 1.8])
    with c_help:
        if st.button("❓ Help", key="nav_help"):
            st.info("RESILIA Contacts Assistance Center")
            
    with c_notif:
        # Notifications Button redirects to notifications.py page
        if st.button("🔔 Notifications (3)", key="nav_notif"):
            try:
                st.switch_page("pages/notifications.py")
            except Exception:
                st.switch_page("notifications.py")
                
    with c_user:
        st.markdown("<div style='text-align: right;'><b>Admin User</b><br><small style='color: #6B7280;'>Authority</small></div>", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# 4. PAGE HEADER & ALERT BADGES
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
# 5. LOCATION-SPECIFIC CONTACT DATA (WITH RELEVANT ICONS)
# -----------------------------------------------------------------------------
contacts_data = [
    {
        "icon": "💧", "bg": "#EFF6FF", "title": "Water Management",
        "dept": "Dubai Municipality HQ", "loc": "Al Wasl Rd, Dubai, UAE",
        "person": "Eng. Ahmed Al Mansoori", "phone": "+971 4 123 4567",
        "hours": "07:30 AM - 03:30 PM", "response_time": "< 30 mins"
    },
    {
        "icon": "⚡", "bg": "#FEF3C7", "title": "Electricity",
        "dept": "DEWA Headquarters", "loc": "Al Ittihad Rd, Dubai, UAE",
        "person": "Eng. Fatima Al Zaabi", "phone": "+971 4 234 5678",
        "hours": "24/7 Emergency Response", "response_time": "Immediate"
    },
    {
        "icon": "🏠", "bg": "#EFF6FF", "title": "Roof Management",
        "dept": "Dubai Building Dept.", "loc": "Business Bay, Dubai, UAE",
        "person": "Eng. Omar Hassan", "phone": "+971 4 345 6789",
        "hours": "08:00 AM - 04:00 PM", "response_time": "< 2 hours"
    },
    {
        "icon": "🏗️", "bg": "#EFF6FF", "title": "Structural Stability",
        "dept": "Trakhees - Structural Dept.", "loc": "Port Saeed, Dubai, UAE",
        "person": "Eng. Salma Tariq", "phone": "+971 4 456 7890",
        "hours": "07:30 AM - 02:30 PM", "response_time": "< 1 hour"
    },
    {
        "icon": "🌩️", "bg": "#F3F4F6", "title": "Weather Related",
        "dept": "National Center of Meteorology", "loc": "Al Barsha, Dubai, UAE",
        "person": "Dr. Khalid Al Nuaimi", "phone": "+971 4 567 8901",
        "hours": "24/7 Weather Monitoring", "response_time": "Real-time"
    },
    {
        "icon": "🧱", "bg": "#FFEDD5", "title": "Exterior Walls",
        "dept": "Dubai Municipality - Buildings", "loc": "Deira, Dubai, UAE",
        "person": "Eng. Mariam Farid", "phone": "+971 4 678 9012",
        "hours": "08:00 AM - 03:00 PM", "response_time": "< 4 hours"
    },
    {
        "icon": "🛠️", "bg": "#FEE2E2", "title": "Drainage Systems",
        "dept": "Dubai Municipality - Sewage Dept.", "loc": "Umm Ramool, Dubai, UAE",
        "person": "Eng. Yousuf Ibrahim", "phone": "+971 4 789 0123",
        "hours": "24/7 Rapid Response", "response_time": "< 20 mins"
    },
    {
        "icon": "🚪", "bg": "#DCFCE7", "title": "Interior",
        "dept": "Dubai Municipality - Interior Dept.", "loc": "Al Jaddaf, Dubai, UAE",
        "person": "Eng. Noor Al Hammadi", "phone": "+971 4 890 1234",
        "hours": "08:00 AM - 04:00 PM", "response_time": "< 3 hours"
    },
    {
        "icon": "🛡️", "bg": "#F3F4F6", "title": "Security",
        "dept": "Dubai Police - Community Safety", "loc": "Al Kifaf, Dubai, UAE",
        "person": "Lt. Ahmed Bin Rashid", "phone": "+971 4 901 2345",
        "hours": "24/7 Control Room", "response_time": "Immediate"
    }
]

# -----------------------------------------------------------------------------
# 6. RENDER CARDS GRID (3 COLUMNS X 3 ROWS)
# -----------------------------------------------------------------------------
for row in range(0, 9, 3):
    cols = st.columns(3)
    for col_idx in range(3):
        data_idx = row + col_idx
        item = contacts_data[data_idx]
        
        with cols[col_idx]:
            # Outer Card Container (Fixed size wrapping text AND buttons inside)
            with st.container():
                st.markdown(f"""
                    <div class="card-container">
                        <div>
                            <div class="card-header-flex">
                                <div class="card-icon-title">
                                    <div class="card-icon-bg" style="background-color: {item['bg']};">{item['icon']}</div>
                                    <div>
                                        <h4 class="card-title-text">{item['title']}</h4>
                                        <p class="card-subtitle-text">{item['dept']}<br>{item['loc']}</p>
                                    </div>
                                </div>
                                <span style="color: #9CA3AF; font-size: 0.85rem;">⌵</span>
                            </div>
                            <p class="person-name">{item['person']}</p>
                            <p class="phone-number">{item['phone']}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Enclosed Action Buttons aligned cleanly inside the lower box area
                b_col1, b_col2, b_col3 = st.columns([1.8, 2.2, 1.2])
                with b_col1:
                    if st.button("Contact", key=f"contact_btn_{data_idx}", use_container_width=True):
                        st.toast(f"Contact request initiated for {item['person']}.")
                with b_col2:
                    # Light grayish shade button triggering More Help Pop-up Modal
                    if st.button(" More Help", key=f"help_btn_{data_idx}", use_container_width=True):
                        show_more_help_modal(item)
                with b_col3:
                    # Dial button triggering Calling Pop-up Modal
                    if st.button("📞", key=f"call_btn_{data_idx}", use_container_width=True):
                        show_calling_modal(item)
                        
    st.write("")

# -----------------------------------------------------------------------------
# 7. FOOTER
# -----------------------------------------------------------------------------
st.markdown("<hr style='margin-top: 30px; border-color: #E5E7EB;'>", unsafe_allow_html=True)
ft_col1, ft_col2 = st.columns([4, 1])
with ft_col1:
    st.caption("© 2026 RESILIA. All rights reserved.  |  About Us  |  How It Works  |  Privacy Policy  |  Terms of Use  |  Data Sources  |  Contact Us")
with ft_col2:
    st.markdown("<div style='text-align: right;'><small style='color: #6B7280;'>License & Compliance</small></div>", unsafe_allow_html=True)
