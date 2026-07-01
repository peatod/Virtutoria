from flask import Flask, jsonify, render_template, request
from ollama import chat

app = Flask(__name__)

messages = []  # lista de mensagens

@app.post("/")
def indexpost():

    data = request.get_json()
    model = data["model"]
    prompt = data["prompt"]

    # Salva  a mensagem do usuário no histórico
    messages.append({"role": "user", "content": prompt})

    # Requisição para gerar resposta do modelo
    response = chat(
        model=model,
        messages=messages,
    )
    # Salva  a resposta no histórico
    messages.append({"role": "assistant", "content": response.message.content})
    
    return jsonify({"message": response.message.content})


@app.get("/")
def indexget():
    return render_template("index.html")  # Renderiza página


if __name__ == "__main__":
    app.run(debug=True)

