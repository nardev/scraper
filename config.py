# lol contract nije obavezno polje nego je tu iskljucivo radi lakse pretrage
#	
# - Obavezne su samo one postavke za provajdere koje zeli te provjeravati, sotale treba potpuno pobrisati!
# - Za Elektroprivredu BiH 'epbih', polje 'contract' u biti nije obavezno nego je tu iskljucivo radi lakse pretrage. Za sada samo za jedno brojno mjesto!
# - Za Logosoft 'lol', polje 'contract' je nuzno radi lakse pretrage po stranici.
#
#	credentials = {
#				Registracija (samoz mobilnu): https://moj.bhtelecom.ba/registracija
#		'bht': {
#			'username_full': '',	# Ovdje ide broj u punom formatu sa pozivnim za drzavu, ex: 38761123456
#			'username_short': '',	# Broj u skracenoj formi, ex: 061123456
#			'password': ''	# Password se doije prilikom aktiviranja ili registrovanja na portal moj.bhtelecom.ba ili nakon promjene ako vec posjedujete account.
#		},
#					Za registraciju: https://www.epbih.ba/register
#					Tek nakon registracije ce biti potrebno dodati brojno mjesto a za to ce vam biti neophodan broj ugovora
#		'epbih': { 
#			'username': '',	# Korisnicko ime koje ste postavili prilikom registracije.
#			'password': '',	# Password koji ste takodje sami postavili.
#			'contract': ''	# Broj ugovora koji je moguce naci na racunu. Sve sa znakom '-' ex: 10203-D-4567892
#		},
#					Aktivirati nalog prema uputama: http://www.rad.com.ba/naplatna1.htm inace login stranica: http://www.rad.com.ba/naplatna1.htm
#		'kjkprad':{
#			'username': '', # Sifra korisnika tj. broj sa racuna koji je tako nazvan
#			'password': '' # Lozinka koju ste odabrali prilikom registracije
#		},
#				Prilikom potpisivanja ugovora, dobili ste logim podatke. Login inace na: https://www.lol.ba
#		'lol': {	
#			'username': '', # korisnicko ime koje vam je odredjeno
#			'password': '', # Password koji vam je dodjeljen
#			'contract': '' # Nakon manuelnog logina, na lijevoj strani je zeleni box u kojem jasno, bold slovima stoji broj ugovora ex: 12345-02-SA/19
#		},
#				Nije potrebna nikakva registracija, svi pdoatci su na racunu: https://www.sarajevogas.ba/provjeraracuna
#		'sagas': {
#			'name': '', # JAKO VAZNO!!! Treba upisati ime i prezime, velikim slovima, sa zamjenskim karakterima za nasa slova i sa razmakom. Prvo prezime ex: HAPIC HAMO
#			'user_id': '' # Sifra kupca koja se nalazi na svakom dobijenom racunu
#		},
#		'tsa': { # http://www.toplanesarajevo.ba/korisnici/stanje-racuna
#			'user_id':'' # Potrebna vam je sifra korisnika koja se inace nalazi na svakom vasem racunu ex: 1234567893
#		},
#
# 				Potrebno prvo izvrsiti registraciju. Pratiti upute na: http://www.viksa.ba/wrapper/stanje_racuna
#				JAKO VAZNO, tek nakon registracije se dodaje brojno mjesto a za to vam takodje treba racun sa sifrom kupca!!!
#				Ova skripta ce samo pokupiti podatke za prvo brojno mjesto!
#		'vik': {
#			'username': '', # korisnicko ime koje bude te odabrali
#			'password': '' # password koji bude te odabrali
#		}
#	}


credentials = {
	'bht': {
		'username_full': '',
		'username_short': '',
		'password': ''
	},
	'epbih': {
		'username': '',
		'password': '',
		'contract': ''
	},
	'kjkprad':{
		'username': '',
		'password': ''
	},
	'lol': {
		'username': '',
		'password': '',
		'contract': ''
	},
	'sagas': {
		'name': '',
		'user_id': ''
	},
	'tsa': {
		'user_id':''
	},
	'vik': {
		'username': '',
		'password': ''
	}
}
