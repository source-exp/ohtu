# AI-tehtävän raportti

## Ohjetiedosto

Projektin ohjetiedosto on `viikko3/login/.github/copilot-instructions.md`.
Se on tiivis ja kertoo, että projekti käyttää `uv`:ia, komennot suoritetaan
`uv run` -muodossa, sovellus käynnistyy porttiin 5001, Robot-testit ajetaan
komennolla `uv run robot src/tests` sovelluksen ollessa käynnissä, ja
validointi sijaitsee `UserService.validate`-metodissa. Ohjetiedostoon ei
tarvittu laajaa sisältöä; varmistin erityisesti projektin oikean juurihakemiston
ja täsmälliset komennot.

## Agentin toiminta

Pyysin agenttia käsittelemään user storyt yksi kerrallaan ja kirjoittamaan
hyväksymiskriteerit ensin `register.robot`-testeiksi. Agentti lisäsi testit
ennen tuotantokoodia. Ennen toteutusta testien suorittaminen estyi kuitenkin
Playwrightin puuttuvasta Chromium-binaarista, joten tarkistin myöhemmin testit
järjestelmän Google Chromella.

Agenttia piti ohjata melko tarkasti test-first-järjestyksestä, rajatusta
muutoksesta ja siitä, ettei toista storya käsitellä ensimmäisen yhteydessä.
Lopullinen muutos jäi pieneksi: uudet rekisteröitymistestit ja
`UserService.validate`-metodin kirjainrajoitus.

## Testit ja mutaatiotestaus

Kaikki 15 Robot Framework -testiä menivät lopuksi läpi. Tarkistin lisäksi
testien herkkyyden kahdella tarkoituksellisella rikkomisella:

1. Poistin kirjainrajoituksen. Tällöin kaksi kirjain-only-salasanojen testiä
   epäonnistui.
2. Poistin salasanan ja vahvistuksen vertailun. Tällöin eri vahvistuksen testi
   epäonnistui.

Tämä osoittaa, että testit eivät ainoastaan suorita koodia, vaan tarkistavat
myös molempien uusien vaatimusten lopputuloksen.

## Mitä opin

Opin, että agentin tuottamat testit on arvioitava itse eikä pelkkä testien
määrä tai läpimeno riitä. Mutaatiotestaus paljastaa nopeasti, testaavatko
testit oikeasti vaadittua käyttäytymistä. Lisäksi agentin komennot, diffi ja
muutosten rajaus on tarkistettava, koska vastuu lopputuloksesta säilyy
ohjelmoijalla.

Luettuani materiaalin luvun *Vastuu ja osaaminen* ymmärsin erityisesti, että
agentti tarvitsee ihmiseltä suunnan, vaatimusten tulkinnan ja teknisen
katselmoinnin. Agentti voi toteuttaa väärän asian tehokkaasti, ellei ihminen
ymmärrä vaatimuksia ja tarkista tuotosta.
