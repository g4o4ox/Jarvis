from brain import Brain
from voice import Voice
brain = Brain()
voice = Voice()

while True:

    text = voice.listen()
    
    if not text:
        print("?")
        continue

    print (f"eu:{text}")
    
    #ask = input("HI: ")
    #if ask == "sair":
       # break

    answer = brain.think(text)
    voice.speak(answer)
    #print("Jarvis: ", answer)

