from pyfiglet import figlet_format

def cool_text():
    testo = input("Scrivi il tuo nome: ")
    print(figlet_format(testo))

cool_text()