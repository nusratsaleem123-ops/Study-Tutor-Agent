from crewai import Memory


def create_memory():
    """
    Create the CrewAI memory system.

    Groq is used for the LLM.
    Hugging Face is used for embeddings.
    """

    memory = Memory(
        llm="groq/openai/gpt-oss-120b",

        embedder={
            "provider": "huggingface",
            "config": {
                "model_name": "sentence-transformers/all-MiniLM-L6-v2"
            },
        },

        recency_weight=0.3,
        semantic_weight=0.5,
        importance_weight=0.2,
    )

    return memory
