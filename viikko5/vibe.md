# Vibe coding -katselmointi

Tehtävän alkuperäinen tavoite oli antaa Ohtuvaraston web-käyttöliittymä
GitHub Copilotin pilviagentille issue-kuvauksen perusteella. Issue #2 luotiin
GitHubiin yksityiskohtaisella kuvauksella ja hyväksymiskriteereillä.
Copilot-agentin assignointi kuitenkin epäonnistui GitHubin ilmoitukseen
`Bot does not have access to the repository (replaceActorsForAssignable)`.
Siksi toteutus tehtiin paikallisena fallback-ratkaisuna eikä Copilotin
tuottamana koodina.

Toteutukseen tehtiin pieni Flask-sovellus hakemistoon `viikko5/web-ui`.
Sovellus voi luoda useita nimettyjä varastoja, listata niiden kapasiteetit ja
saldot sekä lisätä ja poistaa tavaraa. Data säilyy vain sovelluksen
käynnissäolon ajan, eikä tehtävän ulkopuolisia ominaisuuksia lisätty.

Toiminta varmistettiin automaattisilla testeillä komennolla
`python3 -m pytest viikko5/web-ui/src/tests`. Testeissä tarkistetaan varaston
luonti ja listaus, tavaran lisääminen ja poistaminen, liian suuren poiston
estäminen sekä virheellisen syötteen käsittely. Kaikki neljä testiä menivät
läpi.

Koodi on pieni ja jaettu varaston tilasta vastaavaan `WarehouseStore`-luokkaan
sekä Flask-reitteihin. Jinja2:n automaattinen HTML-escaping suojaa käyttäjän
antaman nimen tulostusta. Ratkaisu ei kuitenkaan ole tuotantokäyttöön
tarkoitettu, koska tietoja ei tallenneta pysyvästi eikä sovelluksessa ole
käyttäjähallintaa tai samanaikaisuuden käsittelyä.

Pilviagentin puuttumisen vuoksi tästä työstä ei voi päätellä, millaiseen
ratkaisuun Copilot olisi päätynyt tai mitä uutta sen koodia lukemalla olisi
opittu. Tehtävä osoitti kuitenkin, että tarkka issue-kuvaus auttaa rajaamaan
ominaisuudet ja testattavat hyväksymiskriteerit, riippumatta siitä toteuttaako
ratkaisun pilviagentti vai ihminen.
