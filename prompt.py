def zero_shot_prompt_template(cwe_description,key_words_list):
    return f"""Please read this CWE description:
```
{cwe_description}
```
Now, I have a task for you. Given a CWE-ID and its description, along with a list of keywords, your goal is to combine these keywords (or modify them based on their word forms, verb tenses, noun number, and adjective/adverb forms) to create meaningful phrases that represent the CWE vulnerability. These phrases should consist of 2-3 words and accurately capture the essence of the CWE.

To achieve this, please follow these steps carefully (using Chain-of-Thought reasoning):

1. **Understand the CWE Description**: Analyze the CWE description to identify the core concepts and the type of vulnerability it represents.
2. **Analyze the Keywords**: Examine the list of keywords provided below. For each keyword, consider its different word forms and variations:
   - **Verbs**: Analyze different verb tenses and forms (e.g., base form, present participle, past tense).
     - Example: "inject" -> "injecting" (present participle), "injected" (past tense).
   - **Nouns**: Consider singular and plural forms.
     - Example: "query" -> "queries" (plural).
   - **Adjectives**: Analyze adverb forms derived from adjectives.
     - Example: "malicious" -> "maliciously" (adverb).
   - Think about how these forms can be combined with other words to create meaningful phrases (e.g., "query injection," "injecting malicious code," "maliciously injected payload").
3. **Generate Phrases**: Based on the analysis, combine or modify the keywords to create meaningful phrases that represent the CWE. Ensure that the phrases are concise (2-3 words) and semantically accurate.
4. **Validate the Phrases**: Double-check that the generated phrases align with the CWE description and effectively convey the vulnerability.

Here is the list of keywords:
```
{key_words_list}
```
Please complete this task step by step, and provide your reasoning at each step. The output should be a new list of phrases wrapped by ```KeyWordsList```.
Example Output:
```
KeyWordsList:

query injection

injecting malicious code

maliciously injected payload

unauthorized access

malicious queries
```
Now, please proceed with the task.
"""


def postprocess(output):
    try:
        if "```KeyWordsList" not in output:
            return output
        output = output[output.index("```KeyWordsList") + len("```KeyWordsList"):]
        output = output[:output.index("```")]
    except:
        pass
    return output.strip()