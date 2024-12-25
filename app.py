import streamlit as st

# פונקציה לעיצוב כפתורים
def styled_button(label, key=None):
    return st.button(label, key=key)

# פונקציה לטעינת הדף הנכון
def render_page():
    if st.session_state.get("current_page") == "login":
        login_page()
    elif st.session_state.get("current_page") == "customers":
        customers_page()
    elif st.session_state.get("current_page") == "project_managers":
        project_managers_page()
    elif st.session_state.get("current_page") == "admin":
        admin_page()
    else:
        st.session_state["current_page"] = "login"
        login_page()

# דף התחברות
def login_page():
    st.title("מערכת ניהול פרויקטים - הבית הירוק")
    st.subheader("בחר סוג התחברות:")
    col1, col2, col3 = st.columns(3)
    with col1:
        if styled_button("לקוחות", key="customers_button"):
            st.session_state["current_page"] = "customers"
    with col2:
        if styled_button("מנהלי פרויקטים", key="project_managers_button"):
            st.session_state["current_page"] = "project_managers"
    with col3:
        if styled_button("מנהל חברה", key="admin_button"):
            st.session_state["current_page"] = "admin"

# עמוד לקוחות
def customers_page():
    st.title("תפריט לקוחות")
    if styled_button("פתיחת פניה חדשה"):
        st.write("פתיחת פניה חדשה (בקרוב)")
    if styled_button("עדכון פרטים אישיים"):
        st.write("עדכון פרטים אישיים (בקרוב)")
    if styled_button("ניהול מסמכים נדרשים"):
        st.write("ניהול מסמכים נדרשים (בקרוב)")
    if styled_button("מעקב אחר סטטוס הפרויקט"):
        st.write("מעקב אחר סטטוס הפרויקט (בקרוב)")
    if styled_button("חזור"):
        st.session_state["current_page"] = "login"

# עמוד מנהלי פרויקטים
def project_managers_page():
    st.title("תפריט מנהלי פרויקטים")
    if styled_button("ניהול פרויקטים פעילים"):
        st.write("ניהול פרויקטים פעילים (בקרוב)")
    if styled_button("עדכון סטטוס פרויקט"):
        st.write("עדכון סטטוס פרויקט (בקרוב)")
    if styled_button("סיכום מלאי ושימוש"):
        st.write("סיכום מלאי ושימוש (בקרוב)")
    if styled_button("חזור"):
        st.session_state["current_page"] = "login"

# עמוד מנהל חברה
def admin_page():
    st.title("תפריט מנהל חברה")
    if styled_button("ניהול מלאי והזמנות"):
        st.write("ניהול מלאי והזמנות (בקרוב)")
    if styled_button("תיעוד וארכיון פרויקטים"):
        st.write("תיעוד וארכיון פרויקטים (בקרוב)")
    if styled_button("דוחות ביצועים"):
        st.write("דוחות ביצועים (בקרוב)")
    if styled_button("חזור"):
        st.session_state["current_page"] = "login"

# הפעלת היישום
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "login"

render_page()
