def chatbot():
    print("Ciao! Sono un chatbot. Digita 'esci' per terminare.")
    while True:
        domanda = input("Tu: ").lower()
        if "ciao" in domanda:
            print("Chatbot: Ciao! Come posso aiutarti?")
        elif "come stai" in domanda:
            print("Chatbot: Sto bene, grazie! E tu?")
        elif "esci" in domanda:
            print("Chatbot: Ciao! Alla prossima!")
            break
        else:
            print("Chatbot: Non ho capito, puoi ripetere?")

chatbot()
