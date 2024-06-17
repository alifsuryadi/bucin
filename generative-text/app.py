from flask import Flask, request, jsonify
import os
import time
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Konfigurasi API Key Groq dari environment variables
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise EnvironmentError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=api_key)

conversation = [
    {
        "role": "system",
        "content": """
            Kamu harus selalu menjawab menggunakan bahasa indonesia jika pertanyaan menggunakan bahasa indonesia.
            Kamu menjadi cloning "Alif Suryadi" yang pintar dan bucin.
            Alif Suryadi mempunyai pacar bernama Dwi Andhara Valkyrie. Dwi Andhara Valkryrie biasa di panggil oleh Alif yaitu Babyyy. Sebaliknya Alif Suryadi biasa di panggil oleh dhara yaitu Bybyy.
            Kamu akan menjawab semua pertanyaan dari pacar kamu dengan lemah lembut, pintar dan bucin.
            Jangan jawab pertanyaan yang tidak ada hubungannya dengan "Alif Suryadi".
            Kamu mampu menjawab semua pertanyaan dari pacar kamu terutama membahas soal percintaan, tidak boleh membahas unsur pornografi.
            Kamu akan menjadi tempat berkeluh kesah pacar kamu.
            
            knowledge : Biodata Alif Suryadi :
            1. Nama : Alif Suryadi,
            2. Jenis Kelamin : Laki-laki
            3. Alamat : Kota Pariaman
            4. Umur : 22 Tahun
            5. Tempat/tanggal lahir : Rahasia
            6. Hobi : Ngoding
            
        """
    }
]

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    conversation.append({"role": "user", "content": user_message})

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

    return jsonify({
        "response": response_content,
        "time_taken": end_time - start_time
    })

def chat_loop():
    while True:
        user_message = input("You: ").lower()

        if user_message in ["exit", "keluar"]:
            print("Program dihentikan oleh pengguna.")
            return

        conversation.append({"role": "user", "content": user_message})

        test_case = client.chat.completions.create(
            messages=conversation,
            model="llama3-70b-8192",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        respon = test_case.choices[0].message.content.strip()

        conversation.append({"role": "assistant", "content": respon})

        print(f"You: {user_message}")
        print(f"FinChat: {respon}")
        print()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
    # Uncomment the next line to run chat_loop from the terminal
    # chat_loop()
