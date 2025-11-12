# Käyttöohje

## Ohjelman suorittaminen

Projektissa on käytetty poetrya riippuvuuksien hallintaan.\

Asenna ja valmistele projektin ympäristö suorittamalla projektin juurihakemistossa:\
```
poetry install
```

Suorita ohjelma juurihakemistosta komennolla:\
```
poetry run python src/main.py
```

## Ohjelman käyttö

Ohjelma kysyy aluksi haluaako käyttäjä pelata peliä itse vai antaa tekoälyn pelata. \
Syöttämälle luvun 1 pääsee käyttäjä itse pelaaman peliä. \
Syöttämällä luvun 2 käyttäjä ohjataan antamaan parametrit tekoälyn pelaamiselle. \
Käyttäjän tulee syötää ohjelmaan hakupuun syvyys, eli kuinka monen liikkeen päähän tekoäly katsoo ennen jokaista tekemäänsä liikettä. Tämä vaikuttaa huomattavasti tekoälyn pelaamisen käyttämään aikaan sekä sen pelikyvyn hyvyyteen. \
Käyttäjä syöttää ohjelmalle myös kuinka monta kertaa tekoäly pelaa pelin annetulla syvyydellä. \
Käyttäjän tulee myös syötää kuinka monen liikkeen välein tekoäly tulostaa pelilaudan jotta tekoälyn pelaamista voidaan seurata. \
Syötämällä kirjaimen q ohjelma lopetetaan alkuvalikosta tai palaa alkuvalikkoon joko peliä pelatessa tai tekoälyn parametrejä syötettäessä.
