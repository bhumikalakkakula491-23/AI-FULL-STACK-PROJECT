import streamlit as st
from datetime import date

# Page configuration
st.set_page_config(
    page_title="StudyGenius AI",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 StudyGenius AI")
st.subheader("Smart Study Planner")

st.write(
    "Plan your studies, manage your subjects, "
    "and improve your learning with AI."
)

# Sidebar
st.sidebar.title("📌 Menu")

menu = st.sidebar.selectbox(
    "Select a page",
    [
        "Dashboard",
        "Add Study Task",
        "AI Study Planner",
        "Progress"
    ]
)

# Dashboard
if menu == "Dashboard":

    st.header("🏠 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📚 Subjects", 0)

    with col2:
        st.metric("📝 Tasks", 0)

    with col3:
        st.metric("✅ Completed", 0)

    st.info(
        "Welcome to StudyGenius AI! "
        "Start by adding your study tasks."
    )


# Add Study Task
elif menu == "Add Study Task":

    st.header("➕ Add Study Task")

    subject = st.text_input(
        "Subject",
        placeholder="Example: Mathematics"
    )

    topic = st.text_input(
        "Topic",
        placeholder="Example: Integration"
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    study_hours = st.number_input(
        "Study Hours",
        min_value=0.5,
        max_value=12.0,
        value=1.0,
        step=0.5
    )

    target_date = st.date_input(
        "Target Date",
        value=date.today()
    )

    if st.button("➕ Add Task"):

        if subject and topic:

            st.success(
                f"Task added: {subject} - {topic}"
            )

        else:

            st.warning(
                "Please enter both subject and topic."
            )


# AI Study Planner
elif menu == "AI Study Planner":

    st.header("🤖 AI Study Planner")

    st.write(
        "Enter your subjects and available study time. "
        "StudyGenius AI will create a personalized plan."
    )

    subjects = st.text_area(
        "Enter your subjects",
        placeholder="""Mathematics - Integration
Physics - Thermodynamics
Computer Science - Data Structures
English - Grammar"""
    )

    hours = st.slider(
        "Available study hours per day",
        1,
        12,
        4
    )

    exam_date = st.date_input(
        "Exam Date",
        value=date.today()
    )

    if st.button("🚀 Generate Study Plan"):

        if not subjects:

            st.warning(
                "Please enter your subjects."
            )

        else:

            st.success(
                "Study plan generated!"
            )

            st.markdown(
                f"""
                ### 📅 Your Study Plan

                **Exam Date:** {exam_date}

                **Available Hours:** {hours} hours/day

                #### 📚 Subjects

                {subjects}

                #### 🎯 Recommended Schedule

                - 🕐 1 hour – Difficult topic
                - 🕐 1 hour – Practice questions
                - ☕ 15 minutes – Break
                - 🕐 1 hour – Second subject
                - 🕐 1 hour – Revision

                #### 💡 Study Tips

                1. Start with difficult topics.
                2. Take regular breaks.
                3. Practice questions every day.
                4. Revise previous topics.
                5. Take a mock test before the exam.
                """
            )


# Progress
elif menu == "Progress":

    st.header("📈 Study Progress")

    progress = st.slider(
        "Your study progress",
        0,
        100,
        0
    )

    st.progress(progress)

    st.write(
        f"You have completed {progress}% of your study plan."
    )

    if progress >= 80:

        st.success(
            "🎉 Excellent progress! Keep going!"
        )

    elif progress >= 50:

        st.info(
            "👍 Good progress. Keep studying!"
        )

    else:

        st.warning(
            "💪 Keep working. You can do it!"
        )


# Footer
st.sidebar.divider()

st.sidebar.caption(
    "StudyGenius AI © 2026"
)