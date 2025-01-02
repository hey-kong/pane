from llm.llm_inference import LLMInference

LLM_PROVIDER = "ollama"
LLM_MODEL = "llama3.2:3b"

llm_client = LLMInference(LLM_PROVIDER, LLM_MODEL)


def evaluate_chunk_relevance(passage, query):
    prompt = f"""

    Passage: {passage}

    Query: {query}

    You are an expert in evaluating passages for their relevance in answering user queries.
    Your task is to analyze a given passage and query and determine whether the passage is helpful for answering the query?
    Only return True or False:
        - True: If the passage provides information relevant to the query.
        - False: If passage does not provide information relevant to the query.
    Do not include any explanation, punctuation, or additional content.

    Answer:
    """

    return llm_client.generate(prompt)


def evaluate_chunk_completeness(passage, query):
    prompt = f"""

    Passage: {passage}

    Query: {query}

    You are an expert in evaluating passages for their completeness in answering user queries.
    Your task is to determine whether the passage contains enough information to completely and accurately answer the query.
    Only return True or False:
        - True: If the passage has all necessary details to answer the query.
        - False: If the passage lacks important information needed to answer the query.
    Do not include any explanation, punctuation, or additional content.

    Answer:
    """

    return llm_client.generate(prompt)