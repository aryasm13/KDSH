ner_system = """
You are a highly accurate entity extraction system specialized for narrative analysis and backstory–narrative consistency verification.

Your task is to extract **named entities that are useful for verifying whether a character backstory is consistent or contradictory with a narrative**.

Focus on extracting:
- Character names
- Named locations
- Named objects or artifacts
- Named organizations or institutions
- Named events (if explicitly mentioned)

Do NOT extract:
- Abstract traits, beliefs, or emotions
- Consistency labels (e.g., Consistent, Contradictory)
- General nouns without specific names

Always return entities exactly as they appear in the input text.
"""

query_prompt_one_shot_input = """Please extract all named entities that are important for verifying narrative consistency.

Question: 
Character: Severus Snape
Backstory: Snape was always loyal to Voldemort and never protected Harry Potter.
Label: Contradictory
"""
query_prompt_one_shot_output = """
{"named_entities": ["Severus Snape", "Voldemort", "Harry Potter"]}
"""

# """
prompt_template = [
    {"role": "system", "content": ner_system},
    {"role": "user", "content": query_prompt_one_shot_input},
    {"role": "assistant", "content": query_prompt_one_shot_output},
    {"role": "user", "content": "Question: ${query}"}
]