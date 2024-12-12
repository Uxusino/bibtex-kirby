# Raportti

**Tiimi:** Erik Huuskonen, Kasperi Blomberg, Riina Immonen, Olli Tiainen, Viktoria Lilitskaia

---

## Kohdatut ongelmat

Tiimimme kohtasi useita haasteita projektin aikana. Suurin osa ongelmista liittyi tietokannan arkkitehtuurin suunnitteluun ja sen yhteensopivuuteen backendin kanssa. PostgreSQL:n ja JSON-datan yhteiskäyttö vaati ylimääräistä tutkimista ja sopeutumista. Lisäksi backlogin hallinta oli aluksi hajanaista, ja jouduimme siirtymään uusiin alustoihin, jotta vaatimukset täyttyivät. Lopuksi tiimimme huomasi, että frontendin visuaalinen suunnittelu jäi sprintin loppuun, mikä toi lisäpainetta.

---

## Prosessi

Projektimme eteni iteratiivisesti sprinttiperusteisesti. Aluksi rakensimme Product Backlogin Google Spreadsheetiin ja Sprint Backlogin GitHubiin. Tehtävät jaettiin selkeästi, ja tiimimme jäsenet ottivat vastuuta omista osuuksistaan. Yhteistyö sujui pääasiassa tekstipohjaisesti, mutta käytimme myös lyhyitä ääni- ja tekstikeskusteluja ongelmien ratkaisuun. CI/CD-pipeline otettiin käyttöön tukemaan kehitystä ja testaus oli jatkuvasti mukana prosessissa.

---

## Prosessiin liittyvät ongelmat

- Alkuperäinen backlog-rakenne ei ollut tarpeeksi selkeä, mikä johti sen uudelleensuunnitteluun.  
- Joillakin tiimin jäsenillä oli haasteita löytää riittävästi aikaa tehtäville, mikä johti epätasaisuuksiin sprintin osioissa.  

---

## Projektityöskentely

Tiimimme onnistui jakamaan työtehtävät tehokkaasti. Käyttöliittymän kehitys, tietokantaratkaisut, backendin toiminnallisuudet ja testaus etenivät pääosin rinnakkain. Viestintä tiimin välillä oli sujuvaa, ja kaikki tunsivat projektin yleisen tilanteen. Sprint Backlogin avulla pystyimme seuraamaan tehtävien tilaa ja priorisoimaan tärkeimmät osat.

---

## Projektityöskentelyyn liittyvät ongelmat

- Frontendin visuaalinen suunnittelu jäi liian myöhään aloitettavaksi.  
- Ensimmäisessä sprintissä kaikkien panos ei ollut yhtä aktiivinen, mikä toi lisätyötä muille.  

---

## Tekniset asiat

### Keskeiset saavutukset
- PostgreSQL-tietokanta otettiin käyttöön ja optimoitiin JSON-tietotyypin tukemiseksi.  
- Backend saatiin toimimaan tehokkaasti tietokannan kanssa ja tarjoamaan toiminnallisuudet, kuten lähteiden lisääminen ja hakeminen.  
- CI/CD-pipeline otettiin käyttöön, ja yksikkö- sekä robot-testejä luotiin kattavasti.  

### Teknisiin asioihin liittyvät ongelmat
- Tietokannan ja SQLAlchemy-moduulin yhteensopivuusongelmat hidastivat kehitystä.  
- Tietokannan projektihallintaominaisuus osoittautui ensimmäiseen sprinttiin ylimitoitetuksi tarpeeksi.  

---

## Mikä sujui hyvin

- Tiimimme viestintä ja työnjako toimivat erinomaisesti.  
- Suunnitelmat etenivät johdonmukaisesti, ja suurin osa tehtävistä saatiin valmiiksi ajoissa.  
- Backendin ja tietokannan integraatio onnistui odotuksia paremmin.  
- CI/CD-työkalut varmistivat koodin laadun ja vähensivät virheiden määrää.  

---

## Mitä pitäisi parantaa

1. Backlogin hallinta olisi alusta alkaen selkeämpää yhdellä alustalla.  
2. Visuaalisen suunnittelun aloittaminen aikaisemmin olisi tehnyt sprintistä sujuvamman.  
3. Ajankäytön tasaisempi jakaminen sprintin aikana auttaisi välttämään ruuhkahuippuja.  

---

## Oppiminen

### Mitä opimme
- Tiimimme oppi, miten tietokantojen arkkitehtuuri suunnitellaan ja yhdistetään backend-toiminnallisuuksiin.  
- Ymmärsimme CI/CD-pipelinejen merkityksen ohjelmistokehityksessä.  
- Yhteistyö ja tehtävien priorisointi kehittyivät huomattavasti sprintin aikana.  

### Mitä olisimme halunneet oppia
- Syvempää osaamista käyttöliittymien visuaalisessa suunnittelussa.  
- Kattavamman testauksen toteutuksen.  

---

## Mikä tuntui turhalta

- Backlogin uudelleenjärjestely vei paljon aikaa, mikä olisi voitu käyttää kehitykseen.  
- Tietokannan projektihallintaominaisuuden suunnittelu ei ollut olennaista ensimmäisessä sprintissä.  
