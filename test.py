import ollama


text = "Hi my name is Piyush"
x =ollama.embed(model= 'nomic-embed-text',input=text)

print(type(x))