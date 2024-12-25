import streamlit as st

# פונקציה לעיצוב כפתורים
def styled_button(label, key=None):
    st.markdown(
        f"""
        <style>
        .stButton > button {{
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            margin: 4px 2px;
            }}
        </style>
        """, unsafe_allow_html=True)
    st.button(label, key=key)

# דף התחברות
def login_page():
    st.title("מערכת ניהול פרויקטים - הבית הירוק")
    st.subheader("בחר סוג התחברות:")
    col1, col2, col3 = st.columns(3)
    with col1:
        if styled_button("לקוחות"):
            st.session_state["user_type"] = "לקוחות"
    with col2:
        if styled_button("מנהלי פרויקטים"):
            st.session_state["user_type"] = "מנהלי פרויקטים"
    with col3:
        if styled_button("מנהל חברה"):
            st.session_state["user_type"] = "מנהל חברה"

# עמוד לקוחות
def customers_page():
    st.title("תפריט לקוחות")
    styled_button("פתיחת פניה חדשה")
    styled_button("עדכון פרטים אישיים")
    styled_button("ניהול מסמכים נדרשים")
    styled_button("מעקב אחר סטטוס הפרויקט")

# עמוד מנהלי פרויקטים
def project_managers_page():
    st.title("תפריט מנהלי פרויקטים")
    styled_button("ניהול פרויקטים פעילים")
    styled_button("עדכון סטטוס פרויקט")
    styled_button("סיכום מלאי ושימוש")

# עמוד מנהל חברה
def admin_page():
    st.title("תפריט מנהל חברה")
    styled_button("ניהול מלאי והזמנות")
    styled_button("תיעוד וארכיון פרויקטים")
    styled_button("דוחות ביצועים")

# לוגיקה להצגת הדפים
if "user_type" not in st.session_state:
    st.session_state["user_type"] = None

if st.session_state["user_type"] is None:
    login_page()
elif st.session_state["user_type"] == "לקוחות":
    customers_page()
elif st.session_state["user_type"] == "מנהלי פרויקטים":
    project_managers_page()
elif st.session_state["user_type"] == "מנהל חברה":
    admin_page()
