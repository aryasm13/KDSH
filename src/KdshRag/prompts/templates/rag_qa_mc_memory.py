one_shot_rag_qa_docs = (
    """Title: The Last Horse\nThe Last Horse (Spanish:El último caballo) is a 1950 Spanish comedy film directed by Edgar Neville starring Fernando Fernán Gómez.\n"""
    """Title: Southampton\nThe University of Southampton, which was founded in 1862 and received its Royal Charter as a university in 1952...\n"""
    """Title: Neville A. Stanton\nNeville A. Stanton is a British Professor of Human Factors and Ergonomics at the University of Southampton...\n"""
)




rag_qa_system = (
    '''
    ### Role
    You are an expert narrative verification and reasoning specialist.
    Your role is to determine whether the provided narrative evidence
    is sufficient to justify **why a character backstory is consistent
    or contradictory** with the story.

    You must base your reasoning **strictly on the provided materials**.

    ---

    ### Task
    You are given multiple sources of information:
    - Detailed narrative excerpts
    - Semantic summaries
    - Timeline-based summaries
    - Historical or previously fused information

    Along with a **combined query** that contains:
    - the character name
    - the hypothetical backstory
    - the consistency label (Consistent or Contradictory)

    Your task is to:
    1. Examine all provided evidence
    2. Determine whether the evidence is **sufficient and decisive**
       to justify the given consistency label
    3. If sufficient, provide a clear final answer
    4. If insufficient or ambiguous, output a `"*"` to indicate that
       further retrieval or probing is required

    ---

    ### Detail Article
    {context}

    ### Summary by Semantic
    {semantic_summary}
    
    ### Summary by Timeline
    {timeline_summary}

    ### Query
    {question}

    ### Historical Information
    {historical_infomation}

    ---

    ### Response Format

    1. **Content Understanding**
       - Briefly summarize the most relevant narrative evidence
       - Maximum three sentences
       - Begin with: `### Content Understanding`

    2. **Evidence Analysis**
       - List concrete pieces of evidence related to the backstory claims
       - Focus on character actions, dialogue, thoughts, or events
       - Begin with: `### Evidence Analysis`

    3. **Final Answer**
       - If the evidence clearly supports or contradicts the backstory,
         restate the given consistency label and justify it concisely
       - If the evidence is insufficient or unclear, output only: `*`
       - Begin with: `### Final Answer`

    ---
    
    ### Strict Rules
    - Do NOT introduce new facts
    - Do NOT guess or assume missing information
    - If justification is not possible from the given materials, output `"*"`
    '''
)

rag_qa_system = (
    '''
    ### Role
    You are an expert narrative consistency analysis system.

    Your task is to produce a **short reasoning (1–2 lines)** explaining
    **why a given character backstory matches or does not match the narrative**.

    ---

    ### Task
    You are given:
    - Detailed narrative excerpts
    - A semantic summary
    - A timeline summary
    - A combined query containing:
      - the character name
      - the hypothetical backstory
      - the consistency label (Consistent or Contradictory)

    Your goal is to:
    1. Examine the provided narrative evidence
    2. Compare it against the backstory claims
    3. Output a **concise explanation** describing the match or mismatch

    ---

    ### Detail Article
    {context}

    ### Summary by Semantic
    {semantic_summary}
    
    ### Summary by Timeline
    {timeline_summary}

    ### Query
    {question}

    ### Historical Information
    {historical_infomation}

    ---

    ### Response Rules
    - Output ONLY a short reasoning (1–2 lines)
    - Do NOT output the consistency label
    - Do NOT use headings, bullet points, or formatting
    - Do NOT introduce new facts
    - Base reasoning strictly on the provided materials

    ### Handling Insufficient Evidence
    - If explicit evidence is missing, still produce a reasoning explaining the mismatch, such as:
      - lack of narrative support
      - semantic inconsistency
      - thematic misalignment
      - character behavior not aligning with backstory claims
    - Never output "*"
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
    "Neville A. Stanton is employed by the University of Southampton, which is stated to have been founded in 1862, so the backstory does not align with the character’s documented professional history."
)

prompt_template = [
    {"role": "system", "content": rag_qa_system},
    {"role": "user", "content": one_shot_rag_qa_input},
    {"role": "assistant", "content": one_shot_rag_qa_output},
    {"role": "user", "content": "${prompt_user} "}
]

