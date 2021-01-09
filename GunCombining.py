import csv

grads = []
guns = []

with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\superCombinedGuns.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["State", "County", "GunsByCounty", "GraduationRate"])

    with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\GradRatebyCounty.csv", 'r') as readFile:
        reader = csv.reader(readFile)
        with open(r"C:\Users\timgu\Downloads\BDC\COMBINED\GunsByCounty.csv", 'r') as readFile2:
            reader2 = csv.reader(readFile2)
            for gun in reader2:
                guns.append(gun)
            for gradRates in reader:
                grads.append(gradRates)

    for a in guns:
        for g in grads:
            if a[0].lower() == g[0].lower() and a[1].lower() == g[1].lower() and g[2].replace("%","").replace('.', '', 1).isdigit() and a[2].replace(",","").replace("-","").isdigit():
                writer.writerow([a[0], a[1], a[2].replace(",",""), g[2].replace("%","")])





