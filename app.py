```python
import streamlit as st

from tutor_agent import ask_tutor


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS — MODERN AI / NEON BLUE THEME
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       GLOBAL
    ------------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(0, 191, 255, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(79, 70, 229, 0.12),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #050816 0%,
                #07111f 50%,
                #050816 100%
            );

        color: #f8fafc;
    }

    /* Main content width */

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #07111f 0%,
                #050816 100%
            );

        border-right: 1px solid rgba(0, 212, 255, 0.18);
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {

        color: #f8fafc;
    }


    /* -------------------------------------------------------
       HEADER
    ------------------------------------------------------- */

    .hero {

        padding: 28px 32px;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(0, 212, 255, 0.12),
                rgba(99, 102, 241, 0.08)
            );

        border: 1px solid rgba(0, 212, 255, 0.22);

        box-shadow:
            0 0 35px rgba(0, 212, 255, 0.08);

        margin-bottom: 25px;
    }


    .hero-title {

        font-size: 42px;
        font-weight: 800;

        margin: 0;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #67e8f9,
                #38bdf8
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .hero-subtitle {

        margin-top: 8px;

        color: #94a3b8;

        font-size: 16px;
    }


    /* -------------------------------------------------------
       FEATURE CARDS
    ------------------------------------------------------- */

    .feature-card {

        padding: 20px;

        min-height: 130px;

        border-radius: 18px;

        background:
            rgba(15, 23, 42, 0.72);

        border: 1px solid rgba(148, 163, 184, 0.12);

        box-shadow:
            0 8px 30px rgba(0, 0, 0, 0.20);

        transition: all 0.25s ease;
    }


    .feature-card:hover {

        transform: translateY(-3px);

        border-color:
            rgba(34, 211, 238, 0.35);

        box-shadow:
            0 0 25px rgba(34, 211, 238, 0.10);
    }


    .feature-icon {

        font-size: 27px;
    }


    .feature-title {

        margin-top: 8px;

        font-size: 17px;

        font-weight: 700;

        color: #f8fafc;
    }


    .feature-text {

        margin-top: 5px;

        color: #94a3b8;

        font-size: 13px;
    }


    /* -------------------------------------------------------
       STATUS BADGE
    ------------------------------------------------------- */

    .status-badge {

        display: inline-flex;

        align-items: center;

        gap: 7px;

        padding: 7px 13px;

        border-radius: 999px;

        background:
            rgba(34, 211, 238, 0.08);

        border:
            1px solid rgba(34, 211, 238, 0.25);

        color: #67e8f9;

        font-size: 12px;

        font-weight: 600;
    }


    .status-dot {

        width: 7px;
        height: 7px;

        border-radius: 50%;

        background: #22d3ee;

        box-shadow:
            0 0 10px #22d3ee;
    }


    /* -------------------------------------------------------
       CHAT
    ------------------------------------------------------- */

    [data-testid="stChatMessage"] {

        border-radius: 18px;

        border: 1px solid
            rgba(148, 163, 184, 0.10);

        background:
            rgba(15, 23, 42, 0.58);

        margin-bottom: 12px;

        padding: 12px;
    }


    /* -------------------------------------------------------
       INPUT
    ------------------------------------------------------- */

    [data-testid="stChatInput"] {

        border-radius: 18px;
    }


    [data-testid="stChatInput"] textarea {

        background:
            rgba(15, 23, 42, 0.90) !important;

        color: white !important;

        border:
            1px solid rgba(34, 211, 238, 0.25) !important;
    }


    [data-testid="stChatInput"] textarea:focus {

        border:
            1px solid #22d3ee !important;

        box-shadow:
            0 0 20px rgba(34, 211, 238, 0.15) !important;
    }


    /* -------------------------------------------------------
       BUTTONS
    ------------------------------------------------------- */

    .stButton > button {

        border-radius: 12px;

        border:
            1px solid rgba(34, 211, 238, 0.25);

        background:
            linear-gradient(
                135deg,
                rgba(8, 145, 178, 0.25),
                rgba(37, 99, 235, 0.20)
            );

        color: #e0f2fe;

        font-weight: 600;

        transition: all 0.2s ease;
    }


    .stButton > button:hover {

        border-color: #22d3ee;

        box-shadow:
            0 0 18px rgba(34, 211, 238, 0.18);

        transform: translateY(-1px);
    }


    /* -------------------------------------------------------
       SELECTBOX / INPUTS
    ------------------------------------------------------- */

    div[data-baseweb="select"] > div {

        background:
            rgba(15, 23, 42, 0.75);

        border:
            1px solid rgba(148, 163, 184, 0.15);

        border-radius: 10px;
    }


    /* -------------------------------------------------------
       DIVIDER
    ------------------------------------------------------- */

    hr {

        border-color:
            rgba(148, 163, 184, 0.10);
    }


    /* -------------------------------------------------------
       MEMORY CARD
    ------------------------------------------------------- */

    .memory-card {

        padding: 15px;

        border-radius: 15px;

        background:
            linear-gradient(
                135deg,
                rgba(34, 211, 238, 0.07),
                rgba(59, 130, 246, 0.05)
            );

        border:
            1px solid rgba(34, 211, 238, 0.16);

        color: #cbd5e1;

        font-size: 13px;
    }


    /* -------------------------------------------------------
       FOOTER
    ------------------------------------------------------- */

    .footer {

        text-align: center;

        color: #64748b;

        font-size: 12px;

        padding-top: 35px;
    }


    /* -------------------------------------------------------
       MOBILE
    ------------------------------------------------------- */

    @media (max-width: 768px) {

        .block-container {

            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {

            padding: 22px;
        }

        .hero-title {

            font-size: 30px;
        }

        .hero-subtitle {

            font-size: 14px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


if "student_context" not in st.session_state:

    st.session_state.student_context = ""


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎓 Study Tutor")

    st.caption("Your personal AI learning companion")

    st.divider()

    st.markdown("### 📚 Study Settings")

    subject = st.selectbox(
        "Subject",
        [
            "General",
            "Mathematics",
            "Science",
            "English",
            "Computer Science",
            "Economics",
            "Accounting",
        ],
    )

    level = st.selectbox(
        "Student Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )

    response_style = st.selectbox(
        "Teaching Style",
        [
            "Simple and easy",
            "Step-by-step",
            "Detailed",
            "Exam-focused",
        ],
    )

    st.divider()

    st.markdown("### 🧠 Agent Status")

    st.markdown(
        """
        <div class="memory-card">

        <b>● AI Tutor</b><br><br>

        🧠 Memory: Active<br>
        🛠️ Tools: Ready<br>
        ⚡ Groq: Connected

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True,
    ):

        st.session_state.messages = []

        st.session_state.student_context = ""

        st.rerun()


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="status-badge">

            <span class="status-dot"></span>

            AI TUTOR ONLINE

        </div>

        <div class="hero-title">

            Study Smarter with AI 🎓

        </div>

        <div class="hero-subtitle">

            Learn concepts, practice questions,
            understand your mistakes, and build
            stronger knowledge with your personal AI tutor.

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FEATURE CARDS
# ============================================================

if not st.session_state.messages:

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">📚</div>

                <div class="feature-title">
                    Learn Anything
                </div>

                <div class="feature-text">
                    Get clear explanations adapted
                    to your learning level.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">🧠</div>

                <div class="feature-title">
                    Personalized Memory
                </div>

                <div class="feature-text">
                    Your tutor can remember useful
                    learning context.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">⚡</div>

                <div class="feature-title">
                    Learn by Practice
                </div>

                <div class="feature-text">
                    Ask questions and understand
                    mistakes step by step.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "✨ Ask your Study Tutor anything..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)


    # Recent context

    recent_messages = (
        st.session_state.messages[-8:]
    )

    student_context = "\n".join(
        [
            f'{message["role"]}: '
            f'{message["content"]}'
            for message in recent_messages
        ]
    )


    # AI response

    with st.chat_message("assistant"):

        with st.spinner(
            "🧠 Your AI tutor is thinking..."
        ):

            try:

                answer = ask_tutor(
                    question=question,
                    subject=subject,
                    level=level,
                    response_style=response_style,
                    student_context=student_context,
                )

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

                st.session_state.student_context = (
                    student_context
                )

            except Exception as error:

                st.error(
                    "⚠️ I couldn't generate a response."
                )

                st.caption(
                    f"Technical details: {str(error)}"
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        Built with ❤️ using Streamlit + CrewAI + Groq

    </div>
    """,
    unsafe_allow_html=True,
)
```

### Your resulting interface

The visual hierarchy will be:

```text
┌──────────────────────────────────────────────────────────────┐
│  SIDEBAR       │  ✨ AI TUTOR ONLINE                         │
│                │                                             │
│ 🎓 Study Tutor │  Study Smarter with AI 🎓                   │
│                │  Your personal AI learning companion        │
│ 📚 Subject     │                                             │
│ [Mathematics]  │  ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│                │  │ 📚       │ │ 🧠       │ │ ⚡       │    │
│ 🎯 Level       │  │ Learn    │ │ Memory   │ │ Practice │    │
│ [Beginner]     │  │ Anything │ │          │ │          │    │
│                │  └──────────┘ └──────────┘ └──────────┘    │
│ 🎨 Style       │                                             │
│ [Step-by-step] │                                             │
│                │                                             │
│ 🧠 Agent       │                                             │
│ ● Online       │          💬 AI Conversation                 │
│ Memory Active  │                                             │
│ Tools Ready    │                                             │
│ Groq Connected │                                             │
│                │                                             │
│ 🗑 Clear Chat  │  ✨ Ask your Study Tutor anything...         │
└──────────────────────────────────────────────────────────────┘
```

### One important improvement

I would **not hard-code "Groq: Connected"** in the final production version. Right now it is a visual status indicator. Later, we can make it dynamically show:

* 🟢 Groq Connected
* 🟢 Memory Active
* 🟢 Tools Ready

based on actual application state.

Also, I recommend that we **do not change `tutor_agent.py`, `memory.py`, or `tools.py` yet** just for the visual redesign. Keeping the UI separate from the agent logic is exactly why we made the project modular.

**Next step:** put this `app.py` into your GitHub repository. After that, we can build the **next UI upgrade: a proper "Learn / Practice / Ask Tutor" mode selector and a polished dashboard**, while keeping the CrewAI agent underneath unchanged.
