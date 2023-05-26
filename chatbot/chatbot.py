from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot('Chatbot')
trainer=ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")
#print(chatbot.get_response("what is AI?"))


print("Hi,I am ChatBot ")
while True:
    query=input(">>>")
    print(chatbot.get_response(text=query, search_text=query))

