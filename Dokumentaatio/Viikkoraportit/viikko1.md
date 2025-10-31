# Viikkoraportti 1

Viikolla projektiin käyetyt tunnit: ~40t

1. Mitä tehty tällä viikolla: \
Olin aloittanut projektin valmistelun jo ennen kurssin alkua ja olin tutustunut expectiminimax algoritmiin ja pelin 2048 toteuttammiseen etukäteen, joten pääsin tehokkaasti liikkeelle. \
Projektiin valmistui peliin vaadittavat funktiot ja käyttöliittymä joten peli on pelikelponen. Peliä pelaava tekoäly ja sen käyttämä expectiminimax algoritmi ovat myös valmistuneet ja pelin pelaaminen onnistuu niiltä. 

2. Projektin edistyminen: \
Projekti on periaattessa tällä hetkellä valmis pelin ja sitä pelaavan tekoälyn olemassa olon näkökulmasta. Mitään testejä ei ole tehty vielä joten käytännössä projekti vielä hyvin kesken. \
Tekoäly ei myöskään tällä hetkellä ole kovin hyvä eli se voittaa pelin vain harvoin ja on hyvin hidas. Tekoälyn ja pelin funktiota voisi tehostaa ohjelman nopeuttamiseksi.

3. Mitä opin tällä viikolla: \
Expectiminimax on oikeastaan aika raskas algoritmi tähän tapaukseen koska satunnaisia tapahtumia on potentiaalisesti monta ja niiden määrä kasvattaa hakupuuta näiden määrä kertoimella. Suurin osa satunnaisista tapahtumista on kuitenkin merkityksettömiä pelin pelaamisen kannalta joten mielestäni niiden kaikkien läpikäynti ei ole järkevää.

4. Mitä jäi epäselväksi: \
Puhdasoppisessa expectiminimax algoritmissa idea on että kaikki satunnaiset tapahtumat käydään läpi ja niiden heurististen arvojen painotettu keskiarvo lasketaan. Mietin vain että koska tämä ei oikeastaan ole järkevää niin voiko tässä suorittaa karsintaa vaikka silloin toteutettavaa algoritmia "rikotaan"?

5. Mitä seuraavaksi: \
Projektiin pitää kirjoittaa testit. \
Pelin ja tekoälyn funktioita voisi pyrkiä tehostamaan. Expectiminimaxille voisi myös pyrkiä löytämään parempia heuristiikkoja laudan arvottamiseen. 
