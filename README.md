# 🎓 Study Tutor Agent

An AI-powered personal study tutor built with:

- Streamlit
- CrewAI
- Groq
- CrewAI Memory
- Hugging Face embeddings

## Features

- Ask academic questions
- Explain concepts
- Step-by-step explanations
- Different student levels
- Calculator tool
- Date/time tool
- Student conversation context
- CrewAI memory

## Architecture

Student
↓
Streamlit
↓
CrewAI Study Tutor Agent
↓
Tools + Memory
↓
Groq LLM

## Environment Variable

The application requires:

GROQ_API_KEY

Never put the API key directly inside the source code.

## Run

Streamlit starts the application using:

streamlit run app.py
