# Reflektio

Agentti siirsi testien yhteiset mock-oliot ja niiden toteutukset `setUp`-metodiin.
Ratkaisu poisti toisteisuutta järkevästi, ja testien yksittäiset skenaariot ovat
nyt helpommin luettavia. Testien toiminnallisuus säilyi: `assert_called_with`
tarkistaa edelleen tilisiirron kaikki olennaiset parametrit, eikä tarkistuksia
heikennetty pelkiksi `assert_called`-kutsuiksi.

Tarkistin muutokset itse ja lisäsin lisäksi testit ostoksen nollaamisesta,
uuden viitenumeron pyytämisestä sekä korista poistamisesta. Nämä kattavat
kaupan puuttuneet haarat ja nostavat `Kauppa`-luokan testauskattavuuden
lähelle sataa prosenttia.
