import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="הבית הירוק - מערכת ניהול", layout="wide")

    st.markdown(
        """
        <style>
        body {
            background-color: #f9f9f9;
            font-family: 'Arial';
        }
        .main-header {
            color: #2ecc71;
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 30px;
        }
        .section-header {
            color: #27ae60;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .button {
            background-color: #27ae60;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #2ecc71;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='main-header'>מערכת ניהול - הבית הירוק</div>", unsafe_allow_html=True)

    choice = st.selectbox("בחר סוג התחברות", ["לקוח", "מנהל פרויקטים", "מנהל חברה"])

    username = st.text_input("שם משתמש")
    password = st.text_input("סיסמא", type="password")

    if username and password:
        if choice == "לקוח":
            customer_dashboard(username)
        elif choice == "מנהל פרויקטים":
            project_manager_dashboard(username)
        elif choice == "מנהל חברה":
            company_manager_dashboard(username)

def customer_dashboard(username):
    st.markdown(f"<div class='section-header'>שלום, {username}</div>", unsafe_allow_html=True)

    page = st.sidebar.radio("ניווט", ["עמוד ראשי", "סטטוס פרויקט", "ניהול מסמכים", "אגרות"])

    if page == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.write("ציר זמן פרויקט")
        st.progress(0.6)
        st.write("התראות:")
        st.write("יש לשלם אגרת חיבור עד לתאריך 5.1")

    elif page == "סטטוס פרויקט":
        st.subheader("סטטוס פרויקט")
        status = ["בתהליך רישוי", "ממתין להתקנה", "התקנה"]
        for step in status:
            st.write(f"{step} - מסמכים: טופס רישוי, טופס אישור")

    elif page == "ניהול מסמכים":
        st.subheader("ניהול מסמכים")
        data = pd.DataFrame({"סוג מסמך": ["רישוי", "חיבור"], "סטטוס": ["הושלם", "ממתין"]})
        st.table(data)

    elif page == "אגרות":
        st.subheader("אגרות")
        data = pd.DataFrame({
            "אגרה": ["רישום", "היתר", "חיבור"],
            "סטטוס": ["שולם", "ממתין", "ממתין"],
            "תשלום": ["[לחץ כאן](#)", "[לחץ כאן](#)", "[לחץ כאן](#)"]
        })
        st.table(data)

def project_manager_dashboard(username):
    st.markdown(f"<div class='section-header'>שלום, {username}</div>", unsafe_allow_html=True)

    page = st.sidebar.radio("ניווט", ["עמוד ראשי", "פרויקטים פעילים", "ארכיון פרויקטים", "העלאת מסמכים"])

    if page == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.write("התראות פרויקטים")

    elif page == "פרויקטים פעילים":
        st.subheader("פרויקטים פעילים")
        st.write("תצוגת פרויקטים פעילים וצירי זמן")

    elif page == "ארכיון פרויקטים":
        st.subheader("ארכיון פרויקטים")
        data = pd.DataFrame({"פרויקט": ["פרויקט 1", "פרויקט 2"]})
        st.table(data)

    elif page == "העלאת מסמכים":
        st.subheader("העלאת מסמכים")
        uploaded_file = st.file_uploader("העלה מסמך")
        if uploaded_file:
            st.write("מסמך הועלה בהצלחה!")

def company_manager_dashboard(username):
    st.markdown(f"<div class='section-header'>שלום, {username}</div>", unsafe_allow_html=True)

    page = st.sidebar.radio("ניווט", ["עמוד ראשי", "תשלומים", "פרויקטים פעילים", "ארכיון פרויקטים", "העלאת מסמכים"])

    if page == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.write("התראות כלליות")

    elif page == "תשלומים":
        st.subheader("תשלומים")
        data = pd.DataFrame({"לקוח": ["לקוח א", "לקוח ב"]})
        st.table(data)

    elif page == "פרויקטים פעילים":
        st.subheader("פרויקטים פעילים")
        st.write("צירי זמן ומעקב")

    elif page == "ארכיון פרויקטים":
        st.subheader("ארכיון פרויקטים")
        st.write("פרויקטים גמורים")

    elif page == "העלאת מסמכים":
        st.subheader("העלאת מסמכים")
        uploaded_file = st.file_uploader("העלה מסמך")
        if uploaded_file:
            st.write("מסמך הועלה בהצלחה!")

if __name__ == "__main__":
    main()
