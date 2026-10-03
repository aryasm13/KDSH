one_shot_rag_qa_docs = (
    """Title: The Last Horse\nThe Last Horse (Spanish:El último caballo) is a 1950 Spanish comedy film directed by Edgar Neville starring Fernando Fernán Gómez.\n"""
    """Title: Southampton\nThe University of Southampton, which was founded in 1862 and received its Royal Charter as a university in 1952...\n"""
    """Title: Neville A. Stanton\nNeville A. Stanton is a British Professor of Human Factors and Ergonomics at the University of Southampton...\n"""
)


rag_qa_system = (
    '''
    ### Role
    You are an expert narrative consistency explanation system.

    ### Task
    You are given narrative evidence in three forms:
    - detailed article excerpts
    - semantic summaries
    - timeline summaries

    Along with a **combined query** that includes:
    - a character name
    - a hypothetical backstory
    - a consistency label (Consistent or Contradictory)

    Your task is NOT to decide the label,
    but to explain **why the backstory matches or does not match the narrative**.

    ---

    ### Detail Article
    {context}

    ### Summary by Semantic
    {semantic_summary}
    
    ### Summary by Timeline
    {timeline_summary}

    ### Query
    {question}

    ---

    ### Response Rules
    - Output ONLY a short reasoning (1–2 lines)
    - Do NOT output the label
    - Do NOT include headings, bullet points, or formatting
    - Do NOT introduce new facts
    - Base reasoning strictly on the provided materials
    - If explicit evidence is missing, explain the mismatch using:
      semantic inconsistency, thematic misalignment, or lack of narrative support
    '''
)



one_shot_rag_qa_input = (
    f"{one_shot_rag_qa_docs}"
    "\n\nQuery:\n"
    "Character: Neville A. Stanton\n"
    "Backstory: Neville A. Stanton has always worked at institutions founded after 1950.\n"
    "Label: Contradictory\n"
)


one_shot_rag_qa_output = (
    "Neville A. Stanton is employed by the University of Southampton, which is stated to have been founded in 1862, so the backstory does not align with his documented professional history."
)


prompt_template = [
    {"role": "system", "content": rag_qa_system},
    {"role": "user", "content": one_shot_rag_qa_input},
    {"role": "assistant", "content": one_shot_rag_qa_output},
    {"role": "user", "content": "${prompt_user} "}
]
