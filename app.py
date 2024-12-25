import streamlit as st

# Function to render the timeline
def render_timeline():
    st.header("ציר זמן - התקדמות פרויקט")
    st.markdown("""
    **שלבים:**
    1. פרויקט בתהליך רישוי 🔵
    2. פרויקט ממתין להתקנה 🟠
    3. פרויקט בתהליך התקנה 🟡
    4. פרויקט הושלם ✅
    """)
    st.progress(75)  # Example progress

# Function to render the projects table for project managers
def render_projects_table():
    st.header("רשימת פרויקטים פעילים")
    data = {
        "שם הלקוח": ["חנה ניסים", "דניאל ניסים", "שגית ויוסי"],
        "סטטוס": ["בהתקנה", "המתנה לחיבור", "הושלם"],
        "תאריך התחלה": ["25.8.24", "21.10.24", "29.9.24"],
        "תאריך סיום משוער": ["5.1.25", "18.12.24", "19.11.24"],
    }
    st.table(data)

# Main function
def main():
    st.set_page_config(page_title="מערכת CRM", layout="wide")

    st.title("מערכת CRM - אב טיפוס")

    # Login screen
    user_type = st.radio("בחר סוג התחברות:", ["לקוח", "מנהל פרויקט", "מנהל חברה"])
    username = st.text_input("הכנס שם משתמש")
    if st.button("התחבר"):
        if username:
            st.success(f"שלום, {username}!")
            if user_type == "לקוח":
                st.sidebar.title("תפריט לקוחות")
                st.sidebar.button("ניהול מסמכים")
                st.sidebar.button("מעקב סטטוס פרויקט")
                st.sidebar.button("תשלומים")
                render_timeline()
            elif user_type == "מנהל פרויקט":
                st.sidebar.title("תפריט מנהל פרויקט")
                st.sidebar.button("רשימת פרויקטים פעילים")
                render_projects_table()
            elif user_type == "מנהל חברה":
                st.sidebar.title("תפריט מנהל חברה")
                st.sidebar.button("ניהול מלאי")
                st.sidebar.button("דוחות ביצועים")
                st.sidebar.button("תיעוד פרויקטים")
        else:
            st.error("יש להכניס שם משתמש כדי להתחבר.")

if __name__ == "__main__":
    main()
