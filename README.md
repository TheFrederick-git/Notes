# Poznámkovač

Poznámkovač je triviální webová aplikace, která je schopna ukládat textové vstupy uživatele a zároveň je ukládat do databáze, což zamezí ztrátu dat při opětovném načtení stránky. Uložiště se navíc nachází lokálně spolu se zbylými soubory aplikace, což napomáhá k ochraně citlivých uživatelských dat.

## Funkce

- Intuitivní a responzivní UI/UX
- Lokální uložiště
- Spolehlivost
- Doplňující data uložena spolu s poznámkami
- Čtení poznámek
- Mazání poznámek

## Technologie

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [SQLite3](https://www.sqlite.org/index.html)

## Instalace

Poznámkovač vyžaduje [Python](https://python.org/) v3.7+

##### Instalace doplňkových knihoven
```sh
python -m pip install -r requirements.txt
```

##### Spuštění
```sh
python main.py
```

##### Nasazení do produkce
```sh
nohup python3 main.py
```

Po spuštění bude veškerá aktivita na stránce zobrazována ve standartním výstupu a webová aplikace bude spuštěna na adrese
```sh
https://127.0.0.1:5000
```

## Licence
MIT
