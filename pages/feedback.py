import streamlit as st
from datetime import datetime

# Configure the global browser tab title, icon, and wide page layout
st.set_page_config(
    page_title="RESILIA - Give Feedback", 
    page_icon="🛡️", 
    layout="wide"
)

# -----------------------------------------------------------------------------
# 1. SUCCESS POP-UP MODAL (@st.dialog)
# -----------------------------------------------------------------------------
# Define a modal popup that renders when a user submits their feedback
@st.dialog("Feedback Submitted Successfully")
def show_success_modal(summary_data):
    # Render modal header icon, title, and description using custom HTML
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
    
    # Display an itemized summary of the user's submitted feedback
    st.markdown(f"""
        **Submission Summary:**
        * **Building Address:** {summary_data['building']}
        * **Issue Category:** {summary_data['issue_type']}
        * **Severity Level:** {summary_data['priority']}
        * **Logged By:** {summary_data['user']} ({summary_data['contact']})
        * **Timestamp:** {summary_data['date']}
    """)
    
    # Informational notice regarding AI system downstream processing
    st.info("🤖 **Next Action:** RESILIA's AI model will evaluate this incident and route notice to local municipal authorities.")
    
    # Navigation button to route user back to the main homepage/dashboard
    if st.button("Return to Maintenance Dashboard", use_container_width=True):
        try:
            st.switch_page("pages/homepage.py")
        except Exception:
            st.switch_page("homepage.py")

# -----------------------------------------------------------------------------
# 2. UI STYLING & CUSTOM CSS
# -----------------------------------------------------------------------------
# Inject global CSS overrides for background colors, headers, form cards, and custom buttons
st.markdown("""
    <style>
        /* Base page background color, primary text color, and typography */
        .stApp {
            background-color: #FAF8F5;
            color: #111827;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* Hide standard Streamlit header, footer, and main menu elements */
        #MainMenu, footer, header { visibility: hidden; }

        /* Navigation Bar Container Styling */
        .nav-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #FFFFFF;
            padding: 12px 40px;
            border-bottom: 1px solid #E5E7EB;
            margin-bottom: 30px;
        }

        /* Main Form Card Container Styling */
        .form-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 32px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            margin-bottom: 25px;
        }

        /* Circular Step Badge Indicator (e.g. 1, 2, 3) */
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

        /* Section Header Container in Form */
        .step-header {
            display: flex;
            align-items: center;
            font-size: 1.15rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 20px;
            margin-top: 10px;
        }

        /* Information & Guidance Cards for the Right Sidebar */
        .sidebar-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 20px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02);
        }

        /* Red-highlighted Emergency Contact Banner */
        .emergency-help-card {
            background-color: #FEF2F2;
            border: 1px solid #FEE2E2;
            border-radius: 14px;
            padding: 20px;
            color: #991B1B;
        }

        /* Primary Action Submit Button Override */
        div.stButton > button[key="btn_submit_feedback"] {
            background-color: #CE3834 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            font-size: 1rem !important;
            height: 46px !important;
        }

        /* Secondary Action Reset Button Override */
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
# 3. TOP NAVIGATION BAR
# -----------------------------------------------------------------------------
# Set up a 3-column top navbar layout (Brand Logo / Center Spacer / Navigation Menu)
nav1, nav2, nav3 = st.columns([2, 3, 2])

# Left side: Brand/Logo home redirect button
with nav1:
    if st.button("🛡️ RESILIA", key="nav_brand_home"):
        try:
            st.switch_page("pages/homepage.py")
        except Exception:
            st.switch_page("homepage.py")

# Middle column used as empty layout spacing
with nav2:
    st.write("")

# Right side: Page navigation links and active indicator
with nav3:
    n_maint, n_feed, n_about = st.columns(3)
    
    # Nav link to Maintenance Dashboard
    with n_maint:
        if st.button("📑 Maintenance", key="nav_maint"):
            try:
                st.switch_page("pages/homepage.py")
            except Exception:
                st.switch_page("homepage.py")
                
    # Active tab visual marker for current Feedback page
    with n_feed:
        st.markdown("<b style='color: #CE3834; border-bottom: 2px solid #CE3834; padding-bottom: 4px;'>💬 Feedback</b>", unsafe_allow_html=True)
        
    # Modal trigger info box for AI model version details
    with n_about:
        if st.button("ℹ️ About Model", key="nav_about"):
            st.info("RESILIA AI Risk Assessment Model v2.4")

st.divider()

# -----------------------------------------------------------------------------
# 4. MAIN PAGE HEADER & HERO GRAPHIC AREA
# -----------------------------------------------------------------------------
# Create hero section layout with header text on left and graphic on right
hdr_col, img_col = st.columns([3.2, 1.8])

# Title and descriptive subhead
with hdr_col:
    st.markdown("<h1 style='font-size: 2.3rem; font-weight: 800; margin: 0;'>Give <span style='color: #CE3834;'>Feedback</span></h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='color: #4B5563; font-size: 1.05rem; line-height: 1.6; margin-top: 12px; max-width: 580px;'>
            Help us improve building maintenance and resilience by sharing the issues you are experiencing. 
            Your feedback enables RESILIA to take the right action, faster.
        </p>
    """, unsafe_allow_html=True)

# Radial gradient header illustration placeholder
with img_col:
    st.markdown("""
        <div style="text-align: center; background: radial-gradient(circle, #FEE2E2 0%, rgba(255,255,255,0) 70%); padding: 10px;">
            <span style="font-size: 5rem;">🏢💬🏙️</span>
        </div>
    """, unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# 5. FORM AND SIDEBAR LAYOUT
# -----------------------------------------------------------------------------
# Split main body into form container (left) and guidance sidebar (right)
left_form_col, right_info_col = st.columns([3.2, 1.8])

with left_form_col:
    with st.container():
        # Open wrapper div with class for custom CSS styling
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        
        # --- SECTION 1: BUILDING INFORMATION ---
        st.markdown('<div class="step-header"><span class="step-badge">1</span> Building Information</div>', unsafe_allow_html=True)
        
        # Text input for building location
        building_address = st.text_input(
            "Building Address*",
            placeholder="🔍 Search or enter building address (e.g., Building A17, DIAC, Dubai)",
            key="fb_address"
        )
        
        # Two-column layout for metadata select dropdowns
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
        
        # List of predefined category options mapping (Display Label, Value)
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
        
        # Radio button grid for category selection
        selected_issue = st.radio(
            "Select Issue Category",
            options=[cat[1] for cat in issue_categories],
            horizontal=True,
            label_visibility="collapsed",
            key="fb_issue_cat"
        )
        
        # Multiline text field for detailed description
        issue_description = st.text_area(
            "Describe the Issue*",
            placeholder="Please describe the issue in detail...",
            max_chars=1000,
            key="fb_desc"
        )
        
        # Date input and occurrence frequency selector
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            first_noticed = st.date_input("When did you first notice this issue?*", key="fb_date")
        with d_col2:
            frequency = st.selectbox(
                "How often does it occur?*",
                ["Select frequency", "One-time occurrence", "Intermittent / Occasional", "Continuous / Daily"],
                key="fb_freq"
            )

        # Horizontal radio selectors for urgency priority
        st.caption("Impact / Severity*")
        severity_level = st.radio(
            "Severity Level",
            ["Low", "Medium", "High", "Critical"],
            index=2,
            horizontal=True,
            label_visibility="collapsed",
            key="fb_severity"
        )

        # File uploader input for images/videos
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
        
        # Contact detail inputs
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            user_name = st.text_input("Your Name*", placeholder="Enter your name", key="fb_name")
        with c_col2:
            user_contact = st.text_input("Contact Number / Email*", placeholder="Enter phone number or email", key="fb_contact")

        # Opt-in checkbox for notification updates
        receive_updates = st.checkbox("I would like to receive updates about this issue via email / SMS.", value=True, key="fb_updates")

        st.write("")

        # --- FORM SUBMIT BUTTONS & STATE HANDLING ---
        btn_col1, btn_col2 = st.columns([2, 1.5])
        with btn_col1:
            submit_clicked = st.button("🚀 Submit Feedback", key="btn_submit_feedback", use_container_width=True)
        with btn_col2:
            reset_clicked = st.button("🔄 Reset Form", key="btn_reset_form", use_container_width=True)

        # Form submission logic and validation checks
        if submit_clicked:
            # Validate required fields
            if not building_address or not issue_description or not user_name:
                st.error("⚠️ Please fill in all required fields marked with an asterisk (*).")
            else:
                # Initialize state array if it does not exist yet
                if "feedback_list" not in st.session_state:
                    st.session_state.feedback_list = []

                # Build feedback record payload
                new_feedback_entry = {
                    "user": user_name if user_name else "Anonymous Resident",
                    "date": datetime.now().strftime("%b %d, %Y"),
                    "text": issue_description,
                    "priority": f"{severity_level} Priority",
                    "building": building_address if building_address else "Building A17",
                    "issue_type": selected_issue,
                    "contact": user_contact
                }

                # Prepend output to list to preserve reverse chronological order
                st.session_state.feedback_list.insert(0, new_feedback_entry)

                # Trigger confirmation dialog modal
                show_success_modal(new_feedback_entry)

        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. RIGHT SIDEBAR GUIDANCE CARDS
# -----------------------------------------------------------------------------
with right_info_col:
    # Sidebar Card 1: Value proposition list
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

    # Sidebar Card 2: Form submission guidance tips
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

    # Sidebar Card 3: Emergency assistance escalation banner
    st.markdown("""
        <div class="emergency-help-card">
            <h4 style="margin: 0 0 8px 0; font-weight: 700; color: #DC2626;">📞 Need Immediate Assistance?</h4>
            <p style="font-size: 0.85rem; margin: 0; line-height: 1.5; color: #7F1D1D;">
                For emergencies or urgent safety hazards, please contact your building management or local authorities directly.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Navigation trigger to directory contacts page
    if st.button("📞 Open Contacts Directory", key="btn_to_contacts", use_container_width=True):
        try:
            st.switch_page("pages/contacts.py")
        except Exception:
            st.switch_page("contacts.py")

# -----------------------------------------------------------------------------
# 7. PAGE FOOTER
# -----------------------------------------------------------------------------
st.divider()
st.caption("🛡️ RESILIA — © 2026 RESILIA. All rights reserved.")
