# Testausdokumentti

## Testien ajaminen

Testit voidaan ajaa projektin juurihakemistosta komennolla:
```
poetry run pytest src
```

Testikattavuusraportti saadaan tuotettua ajamalla projektin juurihakemistosta komento:
```
poetry run coverage run --branch -m pytest src
```

Testikattavuusraporttia voidaan tarkastella komenolla:
```
poetry run coverage report -m
```

## Testauksen kattavuusraportti
![Coverage](https://github.com/Lepardi/Tiralabra/blob/main/Dokumentaatio/Images/coverage.PNG)

Testit kattavat muuten kaikki pelin ja tekoälyn koodirivit mutta AI luokassa jää muutama tulosterivi kattamatta. Näillä riveillä ei ole vaikutusta tekoälyn tomintaan vaan ovat käyttäjälle sen toiminnan seuraamista varten.

## Testit
### Game luokan testit
Game luokan testit testaavat pelin funktioiden toimintaa yksikkötesteillä. 

Funktiot ja niiden testaus: 

addNumToBoard() funktion testit: \
Ennalta määritetyn random luokan avulla testaan että funktio lisää laudalle oikein joko uuden luvun 2 tai 4.
Testi testaa myös että funktio lisää satunaiseen paikkaan uuden luvun vertaamalla lautaa funktion kutsua ennen ja jälkeen.

startGame() funktion testit: \
Testi testaa että funktio alustaa laudan jossa on numeroita oikein, niin että siitä löytyy vain yksi 2 tai 4 jostain kohtaa lautaa.

getHighestNum() funktion testit: \
Testi testaa että funktio palauttaa suurimman summan laudalta:
```
[[0,0,0,4],
[0,512,0,0],
[0,0,2,0],
[0,0,0,1024]]
```
Pitää palauttaa: 1024.

getZeroPositions() funktion testit: \
Testi testaa että funktio palauttaa kaikki tyhjät paikat laudalla:
```
[[0,2,2,2],
[2,2,2,2],
[2,2,2,2],
[2,2,0,0]]
```
Pitää palauttaa: [(0,0),(3,2),(3,3)]

getFirstZeroPosition() funktion testit: \
Testataan että funktio palauttaa ensimäinen tyhjän paikan laudalta:
```
[[0,2,2,2],
[2,2,2,2],
[2,2,2,2],
[2,2,0,0]]
```
Pitää palauttaa: (3,2)

Funktio palauttaa: (None, None) tuplen jos sitä kutsutaan täydelle laudalle:
```
[[2,2,2,2],
[2,2,2,2],
[2,2,2,2],
[2,2,2,2]]
```

setNumToBoard() funktion testit:\
Testit testaa että funktio todella lisää halutun numeron halutulle paikalle.
Laudalle:
```
[[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
```
Kutsutaan setNumToBoard(2, (3,2), test_board).
Ja tarkastetaan että paikassa (3,2) on tämän jälkeen luku 2.

isBoardFull() funktion testit:\
Testit testaavat että funktio näkee täyden laudan:
```
[[2,4,8,16],
[256,128,64,32],
[1024,2,4,8],
[2,4,8,2]]
```
Ja palauttaa: True

Funktio näkee epätäyden laudan:
```
[[2,4,8,16],
[256,128,64,32],
[1024,2,4,8],
[2,4,0,2]]
```
Ja palauttaa: False

Funktio näkee laudan jossa voidaan tehdä liike vasemalle, oikealle, ylös tai alas:
```
[[2,4,8,16],
[256,128,64,32],
[1024,2,4,8],
[2,2,2,2]]
```
Ja palauttaa: False

isGameWon() funktion testit:\
Testataan että funktio näkee laudalla luvun 2048 jolloin peli on voitettu, tai huomaa että laudalla ei ole tätä lukua ja peli jatkuu.

Laudalla:
```
[[2,4,8,16],
[256,128,64,32],
[1024,2048,4,8],
[2,2,2,2]]
```
Funktio näkee luvun 2048 ja palauttaa: True

Ja laudalla:
```
[[2,4,8,16],
[256,128,64,32],
[1024,2,4,8],
[2,2,2,2]]
```
Funktio näkee että laudalla ei ole 2048 ja palauttaa: False

funktioden moveBoardUp(), moveBoardDown(), moveBoardLeft() ja moveBoardRight() testit:

Testit testaavat että laudoilla joissa on peräkkäin luvut 2,2,2,2, yhden liikuttamisen jälkeen laudalla jää 0,0,4,4. Eli liikutus yhdistää lukuja vain kerran. Testit testaavat myös että muut luvut laudalla liikkuvat oikeaan paikkaan liikutuksen suunnan mukaisesti.

isMovePossible() funktion testit:\
Testit testaavat kaikilla suunnilla että palautetaan True mikäli: Suuntaan voidaan yhdistää kaksi numeroa tai laudalla on tilaa liikuttaa numeroita suuntaan.

Testit testaavat myös että kaikilla suunnilla palautetaan False: Mikäli numerot eivät voi liikkua laudalla suuntaan. Esimerkiksi tilanteessa jossa lauta täysi tai kaikki laudan numerot ovat kiinni siinä reunassa mihin suuntaaan ollaan liikuttamassa. 

moveBoard() funktion testit:\
Testit testaavat että kaikkiin suuntiin ylös, alas, vasen ja oikea, funktio liikuttaa lautaa oikein ennalta määritellyissä tilanteissa ja laudalla on tämän jälkeen halutut luvut oikeissa paikoissa.  

### Heuristic luokan testit

heuristic() funktion testit: 
1. Funktio palauttaa oikean arvon tyhjälle pelilaudalla 
2. Funktio palauttaa oikean arvon laudalla jossa on yksi luku. 
3. Funktio palauttaa oikean arvon laudalla:

```
[[64,32,16,8],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
```

Palautettavan arvon tulee olla 78517370880. Tämä luku saadaan arvotusmatriisin perusteella: $(64\*(4^15))+(32\*(4^14))+(16\*(4^13))+(8\*(4^12))$

Pelin häviävän laudan heuristisia arvoja ei testata koska tämän tilanteen arvon palauttaminen on expectiminimax funktion velvoite. 

### AI luokan testit

AI luokan testit testaavat yksikkötesteillä että luokan funktiot toimivat oikein. Mukana on myös testejä jotka testaavat että tekoäly saavuuttaa pelissa haluttuja lopputuloksia ennalta asetetuissa pelitilanteissa.

expectiminimax() funktion testit: 
1. Funktio palauttaa oikean arvon tyhjälle pelilaudalla 
2. Funktio palauttaa oikean arvon laudalla jossa on yksi luku syvyydellä 0. Tällöin funktio kutsuu käytänössä vain heuristiikkafunktiota arvioimaan laudan. 
3. Funktio palauttaa oikean arvon täydelle häviön tuottavalle laudalla. 

Seuraavia testejä varten expectiminimaxille on annettu laudan arvotusta varten erillinen heuristiikkafunktio joka palauttaa aina 100000000000000 tilanteessa jossa laudalla on luku 2048 tai tätä suurempi luku. Oikeassa versiossa tätä ei käytetä koska se vääristää tuloksia kun peliä jatketaan luvun 2048 saamisen jälkeen.

4. Funktio palauttaa oikean arvon 100000000000000 kun laudalla on 2048 syvyydellä 0. 
5. Funktio palauttaa oikean arvon 100000000000000 syvyydellä 1 kun laudan lähtötilanne on: 
```
[[1024,1024,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
```
Tällöin yhdellä liikeellä saadaan 2048 ja funktion tulisi nähdä tämä ja palauttaa aina voittoarvo

6. Funktio palauttaa oikean arvon 100000000000000 syvyydellä 3 kun laudan lähtötilanne on: 
```
[[1024,512,256,256],
[16,32,64,16],
[256,8,0,32],
[16,512,128,8]]
```
Tässä tilanteessa luku 2048 voidaan saada kolmella liikeellä mutta lautaa voidaan siirtää kaikkii suuntiin jokaisen liikkeen jälkeen. Syvyydellä 3 funktion tulee nähdä oikeat siirrot joilla saadaan laudalle 2048 ja palautetaan 100000000000000. 


getNextMove() funktion testit: 
1. Funktio palauttaa oikean suunnan (ylös) laudalla jossa allekkain on luvut 1024. 
2. Funktio palauttaa oikean suunnan (vasen) laudalla jossa paras tilanne on yhdistää luku 512 toisen 512 kanssa 1024:ksi toisen 1024:n alle. 

aiLoop() funktion testit: 
1. Funktio palauttaa 1024 tilanteessa jossa se ei voi voittaa peliä ja laudalla on kyseinen luku suurimpana. 
2. Funktio palauttaa vähintään 2048 pelitilassa 1, tilanteessa jossa laudalla on 1024,512,256,256 vierekkäin funktion hakusyvyydellä 1. Tämä testaa että tekoäly pelaa vähintäänki järkevästi tilanteessa jossa on triviaalia saada laudalle ainakin 2048. 
3. Funktio palauttaa yli 2048 pelitilassa 0, tilanteessa jossa laudalla on 1024,512,256,256 vierekkäin funktion hakusyvyydellä 1. Tämä testaa että tekoäly pelaa vähintäänki järkevästi tilanteessa jossa on triviaalia saada laudalle ainakin 2048.

