import streamlit as st

# פונקציה לעיצוב העמודים
def set_page_config():
    st.set_page_config(
        page_title="מערכת ניהול - הבית הירוק",
        page_icon=":seedling:",
        layout="wide",
    )
    st.markdown(
        """
        <style>
        body {
            background-color: #f0fff0;
            color: #2f4f4f;
        }
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #006400;
        }
        .sub-header {
            font-size: 1.5rem;
            color: #006400;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# פונקציה לעמוד ההתחברות
def login_page():
    st.title("מערכת הבית הירוק לניהול פרויקטים")
    st.subheader("ברוכים הבאים!")
    st.write("אנא בחרו את סוג המשתמש והתחברו.")
    
    user_type = st.radio(
        "בחר סוג משתמש",
        ["לקוח", "מנהל פרויקטים", "מנהל חברה"]
    )
    
    username = st.text_input("שם משתמש")
    if st.button("התחבר"):
        if username.strip():
            st.session_state["user_type"] = user_type
            st.session_state["username"] = username.strip()
            st.session_state["logged_in"] = True
        else:
            st.error("אנא הזינו שם משתמש.")

# עמוד הבית של לקוח
def customer_dashboard():
    st.markdown(f"### שלום, {st.session_state['username']}!")
    st.subheader("עמוד ראשי - לקוח")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**סטטוס פרויקט:**")
        st.progress(0.5)
        st.write("ממתין להתקנה")
    with col2:
        st.write("**התראות:**")
        st.warning("יש לשלם אגרת רישום עד 5.1")
    
    if st.button("התנתק"):
        st.session_state["logged_in"] = False

# עמוד סטטוס פרויקט
def project_status():
    st.subheader("סטטוס פרויקט")
    st.write("ציר זמן המציג את שלבי הפרויקט:")
    stages = ["בתהליך רישוי", "ממתין להתקנה", "בהתקנה", "הושלם"]
    progress = [0.25, 0.5, 0.75, 1.0]
    for stage, prog in zip(stages, progress):
        st.write(f"{stage} - {prog * 100:.0f}%")
        st.progress(prog)

# עמוד ניהול מסמכים
def document_management():
    st.subheader("ניהול מסמכים")
    st.write("כאן תוכלו להעלות מסמכים נדרשים ולצפות במסמכים קיימים.")
    col1, col2 = st.columns(2)
    with col1:
        st.write("מסמכים הושלמו:")
        st.success("צילום תעודת זהות")
    with col2:
        st.write("מסמכים נדרשים:")
        st.warning("חתימה על הסכם")

# עמוד התשלומים
def payments():
    st.subheader("תשלומים")
    st.write("סטטוס התשלומים שלכם:")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**אגרות ששולמו:**")
        st.success("אגרת רישום")
    with col2:
        st.write("**אגרות פתוחות:**")
        st.warning("אגרת חיבור לרשת")
    
    if st.button("תשלום אגרות"):
        st.write("מעבר לפורטל חברת החשמל")

# פונקציה לניווט
def navigation():
    if st.session_state["user_type"] == "לקוח":
        menu = st.sidebar.radio(
            "ניווט",
            ["עמוד ראשי", "סטטוס פרויקט", "ניהול מסמכים", "תשלומים"]
        )
        if menu == "עמוד ראשי":
            customer_dashboard()
        elif menu == "סטטוס פרויקט":
            project_status()
        elif menu == "ניהול מסמכים":
            document_management()
        elif menu == "תשלומים":
            payments()
    else:
        st.write("ממשק מנהלים בפיתוח...")

# הגדרת עמוד
set_page_config()

# לוגיקת התחברות וניווט
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    navigation()
else:
    login_page()
