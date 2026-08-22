import streamlit as st
from datetime import datetime

# Configure global browser tab title, icon, and wide page layout
st.set_page_config(
    page_title="RESILIA - Give Feedback", 
    page_icon="🛡️", 
    layout="wide"
)

# -----------------------------------------------------------------------------
# 1. SUCCESS POP-UP MODAL (@st.dialog)
# -----------------------------------------------------------------------------
@st.dialog("Feedback Submitted Successfully")
def show_success_modal(summary_data):
    # Modal header icon, title, and description
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <div style="font-size: 3.5rem; color: #16A34A; margin-bottom: 10px;">✅</div>
            <h2 style="color: #111827; font-weight: 800; margin: 0;">Thank You!</h2>
            <p style="color: #4B5563; font-size: 0.95rem; margin-top: 6px;">
                Your feedback has been logged into the RESILIA Central System and synchronized with the Maintenance Dashboard.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Summary list of submitted data
    st.markdown(f"""
        **Submission Summary:**
        * **Building Address:** {summary_data['building']}
        * **Issue Category:** {summary_data['issue_type']}
        * **Severity Level:** {summary_data['priority']}
        * **Logged By:** {summary_data['user']} ({summary_data['contact']})
        * **Timestamp:** {summary_data['date']}
    """)
    
    st.info("🤖 **Next Action:** RESILIA's AI model will evaluate this incident and route notice to local municipal authorities.")
    
    # Return button to navigate back to dashboard
    if st.button("Return to Maintenance Dashboard", use_container_width=True):
        try:
            st.switch_page("pages/homepage.py")
        except Exception:
            st.switch_page("homepage.py")

# -----------------------------------------------------------------------------
# 2. UI STYLING & CUSTOM CSS
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        /* Base page background color and font family */
        .stApp {
            background-color: #FAF8F5;
            color: #111827;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Hide Streamlit default UI components */
        #MainMenu, footer, header { visibility: hidden; }

        /* Card Container Styling */
        .form-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            margin-bottom: 25px;
        }

        /* Circular Step Badge Indicator */
        .step-badge {
            background-color: #CE3834;
            color: #FFFFFF;
            border-radius: 50%;
            width: 26px;
            height: 26px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.85rem;
            margin-right: 10px;
        }

        /* Section Header Container */
        .step-header {
            display: flex;
            align-items: center;
            font-size: 1.15rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 20px;
            margin-top: 10px;
        }

        /* Right Sidebar Component Cards */
        .sidebar-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 20px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }

        /* Red Emergency Banner Card */
        .emergency-help-card {
            background-color: #FEF2F2;
            border: 1px solid #FEE2E2;
            border-radius: 14px;
            padding: 20px;
            color: #991B1B;
        }

        /* Form Buttons Styling */
        div.stButton > button[key="btn_submit_feedback"] {
            background-color: #CE3834 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            font-size: 1rem !important;
            height: 46px !important;
        }

        div.stButton > button[key="btn_reset_form"] {
            background-color: #FFFFFF !important;
            color: #CE3834 !important;
            border: 1px solid #FCA5A5 !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            height: 46px !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. TOP NAVIGATION BAR (EXPANDED BUTTONS & NOTIFICATIONS ROUTE)
# -----------------------------------------------------------------------------
# Grid columns layout for expanded horizontal button widths
nav_cols = st.columns([1.5, 1.2, 1.2, 1.4, 1.2, 0.5])

# Brand button
with nav_cols[0]:
    if st.button("🛡️ RESILIA", key="nav_brand_home", use_container_width=True):
        try:
            st.switch_page("pages/homepage.py")
        except Exception:
            st.switch_page("homepage.py")

# Maintenance link
with nav_cols[1]:
    if st.button("📑 Maintenance", key="nav_maint", use_container_width=True):
        try:
            st.switch_page("pages/homepage.py")
        except Exception:
            st.switch_page("homepage.py")

# Active page display for Feedback
with nav_cols[2]:
    st.markdown(
        "<div style='border-bottom: 3px solid #CE3834; text-align: center; padding-bottom: 6px; font-weight: 700; color: #CE3834; font-size: 0.95rem; margin-top: 4px;'>"
        "💬 Feedback"
        "</div>", 
        unsafe_allow_html=True
    )

# Notifications link routing to pages/notifications.py
with nav_cols[3]:
    if st.button("🔔 Notifications", key="nav_notif", use_container_width=True):
        try:
            st.switch_page("pages/notifications.py")
        except Exception:
            st.switch_page("notifications.py")

# About Model button
with nav_cols[4]:
    if st.button("ℹ️ About Model", key="nav_about", use_container_width=True):
        st.info("RESILIA AI Risk Assessment Model v2.4")

# User profile icon container
with nav_cols[5]:
    st.markdown("<div style='text-align: center; font-size: 1.2rem; padding-top: 4px;'>👤</div>", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# 4. MAIN PAGE HEADER (SINGLE-LINE TITLE & HERO AREA)
# -----------------------------------------------------------------------------
# Ratio configured to keep single-line text formatting without wrapping
hdr_col, img_col = st.columns([4.2, 0.8])

with hdr_col:
    # Single-line title setting whitespace to nowrap
    st.markdown("<h1 style='font-size: 2.3rem; font-weight: 800; margin: 0; white-space: nowrap;'>Give <span style='color: #CE3834;'>Feedback</span></h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='color: #4B5563; font-size: 1.05rem; line-height: 1.6; margin-top: 12px;'>
            Help us improve building maintenance and resilience by sharing the issues you are experiencing. 
            Your feedback enables RESILIA to take the right action, faster.
        </p>
    """, unsafe_allow_html=True)

with img_col:
    # Graphic header icon align
    st.markdown("""
        <div style="text-align: right; padding-top: 10px;">
            <span style="font-size: 3.5rem;">🏢💬</span>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 5. FORM AND SIDEBAR LAYOUT
# -----------------------------------------------------------------------------
left_form_col, right_info_col = st.columns([3.2, 1.8])

with left_form_col:
    with st.container():
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        
        # --- SECTION 1: BUILDING INFORMATION ---
        st.markdown('<div class="step-header"><span class="step-badge">1</span> Building Information</div>', unsafe_allow_html=True)
        
        building_address = st.text_input(
            "Building Address*",
            placeholder="🔍 Search or enter building address (e.g., Building A17, DIAC, Dubai)",
            key="fb_address"
        )
        
        b_col1, b_col2 = st.columns(2)
        with b_col1:
            property_type = st.selectbox(
                "Property Type*",
                ["Select property type", "Academic / Educational", "Residential Apartment", "Commercial Office", "Retail / Facility"],
                key="fb_prop_type"
            )
        with b_col2:
            user_role = st.selectbox(
                "Your Role*",
                ["Select your role", "Resident", "Student", "Faculty / Staff", "Visitor", "Property Manager"],
                key="fb_role"
            )

        st.write("")
        
        # --- SECTION 2: ISSUE DETAILS ---
        st.markdown('<div class="step-header"><span class="step-badge">2</span> Issue Details</div>', unsafe_allow_html=True)
        st.caption("Type of Issue*")
        
        issue_categories = [
            ("💧 Water Management", "Water Management"),
            ("⚡ Electricity", "Electricity"),
            ("🏠 Roof", "Roof Management"),
            ("🏗️ Structural Stability", "Structural Stability"),
            ("🌧️ Weather", "Weather Related"),
            ("🧱 Exterior Walls", "Exterior Walls"),
            ("🚰 Drainage", "Drainage Systems"),
            ("🚪 Interior", "Interior"),
            ("🔒 Security", "Security")
        ]
        
        selected_issue = st.radio(
            "Select Issue Category",
            options=[cat[1] for cat in issue_categories],
            horizontal=True,
            label_visibility="collapsed",
            key="fb_issue_cat"
        )
        
        issue_description = st.text_area(
            "Describe the Issue*",
            placeholder="Please describe the issue in detail...",
            max_chars=1000,
            key="fb_desc"
        )
        
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            first_noticed = st.date_input("When did you first notice this issue?*", key="fb_date")
        with d_col2:
            frequency = st.selectbox(
                "How often does it occur?*",
                ["Select frequency", "One-time occurrence", "Intermittent / Occasional", "Continuous / Daily"],
                key="fb_freq"
            )

        st.caption("Impact / Severity*")
        severity_level = st.radio(
            "Severity Level",
            ["Low", "Medium", "High", "Critical"],
            index=2,
            horizontal=True,
            label_visibility="collapsed",
            key="fb_severity"
        )

        st.caption("Add Photos or Videos (Optional)")
        uploaded_files = st.file_uploader(
            "Drag and drop files here or click to upload",
            type=["jpg", "png", "mp4"],
            accept_multiple_files=True,
            key="fb_files"
        )

        st.write("")

        # --- SECTION 3: YOUR CONTACT INFORMATION ---
        st.markdown('<div class="step-header"><span class="step-badge">3</span> Your Contact Information</div>', unsafe_allow_html=True)
        
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            user_name = st.text_input("Your Name*", placeholder="Enter your name", key="fb_name")
        with c_col2:
            user_contact = st.text_input("Contact Number / Email*", placeholder="Enter phone number or email", key="fb_contact")

        receive_updates = st.checkbox("I would like to receive updates about this issue via email / SMS.", value=True, key="fb_updates")

        st.write("")

        # --- FORM SUBMIT BUTTONS ---
        btn_col1, btn_col2 = st.columns([2, 1.5])
        with btn_col1:
            submit_clicked = st.button("🚀 Submit Feedback", key="btn_submit_feedback", use_container_width=True)
        with btn_col2:
            reset_clicked = st.button("🔄 Reset Form", key="btn_reset_form", use_container_width=True)

        if submit_clicked:
            if not building_address or not issue_description or not user_name:
                st.error("⚠️ Please fill in all required fields marked with an asterisk (*).")
            else:
                if "feedback_list" not in st.session_state:
                    st.session_state.feedback_list = []

                new_feedback_entry = {
                    "user": user_name if user_name else "Anonymous Resident",
                    "date": datetime.now().strftime("%b %d, %Y"),
                    "text": issue_description,
                    "priority": f"{severity_level} Priority",
                    "building": building_address if building_address else "Building A17",
                    "issue_type": selected_issue,
                    "contact": user_contact
                }

                st.session_state.feedback_list.insert(0, new_feedback_entry)
                show_success_modal(new_feedback_entry)

        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. RIGHT SIDEBAR GUIDANCE CARDS
# -----------------------------------------------------------------------------
with right_info_col:
    st.markdown("""
        <div class="sidebar-card">
            <h4 style="margin: 0 0 10px 0; font-weight: 700;">👥 Why Your Feedback Matters</h4>
            <p style="font-size: 0.85rem; color: #4B5563; line-height: 1.5;">
                Your reports help RESILIA's AI detect problems early, prioritize maintenance actions, and improve building resilience for everyone.
            </p>
            <ul style="font-size: 0.85rem; color: #374151; padding-left: 18px; margin-top: 10px; line-height: 1.8;">
                <li>🤖 <b>Issues analyzed</b> by our AI system</li>
                <li>🎯 <b>Assigned</b> to the right authorities</li>
                <li>⚡ <b>Faster response</b> and resolution</li>
                <li>🛡️ <b>Safer, more resilient</b> communities</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="sidebar-card">
            <h4 style="margin: 0 0 10px 0; font-weight: 700;">💡 Tips for Helpful Feedback</h4>
            <ul style="font-size: 0.85rem; color: #374151; padding-left: 18px; margin: 0; line-height: 1.9;">
                <li>☑️ Be as specific as possible about the issue.</li>
                <li>☑️ Mention the exact location (if possible).</li>
                <li>☑️ Add photos or videos to help us understand better.</li>
                <li>☑️ Share how long the issue has been happening.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="emergency-help-card">
            <h4 style="margin: 0 0 8px 0; font-weight: 700; color: #DC2626;">📞 Need Immediate Assistance?</h4>
            <p style="font-size: 0.85rem; margin: 0; line-height: 1.5; color: #7F1D1D;">
                For emergencies or urgent safety hazards, please contact your building management or local authorities directly.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("📞 Open Contacts Directory", key="btn_to_contacts", use_container_width=True):
        try:
            st.switch_page("pages/contacts.py")
        except Exception:
            st.switch_page("contacts.py")

# Footer
st.divider()
st.caption("🛡️ RESILIA — © 2026 RESILIA. All rights reserved.")
