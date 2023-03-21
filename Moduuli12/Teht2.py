import requests

paikkakunta = input("Syötä paikkakunna nimi: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=f9a58cbb9d33d3d6287c539614555b8a&units=metric"
vastaus = requests.get(pyyntö).json()

sää1 = vastaus["weather"]
sää2 = sää1[0]["description"]

lämpötila1 = vastaus["main"]
lämpötila2 = lämpötila1["temp"]

print(f"Säätila paikkakunnalla on {sää2}, sekä lämpötila on {lämpötila2}°C")
