# SCRAPER
Scraper dohvaća podataka o vašim troškovima sa web stranica javnih i privatnih preduzeća u Kantonu Sarajevo.


<a href="https://www.buymeacoffee.com/usci8e4yG" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-green.png" alt="Buy Me A Coffee" height="40" ></a>


## Scraper README [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](nardev.org)
* Za potrebe prikaza u Home Assistant-u, napravio sam nekoliko modula koji uz adekvatno konfigurisanje mogu jednostavno da dohvate stanje dugovanja, uplata a nekada i trenutne potrošnje za usluge.


## PROVIDERS
---
Ovo je bezvezan naziv za firme. Da bi uspješno dobili potrebne podatke koji su vam potrebni za ovu skriptu, slijedite naredne savjete. Takođe, u `config.py` fajlu je moguće dobiti dodatne opise za podatke.

#### BH TELECOM
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/bht.jpg" align="right" />  

* Potrebna registracija na: <a href="https://moj.bhtelecom.ba/registracija" target="_blank">https://moj.bhtelecom.ba/registracija</a>
* Prema uputama u `config.py` upisati svoj broj telefona, u skraćenoj (ex: 061123456) i proširenoj (38761123456) formi kao i password.
* Skrejpanje trenutno uspješno radi samo za pregled mobilne telefonije, ako neko napravi za ostale usluge, rado ću dodati i to.

#### ELEKTROPRIVREDA D.D. BIH
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/epbih.jpg" align="right" />  
  
* Za registraciju slijediti upute ovdje: <a href="https://www.epbih.ba/register" target="_blank">https://www.epbih.ba/register</a>
* Nakon registracije i prvog logina, dodajete mjerno mjesto koje ćete pratiti.
* Iako je moguce dodati više mjesta koja pratite, ova skripta će samo "skrejpati" podatke za prvo koje se pojavi na listi.


#### KJKP RAD D.O.O. SARAJEVO
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/kjkprad.jpg" align="right" /> 
  
* Aktivirati nalog prema uputama: <a href="https://moj.bhtelecom.ba/registracija" target="_blank">http://www.rad.com.ba/naplatna1.htm</a>
* Šifra korisnika za pristup podatcima nalazi se na svakom mjesečnom računu.
* Samo za PRVI pristup sistemu Lozinka je Referenca sa računa.
* Nakon toga, unese te vašu lozinku i nju koristite u `config.py`

#### LOGOSOFT D.O.O. SARAJEVO
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/lol.jpg" align="right" />  

* Login na naslovnoj stranici ovdje: <a href="http://www.lol.ba" target="_blank">http://www.lol.ba</a>
* Svi podatci su u vašem ugovoru.  
* Pošto je moguće imati više ugovora na jedno ime, potrebno je u `config.py` dodati i broj ugovora.  
* Nakon manuelnog logina, na lijevoj strani je zeleni box u kojem jasno, bold slovima stoji broj ugovora (ex: 12345-02-SA/19)  
  
#### KJKP "SARAJEVO GAS" D.O.O.
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/sagas.jpg" align="right" />  
  
* Web za provjeru računa: <a href="https://www.sarajevogas.ba/provjeraracuna" target="_blank">https://www.sarajevogas.ba/provjeraracuna</a>
* Registracija nije potrebna.
* Svi potrebni pdoatci su na računu!
* !!! VAŽNO !!! Prilikom unosa imena korisnika u `config.py` potrebno je kucati u formatu "PREZIME IME" te pritom naše karaktere zamijeniti uobičajenim zamjenama.


#### KJKP TOPLANE SARAJEVO  
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/tsa.jpg" align="right" />  
  
* Provjera stanja računa je inače ovdje: <a href="http://www.toplanesarajevo.ba/korisnici/stanje-racuna" target="_blank">http://www.toplanesarajevo.ba/korisnici/stanje-racuna</a>
* Nije potreban nikakav login, dovoljna je samo šifra korisnika sa računa!  
  
#### VODOVOD I KANALIZACIJA SARAJEVO  
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/vik.jpg" align="right" />  
  
* Potrebno prvo izvršiti registraciju.
* Pratiti upute na: <a href="http://www.viksa.ba/wrapper/stanje_racuna" target="_blank">http://www.viksa.ba/wrapper/stanje_racuna</a>  
* Tek nakon registracije se dodaje mjerno mjesto u vaš nalog.  
* Iako je moguće imati više mjernih mjesta, ova skripta prati samo prvo na listi!  

#### TELEMACH D.O.O. SARAJEVO  
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/tmch.jpg" align="right" />  
  
* Login je prilično atipičan. Pokušat ću neku drugi put da pripremim i ovaj "skrejper".  
* Ako neko napravi skriptu, neka napravi pull request da to merdžamo!  
* Korisničko ime ćete odabrati prilikom registracije!  
* Lozinku ćete takodje odabrati prilikom registracije!  


## HOW TO USE THIS SHIT:

* Kloniranje Repozitorija lokalno i instalacija potrebnih modula i biblioteka: `gti clone git@github.com:nardev/scraper.git`  

* Predpostavljam da ćete se snaci sa pip-om, u biti, van standardnih modula, potrebno vam je:
```bash
pip3 install beautifulsoup4 progress prettytable argparse
```

* Svakako, prikupiti i aktivirati sve login podatke koji su opisani iznad!

* Dodati svoje postavke u `config.py`, te pobrisati nodove za "provajdere" koje nećete koristiti!

* Zgodno je, ali nije obavezno, postaviti izvrsne permisije za `scraper.py` skriptu `chmod +x scraper.py`. tako da ju je moguce pokretati sa:
```bash
user@host$ ./scraper.py
```

* Skripta daje dva osnovna formata ispisa `json` koji je ujedno i defaultni te `table`.

#### PRIMJERI I OPCIJE:

* Osnovni ispis, skripta po defaultu pravi request za svakog provajdera koji je u `config.py` te vraća jedan json u kojem su svi pdoatci. Taj json nije formatiran!  
  
```bash
user@host$ ./scraper.py
```  
  
##### OPCIJE  

* Opcija `-a` ili `--fetch-all` pokušava dohvatiti podatke za sve setovane postavke u `config.py`  

* Opcija `-p` ili `--providers` uz dodatno navedenu listu provajdera, moguće navesti nekoliko željenih provajdera a koji su prije toga setovani u `config.py`. Potom skripta pokušava dohvatiti samo te provajdere. Lista mogućih provajdera za sada je: `['bht', 'epbih', 'lol', 'sagas', 'tsa', 'vik']`  
  
* Opcija `-f` uz opcije `['json', 'table']` formatira ispis u json ili tabelu.  
  
##### PRIMJERI

---

```bash
# Dohvatanje podataka za troskove "Vodovod i kanalizazciju" u formi tabele.
user@host$ ./scraper.py -p vik -f table
```
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/preview01.png" width="750" />


```bash
# Dohvatanje podataka za sve provajdere koji su podeseni, u formi tabele.
user@host$ ./scraper.py -a -f table
```
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/preview02.png" width="750" />


```bash
# Dohvatanje podataka za sve provajdere koji su podeseni, u json formi.
user@host$ ./scraper.py -a -f json
```
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/preview03.png" width="400" />


---  

#### NAPOMENE
* Moguće da se vođeno ovim primjerima skripti iz "providers/" može napraviti i još poneka skripta. Firme koje su meni bile ptorebne su već tu. Predpostavljam da bi u Kantonu Sarajevo odgovaralo da tu bude još i "OKI" i recimo "Sarajevo Stan" ali oni jednostavno nemaju pregled dugovanja online. Takođe, za sada nisam uspio bolje pogledati web sajt "Telemach"-a kao ni "BH Telecom" usluge za "MojuTV", "Fiksni Telefon" i "ADSL" priključak. Za sada uspješno "skrejpamo" samo "BH Telecom mobilnu.  
* Sve firme imaju potpuno drugačiji prikaz tako se nisam ni trudio da skripta vrati neki ispis koji je ujednačene forme za sve. Naprimjer VIK ako ste u pretplati, stavi vam "-" minus ispred cifre dugovanja. Ili recimo Toplane Sarajevo stave neke napomene u polje gdje se nalazi tekst za stanje pa takve stvari nisam brisao. Potom, neke firme kao Logosoft, na stanje vam stave odmah i troskove cijelog trenutnog mjeseca. Tako da ste po prikazu stalno u minusu.  
* Smatram da ako ste se jednom ulogovali na željeni servis, može te jednostavno shvatiti smisao sadržaj ovih ispisa.
* `config.py` je linkovan kao simbolički link u direktoriju `providers` kako bi se moduli u istom mogli i zasebno koristiti. Ex: `python3 bht.py`  
* Ako slučajno bude nekih bug-ova i grešaka, molim vas da mi javite na vedran@nardev.org   


## KOD PISO':  
@nardev  
@gondzo