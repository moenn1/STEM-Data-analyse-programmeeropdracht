#importeren om functies zoals numpy beschikaar te krijgen
import numpy
import matplotlib as mpl 
import matplotlib.pyplot

data = numpy.loadtxt("dataset.txt", dtype = str, delimiter = ", ")

print(data)

shape = data.shape
print()
#de range functie produceert een lijst
for i in range(0,shape[0]):
 str1 = data[i,0]
 str2 = data[i,4]
  #Replace vervangt een specifieke karakter
 data[i,0] = str1.replace('[','')
 data[i,4] = str2.replace(']','')
#print(data)
print()
for kolom in range(0,shape[1]):
 for rij in range(0, shape[0]):
  item = data[rij,kolom]
  data[rij,kolom] = item.replace("'", '')
   
print(data)

# Eerst nemen we de gender kolom apart, in dit geval is dat de kolom op index 0
genders = data[:,0]
# Vervolgens maken we een variabele aan om de tel van het aantal mannen in bij te houden
aantal_mannen = 0
# In een for-loop gaan we elk element in genders bij langs. Is het een man? Dan tellen we 1 op bij de tel variabele aantal_mannen.
for gender in genders:
 if gender.lower() == "man": #lower() maakt eventuele hoofdletters klein
  aantal_mannen = aantal_mannen + 1
print("Aantal mannen in de data: ")
print(aantal_mannen)

genders = data[:,0]
print("Aantal vrouwen in de data: ")
aantal_vrouwen = list(genders).count("vrouw")
print(aantal_vrouwen)
print()
# Eerst nemen we de leeftijd kolom apart, de leeftijden staan op index 1 
leeftijden = data[:,1]
#print(leeftijden)

# Nu zijn alle waarden nog strings. We kunnen alleen gemiddeldes berekenen met floats (floats zijn getallen die decimalen kunnen hebben)

leeftijden = leeftijden.astype(float)

print(leeftijden)

# Nu kunnen we het gemiddelde berekenen 
print(numpy.mean(leeftijden))

print()

# Verander alle ja's in 1
data[data == 'ja'] = 1
# Verander alle nee's in 0
data[data == 'nee'] = 0
# Verander alle 'onbekend' in een missing value (nan)
data[data == 'onbekend'] = numpy.nan
print(data)

print()

## Totaal score op vragen per respondent 
scores = data[:,2:5]
print(scores)
scores = scores.astype(float) 
print (scores)
# We berekenen de som per rij met 'nansum'. Deze functie kan de missende vragen negeren. Met axis = 1 zorgen we ervoor dat de som per rij wordt berekend. 
print()
totaalsom_per_respondent = numpy.nansum(scores, axis = 1) 
print(totaalsom_per_respondent)

print()
gemiddelde_score_per_respondent = numpy.nanmean(scores, axis = 1) 
print(gemiddelde_score_per_respondent)

print()

mpl.use('Agg')
# de coordinaten per punt 
x_coords = [0,1,2,3,4,5] 
y_coords =[0,1,4,9,16,25]

#go is groen, -r is rood
matplotlib.pyplot.plot(x_coords,y_coords,'go')
matplotlib.pyplot.savefig('graph.png')

x_values = [0,1,2,3,4,5] 
x_squared = [0,1,4,9,16,25] 
x_cubed = [0,1,8,27,64,125]
matplotlib.pyplot.plot(x_values, x_squared, 'go', x_values, x_cubed, 'r-')
# Geef de x-as en y-as een label
matplotlib.pyplot.xlabel('de x-ax is klein')
matplotlib.pyplot.ylabel('de y-ax is groot', fontsize = 25)
matplotlib.pyplot.text(1.00,100., "mijn eerste plotje", color = 'blue', fontsize = 20)
matplotlib.pyplot.text(4.00,100., "$x^3$", color = 'red', fontsize = 20)
matplotlib.pyplot.savefig('graph2.png')


numpy_hist=matplotlib.pyplot.figure() 
matplotlib.pyplot.hist([1,2,1], bins=[0,1,2,3])
matplotlib.pyplot.savefig('graph3.png')