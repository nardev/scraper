# scraper
Scraper za dohvacanje podataka o vasim troskovima sa web stranica javnih i privatnih preduzeca u Kantonu Sarajevo.


<a href="https://www.buymeacoffee.com/usci8e4yG" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-green.png" alt="Buy Me A Coffee" align="right" style="height: 40px" ></a>


## Scraper README [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](nardev.org)

	Za potrebe prikaza u Home Assistant-u, napravio sam nekoliko modula koji uz adekvatno konfigurisanje mogu jednostavno da dohvate stanje dugovanja, uplata a nekada i trenutne potrosnje za usluge. Moguce da se codjeno ovim primjerima skripti iz "providers/" moze napraviti i jos poneka skripta. Firme koje su meni bilo ptorebne su vec tu. Predpostavljam da bi u Kantonu Sarajevo odgovaralo da tu bude jos i OKI i recimo Sarajevo Stan ali oni jednostavno nemaju pregled dugovanja online. Takodje, za sada nisam uspio bolje pogledati web sajt telemach-a kao ni BH Telecom usluge za MojuTV, Fiksni Telefon i ADSL prikljucak. Za sada uspjesno "skrejpamo" samo BH Telecom mobilnu.  
	Manje vise sve firme imaju potpuno drugaciji prikaz tako se nisam ni trudio da skripta vrati neki ispis koji je logicniji. Naprimjer VIK ako ste u pretplati, stavi vam "-" minus ispred cifre dugovanja. Ili recimo Toplane Sarajevo stave neke napomene u polje gdje se nalazi tekst za stanje pa takve stvari nisam brisao. Potom, neke firme kao Logosoft, na stanje vam stave odmah i troskove cijelog trenutnog mjeseca. Tako da ste po prikazu zapravo u minusu stalno.  
	Smatram da ako ste se jednom ulogovali, znat ce te sta je smisao tog prikaza.


## Providers
---
> Ovo je bezvezan naziv za firme. Da bi uspjesno dobili potrebne podatke koji su vam potrebni za ovu skriptu, slijedi te naredne savjete. Takodje, u config.py fajlu je moguce dobiti dodatne opise za podatke.

#### BH TELECOM
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/bht.jpg" align="right" />

* Potrebna registracija na: <a href="https://moj.bhtelecom.ba/registracija" target="_blank">https://moj.bhtelecom.ba/registracija</a>
* Prema uputama u config.py upisati svoj broj telefona, u skracenoj i prosirenoj formi kao i password
* Skrejpanje trenutno uspjesno radi samo za pregled mobilne, ako neko napravi za ostale usluge, rado cu dodati i to.


#### Elektroprivreda d.d. BiH
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/epbih.jpg" align="right" />
* Za registraciju slijediti upute ovdje: <a href="https://www.epbih.ba/register" target="_blank">https://www.epbih.ba/register</a>
* Nakon registracije i prvog logina, dodaje te mjerno mjesto koje cete pratiti.
* Iako je moguce dodati vise mjesta koja pratite, ova skripta ce samo "skrejpati" podatke za prvo koje se pojavi na listi.



#### KJKP Rad d.o.o. Sarajevo
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/kjkprad.jpg" align="right" />
* Aktivirati nalog prema uputama: http://www.rad.com.ba/naplatna1.htm
> Šifra korisnika za pristup podacima nalazi se na svakom mjesečnom računu
> Samo za PRVI pristup sistemu Lozinka je Referenca sa računa
* Nakon toga, unese te vasu lozinku i to koristi te u config.py

#### Logosoft d.o.o. Sarajevo
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/lol.jpg" align="right" />
* Svi podatci su u vasem ugovoru
* Posto je moguce imati vise ugovora na jedno ime, potrebno je u config.py dodati i broj ugovora.
* Nakon manuelnog logina, na lijevoj strani je zeleni box u kojem jasno, bold slovima stoji broj ugovora ex: 12345-02-SA/19


#### KJKP "Sarajevo Gas" d.o.o.
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/sagas.jpg" align="right" />
* Web za provjeru: <a href="https://www.sarajevogas.ba/provjeraracuna" target="_blank">https://www.sarajevogas.ba/provjeraracuna</a>
* Registracija nije potrebna
* Nije potrebna nikakva registracija, svi pdoatci su na racunu!
* !!! VAZNO !!! Prilikom unosa imena korisnika u config.py potrebno je kucati u formatu "PREZIME IME" te pritom nase karaktere zamijeniti uobicajenim zamjenama.


#### KJKP Toplane Sarajevo
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/tsa.jpg" align="right" />
* Provjera stanja racuna je inace ovdje: <a href="http://www.toplanesarajevo.ba/korisnici/stanje-racuna" target="_blank">http://www.toplanesarajevo.ba/korisnici/stanje-racuna</a>
* Nije potreban nikakav login, dovoljna je samo sifra korisnika sa racuna!

#### Vodovod i Kanalizacija Sarajevo
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/vik.jpg" align="right" />
* Potrebno prvo izvrsiti registraciju. Pratiti upute na: <a href="http://www.viksa.ba/wrapper/stanje_racuna" target="_blank">http://www.viksa.ba/wrapper/stanje_racuna</a>
* Tek nakon registracije se dodaje mjerno mjesto.
* Iako je moguce imati vise mjernih mjesta, ova skripta prati samo prvo na listi!
*


#### Telemach d.o.o. Sarajevo 
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/tmch.jpg" align="right" />
* Login je prilicno atipican. Pokusat cu neku drugi put da pripremim i ovaj "skrejper".
* Ako neko napravi skriptu, neka napravi pull request da to merdzamo!
* Korisnicko ime cete odabrati prilikom registracije!
* Lozinku cete takodje odabrati prilikom registracije!


## How to use this shit:

* Kloniranje Repozitorija lokalno i instalacija potrebnih modula i biblioteka: `gti clone git@github.com:nardev/scraper.git`  

* Predpostavljam da cete se snaci sa pip-om, u biti, van standardnih modula, potrebno vam je:
```bash
pip3 install beautifulsoup4 progress prettytable argparse
```

* Svakako, prikupiti i aktivirati sve login podatke koji su opisani iznad!

* Dodati svoje postavke u `config.py`, te pobrisati nodove za "provajdere" koje necete koristiti!

* Zgodno je, ali nije obavezno, postaviti izvrsne permisije za `scraper.py` skriptu `chmod +x scraper.py`. tako da ju je moguce pokretati sa:
```bash
user@host$ ./scraper.py
```

* Skripta daje dva osnovna formata ispisa `json` koji je ujedno i defaultni te `table`.

##### Primjeri:

* Osnovni ispis, skripta po defaultu pravi request za svakog provajdera koji je u `config.py` te vraca jedan json u kojem su svi pdoatci. Taj json nije formatiran!  
  
```bash
user@host$ ./scraper.py
```  

###### Opcije

* Opcija `-a` ili `--fetch-all` pokusava dohvatiti podatke za sve setovane postavke u `config.py`

* Opcija `-p` ili `--providers` uz dodatno navedenu listu provajdera, a koji su prije toga setovani u `config.py`, pokusava dohvatiti samo te provajdere. Lista mogucih provajdera za sada: `['bht', 'epbih', 'lol', 'sagas', 'tsa', 'vik']`  
  
* Opcija `-f` uz opcije `['json', 'table']` formatira ispis u json ili tabelu.

###### Primjeri

---
```bash
# Dohvacanje podataka za troskove "Vodovod i kanalizazciju" u formi tabele.
user@host$ ./scraper.py -p vik -f table
```
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/preview01.png" width="750" />


```bash
# Dohvacanje podataka zaz sve provajdere koji su podeseni, u formi tabele.
user@host$ ./scraper.py -a -f table
```
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/preview02.png" width="750" />


```bash
# Dohvacanje podataka zaz sve provajdere koji su podeseni, u json formi.
user@host$ ./scraper.py -a -f json
```
<img src="https://raw.githubusercontent.com/nardev/scraper/master/images/preview03.png" width="400" />




## Authors:  
@nardev  
@gondzo