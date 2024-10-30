meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
}

for _ in range(5):  # Bucle que se ejecuta 5 veces
    word = input("Escribe una palabra que no entiendas: ").upper()
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No conozco esa palabra")
