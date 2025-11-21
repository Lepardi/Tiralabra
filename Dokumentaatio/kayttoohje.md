# Käyttöohje

## Ohjelman suorittaminen

Projektissa on käytetty poetrya riippuvuuksien hallintaan.

Asenna ja valmistele projektin ympäristö suorittamalla projektin juurihakemistossa:
```
poetry install
```

Suorita ohjelma sen juurihakemistosta komennolla:
```
poetry run python src/main.py
```

Ohjelmassa ei oikeastaan ole mitään riippuvuuksia joten mikäli poetryn kanssa ilmenee ongelmia ohjelman ajaminen pitäisi onnistua myös juurihakemistosta komennolla:
```
python src/main.py
```

## Ohjelman käyttö

Ohjelma kysyy aluksi haluaako käyttäjä pelata peliä itse vai antaa tekoälyn pelata. 
\
Syöttämälle luvun 1 pääsee käyttäjä pelaamaan peliä itse. 
\
Syöttämällä luvun 2 käyttäjä ohjataan antamaan parametrit tekoälyn pelaamiselle. 
\
Käyttäjän tulee syötää ohjelmaan hakupuun syvyys, eli kuinka monen liikkeen päähän tekoäly katsoo ennen jokaista tekemäänsä liikettä. Tämä vaikuttaa huomattavasti tekoälyn pelaamisen käyttämään aikaan sekä sen pelikyvyn hyvyyteen.
Syvyydellä 0 tekoäly tarkastelee vain yhden liikkeen päähän. \
Syvyydellä 1 tekoäly tarkastelee liikkeen, satunaisen luvun lisäämisen ja yhden liikkeen päähän pelitilanetta.\
Syvyyden kasvattaminen lisää tarkasteluun aina yhden satunaisen luvun lisäämisen ja yhden liikkeen lisää.\
\
Käyttäjä syöttää ohjelmalle myös kuinka monta kertaa tekoäly pelaa pelin annetulla syvyydellä. 
\
Käyttäjän tulee myös syötää kuinka monen liikkeen välein pelilauta tulostetaan jotta tekoälyn pelaamista voidaan seurata. 
\
Viimeiseksi käyttäjän tulee syötää missä tilassa tekoälypelaa. 
Syöttämällä 1 tekoäly pelaa käyttäen expectiminimaxia jossa kaikki satunaiset tapahtumat otetaan huomioon. 
Syöttämällä 0 tekoäly pelaa käyttäen expectiminimaxia jossa tarkastellaan satunaisen tapahtuman kohdalla vain tilanteet missä ensimäiseen vapaaseen ruutuun ilmestyy 2. 
\
Tekoälypelaa peliä kunnes lauta tulee täyteen eikä se voi tehdä enään uusia liikkeitä.
\
Kun tekoäly on pelannut käyttäjän määrittämän määrän pelejä, ohjelma näyttää suurimmat luvut mitä laudalla on jokaisen pelin lopussa ollut.
\
Syötämällä kirjaimen q ohjelma sammuu alkuvalikosta.
Syötämällä kirjaimen q pelataessa tai tekoälyn parametrejä syötettäessä ohjelma palaa alkuvalikkoon.
