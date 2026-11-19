# TDD agentin kanssa

Agentti päätyi toimivaan ja selkeään ostoskorin toteutukseen. Testit kattavat
ostoskorin hinnan, tavaroiden määrän, ostokset, saman tuotteen yhdistämisen,
poistamisen ja tyhjentämisen. Lopuksi agentti refaktoroi hinnan ja tavaroiden
määrän päivityksen yhteiseen apumetodiin, eikä toiminnallisuus muuttunut.

Osassa A agentti pysyi minimitoteutuksessa ja jätti testit rauhaan silloin,
kun sille annettiin yksi rajattu askel kerrallaan. Se ei yrittänyt huijata
kovakoodaamalla testien odottamia arvoja, vaan toteutti tarvittavan tilan ja
Ostos-oliot vaiheittain.

Osassa B agentti kirjoitti testit, jotka vastasivat annettuja vaatimuksia:
esimerkiksi ostokset-listan kokoa sekä tuotteen nimeä ja lukumäärää
tarkistettiin suoraan. Tarkistin testit ja muutokset ennen jokaista committia.

Osien A ja B työnjaosta osa B tuntui tehokkaammalta, koska agentti pystyi
kirjoittamaan pienen testin ja toteutuksen samalla kertaa. Osa A oli kuitenkin
parempi oppimisen kannalta, koska testin tarkoitus ja toteutuksen pienin
tarvittava askel oli helpompi arvioida itse.
