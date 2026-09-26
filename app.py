import os
import streamlit as st

# Connect Streamlit Cloud secret to the environment variable
try:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

from tutor_agent import ask_tutor


# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🎓",
    layout="wide",
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(0, 220, 255, 0.12),
                transparent 35%
            ),
            radial-gradient(
                circle at top right,
                rgba(0, 100, 255, 0.10),
                transparent 35%
            ),
            #07111f;
        color: #ffffff;
    }

    .main-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #ffffff;
        text-shadow:
            0 0 10px rgba(0, 220, 255, 0.7),
            0 0 30px rgba(0, 220, 255, 0.35);
    }

    .subtitle {
        text-align: center;
        color: #a8c7d9;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .feature-card {
        background: rgba(10, 25, 45, 0.75);
        border: 1px solid rgba(0, 220, 255, 0.25);
        border-radius: 18px;
        padding: 22px;
        min-height: 150px;
        box-shadow:
            0 0 20px rgba(0, 180, 255, 0.08);
    }

    .feature-title {
        font-size: 20px;
        font-weight: 700;
        color: #00d9ff;
        margin-bottom: 8px;
    }

    .feature-text {
        color: #b9cddd;
        font-size: 14px;
        line-height: 1.6;
    }

    .status-card {
        background: rgba(8, 20, 35, 0.9);
        border: 1px solid rgba(0, 220, 255, 0.2);
        border-radius: 14px;
        padding: 15px;
        margin-bottom: 20px;
    }

    .status-title {
        color: #00d9ff;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .status-item {
        color: #b8c9d8;
        font-size: 14px;
        margin: 6px 0;
    }

    .stChatMessage {
        border-radius: 15px;
    }

    [data-testid="stSidebar"] {
        background: #081522;
        border-right: 1px solid rgba(0, 220, 255, 0.15);
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #00d9ff;
    }

    @media (max-width: 768px) {

        .main-title {
            font-size: 34px;
        }

        .subtitle {
            font-size: 15px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown("## 🎓 Study Tutor AI")

    st.markdown("---")

    subject = st.selectbox(
        "📚 Subject",
        [
            "General",
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "Computer Science",
            "English",
            "Accounting",
            "Economics",
        ],
    )

    level = st.selectbox(
        "🎯 Student Level",
        [
            "Beginner",
            "School",
            "IGCSE",
            "Intermediate",
            "University",
        ],
    )

    response_style = st.selectbox(
        "💬 Teaching Style",
        [
            "Simple Explanation",
            "Step-by-Step",
            "Detailed",
            "Exam Focused",
            "With Examples",
        ],
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="status-card">
            <div class="status-title">⚡ AI Tutor Status</div>

            <div class="status-item">
                🧠 Memory: Active
            </div>

            <div class="status-item">
                🛠️ Tools: Ready
            </div>

            <div class="status-item">
                🤖 Groq AI: Connected
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">Study Smarter with AI 🎓</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'Your personal AI study tutor powered by CrewAI and Groq'
    '</div>',
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">📖 Learn Anything</div>
            <div class="feature-text">
                Ask questions about your subjects and
                get explanations in simple language.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">🧠 Personalized Learning</div>
            <div class="feature-text">
                The tutor adapts explanations to your
                selected level and teaching style.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">✏️ Practice & Improve</div>
            <div class="feature-text">
                Practice questions, understand mistakes,
                and improve your learning.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<br>", unsafe_allow_html=True)


# ---------------------------------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------------

question = st.chat_input(
    "Ask your Study Tutor a question..."
)


# ---------------------------------------------------------
# ASK THE AI TUTOR
# ---------------------------------------------------------

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🧠 Thinking..."):

            try:

                answer = ask_tutor(
                    question=question,
                    subject=subject,
                    level=level,
                    response_style=response_style,
                    student_context="",
                )

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

            except Exception as e:

                error_message = (
                    "⚠️ Something went wrong.\n\n"
                    f"Error: `{str(e)}`"
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                    }
                )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#78909c;">
        Study Tutor AI • Built with Streamlit + CrewAI + Groq
    </div>
    """,
    unsafe_allow_html=True,
)
