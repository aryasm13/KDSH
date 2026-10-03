

one_shot_rag_qa_docs = (
    """Title: The Last Horse\nThe Last Horse (Spanish:El último caballo) is a 1950 Spanish comedy film directed by Edgar Neville starring Fernando Fernán Gómez.\n"""
    """Title: Southampton\nThe University of Southampton, which was founded in 1862 and received its Royal Charter as a university in 1952, has over 22,000 students. The university is ranked in the top 100 research universities in the world in the Academic Ranking of World Universities 2010. In 2010, the THES - QS World University Rankings positioned the University of Southampton in the top 80 universities in the world. The university considers itself one of the top 5 research universities in the UK. The university has a global reputation for research into engineering sciences, oceanography, chemistry, cancer sciences, sound and vibration research, computer science and electronics, optoelectronics and textile conservation at the Textile Conservation Centre (which is due to close in October 2009.) It is also home to the National Oceanography Centre, Southampton (NOCS), the focus of Natural Environment Research Council-funded marine research.\n"""
    """Title: Stanton Township, Champaign County, Illinois\nStanton Township is a township in Champaign County, Illinois, USA. As of the 2010 census, its population was 505 and it contained 202 housing units.\n"""
    """Title: Neville A. Stanton\nNeville A. Stanton is a British Professor of Human Factors and Ergonomics at the University of Southampton. Prof Stanton is a Chartered Engineer (C.Eng), Chartered Psychologist (C.Psychol) and Chartered Ergonomist (C.ErgHF). He has written and edited over a forty books and over three hundered peer-reviewed journal papers on applications of the subject. Stanton is a Fellow of the British Psychological Society, a Fellow of The Institute of Ergonomics and Human Factors and a member of the Institution of Engineering and Technology. He has been published in academic journals including "Nature". He has also helped organisations design new human-machine interfaces, such as the Adaptive Cruise Control system for Jaguar Cars.\n"""
    """Title: Finding Nemo\nFinding Nemo Theatrical release poster Directed by Andrew Stanton Produced by Graham Walters Screenplay by Andrew Stanton Bob Peterson David Reynolds Story by Andrew Stanton Starring Albert Brooks Ellen DeGeneres Alexander Gould Willem Dafoe Music by Thomas Newman Cinematography Sharon Calahan Jeremy Lasky Edited by David Ian Salter Production company Walt Disney Pictures Pixar Animation Studios Distributed by Buena Vista Pictures Distribution Release date May 30, 2003 (2003 - 05 - 30) Running time 100 minutes Country United States Language English Budget $$94 million Box office $$940.3 million"""
)


rag_qa_system = (
    '''
    ### Role
    You are an expert narrative consistency explanation system.

    ### Task
    You are given narrative evidence from a story, along with a combined query
    that contains:
    - a character name
    - a hypothetical backstory
    - a consistency label (Consistent or Contradictory)

    Your task is NOT to answer a factual question.
    Your task is to explain **why the given backstory matches or does not match**
    the narrative evidence.

    ---

    ### Detail Article
    {context}

    ### Query
    {question}

    ---

    ### Response Rules
    - Output ONLY a short reasoning (1–2 lines)
    - Do NOT output the consistency label
    - Do NOT include headings, bullet points, or formatting
    - Do NOT introduce new facts
    - Base reasoning strictly on the provided narrative
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
    "Neville A. Stanton is described as working at the University of Southampton, which is explicitly stated to have been founded in 1862, so the backstory does not align with the narrative evidence."
)


prompt_template = [
    {"role": "system", "content": rag_qa_system},
    {"role": "user", "content": one_shot_rag_qa_input},
    {"role": "assistant", "content": one_shot_rag_qa_output},
    {"role": "user", "content": "${prompt_user}"}
]
