# Määrittelydokumentti

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti

Dokumentaation kieli: Suomi

Projektin ohjelmointikieli: Python \
Voin vertaisarvioida muita Pythonilla toteutettuja projekteja.

Aihe: 2048 pelin toteuttaminen ja sitä pelaavan expectiminimax algoritmia hyödyntävän tekoälyn toteuttaminen. Peli on 4x4 laudalla pelattava peli jossa on tarkoitus yhdistää samoja numeroita näiden summaksi liikuttamalla laudalla olevia numeroita joko ylös, alas, vasemalle tai oikealle. Pelin tavoitteena on saadaan muodostettua numero 2048. Laudalle ilmestyy jokaisen liikutuksen jälkeen satunnaiseen vapaaseen paikkaan joko numero 2 tai 4.

Projektin ydin: Peliä pelaava tekoäly ja sitä varten toteutettava expectiminimax algoritmi ja sen heuristiikat joilla määritetään mitä siirtoja tekoäly tekee. 

Toteutus: Toteutan pelille konsolista käytettävän tekstikäyttöliittymän jolla itse peliä voi pelata. Käyttäjä voin syöttää konsoliin komentonsa pelin pelaamiiseen tai laittaa tekoälyn pelaamaan peliä. Tekoälyn tapauksessa pelaaja voi syöttää ohjelmalle syvyyden mihin asti expectiminimax algoritmin hakupuu ulotetaan siirtoja tutkittaessa. Käyttäjä voi myös määrittää kuinka monta kertaa äly pelaa peliä, sekä kuinka monen siirron jälkeen ohjelma tulostaa laudan tilan pelin kulun seuraamista varten. 

Algoritmit ja tietorakenteet: Projektissa toteutan expectiminimax algoritmin. Heuristiikkoina pelilaudan hyvyyden arviointiin tulen kokeilemaan  Nie et al:in paperin mukaisia heuristiikkoja. Näissä laudalla olevia numeroita arvotetaan niiden sijainnin ja suuruuden perusteella. 
Pelilauta tallennetaan matriisiin jotka toteutetaan Pythonin listana joka sisältää listoja jotka sisältävät numeroita.

Aika- ja tilavaativuudet: Expectiminimax algoritmin aikavaativuus on pahimassa tapauksessa $O(b^m n^m)$ missä b on haarautumiskerroin (Mahdollisten liikkeiden määrä per solmu), n on mahdollisten satunaisten tapahtumien määrä (Tyhjien ruutujen määrä) ja m on haun syvyys (Eli kuinka monen liikkeen päähän algoritmi katsoo jokaisessa tilanteessa). Tilavaativuus $O(m)$ koska algoritmi on rekursiivinen ja käy läpi aina yhden hakupuun haaran jolloin se täytyy pitää muistissaan haaran syvyyden verran laudan eri tiloja.

Lähteet: \
https://en.wikipedia.org/wiki/Expectiminimax \
Yun Nie, Wenqi Hou, Yicheng An, AI Plays 2048 (https://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf)