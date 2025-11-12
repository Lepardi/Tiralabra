# Testausdokumentti

[Tämä dokumentti on kesken ja täydentyy]

## Testauksen kattavuusraportti
![Coverage](https://github.com/Lepardi/Tiralabra/blob/main/Dokumentaatio/Images/coverage.PNG)

Testit kattavat muuten kaikki pelin ja tekoälyn koodirivit mutta AI luokassa jää muutama tulosterivi kattamatta. Näillä riveillä ei ole vaikutusta tekoälyn tomintaan vaan ovat käyttäjälle sen toiminnan seuraamista varten.

## Testit
### Game luokan testit
Game luokan testit testaavat pelin funktioiden toimintaa yksikkötesteillä. \

### AI luokan testit

AI luokan testit testaavat yksikkötesteillä että luokan funktiot toimivat oikein. Mukana on myös testejä jotka testaavat että tekoäly saavuuttaa pelissa haluttuja lopputuloksia ennalta asetetuissa pelitilanteissa.

heuristic() funktion testit: \
1. Funktio palauttaa oikean arvon tyhjälle pelilaudalla \
2. Funktio palauttaa oikean arvon laudalla jossa on yksi luku. \
3. Funktio palauttaa oikean arvon laudalla jossa suurin pelinumero 64 on laudan vasemassa yläkulmassa ja tätä seuraavissa ruuduissa vasemalle on luvut 32, 16 ja 8. Tämä testaa sitä että heuristiikka palkitsee oikein siitä että toisiaan seuraavat luvut ovat sijoitettu laudan yläreunaan. \

Pelin voittavan ja häviävät laudan heuristisia arvoja ei testata koska näiden tilanteiden arvon palauttaminen on expectiminimax funktion velvoite. \

expectiminimax() funktion testit: \
1. Funktio palauttaa oikean arvon tyhjälle pelilaudalla \
2. Funktio palauttaa oikean arvon laudalla jossa on yksi luku. \
3. Funktio palauttaa oikean arvon laudalle jossa on voittava luku 2048. \
4. Funktio palauttaa oikean arvon täydellen häviön tuottavalle laudalla. \

getNextMove() funktion testit: \
1. Funktio palauttaa oikean suunnan (ylös) laudalla jossa paras tilanne on siirtää luvun 1024 toisen 1024 viereen. \
2. Funktio palauttaa oikean suunnan (vasen) laudalla jossa paras tilanne on yhdistää luku 512 toisen 512 kanssa 1024:ksi toisen 1024:n alle. \
3. Funktio palauttaa oikean suunnan (alas) laudalla jossa paras tilanne on siirtää 1024 alas lukujen 512, 256, 256 viereen josta nämä voidaan yhdistää voittavaksi 2048:ksi. Jos tilanteessa ensin pyrkisi yhdistämään luvut 512, 256, 256, tukkisi uusien lukujen ilmestyminen laudalla tien voittoon. \
4. Funktio palauttaa oikean suunnan (ylös) tilanteessa jossa laudalle on rakennettu voittava suora 1024,256,256,256 missä vielä viimeisen 256 alapuolella on tämä sama luku jotka yhdistetään 512:ksi. \
5. Funktio palauttaa oikean suunnan (ylös) tilanteessa jossa pelilaudan yläreunaan on rakenettu luvut 1024,256,128,64. Siirtämällä ylös saadaan toiseksi ylimmäksi riviksi luvut 4,8,16,32. Tästä tilanteessa voidaan suoraan rakentaa laudalla tilanne jossa yläreunassa ovat luvut 1024 ja 512. \

aiLoop() funktion testit: \
1. Funktio palauttaa 1024 tilanteessa jossa se ei voi voittaa peliä ja laudalla on kyseinen luku suurimpana. \
2. Funktio voittaa pelin (palauttaa 2048) tilanteessa jossa laudalla on 1024,512,256,256 vierekkäin ja funktion hakusyvyys on 3 jolloin se näkee siirtoja voittavaan tilanteeseen asti. \
3. Funktio voittaa pelin (palauttaa 2048) tilanteessa jossa hakusyvyys on 4 ja laudalla on ylärivillä 1024,512,256,128 vierekkäin ja 128 alla on toinen 128. Tässä tilanteessa voitto on mahdollinen 4 siirrolla joten funktion pitäisi nähdä voittoon johtavat siirrot. \
4. Funktio voittaa pelin (palauttaa 2048) tilanteessa jossa hakusyvyys on 5 ja laudalla on ylärivillä 1024,512,256,128 vierekkäin ja 256 alla on 128 ja sen vieressä oikealla 0. Tässä tilanteessa voitto on mahdollinen 5 siirrolla joten funktion pitäisi nähdä voittoon johtavat siirrot. \

