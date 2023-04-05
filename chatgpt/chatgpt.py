from pychatgpt import Chat

chat = Chat(email="email", password="password")
chat.cli_chat()

# options.chat_log = "chat_log.txt"
# options.id_log = "id_log.txt"

# Create a Chat object
chat = Chat(email="315876632@qq.com", password="Klwdsr910318@", options=options)
answer = chat.ask("How are you?")
print(answer)