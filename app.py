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
        **סטטוס פרויקט:**
        - פרויקט כרגע במצב ממתין להתקנה.
        """)
        st.progress(50)  # Example project progress
        st.markdown("""
        **מסמכים נדרשים לטיפול:**
        - אישור חשמל (ממתין למילוי)
        - חוזה התקשרות (הושלם)
        """)
        st.markdown("""
        **התראות עבור תשלומי אגרות:**
        - אגרת רישום: ₪500 (מועד אחרון לתשלום: 5.1)
        """)
    elif choice == "ניהול מסמכים":
        st.subheader("ניהול מסמכים")
        data = {
            "מסמך": ["חוזה התקשרות", "אישור חשמל", "תעודת זהות"],
            "סטטוס": ["הושלם", "ממתין למילוי", "הושלם"],
            "הנחיות למילוי": ["חתום על ידי שני הצדדים", "חתום וחתום ע״י עורך דין", "צילום קריא"]
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
        **סך כל האגרות:** ₪1500
        - **אגרת רישום:** ₪500 (שולם)
        - **אגרת היתר:** ₪700 (ממתין לתשלום)
        - **אגרת חיבור לרשת:** ₪300 (ממתין לתשלום)
        """)
        st.markdown("[לחץ כאן לתשלום בפורטל חברת החשמל](https://example.com)")

# Function to render the project manager dashboard
def project_manager_dashboard():
    st.sidebar.title("תפריט מנהל פרויקטים")
    choice = st.sidebar.radio(
        "בחר פעולה:",
        ["עמוד ראשי", "רשימת פרויקטים פעילים", "פרויקטים גמורים", "העלאת מסמכים"]
    )
    if st.sidebar.button("התנתק"):
        st.session_state["user_type"] = None
        st.session_state["username"] = None

    st.header(f"שלום, {st.session_state['username']}!")

    if choice == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.markdown("""
        **פרויקטים פעילים:**
        - פרויקט א: ממתין למסמכים
        - פרויקט ב: התקנה בתהליך
        """)
        st.markdown("""
        **משימות לטיפול:**
        - בדיקת מסמכי הלקוח לפרויקט א.
        - ווידוא תשלום אגרה לפרויקט ב.
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
    elif choice == "פרויקטים גמורים":
        st.subheader("פרויקטים גמורים")
        data = {
            "שם הלקוח": ["שגית ויוסי", "מרטין מפלסים"],
            "תאריך התחלה": ["21.10.24", "29.9.24"],
            "תאריך סיום": ["18.12.24", "19.11.24"],
            "מסמכים": ["הושלמו", "הושלמו"]
        }
        st.table(data)
    elif choice == "העלאת מסמכים":
        st.subheader("העלאת מסמכים")
        uploaded_file = st.file_uploader("העלה מסמך")
        if uploaded_file:
            st.write("מסמך הועלה בהצלחה!")

# Function to render the company manager dashboard
def company_manager_dashboard():
    st.sidebar.title("תפריט מנהל חברה")
    choice = st.sidebar.radio(
        "בחר פעולה:",
        ["עמוד ראשי", "סטטוס פרויקטים", "ארכיון פרויקטים", "תשלומים מלקוחות"]
    )
    if st.sidebar.button("התנתק"):
        st.session_state["user_type"] = None
        st.session_state["username"] = None

    st.header(f"שלום, {st.session_state['username']}!")

    if choice == "עמוד ראשי":
        st.subheader("עמוד ראשי")
        st.markdown("""
        **רווח חודשי ממוצע:** ₪200,000
        **מספר פרויקטים חדשים:** 5
        """)
    elif choice == "סטטוס פרויקטים":
        st.subheader("סטטוס פרויקטים")
        st.markdown("כאן תוכל לצפות בסטטוס כלל הפרויקטים.")
    elif choice == "ארכיון פרויקטים":
        st.subheader("ארכיון פרויקטים")
        st.markdown("כאן תוכל לגשת לתיעוד הפרויקטים שהושלמו.")
    elif choice == "תשלומים מלקוחות":
        st.subheader("תשלומים מלקוחות")
        st.markdown("כאן תוכל לראות את כלל התשלומים של הלקוחות.")

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
