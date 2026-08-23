import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.set_page_config(page_title="RESILIA - Maintenance Dashboard", page_icon="🛡️", layout="wide")

# -----------------------------------------------------------------------------
# GPS & GEOCODING INITIALIZATION
# -----------------------------------------------------------------------------
geolocator = Nominatim(user_agent="resilia_interactive_diac_app_v5")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
reverse = RateLimiter(geolocator.reverse, min_delay_seconds=1)

# Central Coordinates for Dubai International Academic City (DIAC)
DIAC_CENTER_LAT = 25.1212
DIAC_CENTER_LON = 55.3881

if "map_center" not in st.session_state:
    st.session_state.map_center = [DIAC_CENTER_LAT, DIAC_CENTER_LON]

if "location_data" not in st.session_state:
    st.session_state.location_data = {
        "display_name": "DIAC Main Campus Hub",
        "full_address": "Dubai International Academic City, Academic City, Dubai, United Arab Emirates",
        "city": "Dubai",
        "country": "United Arab Emirates"
    }

# Authentic landmarks strictly confined to Dubai International Academic City (DIAC)
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

# Handle page navigation query parameters
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
# CUSTOM STYLING
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

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border: none !important;
            box-shadow: none !important;
            background-color: #FAF6F0 !important;
        }

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
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. TOP NAVIGATION HEADER WITH CLEAN FUNCTIONAL SEARCH
# -----------------------------------------------------------------------------
nav_col1, nav_col2, nav_col3 = st.columns([1.5, 3.2, 1.8])

with nav_col1:
    st.markdown("### 🛡️ **RESILIA**")
    st.caption("Building Intelligence for Safer Communities")

with nav_col2:
    with st.form(key="top_search_form", clear_on_submit=False):
        s_col1, s_col2 = st.columns([4, 1])
        with s_col1:
            search_query = st.text_input(
                "Search Location",
                placeholder="🔍 e.g., Block 11, Academic City, Dubai, UAE",
                label_visibility="collapsed"
            )
        with s_col2:
            submit_search = st.form_submit_button("Search 📍", use_container_width=True)

    if submit_search and search_query.strip():
        try:
            target_query = search_query if "academic city" in search_query.lower() or "dubai" in search_query.lower() else f"{search_query}, Academic City, Dubai, UAE"
            loc_result = geocode(target_query)
            if loc_result:
                st.session_state.map_center = [loc_result.latitude, loc_result.longitude]
                raw_address = loc_result.address
                address_parts = [p.strip() for p in raw_address.split(",")]
                
                st.session_state.location_data = {
                    "display_name": address_parts[0],
                    "full_address": raw_address,
                    "city": "Academic City, Dubai",
                    "country": "United Arab Emirates"
                }
                st.rerun()
            else:
                st.toast("⚠️ Location not found. Try entering a specific DIAC block or address.")
        except Exception as e:
            st.toast(f"Geocoding Error: {e}")

with nav_col3:
    c_help, c_notif, c_user = st.columns([1, 1.2, 1.8])
    with c_help:
        if st.button("❓ Help"):
            st.info("Help & Support documentation module.")
            
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
# 2. ISOLATED FRAGMENT FOR MAP & ADDRESS DISPLAY (PREVENTS WHITEOUT)
# -----------------------------------------------------------------------------
@st.fragment
def render_map_and_address_card():
    # REAL-TIME LOCATION ADDRESS DISPLAY BOX
    st.markdown(f"""
        <div class="card-box">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <h2 style="margin: 0; color: #111827;">📍 {st.session_state.location_data['display_name']}</h2>
                    <p style="color: #059669; font-weight: 600; margin-top: 6px; font-size: 0.9rem;">
                        Verified Physical Address:
                    </p>
                    <p style="color: #374151; background-color: #F3F4F6; padding: 10px; border-radius: 6px; font-size: 0.88rem; margin-top: 2px;">
                        {st.session_state.location_data['full_address']}
                    </p>
                </div>
            </div>
            <div style="display: flex; gap: 20px; font-size: 0.85rem; color: #4B5563; margin-top: 10px;">
                <span><b>Latitude:</b> {st.session_state.map_center[0]:.5f}</span>
                <span><b>Longitude:</b> {st.session_state.map_center[1]:.5f}</span>
                <span><b>Zone:</b> DIAC, Dubai</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    v1, v2, v3, _ = st.columns([1, 1, 1, 3])
    with v1: st.button("Aerial View", use_container_width=True)
    with v2: st.button("Map View", use_container_width=True)
    with v3: st.button("Street View", use_container_width=True)

    # MAP GENERATION CENTERING DIAC WITH Surrounding DIAC Markers
    m = folium.Map(
        location=st.session_state.map_center,
        zoom_start=16,
        control_scale=True
    )

    # Active selected point marker
    folium.Marker(
        location=st.session_state.map_center,
        popup=st.session_state.location_data['display_name'],
        tooltip="📍 Active Selected Point",
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

    # Add nearby DIAC red landmark pins
    for lm in DIAC_LANDMARKS:
        folium.Marker(
            location=lm["coords"],
            popup=lm["name"],
            tooltip=f"📍 Red Marker: {lm['name']} (Click to jump)",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    # Render interactive map component
    map_data = st_folium(
        m,
        key=f"diac_map_{st.session_state.map_center[0]:.4f}_{st.session_state.map_center[1]:.4f}",
        width="100%",
        height=390,
        returned_objects=["last_clicked"]
    )

    # MAP CLICK & MARKER SELECTION HANDLING
    if map_data and map_data.get("last_clicked"):
        clicked_lat = map_data["last_clicked"]["lat"]
        clicked_lon = map_data["last_clicked"]["lng"]
        
        # Check if coordinates changed significantly
        if [round(clicked_lat, 4), round(clicked_lon, 4)] != [round(st.session_state.map_center[0], 4), round(st.session_state.map_center[1], 4)]:
            st.session_state.map_center = [clicked_lat, clicked_lon]
            
            # Check if clicked coordinate matches a DIAC preset pin
            matched_lm = None
            for lm in DIAC_LANDMARKS:
                if abs(lm["coords"][0] - clicked_lat) < 0.002 and abs(lm["coords"][1] - clicked_lon) < 0.002:
                    matched_lm = lm
                    break

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
                        raw_addr = rev_loc.address
                        parts = [p.strip() for p in raw_addr.split(",")]
                        st.session_state.location_data = {
                            "display_name": parts[0] if parts else "DIAC Location Pin",
                            "full_address": raw_addr,
                            "city": "Academic City, Dubai",
                            "country": "United Arab Emirates"
                        }
                except Exception:
                    st.session_state.location_data = {
                        "display_name": f"DIAC Point ({clicked_lat:.4f}, {clicked_lon:.4f})",
                        "full_address": f"DIAC Coordinates: {clicked_lat:.5f}, {clicked_lon:.5f}, Dubai, UAE",
                        "city": "Academic City, Dubai",
                        "country": "United Arab Emirates"
                    }
            st.rerun(scope="fragment")

# -----------------------------------------------------------------------------
# 3. MAIN DASHBOARD GRID
# -----------------------------------------------------------------------------
left_col, center_col, right_col = st.columns([1.2, 3, 1.4])

# --- LEFT SIDEBAR ---
with left_col:
    st.markdown(f"""
        <div class="card-box" style="background-color: #FFFBEB; border-color: #FCD34D;">
            <b>🏢 Monitored Location</b><br>
            <small style="color: #4B5563;">{st.session_state.location_data['display_name']}</small>
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

# --- CENTER CANVAS ---
with center_col:
    render_map_and_address_card()

    st.subheader("AI Diagnostics & Insights")
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

# --- RIGHT SIDEBAR ---
with right_col:
    st.markdown("""
        <div class="flag-box">
            <h4 style="margin: 0;">🚨 3 Issues Flagged</h4>
            <small>Requires immediate attention</small>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="card-box">
            <h4>AI Telemetry Summary</h4>
            <p style="color: #6B7280; font-size: 0.85rem;">Based on aerial analysis, local sensor records, weather telemetry, and community reports.</p>
            <div style="background-color: #F8FAFC; border: 1px dashed #CBD5E1; padding: 15px; border-radius: 6px; text-align: center; color: #64748B; font-size: 0.85rem; margin-bottom: 10px;">
                [ AI Analytics Active for Selected Coordinates ]
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("View Full Analysis >", use_container_width=True):
        st.info("Full AI analysis view placeholder.")

    st.subheader("Recent Feedback")
    
    if "feedback_list" not in st.session_state:
        st.session_state.feedback_list = [
            {
                "user": "Resident",
                "date": "Aug 2026",
                "text": "Water leaking from ceiling during heavy rain.",
                "priority": "High Priority"
            },
            {
                "user": "Anonymous",
                "date": "Aug 2026",
                "text": "Water accumulation near basement entrance.",
                "priority": "Medium Priority"
            },
            {
                "user": "Faculty Member",
                "date": "Aug 2026",
                "text": "Flickering lights in the 2nd floor hall.",
                "priority": "Medium Priority"
            }
        ]

    with st.container(height=240):
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

    st.markdown("""
        <div class="yellow-card-container">
            <span class="yellow-card-title">📝 REPORT AN ISSUE</span>
            <span class="yellow-card-subtitle">Log maintenance hazards directly to dispatch</span>
            <a href="?navigate=feedback" target="_self" class="yellow-card-button">📢 Report the Issue</a>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. BOTTOM CONTACTS BAR
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
