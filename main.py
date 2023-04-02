# auteur: Merve zorluer
# Klas: DTPV1.E2

# Instructies voor de vragenlijst
print("introductie:")
print(
    "Heeft u vaak last van een gespannen gevoel? of voelt u zich vaak zenuwachtig en vermijd u bepaalde situaties of plekken?"
)
print("In deze vragenlijst wordt u getest op een angststoornis.")
print(" ")
print(
    "De vragenlijst bestaat 17 vragen. Hoeveel vragen u krijgt is afhankelijk van uw antwoorden."
)
print("Vragen beantwoordt u door ja of nee in te typen.")
print(" ")

# Lijst voor domein fobie
fobie_q = [
    "1A  Ik ben angstig voor een specifieke situatie (vliegen, dieren, hoogtes, bloed zien).\n",
    "Ik verstijf of ren weg als ik word geconfronteerd met die specifieke situatie.\n",
    "3A Ik krijg direct last van hevige angst als ik in die specifieke situatie ben.\n",
    "4A Ik vermijd deze specifieke situatie.\n",
    "5A Ik heb angst voor 2 of meer van de volgende situaties:Openbaar vervoer, in open ruimte zijn (pleinen, parkeerplaatsen), in afgesloten ruimte zijn (winkels, theater), in de rij staan, in een menigte zijn of alleen buitenshuis zijn.\n",
    "Ik heb al langer dan 6 maanden last van deze klachten.\n"
]

#Lijst voor de domein sociale angst
sociale_angst_q = [
    "1B Ik ben angstig in sociale situaties",
    "2B Ik ben angstig dat mensen aan mij zien dat ik angstig ben.",
    "3B Ik heb regelmatig last van een plotselinge aanval van intense langs die binnen enkele minuten een piek bereikt.",
    "4B Mijn angst is heviger dan je zou verwachten in sociale situaties.",
    "5B Ik vermijd sociale situaties.",
    "6B Ik heb deze angst al langer dan 6 maanden.  "
]

#Lijst voor de domein paniekklachten
paniekklachten_q = [
    "1C Ik heb regelmatig last van een plotselinge aanval van intense angst die binnen enkele minuten een piek bereikt.",
    "2C  Ik ervaar 4 of meer van de volgende symptomen:Veranderde hartslag, trillen, opvliegers, buikpijnklachten, misselijkheid, ademnood, hyperventileren, onaangenaam gevoel op de borst, duizeligheid, verdoofd tintelend gevoel.",
    "3C Door deze klachten ben ik mij anders gaan gedragen om een volgende aanval te vermijden.",
    "4C Ik ben constant bezorgd over of er een nieuwe paniekaanval zal komen en wat daar de gevolgen van zijn.",
    "5C Ik heb last van hart- of longklachten."
]

#Lijst voor het opslaan van de antwoorden
fobie_a = []
sociale_angst_a = []
paniekklachten_a = []
geslacht_a = []
leeftijd_a = []
a = 0
b = 0
c = 0


# functie  domein fobie
def fobie():
	print("U heeft gekozen voor het domein fobie.\n")
	print("Let er op dat u alleen maar kan antwoorden met ja of nee.\n")
	print("" "")

	for x in fobie_q:
		print("")
		global a
		a = a + 1
		while True:
			print(x)
			print("")
			aa = input()
			if (aa == "ja" or aa == "nee"):
				f = open("antwoord.txt", "a")
				tx = "Fobie Antwoord " + str(a) + "A "

				f.write(tx)
				f.write(aa)
				f.write("\n")
				print(" ")
				f.close()
				fobie_a.append(a)
				#Wanneer er een verkeerd antwoord gegeven wordt
				break
			else:
				print("")
				print("Onjuist antwoord")
				print("U heeft geantwoord met", a)
				print("")
				print("Antwoord alleen maar met ja/nee. \n")
				print("")
				continue


#functie sociale angst
def socialeangst():
	print("U heeft gekozen voor het domein sociale angst. \n")
	print("Antwoord alleen maar met ja of nee. \n")
	print("" "")

	for x in sociale_angst_q:
		print("")
		global b
		b = b + 1
		while True:
			print(x)
			print("")
			aa = input()
			if (aa == "ja" or aa == "nee"):
				f = open("antwoord.txt", "a")
				tx = "Sociale angst Antwoord " + str(b) + "B "
				f.write(tx)
				f.write(aa)
				f.write("\n")
				print(" ")
				f.close()
				#verkeerd antwoord ingevuld
				sociale_angst_a.append(a)
				break
			else:
				print("")
				print("onjuist antwoord")
				print("U heeft geantwoord met ", a)
				print("")
				print("Antwoord alleen maar met ja/nee.\n")
				print("")
				continue


#functie paniekklachten
def paniekklachten():
	print("U heeft gekozen voor het domein paniekklachten.\n")
	print("U kunt alleen maar antwoorden met ja of nee.\n")
	print("" "")

	for x in paniekklachten_q:
		print("")
		global c
		c = c + 1
		while True:
			print(x)
			print("")
			aa = input()
			if (aa == "ja" or aa == "nee"):
				f = open("antwoord.txt", "a")
				tx = "Paniekklachten " + str(c) + "C "
				f.write(tx)
				f.write(aa)
				f.write("\n")
				print(" ")
				f.close()
				paniekklachten_a.append(a)
				#Wanneer er een verkeerd antwoord ingevuld wordt.
				break
			else:
				print("")
				print("Onjuist antwoord")
				print("U heeft geantwoord met", a)
				print("")
				print("Antwoord alleen maar met ja/nee. \n")
				print("")
				continue


#MAIN FUNCTION
if __name__ == '__main__':

	# demografische vraag geslacht
	print("Wat is uw geslacht ?")
	print("Typ 1 voor man")
	print("Typ 2 voor vrouw \n")
	f = open("antwoord.txt", "a")
	antwoord1 = input()
	f.write("geslacht\n")
	f.write(antwoord1)
	f.write("\n")
	print(" ")
	f.close()
	geslacht_a.append(antwoord1)
	# demografische vraag leeftijd
	print("Wat is uw leeftijd?\n")
	f = open("antwoord.txt", "a")
	antwoord2 = input()
	f.write("leeftijd\n")
	f.write(antwoord2)
	f.write("\n")
	print(" ")
	f.close()
	leeftijd_a.append(antwoord2)
	print("")

	# Openingsvraag
	print("Ervaart u angst?  ja/nee\n")
	str1 = input()
	f = open("antwoord.txt", "a")
	f.write("Ervaart u angst ? \n")
	f.write(str1)
	f.write("\n")  #
	print(" ")
	f.close()
	leeftijd_a.append(antwoord2)
	print(" ")
	if str1 == "ja":
		print(
		    "Welk domein wilt u testen?\n 1 voor fobie \n 2 voor sociale angst\n 3 voor paniekklachten \n"
		)
		print(" ")
		x = input()
		f = open("antwoord.txt", "a")
		f.write(
		    "Welk domein wilt u testen? 1 voor fobie 2 voor sociale angst 3 voor paniekklachten \n"
		)

		print(" ")
		f.close()
		print(" ")
		#domein fobie
		if x == "1":
			fobie()
			print(
			    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee. "
			)
			check = input()
			print(" ")
			#vervolgdomein
			if check == "ja":
				print(
				    "Welk domein wilt u testen? U kunt kiezen uit sociale angst en paniekklachten.  "
				)
				print("Typ 1 for Sociale angst")
				print("Typ 2 2 voor paniekklachten")
				y = int(input())
				print(" ")
				#domein sociale angst
				if y == 1:
					socialeangst()
					print(
					    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee."
					)
					check = input()
					#vervolgdomein
					if check == "ja":
						print("paniekklachten \n ")
						paniekklachten()
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.write("")
						f.close()
						exit()
					else:
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
			# domein paniekklachten
				elif (y == 2):
					paniekklachten()
					print(
					    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee."
					)
					check = input()
					if check == "ja":
						print("socialeangst \n ")
						socialeangst()
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
					else:
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
			else:
				print(
				    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
				)
				f = open("antwoord.txt", "a")
				f.write("*----*----*----*----*----*----*----*----*\n")
				# f.write("\n")
				f.close()
				exit()

	# domein sociale angst
		elif x == "2":
			socialeangst()
			print("")
			check = input()
			print(
			    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee. "
			)
			# vervolg domein uitkiezen
			if check == "ja":
				print(
				    "Welk domein wilt u testen? U kunt kiezen uit fobie en paniekklachten. "
				)
				print("Typ 1 voor fobie")
				print("Typ 2 voor paniekklachten")
				y = int(input())
				print(" ")
				if y == 1:
					fobie()
					print(
					    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee."
					)
					check = input()
					if check == "ja":
						print("paniekklachten\n ")
						paniekklachten()
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
					else:
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
						#domein paniekklachten
				elif y == 2:
					paniekklachten()
					print(
					    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee."
					)
					check = input()
					if check == "ja":
						print("fobie \n ")
						fobie()
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
					else:
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()

			else:
				print(
				    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
				)
				f = open("antwoord.txt", "a")
				f.write("*----*----*----*----*----*----*----*----*\n")
				f.close()
				exit()
	#paniekklachten domein
		elif x == "3":
			paniekklachten()
			print(
			    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee."
			)
			check = input()
			print(" ")
			#Vervolgdomein kiezen
			if check == "ja":
				print(
				    "Welk domein wilt u testen? U kunt kiezen uit sociale angst en paniekklachten."
				)
				print("Typ 1 voor Sociale angst")
				print("Typ 2 voor fobie")
				y = int(input())
				print(" ")
				#keuze sociale angst
				if y == 1:
					socialeangst()
					print(
					    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee."
					)
					check = input()
					if check == "ja":
						print("fobie \n ")
						fobie()
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
					else:
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()

			# gekozen voor fobie
				elif y == 2:
					fobie()
					print(
					    "Wilt u ook nog andere domeinen testen? let er op dat u alleen maar kan antwoorden met ja of nee."
					)
					check = input()
					if check == "ja":
						print("socialeangst \n ")
						socialeangst()
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()
					else:
						print(
						    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
						)
						f = open("antwoord.txt", "a")
						f.write("*----*----*----*----*----*----*----*----*\n")
						f.close()
						exit()

			else:
				print(
				    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen.s"
				)
				f = open("antwoord.txt", "a")
				f.write("*----*----*----*----*----*----*----*----*\n")
				f.close()
				exit()

# einde vragenlijst
	else:
		print(
		    "Hartelijk dank voor het invullen van de vragenlijst. Uw antwoorden worden automatisch opgeslagen."
		)
		f = open("antwoord.txt", "a")
		f.write("*----*----*----*----*----*----*----*----*\n")
		#f.write("\n")
		f.close()
		exit()


