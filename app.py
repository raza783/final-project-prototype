import streamlit as st

# App state to manage logged-in user
if "user_type" not in st.session_state:
    st.session_state["user_type"] = None
if "username" not in st.session_state:
    st.session_state["username"] = None

# Function to render the client dashboard
def client_dashboard():
    st.sidebar.title("תפריט לקוחות")
    choice = st.sidebar.radio(
        "בחר פעולה:",
        ["עמוד ראשי", "ניהול מסמכים", "מעקב סטטוס פרויקט", "תשלומים"]
    )
    if st.sidebar.button("התנתק"):
        st.session_state["user_type"] = None
        st.session_state["username"] = None

    st.header(f"שלום, {st.session_state['username']}!")

    if choice == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.markdown("""
        - **סטטוס פרויקט**: פרויקט כרגע במצב ממתין להתקנה.
        - **התראות:** יש לשלם אגרה עד לתאריך 5.1.
        """)
        st.progress(50)  # Example project progress
    elif choice == "ניהול מסמכים":
        st.subheader("ניהול מסמכים")
        data = {
            "מסמך": ["חוזה התקשרות", "אישור חשמל", "תעודת זהות"],
            "סטטוס": ["הושלם", "ממתין למילוי", "הושלם"]
        }
        st.table(data)
    elif choice == "מעקב סטטוס פרויקט":
        st.subheader("מעקב סטטוס פרויקט")
        st.markdown("""
        **ציר זמן:**
        1. תהליך רישוי 🔵
        2. ממתין להתקנה 🟠
        3. התקנה בתהליך 🟡
        4. הושלם ✅
        """)
        st.progress(50)
    elif choice == "תשלומים":
        st.subheader("תשלומים")
        st.markdown("""
        - **אגרות פתוחות לתשלום:**
            - אגרה 1: ₪500 (מועד אחרון לתשלום: 5.1)
        - **יתרה לתשלום:** ₪2000
        """)

# Function to render the project manager dashboard
def project_manager_dashboard():
    st.sidebar.title("תפריט מנהל פרויקטים")
    choice = st.sidebar.radio(
        "בחר פעולה:",
        ["עמוד ראשי", "רשימת פרויקטים פעילים", "ניהול מלאי", "עדכון סטטוס"]
    )
    if st.sidebar.button("התנתק"):
        st.session_state["user_type"] = None
        st.session_state["username"] = None

    st.header(f"שלום, {st.session_state['username']}!")

    if choice == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.markdown("""
        - **פרויקטים פעילים:** 15
        - **פרויקטים ממתינים:** 3
        """)
    elif choice == "רשימת פרויקטים פעילים":
        st.subheader("רשימת פרויקטים פעילים")
        data = {
            "שם הלקוח": ["חנה ניסים", "דניאל ניסים", "שגית ויוסי"],
            "סטטוס": ["בהתקנה", "ממתין לחיבור", "הושלם"],
            "תאריך התחלה": ["25.8.24", "21.10.24", "29.9.24"],
            "תאריך סיום משוער": ["5.1.25", "18.12.24", "19.11.24"],
        }
        st.table(data)
    elif choice == "ניהול מלאי":
        st.subheader("ניהול מלאי")
        st.markdown("""
        - **מלאי נוכחי:** 500 פאנלים.
        - **מלאי להזמנה:** 200 פאנלים.
        """)
    elif choice == "עדכון סטטוס":
        st.subheader("עדכון סטטוס")
        st.markdown("כאן תוכל לעדכן את הסטטוס של פרויקטים פעילים.")

# Function to render the company manager dashboard
def company_manager_dashboard():
    st.sidebar.title("תפריט מנהל חברה")
    choice = st.sidebar.radio(
        "בחר פעולה:",
        ["עמוד ראשי", "דוחות ביצועים", "ניהול מלאי", "תיעוד פרויקטים"]
    )
    if st.sidebar.button("התנתק"):
        st.session_state["user_type"] = None
        st.session_state["username"] = None

    st.header(f"שלום, {st.session_state['username']}!")

    if choice == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.markdown("""
        - **רווח חודשי ממוצע:** ₪200,000
        - **מספר פרויקטים חדשים:** 5
        """)
    elif choice == "דוחות ביצועים":
        st.subheader("דוחות ביצועים")
        st.markdown("כאן תוכל לצפות בדוחות ביצועים של החברה.")
    elif choice == "ניהול מלאי":
        st.subheader("ניהול מלאי")
        st.markdown("""
        - **מלאי נוכחי:** 500 פאנלים.
        - **מלאי להזמנה:** 200 פאנלים.
        """)
    elif choice == "תיעוד פרויקטים":
        st.subheader("תיעוד פרויקטים")
        st.markdown("כאן תוכל לגשת לתיעוד הפרויקטים שהושלמו.")

# Login function
def login_page():
    st.title("מסך התחברות")
    user_type = st.radio("בחר סוג התחברות:", ["לקוח", "מנהל פרויקט", "מנהל חברה"])
    username = st.text_input("הכנס שם משתמש")
    if st.button("התחבר"):
        if username:
            st.session_state["user_type"] = user_type
            st.session_state["username"] = username

# Main function
def main():
    st.set_page_config(page_title="מערכת CRM", layout="wide")
    
    if st.session_state["user_type"] is None:
        login_page()
    else:
        if st.session_state["user_type"] == "לקוח":
            client_dashboard()
        elif st.session_state["user_type"] == "מנהל פרויקט":
            project_manager_dashboard()
        elif st.session_state["user_type"] == "מנהל חברה":
            company_manager_dashboard()

if __name__ == "__main__":
    main()
