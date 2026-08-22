import streamlit as st
from datetime import datetime

st.set_page_config(page_title="RESILIA - Notifications", page_icon="🔔", layout="wide")

# -----------------------------------------------------------------------------
# 1. INITIALIZE SESSION STATE DATA
# -----------------------------------------------------------------------------
if "notifications" not in st.session_state:
    st.session_state.notifications = [
        {
            "id": 1,
            "title": "High Priority Issue Detected",
            "type": "ALERT",
            "message": "Structural crack detected on Building A-102. Immediate inspection is recommended.",
            "building": "Building A-102",
            "category": "Structural Stability",
            "time": "10:30 AM",
            "day": "Today",
            "is_read": False,
            "icon": "⚠️",
            "bg_color": "#FEE2E2",
            "details": "A structural displacement of >3.2mm was detected on the north-facing exterior wall via visual telemetry. Inspection team dispatch recommended."
        },
        {
            "id": 2,
            "title": "Maintenance Completed",
            "type": "UPDATE",
            "message": "Drainage cleaning at Building C-205 has been completed successfully.",
            "building": "Building C-205",
            "category": "Drainage",
            "time": "9:15 AM",
            "day": "Today",
            "is_read": True,
            "icon": "✅",
            "bg_color": "#DCFCE7",
            "details": "Sub-surface drainage clearance performed. Standard flow rate restored to 120 L/min. No blockage detected."
        },
        {
            "id": 3,
            "title": "New Feedback Received",
            "type": "UPDATE",
            "message": "A new feedback has been submitted for Building B-301.",
            "building": "Building B-301",
            "category": "Water Management",
            "time": "8:45 AM",
            "day": "Today",
            "is_read": False,
            "icon": "💬",
            "bg_color": "#E0F2FE",
            "details": "Resident logged report regarding water pressure fluctuation on floor 3. Severity tagged as Medium."
        },
        {
            "id": 4,
            "title": "Weather Alert",
            "type": "ALERT",
            "message": "Heavy rainfall expected in your area over the next 48 hours.",
            "building": "Dubai, UAE",
            "category": "Weather",
            "time": "Yesterday, 6:20 PM",
            "day": "Yesterday",
            "is_read": False,
            "icon": "⚠️",
            "bg_color": "#FEF3C7",
            "details": "NCMS regional advisory: Expected precipitation exceeding 45mm. Recommend verifying perimeter drainage and roof seal integrity."
        },
        {
            "id": 5,
            "title": "Building Assessment Completed",
            "type": "UPDATE",
            "message": "Assessment report is ready for Building D-404. View the full analysis.",
            "building": "Building D-404",
            "category": "Assessment",
            "time": "Yesterday, 3:10 PM",
            "day": "Yesterday",
            "is_read": True,
            "icon": "📋",
            "bg_color": "#F3E8FF",
            "details": "Annual Structural Integrity and HVAC Diagnostics report synthesized. Overall building score: 91/100."
        },
        {
            "id": 6,
            "title": "System Update",
            "type": "SYSTEM",
            "message": "RESILIA system was updated to improve detection accuracy.",
            "building": "System Core",
            "category": "System",
            "time": "Yesterday, 11:45 AM",
            "day": "Yesterday",
            "is_read": False,
            "icon": "⚙️",
            "bg_color": "#F1F5F9",
            "details": "v2.4.1 Model Deployment: False positive rate reduced by 14% on exterior surface crack classification models."
        }
    ]

if "active_filter" not in st.session_state:
    st.session_state.active_filter = "All"

ALL_CATEGORIES = [
    "Water Management", "Electricity", "Roof", "Structural Stability",
    "Weather", "Exterior Walls", "Drainage", "Interior", "Security"
]

if "selected_categories" not in st.session_state:
    st.session_state.selected_categories = ALL_CATEGORIES.copy()

# -----------------------------------------------------------------------------
# 2. POP-UP DIALOG (NOTIFICATION DETAILS)
# -----------------------------------------------------------------------------
@st.dialog("Notification Diagnostics")
def show_notification_dialog(notification):
    st.markdown(f"### {notification['icon']} {notification['title']}")
    st.caption(f"**Timestamp:** {notification['time']} | **Category:** {notification['category']}")
    st.divider()
    st.markdown(f"**Location/Target:** `{notification['building']}`")
    st.markdown(f"**Summary:** {notification['message']}")
    
    st.info(f"**Diagnostic Payload:**\n\n{notification['details']}")
    
    c1, c2 = st.columns([1, 1])
    with c1:
        if st.button("Mark as Read" if not notification['is_read'] else "Mark as Unread", use_container_width=True):
            notification['is_read'] = not notification['is_read']
            st.rerun()
    with c2:
        if st.button("Close Modal", use_container_width=True):
            st.rerun()

# -----------------------------------------------------------------------------
# 3. GLOBAL CSS STYLING & UNIFIED COLOR SCHEMES
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #FAF6F0;
            color: #1E293B;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        #MainMenu, footer, header { visibility: hidden; }

        .notif-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 12px;
            transition: all 0.2s ease-in-out;
        }
        .notif-card:hover {
            border-color: #CBD5E1;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        }

        .unread-dot {
            height: 8px;
            width: 8px;
            background-color: #DC2626;
            border-radius: 50%;
            display: inline-block;
        }

        .sidebar-card {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
        }

        /* -------------------------------------------------------------------------
           1. UNIFORM COLOR FOR SUB-CATEGORIES (TABS & SIDEBAR SUBCATEGORY BUTTONS)
           All filters (All, Unread, Alerts, Updates, System) use a matching slate tone.
           ------------------------------------------------------------------------- */
        div.stButton > button {
            border-radius: 6px !important;
            background-color: #F1F5F9 !important;
            color: #334155 !important;
            border: 1px solid #CBD5E1 !important;
            font-weight: 600 !important;
            transition: all 0.2s ease;
        }
        div.stButton > button:hover {
            background-color: #E2E8F0 !important;
            color: #0F172A !important;
            border-color: #94A3B8 !important;
        }

        /* -------------------------------------------------------------------------
           2. UNIFORM COLOR FOR CATEGORY CHECKBOXES
           Applies a consistent dark slate theme to all multi-select categories.
           ------------------------------------------------------------------------- */
        div[data-testid="stCheckbox"] label {
            color: #334155 !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
        }

        /* -------------------------------------------------------------------------
           3. UNIFORM COLOR FOR ALL BOTTOM CONTACT AUTHORITY CARDS & BUTTONS
           Every contact action button is styled uniformly in a soft amber accent.
           ------------------------------------------------------------------------- */
        .contact-box-unified {
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 14px;
            margin-bottom: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            text-align: center;
        }

        .btn-unified-contact {
            display: block;
            width: 100%;
            text-align: center;
            background-color: #D97706 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 8px 0 !important;
            font-size: 0.85rem !important;
            font-weight: 700 !important;
            text-decoration: none !important;
            transition: background-color 0.2s ease, box-shadow 0.2s ease;
        }
        .btn-unified-contact:hover {
            background-color: #B45309 !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 10px rgba(180, 83, 9, 0.25);
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. TOP NAVIGATION HEADER
# -----------------------------------------------------------------------------
header_cols = st.columns([1.5, 1, 1, 1.2, 1, 0.5])

with header_cols[0]:
    st.markdown("### 🛡️ **RESILIA**")

with header_cols[1]:
    if st.button("🛠️ Maintenance", use_container_width=True):
        try:
            st.switch_page("app.py")
        except Exception:
            st.switch_page("main.py")

with header_cols[2]:
    if st.button("💬 Feedback", use_container_width=True):
        try:
            st.switch_page("pages/feedback.py")
        except Exception:
            st.switch_page("feedback.py")

with header_cols[3]:
    st.markdown("<div style='border-bottom: 3px solid #DC2626; text-align: center; padding-bottom: 4px;'><b>🔔 Notifications</b></div>", unsafe_allow_html=True)

with header_cols[4]:
    if st.button("ℹ️ About Model", use_container_width=True):
        st.info("RESILIA Structural Diagnostics v2.4")

with header_cols[5]:
    st.markdown("👤")

st.divider()

# -----------------------------------------------------------------------------
# 5. DYNAMIC STATS COMPUTATION
# -----------------------------------------------------------------------------
total_cnt = len(st.session_state.notifications)
unread_cnt = sum(1 for n in st.session_state.notifications if not n["is_read"])
alerts_cnt = sum(1 for n in st.session_state.notifications if n["type"] == "ALERT")
updates_cnt = sum(1 for n in st.session_state.notifications if n["type"] == "UPDATE")
system_cnt = sum(1 for n in st.session_state.notifications if n["type"] == "SYSTEM")

# -----------------------------------------------------------------------------
# 6. PAGE TITLE & MARK ALL AS READ
# -----------------------------------------------------------------------------
title_col1, title_col2 = st.columns([3, 1])

with title_col1:
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="background-color: #FEE2E2; padding: 12px; border-radius: 50%; font-size: 1.5rem;">🔔</div>
            <div>
                <h1 style="margin: 0; font-size: 1.8rem; font-weight: 700;">Notifications</h1>
                <p style="margin: 0; color: #64748B; font-size: 0.9rem;">Stay updated on building assessments, feedback, and maintenance actions.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with title_col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✓ Mark all as read", use_container_width=True):
        for n in st.session_state.notifications:
            n["is_read"] = True
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. MAIN CONTENT & SIDEBAR GRID
# -----------------------------------------------------------------------------
main_col, side_col = st.columns([2.8, 1.2])

with main_col:
    # UNIFORM SUB-CATEGORY FILTER TABS
    t_all, t_unread, t_alerts, t_updates, t_system = st.columns(5)
    
    with t_all:
        if st.button(f"All ({total_cnt})", key="tab_all", use_container_width=True):
            st.session_state.active_filter = "All"
            st.rerun()
    with t_unread:
        if st.button(f"Unread ({unread_cnt})", key="tab_unread", use_container_width=True):
            st.session_state.active_filter = "Unread"
            st.rerun()
    with t_alerts:
        if st.button(f"Alerts ({alerts_cnt})", key="tab_alerts", use_container_width=True):
            st.session_state.active_filter = "Alerts"
            st.rerun()
    with t_updates:
        if st.button(f"Updates ({updates_cnt})", key="tab_updates", use_container_width=True):
            st.session_state.active_filter = "Updates"
            st.rerun()
    with t_system:
        if st.button(f"System ({system_cnt})", key="tab_system", use_container_width=True):
            st.session_state.active_filter = "System"
            st.rerun()

    st.markdown(f"<small style='color: #64748B;'>Active Filter: <b>{st.session_state.active_filter}</b></small>", unsafe_allow_html=True)
    st.divider()

    filtered_list = []
    for n in st.session_state.notifications:
        if st.session_state.active_filter == "Unread" and n["is_read"]:
            continue
        elif st.session_state.active_filter == "Alerts" and n["type"] != "ALERT":
            continue
        elif st.session_state.active_filter == "Updates" and n["type"] != "UPDATE":
            continue
        elif st.session_state.active_filter == "System" and n["type"] != "SYSTEM":
            continue
        
        if n["category"] in st.session_state.selected_categories or n["type"] == "SYSTEM" or n["category"] == "Assessment":
            filtered_list.append(n)

    days = ["Today", "Yesterday"]
    
    for day in days:
        day_items = [item for item in filtered_list if item["day"] == day]
        if day_items:
            st.markdown(f"#### **{day}**")
            for item in day_items:
                unread_indicator = '<span class="unread-dot"></span>' if not item["is_read"] else ''
                
                card_col1, card_col2 = st.columns([4.5, 0.5])
                
                with card_col1:
                    st.markdown(f"""
                        <div class="notif-card">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                                <div style="display: flex; gap: 12px; align-items: center;">
                                    <div style="background-color: {item['bg_color']}; padding: 10px; border-radius: 50%; font-size: 1.2rem;">
                                        {item['icon']}
                                    </div>
                                    <div>
                                        <b>{item['title']}</b>
                                        <p style="margin: 4px 0; font-size: 0.88rem; color: #475569;">{item['message']}</p>
                                        <small style="color: #94A3B8;">🏢 {item['building']} &nbsp;•&nbsp; Tag: {item['category']}</small>
                                    </div>
                                </div>
                                <div style="text-align: right;">
                                    <small style="color: #94A3B8;">{item['time']}</small> {unread_indicator}
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                
                with card_col2:
                    if st.button("➔", key=f"btn_open_{item['id']}"):
                        show_notification_dialog(item)

    if not filtered_list:
        st.info("No notifications match the selected tab and category filters.")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Load More 🠗", use_container_width=True):
        st.toast("All notifications loaded.", icon="ℹ️")

# -----------------------------------------------------------------------------
# 8. RIGHT SIDEBAR (SUMMARY & UNIFORM FILTERS)
# -----------------------------------------------------------------------------
with side_col:
    st.markdown("""
        <div class="sidebar-card">
            <h4 style="margin-top:0;">Notification Summary</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 1.2rem;">🔔</span> <b>{unread_cnt}</b><br>
                    <small style="color: #64748B;">Unread</small>
                </div>
                <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 1.2rem;">⚠️</span> <b>{alerts_cnt}</b><br>
                    <small style="color: #64748B;">Alerts</small>
                </div>
                <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 1.2rem;">🔄</span> <b>{updates_cnt}</b><br>
                    <small style="color: #64748B;">Updates</small>
                </div>
                <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 1.2rem;">⚙️</span> <b>{system_cnt}</b><br>
                    <small style="color: #64748B;">System</small>
                </div>
            </div>
        </div>
    """.format(unread_cnt=unread_cnt, alerts_cnt=alerts_cnt, updates_cnt=updates_cnt, system_cnt=system_cnt), unsafe_allow_html=True)

    # UNIFORM SUB-CATEGORY SIDEBAR BUTTONS
    st.markdown("#### **Filter Notifications**")
    if st.button(f"🔔 All Notifications ({total_cnt})", use_container_width=True):
        st.session_state.active_filter = "All"
        st.rerun()
    if st.button(f"⚠️ Alerts ({alerts_cnt})", use_container_width=True):
        st.session_state.active_filter = "Alerts"
        st.rerun()
    if st.button(f"💬 Updates ({updates_cnt})", use_container_width=True):
        st.session_state.active_filter = "Updates"
        st.rerun()
    if st.button(f"⚙️ System ({system_cnt})", use_container_width=True):
        st.session_state.active_filter = "System"
        st.rerun()

    st.divider()

    # UNIFORM CATEGORY CHECKBOXES
    st.markdown("#### **Filter by Category**")
    selected_cats = []
    for cat in ALL_CATEGORIES:
        is_checked = cat in st.session_state.selected_categories
        if st.checkbox(cat, value=is_checked, key=f"chk_{cat}"):
            selected_cats.append(cat)
            
    if selected_cats != st.session_state.selected_categories:
        st.session_state.selected_categories = selected_cats
        st.rerun()

# -----------------------------------------------------------------------------
# 9. BOTTOM CONTACTS BAR (UNIFORM COLOR PALETTE)
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
    st.markdown("""
        <div class="contact-box-unified">
            <b style="color: #1E293B;">Property Management</b><br>
            <small style="color: #64748B;">+971 4 123 4567</small>
            <br><br>
            <a href="javascript:void(0)" class="btn-unified-contact">Contact</a>
        </div>
    """, unsafe_allow_html=True)

with cnt2:
    st.markdown("""
        <div class="contact-box-unified">
            <b style="color: #1E293B;">Water / Drainage</b><br>
            <small style="color: #64748B;">Dubai Municipality — 800 900</small>
            <br><br>
            <a href="javascript:void(0)" class="btn-unified-contact">Contact</a>
        </div>
    """, unsafe_allow_html=True)

with cnt3:
    st.markdown("""
        <div class="contact-box-unified">
            <b style="color: #1E293B;">Electricity</b><br>
            <small style="color: #64748B;">DEWA — 991</small>
            <br><br>
            <a href="javascript:void(0)" class="btn-unified-contact">Contact</a>
        </div>
    """, unsafe_allow_html=True)

with cnt4:
    st.markdown("""
        <div class="contact-box-unified">
            <b style="color: #1E293B;">Structural / Safety</b><br>
            <small style="color: #64748B;">Dubai Civil Defense — 997</small>
            <br><br>
            <a href="javascript:void(0)" class="btn-unified-contact">Contact</a>
        </div>
    """, unsafe_allow_html=True)

with cnt5:
    st.markdown("""
        <div class="contact-box-unified">
            <b style="color: #1E293B;">Emergency</b><br>
            <small style="color: #64748B;">Emergency Services — 999</small>
            <br><br>
            <a href="javascript:void(0)" class="btn-unified-contact">Call Now</a>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 RESILIA. All rights reserved. | About Us | How It Works | Privacy Policy | Terms of Use | Data Sources | Contact Us")
