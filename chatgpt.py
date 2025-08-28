import os

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), max_retries=0)
    OPENAI_CLIENT = 'v1'
except Exception:
    client = None
    OPENAI_CLIENT = None


def get_embedding(text: str):
    resp = client.embeddings.create(model="text-embedding-3-small", input=text)
    return resp.data[0].embedding

# Chat call

def chat(system_prompt: str, user_text: str):
    try:
        resp = client.responses.create(
            model="gpt-4o",
            instructions=system_prompt,
            input=user_text,
        )
        return resp.output_text
    except Exception as e:
        return f"Error calling OpenAI API: {e}"
