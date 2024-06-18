from groq import Groq
import time
from .config import GROQ_API_KEY
from .conversation import conversation

client = Groq(api_key=GROQ_API_KEY)

def get_response(user_message):
    conversation.append({"role": "user", "content": user_message.lower()})

    try:
        start_time = time.time()
        response = client.chat.completions.create(
            messages=conversation,
            model="llama3-70b-8192",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )
        end_time = time.time()

        response_content = response.choices[0].message.content.strip()
        conversation.append({"role": "assistant", "content": response_content})

        return {
            "response": response_content,
            "time_taken": end_time - start_time
        }
    except Exception as e:
        return {
            "error": str(e)
        }
