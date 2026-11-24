# Koodin katselmointi

Tennistehtävän refaktorointi on haarassa `tennis_refactoring`. Pull request
tehtiin haarasta `tennis_refactoring` haaraan `main`, ja se mergeättiin
onnistuneesti.

Copilotin PR-katselmointi valmistui PR:lle #1. Katselmointi tehtiin GitHubin
CLI:llä, jonka käyttämä taso oli Balanced. Tehtävänannossa suositeltua Lite-
tasoa ei voinut valita CLI-komennolla.

Oma katselmointi keskittyi siihen, että pisteenlaskennan julkinen rajapinta
säilyi ennallaan, taikanumerot korvattiin nimetyillä vakioilla ja
`get_score`-metodin päätöksenteko jaettiin pieniin nimettyihin metodeihin.
Testit ajettiin komennolla `python3 -m pytest viikko5/tennis/src/tests`, ja
kaikki testit menivät läpi.

Copilot löysi yhden korkean tason ongelman: `won_point` vertasi parametria
kovakoodattuihin merkkijonoihin `"player1"` ja `"player2"` eikä käyttänyt
konstruktorissa annettuja pelaajien nimiä. Esimerkiksi
`TennisGame("Alice", "Bob").won_point("Alice")` kirjasi pisteen väärälle
pelaajalle. Ehdotus oli hyvä ja korjasin ongelman muuttamalla vertailun
käyttämään `self.player1_name`- ja `self.player2_name`-arvoja.

Katselmointi oli hyödyllinen, koska se löysi rajatapauksen, jota alkuperäiset
testit eivät kattaneet. Samalla se osoitti, että kattava testimäärä ei takaa,
että kaikki julkisen rajapinnan käyttötilanteet on testattu. Copilot ei
huomauttanut muista olennaisista ongelmista. Ihmiskatselmoinnissa palautteen
tulee olla konkreettista, perusteltua ja rajattua muutoksen kannalta
olennaisiin asioihin. Lisäksi katselmoijan kannattaa erottaa toiminnalliset
virheet, ylläpidettävyyteen liittyvät huomiot ja pelkät tyylimieltymykset.
