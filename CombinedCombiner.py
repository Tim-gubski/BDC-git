import csv

grads = []
agr = []

with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombined.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["State", "County", "GrossAgriculture", "GraduationRate"])

    with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\GradRatebyCounty.csv", 'r') as readFile:
        reader = csv.reader(readFile)
        with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\combined.csv", 'r') as readFile2:
            reader2 = csv.reader(readFile2)
            for grossAgr in reader2:
                agr.append(grossAgr)
            for gradRates in reader:
                grads.append(gradRates)

    for a in agr:
        for g in grads:
            if a[0].lower() == g[0].lower() and a[1].lower() == g[1].lower() and g[2].replace("%","").replace('.', '', 1).isdigit() and a[2].replace(",","").replace('-', '').isdigit():
                writer.writerow([a[0], a[1], a[2].replace(",",""), g[2].replace("%","")])




