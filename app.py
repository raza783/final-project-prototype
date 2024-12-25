import streamlit as st
from streamlit_option_menu import option_menu

# עיצוב כללי
st.set_page_config(page_title="הבית הירוק - מערכת ניהול", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #2d572c;
    }
    .stButton>button {
        background-color: #2d572c;
        color: white;
        border-radius: 5px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #4caf50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def customer_dashboard():
    selected = option_menu(
        menu_title="תפריט לקוח",
        options=["עמוד ראשי", "סטטוס פרויקט", "ניהול מסמכים", "אגרות"],
        icons=["house", "bar-chart", "file-text", "wallet"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"background-color": "#2d572c"},
            "nav-link": {"font-size": "18px", "text-align": "center", "margin": "5px", "color": "white"},
            "nav-link-selected": {"background-color": "#4caf50"},
        },
    )

    if selected == "עמוד ראשי":
        st.header("שלום, לקוח יקר")
        st.subheader("סטטוס פרויקט")
        st.progress(0.6)  # התקדמות לדוגמה
        st.info("שלב נוכחי: ממתין להתקנה")

        st.subheader("מסמכים נדרשים")
        st.write("- חוזה התקשרות: הושלם")
        st.write("- תוכנית הנדסית: ממתין למילוי")

        st.subheader("התראות אגרות")
        st.warning("יש לשלם את אגרת החיבור עד לתאריך 5.1")

    elif selected == "סטטוס פרויקט":
        st.header("סטטוס פרויקט")
        st.write("ציר הזמן מציג את מצב הפרויקט בשלבים הבאים:")
        timeline = {
            "תהליך רישוי": "הושלם",
            "ממתין להתקנה": "פעיל",
            "חיבור לרשת": "טרם החל",
        }
        for stage, status in timeline.items():
            st.write(f"{stage}: {status}")

    elif selected == "ניהול מסמכים":
        st.header("ניהול מסמכים")
        st.write("רשימת המסמכים הנדרשים:")
        documents = ["חוזה התקשרות", "תוכנית הנדסית", "אישור בנייה"]
        for doc in documents:
            st.write(f"- {doc}: [העלה מסמך](#)")

    elif selected == "אגרות":
        st.header("אגרות")
        st.write("סיכום תשלומים:")
        st.write("- אגרת רישום: שולם")
        st.write("- אגרת היתר: ממתין לתשלום")
        st.write("- אגרת חיבור: טרם שולם")
        st.markdown("[לתשלום לחץ כאן](https://www.example.com)")

def project_manager_dashboard():
    selected = option_menu(
        menu_title="תפריט מנהל פרויקטים", 
        options=["עמוד ראשי", "פרויקטים פעילים", "ארכיון פרויקטים", "ניהול מסמכים"], 
        icons=["house", "list-task", "archive", "upload"], 
        menu_icon="cast", 
        default_index=0, 
        orientation="horizontal",
        styles={
            "container": {"background-color": "#2d572c"},
            "nav-link": {"font-size": "18px", "text-align": "center", "margin": "5px", "color": "white"},
            "nav-link-selected": {"background-color": "#4caf50"},
        },
    )

    if selected == "עמוד ראשי":
        st.header("עמוד ראשי")
        st.write("סטטוס כללי של פרויקטים פעילים.")
        st.progress(0.5)

    elif selected == "פרויקטים פעילים":
        st.header("פרויקטים פעילים")
        st.write("רשימת פרויקטים פעילים בשלבים שונים.")

    elif selected == "ארכיון פרויקטים":
        st.header("ארכיון פרויקטים")
        st.write("פרויקטים שהושלמו.")

    elif selected == "ניהול מסמכים":
        st.header("ניהול מסמכים")
        st.write("אפשרות להעלאת מסמכים ובדיקתם.")

# דשבורד מנהל חברה (יישום דומה)
def company_manager_dashboard():
    pass  # ניתן להוסיף פונקציות דומות בהתאם לדרישות

# התחלה
st.title("מערכת ניהול - הבית הירוק")
role = st.selectbox("בחר את סוג המשתמש:", ["לקוח", "מנהל פרויקטים", "מנהל חברה"])

if role == "לקוח":
    customer_dashboard()
elif role == "מנהל פרויקטים":
    project_manager_dashboard()
elif role == "מנהל חברה":
    company_manager_dashboard()
