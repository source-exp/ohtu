# Koodin katselmointi

Tennistehtävän refaktorointi on haarassa `tennis_refactoring`. Pull request
tehtiin haarasta `tennis_refactoring` haaraan `main`, ja se mergeättiin
onnistuneesti.

GitHub Copilotin varsinaista PR-katselmointia ei saatu käynnistettyä tässä
ympäristössä. Siksi raportissa ei ole Copilotin tekemiä kommentteja tai
ehdotettuja muutoksia, eikä niitä pidä tulkita tehdyksi katselmoinniksi.

Oma katselmointi keskittyi siihen, että pisteenlaskennan julkinen rajapinta
säilyi ennallaan, taikanumerot korvattiin nimetyillä vakioilla ja
`get_score`-metodin päätöksenteko jaettiin pieniin nimettyihin metodeihin.
Testit ajettiin komennolla `python3 -m pytest viikko5/tennis/src/tests`, ja
kaikki testit menivät läpi.

Jos Copilot-katselmointi olisi ollut käytettävissä, sen hyödyllisyys olisi
riippunut erityisesti siitä, löytäisikö se testien ulkopuolisia rajatapauksia
tai luettavuutta heikentäviä ratkaisuja. Ihmiskatselmoinnissa palautteen tulee
olla konkreettista, perusteltua ja rajattua muutoksen kannalta olennaisiin
asioihin. Lisäksi katselmoijan kannattaa erottaa toiminnalliset virheet,
ylläpidettävyyteen liittyvät huomiot ja pelkät tyylimieltymykset.
