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

# Main dashboard for each user type
def client_dashboard(username):
    st.sidebar.title("תפריט לקוחות")
    st.sidebar.button("ניהול מסמכים")
    st.sidebar.button("מעקב סטטוס פרויקט")
    st.sidebar.button("תשלומים")
    st.success(f"שלום, {username}!")
    render_timeline()

def project_manager_dashboard(username):
    st.sidebar.title("תפריט מנהל פרויקט")
    st.sidebar.button("רשימת פרויקטים פעילים")
    st.sidebar.button("ניהול מלאי")
    st.sidebar.button("עדכון סטטוס")
    st.success(f"שלום, {username}!")
    render_projects_table()

def company_manager_dashboard(username):
    st.sidebar.title("תפריט מנהל חברה")
    st.sidebar.button("ניהול מלאי")
    st.sidebar.button("דוחות ביצועים")
    st.sidebar.button("תיעוד פרויקטים")
    st.success(f"שלום, {username}!")
    st.info("כאן תוכל לראות דוחות ותיעוד שונים עבור החברה.")

# Login function
def login_page():
    st.title("מסך התחברות")
    user_type = st.radio("בחר סוג התחברות:", ["לקוח", "מנהל פרויקט", "מנהל חברה"])
    username = st.text_input("הכנס שם משתמש")
    if st.button("התחבר"):
        if username:
            return user_type, username
        else:
            st.error("יש להכניס שם משתמש כדי להתחבר.")
            return None, None
    return None, None

# Main function
def main():
    st.set_page_config(page_title="מערכת CRM", layout="wide")

    user_type, username = login_page()
    if user_type and username:
        if user_type == "לקוח":
            client_dashboard(username)
        elif user_type == "מנהל פרויקט":
            project_manager_dashboard(username)
        elif user_type == "מנהל חברה":
            company_manager_dashboard(username)

if __name__ == "__main__":
    main()
