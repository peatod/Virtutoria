from flask import Flask, jsonify, render_template, request
from ollama import chat

app = Flask(__name__)


@app.post("/")
def indexpost():
    messages = []  # lista de mensagens

    data = request.get_json()
    response = chat(  # Requisição para gerar resposta do modelo
        data.model,
        messages=[*messages, {"role": "user", "content": data.prompt}],
    )

    messages += [
        {"role": "user", "content": data.prompt},
        {"role": "assistant", "content": response.message.content},
    ]

    return jsonify({"message": response.message})


@app.get("/")
def indexget():
    return render_template("index.html")  # Renderiza página


if __name__ == "__main__":
    app.run(debug=True)

"""---------------------------------------------------------------
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)

---------------------------------------------------------------------
from ollama import chat

messages = []

while True:
  user_input = input('Chat with history: ')
  response = chat(
    'gemma3',
    messages=[*messages, {'role': 'user', 'content': user_input}],
  )

  # Add the response to the messages to maintain the history
  messages += [
    {'role': 'user', 'content': user_input},
    {'role': 'assistant', 'content': response.message.content},
  ]
  print(response.message.content + '\n')
  """
