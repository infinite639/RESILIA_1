import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="RESILIA — Contacts",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================

if "open_contact" not in st.session_state:
    st.session_state.open_contact = None

if "help_contact" not in st.session_state:
    st.session_state.help_contact = None


# ============================================================
# DATA
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
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ----------------------------------------------------------
   GLOBAL
---------------------------------------------------------- */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #ffffff;
    color: #101827;
}

.block-container {
    max-width: 1490px !important;
    padding: 0 20px 20px 20px !important;
}


/* Remove Streamlit default spacing */

div[data-testid="stVerticalBlock"] {
    gap: 0;
}


/* ----------------------------------------------------------
   TOP HEADER
---------------------------------------------------------- */

.top-header {
    height: 78px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #edf0f3;
    margin-bottom: 28px;
}

.brand-area {
    width: 410px;
    display: flex;
    align-items: center;
}

.logo-shield {
    width: 42px;
    height: 42px;
    border: 3px solid #182230;
    border-radius: 8px 8px 13px 13px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 12px;
    font-size: 20px;
    color: #f0b51b;
    position: relative;
}

.logo-shield:after {
    content: "";
    position: absolute;
    width: 13px;
    height: 13px;
    border: 2px solid #f0b51b;
    border-radius: 2px;
}

.brand-name {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #17202c;
}

.brand-tagline {
    font-size: 13px;
    line-height: 19px;
    color: #202735;
    margin-left: 24px;
}

.search-box {
    height: 48px;
    flex: 1;
    max-width: 470px;
    border: 1px solid #e0e4e9;
    border-radius: 11px;
    display: flex;
    align-items: center;
    color: #6b7280;
    overflow: hidden;
    margin-left: 20px;
}

.search-icon {
    font-size: 20px;
    margin-left: 16px;
}

.search-text {
    font-size: 14px;
    margin-left: 15px;
}

.search-button {
    margin-left: auto;
    height: 48px;
    width: 52px;
    background: #ffedc3;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #111827;
    font-size: 20px;
}

.header-right {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 34px;
}

.header-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
    color: #101827;
}

.notification {
    position: relative;
}

.notification-badge {
    position: absolute;
    top: -10px;
    left: 13px;
    width: 19px;
    height: 19px;
    border-radius: 50%;
    background: #e22d2d;
    color: white;
    font-size: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.user-area {
    display: flex;
    flex-direction: column;
    min-width: 115px;
}

.user-name {
    font-size: 14px;
    font-weight: 600;
}

.user-role {
    font-size: 12px;
    color: #69717e;
    margin-top: 5px;
}


/* ----------------------------------------------------------
   PAGE HEADER
---------------------------------------------------------- */

.page-heading {
    display: flex;
    align-items: center;
    margin: 0 0 26px 0;
}

.page-title {
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 7px;
}

.page-subtitle {
    font-size: 13px;
    color: #394150;
}


/* ----------------------------------------------------------
   TOP ALERTS
---------------------------------------------------------- */

.alert-row {
    display: flex;
    gap: 22px;
    margin-left: auto;
}

.alert-box {
    height: 62px;
    border: 1px solid #f0e4c5;
    border-radius: 9px;
    padding: 10px 20px;
    min-width: 350px;
    display: flex;
    align-items: center;
    background: #fffdfa;
}

.emergency-box {
    border-color: #ffd4d4;
    background: #fffafa;
}

.alert-icon {
    font-size: 25px;
    margin-right: 18px;
}

.alert-title {
    font-size: 14px;
    font-weight: 600;
}

.alert-description {
    font-size: 12px;
    color: #69717e;
    margin-top: 4px;
}

.emergency-box .alert-title {
    color: #e33232;
}


/* ----------------------------------------------------------
   CONTACT GRID
---------------------------------------------------------- */

.contact-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-top: 5px;
}


/* ----------------------------------------------------------
   CONTACT CARD
---------------------------------------------------------- */

.contact-card {
    min-height: 235px;
    border: 1px solid #e4e8ec;
    border-radius: 11px;
    padding: 18px 18px 16px 18px;
    background: #ffffff;
    box-sizing: border-box;
    transition: 0.15s ease;
}

.contact-card:hover {
    box-shadow: 0 5px 18px rgba(20, 30, 40, 0.06);
}

.card-top {
    display: flex;
    align-items: flex-start;
}

.category-icon {
    width: 54px;
    height: 54px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 27px;
    margin-right: 17px;
    flex-shrink: 0;
}

.icon-blue {
    background: #f1f8ff;
    color: #1770ad;
}

.icon-yellow {
    background: #fff9e9;
    color: #f5b600;
}

.icon-grey {
    background: #f4f5f6;
    color: #394353;
}

.icon-orange {
    background: #fff5ef;
    color: #f07819;
}

.icon-red {
    background: #fff1f1;
    color: #e33333;
}

.icon-green {
    background: #eef9f1;
    color: #228847;
}

.category-content {
    flex: 1;
}

.category-title {
    font-size: 14px;
    font-weight: 600;
    color: #121a28;
    margin-bottom: 8px;
}

.authority {
    font-size: 12px;
    color: #2f3744;
    line-height: 18px;
}

.dropdown {
    font-size: 18px;
    color: #101827;
}


/* ----------------------------------------------------------
   CONTACT PERSON
---------------------------------------------------------- */

.person-area {
    margin-top: 18px;
    display: flex;
    align-items: center;
}

.person-details {
    flex: 1;
}

.person-name {
    font-size: 12px;
    color: #141b27;
    margin-bottom: 7px;
}

.person-phone {
    font-size: 12px;
    color: #202735;
}

.contact-button {
    background: #ffedc3;
    border-radius: 7px;
    padding: 11px 27px;
    font-size: 12px;
    font-weight: 500;
    color: #101010;
}


/* ----------------------------------------------------------
   EXPANDED CONTACT CONTROLS
---------------------------------------------------------- */

.action-row {
    display: flex;
    gap: 14px;
    margin-top: 18px;
}

.help-button {
    height: 50px;
    border: 1px solid #e0e5e9;
    border-radius: 8px;
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    font-size: 12px;
    background: #ffffff;
}

.call-button {
    height: 50px;
    width: 88px;
    border: 1px solid #a9d9b1;
    border-radius: 8px;
    color: #23853f;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 21px;
    background: #ffffff;
}

.action-note {
    margin-top: 10px;
    font-size: 11px;
    color: #6b7280;
}


/* ----------------------------------------------------------
   STREAMLIT BUTTON OVERRIDES
---------------------------------------------------------- */

div.stButton > button {
    font-family: 'Inter', sans-serif;
    border-radius: 7px;
    border: 1px solid #e0e4e9;
    background: #ffffff;
    color: #111827;
    font-size: 12px;
    height: 39px;
}

div.stButton > button:hover {
    border-color: #d6b85d;
    color: #111827;
}


/* Contact button */

.contact-btn div.stButton > button {
    background: #ffedc3;
    border: none;
}


/* Call button */

.call-btn div.stButton > button {
    height: 50px;
    color: #23853f;
    border-color: #a9d9b1;
    font-size: 20px;
}


/* Help button */

.help-btn div.stButton > button {
    height: 50px;
}


/* ----------------------------------------------------------
   FOOTER
---------------------------------------------------------- */

.footer {
    border-top: 1px solid #edf0f3;
    margin-top: 26px;
    padding-top: 22px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #626b78;
    font-size: 11px;
}

.footer-links {
    display: flex;
    gap: 18px;
}

.footer-separator {
    color: #c8ccd1;
}

.footer-right {
    margin-left: auto;
}


/* ----------------------------------------------------------
   RESPONSIVE
---------------------------------------------------------- */

@media (max-width: 1100px) {

    .contact-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .brand-tagline {
        display: none;
    }

    .header-right {
        gap: 15px;
    }

}

@media (max-width: 750px) {

    .contact-grid {
        grid-template-columns: 1fr;
    }

    .search-box {
        display: none;
    }

    .alert-row {
        display: none;
    }

    .brand-area {
        width: auto;
    }

    .header-right {
        margin-left: auto;
    }

    .header-item span {
        display: none;
    }

    .footer {
        flex-direction: column;
        gap: 15px;
        align-items: flex-start;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
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
        <div class="search-icon">⌖</div>
        <div class="search-text">
            Search address or building...
        </div>
        <div class="search-button">
            ⌕
        </div>
    </div>

    <div class="header-right">

        <div class="header-item">
            <span style="font-size:20px;">?</span>
            <span>Help</span>
        </div>

        <div class="header-item notification">
            <span style="font-size:23px;">♧</span>
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
""",
    unsafe_allow_html=True
)


# ============================================================
# PAGE HEADING + ALERTS
# ============================================================

heading_col, emergency_col, assistance_col = st.columns([2.0, 1.15, 1.55], gap="medium")

with heading_col:
    st.markdown(
        """
        <div class="page-heading">
            <div>
                <div class="page-title">Contacts Directory</div>
                <div class="page-subtitle">
                    Connect with the right authority for each building system
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with emergency_col:
    st.markdown(
        """
        <div class="alert-box emergency-box">
            <div class="alert-icon">☎</div>
            <div>
                <div class="alert-title">Emergency Contacts</div>
                <div class="alert-description">24/7 Support</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with assistance_col:
    st.markdown(
        """
        <div class="alert-box">
            <div class="alert-icon">ⓘ</div>
            <div>
                <div class="alert-title">Need Assistance?</div>
                <div class="alert-description">
                    Choose a category to find the right contact person.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CONTACT CARDS
# ============================================================

for row_start in range(0, len(contacts), 3):

    cols = st.columns(3, gap="medium")

    for col_index, contact_index in enumerate(
        range(row_start, min(row_start + 3, len(contacts)))
    ):

        contact = contacts[contact_index]

        with cols[col_index]:

            # Card container
            st.markdown(
                f"""
                <div class="contact-card">

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

                    <div class="person-area">

                        <div class="person-details">

                            <div class="person-name">
                                {contact['name']}
                            </div>

                            <div class="person-phone">
                                {contact['phone']}
                            </div>

                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            # ------------------------------------------------
            # CONTACT BUTTON
            # ------------------------------------------------

            button_key = f"contact_{contact_index}"

            st.markdown(
                '<div class="contact-btn">',
                unsafe_allow_html=True
            )

            clicked = st.button(
                "Contact",
                key=button_key,
                use_container_width=False
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            if clicked:
                if st.session_state.open_contact == contact_index:
                    st.session_state.open_contact = None
                else:
                    st.session_state.open_contact = contact_index

                st.rerun()

            # ------------------------------------------------
            # EXPANDED ACTIONS
            # ------------------------------------------------

            if st.session_state.open_contact == contact_index:

                action_cols = st.columns([2.4, 0.8], gap="small")

                with action_cols[0]:

                    st.markdown(
                        '<div class="help-btn">',
                        unsafe_allow_html=True
                    )

                    help_clicked = st.button(
                        "◉   More Help",
                        key=f"help_{contact_index}",
                        use_container_width=True
                    )

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

                    if help_clicked:
                        st.session_state.help_contact = contact_index

                with action_cols[1]:

                    st.markdown(
                        '<div class="call-btn">',
                        unsafe_allow_html=True
                    )

                    call_clicked = st.button(
                        "☎",
                        key=f"call_{contact_index}",
                        use_container_width=True
                    )

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

                    if call_clicked:
                        st.success(
                            f"Calling {contact['name']} — {contact['phone']}"
                        )

                if st.session_state.help_contact == contact_index:

                    st.markdown(
                        f"""
                        <div class="action-note">
                            Contact {contact['authority']} for assistance
                            regarding {contact['category'].lower()}.
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # Space between rows
            st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
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
""",
    unsafe_allow_html=True
)
