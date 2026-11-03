# Copilot-tehtävän raportti

## Koodin täydennys

Metodin `top_goal_scorers` toteutus oli melko suoraviivainen. Koodin täydentämisestä
oli hyötyä erityisesti siinä, että lajitteluavaimen ja tulosjoukon rajaamisen
perusrakenne löytyi nopeasti. Ehdotus piti kuitenkin lukea läpi: muuttujanimet,
rajatapaukset ja yhteensopivuus muun luokan tyylin kanssa pitää tarkistaa itse.

## Pylint

Pylintin varoitukset puuttuvista docstringeistä ja liian suuresta metodista
olivat aiheellisia. Docstring-säännön tarkoitus on tehdä luokkien ja metodien
vastuut näkyviksi, ja liian suuren metodin varoitus auttaa pitämään yhden
funktion vastuun rajattuna. Korjausten jälkeen `uv run pylint src` antaa
arvosanan 10.00/10.

## Agentin tekemä toiminnallisuus

Joukkuehaku toteutettiin `PlayerStats.top_scorers_by_team`-metodilla. Se huomioi
myös pelaajat, joiden `team`-kentässä on useampi joukkue, ja palauttaa pelaajat
pisteiden mukaan laskevassa järjestyksessä.

Alkuperäinen toteutusyritys toi esiin testien moduulipolkuongelman sekä yhden
testin virheellisen odotuksen. `src` lisättiin pytestin Python-polkuun, testin
odotus korjattiin vastaamaan pistejärjestystä, ja lopputulos toimii.

## Testit

PlayerStats-luokalle tehtiin yksikkötestit `PlayerReaderStub`-luokalla.
Stub palauttaa kiinteät pelaajat, joten testit eivät tee HTTP-pyyntöjä.
Testit kattavat kansalaisuuden perusteella lajittelun, monen joukkueen pelaajan
joukkuehaun ja maalintekijöiden määrän rajoittamisen. Komento
`uv run pytest` menee läpi.

Testeissä rakenne on sama kuin edellisellä viikolla: riippuvuus korvataan
stubilla ennen testattavan palvelun luomista. Nyt pytestin asetuksiin tarvittiin
lisäksi `src`-hakemiston lisääminen Python-polkuun, jotta testit toimivat
suoraan projektin juuresta.

## Mitä opin?

Opin, että automaattisesti ehdotettu koodi ei poista suunnittelun ja tarkistamisen
tarvetta. Testit paljastavat nopeasti sekä import-ongelmat että väärät oletukset
järjestyksestä. Lisäksi joukkueen käsittelyssä täytyy huomioida, että yksi
pelaaja voi esiintyä usean joukkueen listassa.
