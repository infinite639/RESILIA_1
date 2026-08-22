import streamlit as st
from textwrap import dedent

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="RESILIA — Contacts",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CONTACT DATA
# ============================================================

contacts = [
    {
        "category": "Water Management",
        "icon": "💧",
        "icon_class": "blue",
        "authority": "Dubai Municipality HQ",
        "address": "Al Wasl Rd, Dubai, UAE",
        "name": "Eng. Ahmed Al Mansoori",
        "phone": "+971 4 123 4567",
    },
    {
        "category": "Electricity",
        "icon": "ϟ",
        "icon_class": "yellow",
        "authority": "DEWA Headquarters",
        "address": "Al Ittihad Rd, Dubai, UAE",
        "name": "Eng. Fatima Al Zaabi",
        "phone": "+971 4 234 5678",
    },
    {
        "category": "Roof Management",
        "icon": "⌂",
        "icon_class": "grey",
        "authority": "Dubai Building Dept.",
        "address": "Business Bay, Dubai, UAE",
        "name": "Eng. Omar Hassan",
        "phone": "+971 4 345 6789",
    },
    {
        "category": "Structural Stability",
        "icon": "▥",
        "icon_class": "blue",
        "authority": "Trakhees - Structural Dept.",
        "address": "Port Saeed, Dubai, UAE",
        "name": "Eng. Salma Tariq",
        "phone": "+971 4 456 7890",
    },
    {
        "category": "Weather Related",
        "icon": "☁",
        "icon_class": "grey",
        "authority": "National Center of Meteorology",
        "address": "Al Barsha, Dubai, UAE",
        "name": "Dr. Khalid Al Nuaimi",
        "phone": "+971 4 567 8901",
    },
    {
        "category": "Exterior Walls",
        "icon": "▦",
        "icon_class": "orange",
        "authority": "Dubai Municipality - Buildings",
        "address": "Al Wasl Rd, Dubai, UAE",
        "name": "Eng. Mariam Farid",
        "phone": "+971 4 678 9012",
    },
    {
        "category": "Drainage Systems",
        "icon": "♧",
        "icon_class": "red",
        "authority": "Dubai Municipality - Sewage Dept.",
        "address": "Umm Ramool, Dubai, UAE",
        "name": "Eng. Yousuf Ibrahim",
        "phone": "+971 4 789 0123",
    },
    {
        "category": "Interior",
        "icon": "▣",
        "icon_class": "green",
        "authority": "Dubai Municipality - Interior Dept.",
        "address": "Al Barsha, Dubai, UAE",
        "name": "Eng. Noor Al Hammadi",
        "phone": "+971 4 890 1234",
    },
    {
        "category": "Security",
        "icon": "♢",
        "icon_class": "grey",
        "authority": "Dubai Police - Community Safety",
        "address": "Al Kifaf, Dubai, UAE",
        "name": "Lt. Ahmed Bin Rashid",
        "phone": "+971 4 901 2345",
    },
]

# ============================================================
# SESSION STATE
# ============================================================

if "open_contact" not in st.session_state:
    st.session_state.open_contact = None

if "help_contact" not in st.session_state:
    st.session_state.help_contact = None


# ============================================================
# CSS
# ============================================================

st.markdown(
    dedent(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* ==================================================
           GLOBAL
        ================================================== */

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: #ffffff;
            color: #111827;
        }

        .block-container {
            max-width: 1500px !important;
            padding-top: 0 !important;
            padding-left: 22px !important;
            padding-right: 22px !important;
            padding-bottom: 20px !important;
        }

        /* Remove default Streamlit vertical gaps */
        div[data-testid="stVerticalBlock"] {
            gap: 0;
        }

        /* ==================================================
           HEADER
        ================================================== */

        .top-header {
            height: 78px;
            border-bottom: 1px solid #edf0f3;
            display: flex;
            align-items: center;
            margin-bottom: 28px;
        }

        .brand-area {
            display: flex;
            align-items: center;
            width: 410px;
            flex-shrink: 0;
        }

        .logo-shield {
            width: 39px;
            height: 43px;
            border: 3px solid #17202c;
            border-radius: 8px 8px 14px 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #f0b51b;
            font-size: 17px;
            margin-right: 12px;
            box-sizing: border-box;
        }

        .brand-name {
            font-size: 28px;
            line-height: 30px;
            font-weight: 700;
            letter-spacing: 1px;
            color: #17202c;
        }

        .brand-tagline {
            font-size: 12px;
            line-height: 18px;
            color: #252c38;
            margin-left: 25px;
        }

        .search-box {
            height: 47px;
            width: 465px;
            border: 1px solid #e1e5e9;
            border-radius: 11px;
            display: flex;
            align-items: center;
            overflow: hidden;
            color: #68717d;
        }

        .search-location {
            font-size: 19px;
            margin-left: 16px;
        }

        .search-placeholder {
            margin-left: 13px;
            font-size: 14px;
        }

        .search-button {
            margin-left: auto;
            width: 51px;
            height: 47px;
            background: #ffedc3;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #111827;
            font-size: 21px;
        }

        .header-right {
            margin-left: auto;
            display: flex;
            align-items: center;
            gap: 32px;
        }

        .header-item {
            display: flex;
            align-items: center;
            gap: 9px;
            font-size: 14px;
            color: #111827;
            white-space: nowrap;
        }

        .notification {
            position: relative;
        }

        .notification-badge {
            position: absolute;
            top: -11px;
            left: 13px;
            width: 19px;
            height: 19px;
            border-radius: 50%;
            background: #df3030;
            color: #ffffff;
            font-size: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .user-area {
            display: flex;
            flex-direction: column;
            min-width: 105px;
        }

        .user-name {
            font-size: 14px;
            font-weight: 600;
        }

        .user-role {
            color: #6b7280;
            font-size: 12px;
            margin-top: 5px;
        }

        /* ==================================================
           PAGE TITLE
        ================================================== */

        .title-area {
            display: flex;
            align-items: center;
            min-height: 65px;
        }

        .page-title {
            font-size: 23px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 6px;
        }

        .page-subtitle {
            font-size: 13px;
            color: #3e4652;
        }

        /* ==================================================
           ALERTS
        ================================================== */

        .alert-card {
            height: 62px;
            border: 1px solid #f0e1bc;
            border-radius: 10px;
            display: flex;
            align-items: center;
            padding: 0 20px;
            box-sizing: border-box;
            background: #fffdfa;
        }

        .emergency-alert {
            border-color: #ffd0d0;
            background: #fffafa;
        }

        .alert-icon {
            font-size: 26px;
            margin-right: 18px;
        }

        .alert-title {
            font-size: 14px;
            font-weight: 600;
            color: #111827;
        }

        .emergency-alert .alert-title {
            color: #e33131;
        }

        .alert-description {
            margin-top: 5px;
            font-size: 12px;
            color: #6a7280;
        }

        /* ==================================================
           GRID
        ================================================== */

        .contact-card-wrapper {
            border: 1px solid #e3e7eb;
            border-radius: 11px;
            background: #ffffff;
            min-height: 245px;
            box-sizing: border-box;
            padding: 18px;
            margin-bottom: 0;
        }

        .card-top {
            display: flex;
            align-items: flex-start;
            min-height: 64px;
        }

        .category-icon {
            width: 54px;
            height: 54px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            margin-right: 16px;
            font-size: 26px;
        }

        .icon-blue {
            background: #f0f7fd;
            color: #1471ad;
        }

        .icon-yellow {
            background: #fff9e9;
            color: #f4b500;
        }

        .icon-grey {
            background: #f3f5f7;
            color: #3c4654;
        }

        .icon-orange {
            background: #fff4ec;
            color: #ef7419;
        }

        .icon-red {
            background: #fff0f0;
            color: #e33131;
        }

        .icon-green {
            background: #edf8f0;
            color: #218846;
        }

        .category-content {
            flex: 1;
        }

        .category-title {
            font-size: 14px;
            font-weight: 600;
            color: #111827;
            margin-bottom: 7px;
        }

        .authority {
            font-size: 12px;
            line-height: 18px;
            color: #303845;
        }

        .dropdown {
            font-size: 18px;
            color: #111827;
            margin-left: 8px;
        }

        /* ==================================================
           PERSON
        ================================================== */

        .person-row {
            display: flex;
            align-items: center;
            margin-top: 19px;
        }

        .person-info {
            flex: 1;
        }

        .person-name {
            font-size: 12px;
            color: #111827;
            margin-bottom: 7px;
        }

        .person-phone {
            font-size: 12px;
            color: #252d39;
        }

        /* ==================================================
           STREAMLIT BUTTONS
        ================================================== */

        .contact-button-container {
            margin-top: -47px;
            margin-left: auto;
            width: 98px;
            position: relative;
            z-index: 2;
        }

        .contact-button-container button {
            height: 38px !important;
            background: #ffedc3 !important;
            border: none !important;
            border-radius: 7px !important;
            color: #111827 !important;
            font-size: 12px !important;
            font-weight: 500 !important;
        }

        .contact-button-container button:hover {
            background: #ffe6aa !important;
        }

        /* ==================================================
           EXPANDED ACTIONS
        ================================================== */

        .action-area {
            margin-top: 20px;
            display: flex;
            gap: 13px;
        }

        .help-button-container {
            flex: 1;
        }

        .help-button-container button {
            height: 49px !important;
            border: 1px solid #e0e4e8 !important;
            border-radius: 8px !important;
            background: #ffffff !important;
            color: #202734 !important;
            font-size: 12px !important;
        }

        .help-button-container button:hover {
            border-color: #cfd5da !important;
            background: #fafafa !important;
        }

        .call-button-container {
            width: 88px;
        }

        .call-button-container button {
            height: 49px !important;
            border: 1px solid #9bd4a5 !important;
            border-radius: 8px !important;
            background: #ffffff !important;
            color: #248743 !important;
            font-size: 20px !important;
        }

        .call-button-container button:hover {
            background: #f3fbf4 !important;
        }

        .help-message {
            font-size: 11px;
            color: #69717d;
            margin-top: 9px;
            line-height: 16px;
        }

        /* ==================================================
           FOOTER
        ================================================== */

        .footer {
            border-top: 1px solid #edf0f3;
            margin-top: 26px;
            padding-top: 21px;
            display: flex;
            align-items: center;
            color: #646c77;
            font-size: 11px;
        }

        .footer-links {
            display: flex;
            gap: 16px;
            margin-left: 22px;
        }

        .footer-separator {
            color: #c8ccd1;
        }

        .footer-right {
            margin-left: auto;
        }

        /* ==================================================
           RESPONSIVE
        ================================================== */

        @media (max-width: 1200px) {

            .brand-area {
                width: 330px;
            }

            .brand-tagline {
                display: none;
            }

            .search-box {
                width: 360px;
            }

            .header-right {
                gap: 18px;
            }
        }

        @media (max-width: 900px) {

            .contact-card-wrapper {
                min-height: 250px;
            }

            .header-item span {
                display: none;
            }

            .user-area {
                display: none;
            }

            .brand-area {
                width: 250px;
            }

            .search-box {
                width: 300px;
            }
        }

        </style>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    dedent(
        """
        <div class="top-header">

            <div class="brand-area">

                <div class="logo-shield">⌂</div>

                <div class="brand-name">
                    RESILIA
                </div>

                <div class="brand-tagline">
                    Building Intelligence<br>
                    for Safer Communities
                </div>

            </div>

            <div class="search-box">

                <div class="search-location">⌖</div>

                <div class="search-placeholder">
                    Search address or building...
                </div>

                <div class="search-button">
                    ⌕
                </div>

            </div>

            <div class="header-right">

                <div class="header-item">
                    <span style="font-size:19px;">?</span>
                    <span>Help</span>
                </div>

                <div class="header-item notification">
                    <span style="font-size:22px;">♧</span>
                    <span>Notifications</span>
                    <div class="notification-badge">3</div>
                </div>

                <div class="user-area">
                    <div class="user-name">Admin User</div>
                    <div class="user-role">Authority</div>
                </div>

                <div style="font-size:18px;">⌄</div>

            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# TITLE + TOP ALERTS
# ============================================================

title_col, emergency_col, assistance_col = st.columns(
    [2.0, 1.05, 1.55],
    gap="medium",
)

with title_col:
    st.markdown(
        dedent(
            """
            <div class="title-area">

                <div>
                    <div class="page-title">
                        Contacts Directory
                    </div>

                    <div class="page-subtitle">
                        Connect with the right authority for each building system
                    </div>
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )


with emergency_col:
    st.markdown(
        dedent(
            """
            <div class="alert-card emergency-alert">

                <div class="alert-icon">☎</div>

                <div>
                    <div class="alert-title">
                        Emergency Contacts
                    </div>

                    <div class="alert-description">
                        24/7 Support
                    </div>
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )


with assistance_col:
    st.markdown(
        dedent(
            """
            <div class="alert-card">

                <div class="alert-icon">ⓘ</div>

                <div>
                    <div class="alert-title">
                        Need Assistance?
                    </div>

                    <div class="alert-description">
                        Choose a category to find the right contact person.
                    </div>
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )


# ============================================================
# CONTACT GRID
# ============================================================

for row_start in range(0, len(contacts), 3):

    columns = st.columns(3, gap="medium")

    for column_index in range(3):

        contact_index = row_start + column_index

        if contact_index >= len(contacts):
            continue

        contact = contacts[contact_index]

        with columns[column_index]:

            # ----------------------------------------------
            # CARD
            # ----------------------------------------------

            st.markdown(
                dedent(
                    f"""
                    <div class="contact-card-wrapper">

                        <div class="card-top">

                            <div class="category-icon icon-{contact['icon_class']}">
                                {contact['icon']}
                            </div>

                            <div class="category-content">

                                <div class="category-title">
                                    {contact['category']}
                                </div>

                                <div class="authority">
                                    {contact['authority']}<br>
                                    {contact['address']}
                                </div>

                            </div>

                            <div class="dropdown">
                                ⌄
                            </div>

                        </div>

                        <div class="person-row">

                            <div class="person-info">

                                <div class="person-name">
                                    {contact['name']}
                                </div>

                                <div class="person-phone">
                                    {contact['phone']}
                                </div>

                            </div>

                        </div>

                    </div>
                    """
                ),
                unsafe_allow_html=True,
            )

            # ----------------------------------------------
            # CONTACT BUTTON
            # ----------------------------------------------

            st.markdown(
                '<div class="contact-button-container">',
                unsafe_allow_html=True,
            )

            contact_clicked = st.button(
                "Contact",
                key=f"contact_{contact_index}",
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )

            if contact_clicked:

                if st.session_state.open_contact == contact_index:
                    st.session_state.open_contact = None
                else:
                    st.session_state.open_contact = contact_index

                st.rerun()

            # ----------------------------------------------
            # ACTION BUTTONS
            # ----------------------------------------------

            if st.session_state.open_contact == contact_index:

                st.markdown(
                    '<div class="action-area">',
                    unsafe_allow_html=True,
                )

                help_col, call_col = st.columns([2.4, 0.8], gap="small")

                with help_col:

                    st.markdown(
                        '<div class="help-button-container">',
                        unsafe_allow_html=True,
                    )

                    help_clicked = st.button(
                        "◉   More Help",
                        key=f"help_{contact_index}",
                        use_container_width=True,
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True,
                    )

                    if help_clicked:
                        st.session_state.help_contact = contact_index

                with call_col:

                    st.markdown(
                        '<div class="call-button-container">',
                        unsafe_allow_html=True,
                    )

                    call_clicked = st.button(
                        "☎",
                        key=f"call_{contact_index}",
                        use_container_width=True,
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True,
                    )

                    if call_clicked:
                        st.success(
                            f"Calling {contact['name']} — {contact['phone']}"
                        )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )

                if st.session_state.help_contact == contact_index:

                    st.markdown(
                        dedent(
                            f"""
                            <div class="help-message">
                                Contact <strong>{contact['authority']}</strong>
                                for assistance regarding
                                {contact['category'].lower()}.
                            </div>
                            """
                        ),
                        unsafe_allow_html=True,
                    )

            # Space between cards
            st.markdown(
                "<div style='height:18px'></div>",
                unsafe_allow_html=True,
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    dedent(
        """
        <div class="footer">

            <div>
                © 2026 RESILIA. All rights reserved.
            </div>

            <div class="footer-links">

                <span>About Us</span>
                <span class="footer-separator">|</span>

                <span>How It Works</span>
                <span class="footer-separator">|</span>

                <span>Privacy Policy</span>
                <span class="footer-separator">|</span>

                <span>Terms of Use</span>
                <span class="footer-separator">|</span>

                <span>Data Sources</span>
                <span class="footer-separator">|</span>

                <span>Contact Us</span>

            </div>

            <div class="footer-right">
                License & Compliance
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)
