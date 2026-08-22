import streamlit as st

st.set_page_config(page_title="RESILIA - Maintenance Dashboard", page_icon="🛡️", layout="wide")

# Query parameter handling for the Report Issue button click
if st.query_params.get("navigate") == "feedback":
    st.query_params.clear()
    try:
        st.switch_page("pages/feedback.py")
    except Exception:
        st.switch_page("feedback.py")

# -----------------------------------------------------------------------------
# AI MODAL POP-UP
# -----------------------------------------------------------------------------
@st.dialog("Category Details & Diagnostics")
def show_aspect_modal(category_name, status_color):
    st.markdown(f"### {category_name}")
    st.caption(f"Status Indicator: **{status_color}**")
    st.divider()
    
    st.info("🤖 **Backend AI Model Integration Space**\n\nDiagnostic telemetry, model outputs, and detailed sensory metrics for this aspect will be rendered here.")
    
    if st.button("Close Modal"):
        st.rerun()

# -----------------------------------------------------------------------------
# CUSTOM CSS FOR DASHBOARD UI
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #FAF6F0;
            color: #111827;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        #MainMenu, footer, header { visibility: hidden; }

        .card-box {
            background-color: #FFFFFF;
            padding: 16px;
            border-radius: 10px;
            border: 1px solid #E5E7EB;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
            margin-bottom: 12px;
        }

        .map-placeholder {
            width: 100%;
            height: 380px;
            background-color: #E2E8F0;
            border: 2px dashed #94A3B8;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #475569;
            font-weight: 600;
            margin-bottom: 15px;
        }

        .flag-box {
            background-color: #FEF2F2;
            border: 1px solid #FCA5A5;
            border-radius: 8px;
            padding: 15px;
            color: #991B1B;
            margin-bottom: 15px;
        }

        .badge-high {
            background-color: #FEE2E2;
            color: #DC2626;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        .badge-medium {
            background-color: #FEF3C7;
            color: #D97706;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        /* -------------------------------------------------------------------------
           ANNOTATION 1: BORDERLESS FEEDBACK CONTAINER
           Hides Streamlit's default container outline while matching background color.
           ------------------------------------------------------------------------- */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border: none !important;
            box-shadow: none !important;
            background-color: #FAF6F0 !important;
        }

        /* -------------------------------------------------------------------------
           ANNOTATION 2: FULLY EXPANDED YELLOW CARD WRAPPER
           Extends heightwise to completely enclose title, subtext, and action button.
           ------------------------------------------------------------------------- */
        .yellow-card-container {
            background-color: #FEF3C7;
            border: 1px solid #FDE68A;
            border-radius: 10px;
            padding: 18px 16px;
            text-align: center;
            margin-top: 15px;
            width: 100%;
            box-sizing: border-box;
        }

        .yellow-card-title {
            color: #92400E;
            font-size: 0.95rem;
            font-weight: 700;
            display: block;
            margin-bottom: 4px;
        }

        .yellow-card-subtitle {
            color: #78350F;
            font-size: 0.82rem;
            display: block;
            margin-bottom: 14px;
        }

        /* -------------------------------------------------------------------------
           ANNOTATION 3: CLEAN EMBEDDED ACTION BUTTON (NO DARK BORDERS)
           Strips out gray/black borders, focus rings, and outlines entirely.
           ------------------------------------------------------------------------- */
        .yellow-card-button {
            display: block;
            width: 100%;
            background-color: #D97706;
            color: #FFFFFF !important;
            text-decoration: none !important;
            font-weight: 700;
            font-size: 0.88rem;
            padding: 10px 0;
            border-radius: 6px;
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
            transition: background-color 0.2s ease, box-shadow 0.2s ease;
            box-sizing: border-box;
        }

        .yellow-card-button:hover {
            background-color: #B45309;
            color: #FFFFFF !important;
            box-shadow: 0 4px 10px rgba(180, 83, 9, 0.25);
            text-decoration: none !important;
        }

        .yellow-card-button:focus,
        .yellow-card-button:active {
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. TOP NAVIGATION HEADER
# -----------------------------------------------------------------------------
nav_col1, nav_col2, nav_col3 = st.columns([1.5, 3, 1.8])

with nav_col1:
    st.markdown("### 🛡️ **RESILIA**")
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
            st.info("Help & Support documentation module.")
            
    with c_notif:
        if st.button("🔔 Notifications (3)"):
            try:
                st.switch_page("pages/feedback.py")
            except Exception:
                st.switch_page("feedback.py")
                
    with c_user:
        st.markdown("<div style='text-align: right;'><b>Admin User</b><br><small style='color: #6B7280;'>Authority</small></div>", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# 2. MAIN DASHBOARD GRID
# -----------------------------------------------------------------------------
left_col, center_col, right_col = st.columns([1.2, 3, 1.4])

# --- LEFT SIDEBAR: CATEGORIES & OVERVIEW ---
with left_col:
    st.markdown("""
        <div class="card-box" style="background-color: #FFFBEB; border-color: #FCD34D;">
            <b>🏢 Building Overview</b><br>
            <small style="color: #4B5563;">Building A17</small>
        </div>
    """, unsafe_allow_html=True)
    
    categories = [
        ("💧 Water Management", "Green"),
        ("⚡ Electricity", "Yellow"),
        ("🏠 Roof Management", "Red"),
        ("🏗️ Structural Stability", "Green"),
        ("🌧️ Weather Related", "Yellow"),
        ("🧱 Exterior Walls", "Yellow"),
        ("🚰 Drainage Systems", "Red"),
        ("🚪 Interior", "Green"),
        ("🔒 Security", "Green")
    ]
    
    for cat_name, status in categories:
        dot = "🟢" if status == "Green" else "🟡" if status == "Yellow" else "🔴"
        if st.button(f"{cat_name} {dot}", key=f"cat_{cat_name}", use_container_width=True):
            show_aspect_modal(cat_name, status)

# --- CENTER CANVAS: BUILDING DETAILS & MAP PLACEHOLDER ---
with center_col:
    st.markdown("""
        <div class="card-box">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h2>Building A17 ⭐</h2>
                <div>
                    <span style="margin-right: 15px;"><b>Building Type:</b> Academic</span>
                    <span style="margin-right: 15px;"><b>Year Built:</b> 2008</span>
                    <span style="margin-right: 15px;"><b>Total Area:</b> 12,450 m²</span>
                    <span><b>Floors:</b> 5</span>
                </div>
            </div>
            <p style="color: #6B7280; margin-top: 5px;">Dubai International Academic City, Dubai, UAE</p>
        </div>
    """, unsafe_allow_html=True)

    v1, v2, v3, _ = st.columns([1, 1, 1, 3])
    with v1: st.button("Aerial View", use_container_width=True)
    with v2: st.button("Map View", use_container_width=True)
    with v3: st.button("Street View", use_container_width=True)

    st.markdown("""
        <div class="map-placeholder">
            [ Map View Area Placeholder — Ready for GPS Map Integration ]
        </div>
    """, unsafe_allow_html=True)

    st.subheader("AI Insights")
    i1, i2, i3, i4 = st.columns(4)
    
    with i1:
        st.error("**Roof Management**\n\nHigh risk of deterioration detected.")
        if st.button("View Details →", key="vi_1"):
            show_aspect_modal("Roof Management", "Red")
            
    with i2:
        st.warning("**Drainage Systems**\n\nStanding water detected in 2 locations.")
        if st.button("View Details →", key="vi_2"):
            show_aspect_modal("Drainage Systems", "Red")
            
    with i3:
        st.warning("**Electricity**\n\n3 recent complaints reported.")
        if st.button("View Details →", key="vi_3"):
            show_aspect_modal("Electricity", "Yellow")
            
    with i4:
        st.warning("**Exterior Walls**\n\nSigns of surface wear detected.")
        if st.button("View Details →", key="vi_4"):
            show_aspect_modal("Exterior Walls", "Yellow")

# --- RIGHT SIDEBAR: FLAGS, AI SUMMARY, FEEDBACK & UNIFIED YELLOW ACTION CARD ---
with right_col:
    st.markdown("""
        <div class="flag-box">
            <h4 style="margin: 0;">🚨 3 Issues Flagged</h4>
            <small>Requires immediate attention</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="card-box">
            <h4>AI Summary</h4>
            <p style="color: #6B7280; font-size: 0.85rem;">Based on aerial analysis, available records, weather data, and community feedback.</p>
            <div style="background-color: #F8FAFC; border: 1px dashed #CBD5E1; padding: 15px; border-radius: 6px; text-align: center; color: #64748B; font-size: 0.85rem; margin-bottom: 10px;">
                [ AI Summary Content Placeholder — To be populated by ML Backend ]
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("View Full Analysis >", use_container_width=True):
        st.info("Full AI analysis view placeholder.")

    # SCROLLABLE FEEDBACK CONTAINER
    st.subheader("Recent Feedback")
    
    if "feedback_list" not in st.session_state:
        st.session_state.feedback_list = [
            {
                "user": "Resident",
                "date": "May 18, 2026",
                "text": "Water leaking from ceiling during heavy rain.",
                "priority": "High Priority"
            },
            {
                "user": "Anonymous",
                "date": "May 16, 2026",
                "text": "Water accumulation near basement entrance.",
                "priority": "Medium Priority"
            },
            {
                "user": "Faculty Member",
                "date": "May 14, 2026",
                "text": "Flickering lights in the 2nd floor hall.",
                "priority": "Medium Priority"
            }
        ]

    with st.container(height=250):
        for fb in st.session_state.feedback_list:
            badge_class = "badge-high" if "High" in fb["priority"] else "badge-medium"
            st.markdown(f"""
                <div class="card-box">
                    <div style="display: flex; justify-content: space-between;">
                        <b>{fb['user']}</b>
                        <small style="color: #9CA3AF;">{fb['date']}</small>
                    </div>
                    <p style="font-size: 0.85rem; margin: 8px 0; color: #374151;">{fb['text']}</p>
                    <span class="{badge_class}">{fb['priority']}</span>
                </div>
            """, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # ANNOTATION 4: SINGLE CONSOLIDATED HTML CARD CONTAINING BUTTON & TEXT
    # Guarantees the yellow background fully encompasses title, subtext, and button.
    # -------------------------------------------------------------------------
    st.markdown("""
        <div class="yellow-card-container">
            <span class="yellow-card-title">📝 REPORT AN ISSUE</span>
            <span class="yellow-card-subtitle">Log maintenance hazards directly to dispatch</span>
            <a href="?navigate=feedback" target="_self" class="yellow-card-button">📢 Report the Issue</a>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. BOTTOM CONTACTS BAR
# -----------------------------------------------------------------------------
st.divider()
st.subheader("Contact the Right Authority")

cnt1, cnt2, cnt3, cnt4, cnt5 = st.columns(5)

def nav_to_contacts():
    try:
        st.switch_page("pages/contacts.py")
    except Exception:
        st.switch_page("contacts.py")

with cnt1:
    st.markdown("<b>Property Management</b><br><small>+971 4 123 4567</small>", unsafe_allow_html=True)
    if st.button("Contact", key="cnt_btn_1"): nav_to_contacts()

with cnt2:
    st.markdown("<b>Water / Drainage</b><br><small>Dubai Municipality — 800 900</small>", unsafe_allow_html=True)
    if st.button("Contact", key="cnt_btn_2"): nav_to_contacts()

with cnt3:
    st.markdown("<b>Electricity</b><br><small>DEWA — 991</small>", unsafe_allow_html=True)
    if st.button("Contact", key="cnt_btn_3"): nav_to_contacts()

with cnt4:
    st.markdown("<b>Structural / Safety</b><br><small>Dubai Civil Defense — 997</small>", unsafe_allow_html=True)
    if st.button("Contact", key="cnt_btn_4"): nav_to_contacts()

with cnt5:
    st.markdown("<b>Emergency</b><br><small>Emergency Services — 999</small>", unsafe_allow_html=True)
    if st.button("Call Now", key="cnt_btn_5"): nav_to_contacts()

st.divider()
st.caption("© 2026 RESILIA. All rights reserved. | About Us | How It Works | Privacy Policy | Terms of Use | Data Sources | Contact Us")
