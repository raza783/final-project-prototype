import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="הבית הירוק - מערכת ניהול", layout="wide")

    # CSS לעיצוב מותאם
    st.markdown(
        """
        <style>
        body {
            background-color: #f4fdf4;
            font-family: 'Arial', sans-serif;
        }
        .main-header {
            color: #006400;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 40px;
        }
        .section-header {
            color: #228b22;
            font-size: 28px;
            margin-bottom: 20px;
            border-bottom: 2px solid #228b22;
        }
        .button {
            background-color: #2ecc71;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            margin: 5px;
        }
        .button:hover {
            background-color: #27ae60;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='main-header'>מערכת ניהול - הבית הירוק</div>", unsafe_allow_html=True)

    # מסך התחברות ראשי
    choice = st.selectbox("בחר סוג התחברות", ["עמוד ראשי", "לקוח", "מנהל פרויקטים", "מנהל חברה"])

    if choice == "לקוח":
        customer_dashboard()
    elif choice == "מנהל פרויקטים":
        project_manager_dashboard()
    elif choice == "מנהל חברה":
        company_manager_dashboard()
    else:
        home_page()


def home_page():
    st.markdown("<div class='section-header'>ברוכים הבאים למערכת הבית הירוק!</div>", unsafe_allow_html=True)
    st.write("מערכת זו נועדה לנהל פרויקטים בצורה חכמה ויעילה.")


def customer_dashboard():
    page = st.radio("ניווט", ["עמוד ראשי", "סטטוס פרויקט", "ניהול מסמכים", "אגרות"])

    if page == "עמוד ראשי":
        st.markdown("<div class='section-header'>עמוד ראשי - לקוח</div>", unsafe_allow_html=True)
        st.markdown("**סטטוס פרויקט**: ממתין להתקנה")
        st.progress(0.6)
        st.markdown("**התראות:**")
        st.warning("יש לשלם אגרת חיבור עד לתאריך 5.1")

    elif page == "סטטוס פרויקט":
        st.markdown("<div class='section-header'>סטטוס פרויקט</div>", unsafe_allow_html=True)
        stages = ["בתהליך רישוי", "ממתין להתקנה", "בהתקנה", "הושלם"]
        progress = [0.25, 0.6, 0.8, 1.0]
        for stage, prog in zip(stages, progress):
            st.write(f"{stage}: {int(prog * 100)}%")
            st.progress(prog)

    elif page == "ניהול מסמכים":
        st.markdown("<div class='section-header'>ניהול מסמכים</div>", unsafe_allow_html=True)
        st.write("כאן תוכלו להעלות מסמכים ולצפות במסמכים קיימים.")
        uploaded_file = st.file_uploader("העלה מסמך", type=["pdf", "docx"])
        if uploaded_file is not None:
            st.success("המסמך הועלה בהצלחה!")

    elif page == "אגרות":
        st.markdown("<div class='section-header'>אגרות</div>", unsafe_allow_html=True)
        data = pd.DataFrame({
            "אגרה": ["רישום", "היתר", "חיבור"],
            "סטטוס": ["שולם", "ממתין", "ממתין"],
            "קישור לתשלום": ["[לחץ כאן](https://www.example.com)", "[לחץ כאן](https://www.example.com)", "[לחץ כאן](https://www.example.com)"]
        })
        st.table(data)


def project_manager_dashboard():
    page = st.radio("ניווט", ["עמוד ראשי", "פרויקטים פעילים", "ארכיון פרויקטים", "העלאת מסמכים"])

    if page == "עמוד ראשי":
        st.markdown("<div class='section-header'>עמוד ראשי - מנהל פרויקטים</div>", unsafe_allow_html=True)
        st.write("ציר זמן של כל הפרויקטים הפעילים ומשימות לטיפול.")

    elif page == "פרויקטים פעילים":
        st.markdown("<div class='section-header'>פרויקטים פעילים</div>", unsafe_allow_html=True)
        active_projects = pd.DataFrame({
            "פרויקט": ["פרויקט 1", "פרויקט 2"],
            "סטטוס": ["בהתקנה", "ממתין להתקנה"],
            "אחוז התקדמות": [75, 50]
        })
        st.table(active_projects)

    elif page == "ארכיון פרויקטים":
        st.markdown("<div class='section-header'>ארכיון פרויקטים</div>", unsafe_allow_html=True)
        archive_data = pd.DataFrame({
            "פרויקט": ["פרויקט 1", "פרויקט 2"],
            "תאריך התחלה": ["01/01/2023", "05/03/2023"],
            "תאריך סיום": ["15/02/2023", "20/04/2023"]
        })
        st.table(archive_data)

    elif page == "העלאת מסמכים":
        st.markdown("<div class='section-header'>העלאת מסמכים</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("העלה מסמך", type=["pdf", "docx"])
        if uploaded_file is not None:
            st.success("המסמך הועלה בהצלחה!")


def company_manager_dashboard():
    page = st.radio("ניווט", ["עמוד ראשי", "תשלומים", "ארכיון פרויקטים"])

    if page == "עמוד ראשי":
        st.markdown("<div class='section-header'>עמוד ראשי - מנהל חברה</div>", unsafe_allow_html=True)
        st.write("מעקב אחר תשלומים וסטטוס פרויקטים.")

    elif page == "תשלומים":
        st.markdown("<div class='section-header'>תשלומים</div>", unsafe_allow_html=True)
        payment_data = pd.DataFrame({
            "לקוח": ["לקוח א", "לקוח ב"],
            "סכום ששולם": ["10,000", "15,000"],
            "יתרה לתשלום": ["5,000", "2,000"]
        })
        st.table(payment_data)

    elif page == "ארכיון פרויקטים":
        st.markdown("<div class='section-header'>ארכיון פרויקטים</div>", unsafe_allow_html=True)
        archive_data = pd.DataFrame({
            "פרויקט": ["פרויקט 1", "פרויקט 2"],
            "תאריך התחלה": ["01/01/2023", "05/03/2023"],
            "תאריך סיום": ["15/02/2023", "20/04/2023"]
        })
        st.table(archive_data)

if __name__ == "__main__":
    main()
