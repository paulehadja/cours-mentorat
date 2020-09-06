import plot
import consts
import utils
import csv
import sys

X = []
Y = []
fileName = 'sites.csv'
with open(fileName, newline='', encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile)
    try:
        for row in reader:
            X.append(round(float(row[3]), 2))
            Y.append(round(float(row[4]), 2))
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(fileName, reader.line_num, e))


#plot = plot.Plot()

#plot.Plot2D(X = X, Y = Y,
#            titre = "Evolution du ratio de la puissance utilisée en fonction du nombre d'itération", 
#            label="Ratio Puissance")
#plot.Plot2D(titre = "Evolution du ratio de sites utilisés en fonction du nombre d'itération")
#plot.Plot2D(titre = "Evolution du taux de couverture en fonction du nombre d'itération")
#plot.Plot2D(titre = "Evolution du taux d'utilisateurs connectés en fonction du nombre d'itération")

#plot.Plot2D(titre = "Evolution of the power used rate according to the number of iterations")

#plot.PlotScatter(titre = "Positioning of fixed sites on the area of interest")
#plot.PlotScatter(titre = "Final positioning of sites (fixed and added) on the area of interest")

puissance_minimale = float(input("Entrer la puissance minimale :  "))
puissance_maximale = float(input("Entrer la puissance maximale :  "))
superficie = float(input("Entrer la superficie en Km2 :  "))

print(puissance_maximale)
print(puissance_minimale)
print(superficie)