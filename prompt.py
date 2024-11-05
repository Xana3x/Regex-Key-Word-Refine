def zero_shot_prompt_template(cwe_description,key_words_list):
    return f"""Please read this CWE descrption:
```
{cwe_description}
```
According to this description, please select certain words from the list of keywords provided below to form a phrase capable of the meaning of the CWE vulnerability. At the same time, please consider the parts of speech and tenses of each word to synthesize the corresponding phrase.
Here is the list of keywords:
```
{key_words_list}
```
Please finish this task step by step. 
The output should be a new list wrapped by ```KeyWordsList```.
"""

def zero_shot_prompt_template_with_phrase_list(cwe_description,key_words_list,phrase_list):
    return f"""Please read this CWE descrption:
```
{cwe_description}
```
Based on this description and the list of phrases provided to you below, please select some words from the keyword list provided below, combine the words in the keyword list with existing phrases, enrich the content of the keyword list, and generate phrase keywords that are more representative of the CWE description. At the same time, please consider the parts of speech and tenses of each word, and combine them into more diverse phrases.
Here is the list of keywords:
```
{key_words_list}
```
Please finish this task step by step. 
The output should be a new list wrapped by ```KeyWordsList```.
"""


def few_shot_prompt_template(cwe_description,examples,key_words_list):
    return f"""Please read this CWE descrption:
```
{cwe_description}
```
According to this description, please select certain words from the list of keywords provided below to form a phrase capable of the meaning of the CWE vulnerability. At the same time, please consider the parts of speech and tenses of each word to synthesize the corresponding phrase.
Here is the list of keywords:
```
{key_words_list}
```
Here are some examples to demonstrate the proper output:
```
{examples}
```
Please finish this task step by step. 
The output should be a new list wrapped by ```KeyWordsList```.
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