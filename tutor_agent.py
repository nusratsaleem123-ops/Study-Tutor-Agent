import os

from crewai import Agent, Task, Crew, LLM

from tools import calculator, current_datetime
from memory import create_memory


def create_tutor():

    # Check Groq API key
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError(
            "GROQ_API_KEY is not configured. "
            "Please add it to your environment variables."
        )

    # Groq LLM
    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        temperature=0.3,
    )

    # CrewAI memory
    memory = create_memory()

    # Study Tutor Agent
    tutor = Agent(
        role="Personal Study Tutor",

        goal=(
            "Help students understand academic concepts, "
            "practice effectively, and learn from their mistakes."
        ),

        backstory=(
            "You are a patient, encouraging and knowledgeable "
            "personal tutor. You explain difficult ideas in simple "
            "language. You adapt your teaching style to the student's "
            "level and never make the student feel embarrassed about "
            "making mistakes."
        ),

        llm=llm,

        tools=[
            calculator,
            current_datetime,
        ],

        memory=True,

        verbose=False,

        allow_delegation=False,
    )

    return tutor, memory


def ask_tutor(
    question,
    subject,
    level,
    response_style,
    student_context=""
):

    tutor, memory = create_tutor()

    task_description = f"""
You are tutoring a student.

Student question:
{question}

Subject:
{subject}

Student level:
{level}

Preferred response style:
{response_style}

Previous student context:
{student_context}

Your job is to teach, not simply provide an answer.

Follow these rules:

1. Explain the concept clearly.
2. Use language appropriate for the student's level.
3. Use examples when useful.
4. If this is a mathematical problem, show the solution step-by-step.
5. If the student appears to have made a mistake, explain the mistake
   and how to correct it.
6. Encourage the student to understand the reasoning.
7. Do not shame or criticize the student.
8. Use the Calculator tool whenever accurate arithmetic is needed.
9. Use the Current Date and Time tool when the question requires
   the current date or time.
10. If you are uncertain about something, clearly say so.

Give a useful educational response.
"""

    task = Task(
        description=task_description,

        expected_output=(
            "A clear educational answer that explains the concept, "
            "provides reasoning and examples where appropriate, "
            "and helps the student learn."
        ),

        agent=tutor,
    )

    crew = Crew(
        agents=[tutor],

        tasks=[task],

        memory=memory,

        verbose=False,
    )

    result = crew.kickoff()

    return str(result)
