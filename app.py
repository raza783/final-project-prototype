import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="הבית הירוק - מערכת ניהול", layout="wide")

    # CSS לעיצוב מותאם
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
        .highlight {
            background-color: #2ecc71;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
        }
        .button {
            background-color: #27ae60;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
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

    # מסך התחברות ראשי
    choice = st.selectbox("בחר סוג התחברות", ["לקוח", "מנהל פרויקטים", "מנהל חברה"])

    if choice == "לקוח":
        customer_dashboard()
    elif choice == "מנהל פרויקטים":
        project_manager_dashboard()
    elif choice == "מנהל חברה":
        company_manager_dashboard()


def customer_dashboard():
    username = st.text_input("הזן שם משתמש")

    if username:
        st.markdown(f"<div class='section-header'>שלום, {username}</div>", unsafe_allow_html=True)
        st.subheader("עמוד ראשי")

        # תצוגת סטטוס פרויקט
        st.markdown("**סטטוס פרויקט**: ממתין להתקנה")
        st.progress(0.6)

        # התראות
        st.markdown("<div class='section-header'>התראות</div>", unsafe_allow_html=True)
        st.write("יש לשלם אגרת חיבור עד לתאריך 5.1")
        st.write("יש למלא את מסמך רישוי מספר 3")

        # ניהול מסמכים
        st.markdown("<div class='section-header'>ניהול מסמכים</div>", unsafe_allow_html=True)
        st.write("מסמך 1 - הושלם")
        st.write("מסמך 2 - ממתין למילוי")

        # אגרות
        st.markdown("<div class='section-header'>אגרות</div>", unsafe_allow_html=True)
        data = pd.DataFrame({
            "אגרה": ["רישום", "היתר", "חיבור"],
            "סטטוס": ["שולם", "ממתין", "ממתין"],
            "קישור לתשלום": ["[לחץ כאן](https://www.example.com)", "[לחץ כאן](https://www.example.com)", "[לחץ כאן](https://www.example.com)"]
        })
        st.table(data)


def project_manager_dashboard():
    st.markdown("<div class='section-header'>מנהל פרויקטים</div>", unsafe_allow_html=True)

    # פרויקטים פעילים
    st.subheader("פרויקטים פעילים")
    st.write("ציר זמן של כל פרויקט, תצוגת משימות לטיפול.")
    
    # ארכיון פרויקטים
    st.subheader("ארכיון פרויקטים")
    archive_data = pd.DataFrame({
        "פרויקט": ["פרויקט 1", "פרויקט 2"],
        "תאריך התחלה": ["01/01/2023", "05/03/2023"],
        "תאריך סיום": ["15/02/2023", "20/04/2023"]
    })
    st.table(archive_data)

    # העלאת מסמכים
    st.subheader("העלאת מסמכים")
    uploaded_file = st.file_uploader("העלה מסמך", type=["pdf", "docx"])
    if uploaded_file is not None:
        st.write("מסמך הועלה בהצלחה!")


def company_manager_dashboard():
    st.markdown("<div class='section-header'>מנהל חברה</div>", unsafe_allow_html=True)

    # סטטוס תשלומים
    st.subheader("תשלומים")
    payment_data = pd.DataFrame({
        "לקוח": ["לקוח א", "לקוח ב"],
        "סכום ששולם": ["10,000", "15,000"],
        "יתרה לתשלום": ["5,000", "2,000"]
    })
    st.table(payment_data)

    # ארכיון פרויקטים
    st.subheader("ארכיון פרויקטים")
    archive_data = pd.DataFrame({
        "פרויקט": ["פרויקט 1", "פרויקט 2"],
        "תאריך התחלה": ["01/01/2023", "05/03/2023"],
        "תאריך סיום": ["15/02/2023", "20/04/2023"]
    })
    st.table(archive_data)

if __name__ == "__main__":
    main()
