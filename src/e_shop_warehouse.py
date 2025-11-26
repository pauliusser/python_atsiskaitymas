import random
import csv

def duomenuNuskaitymas(filepath):
  data = []
  try:
    with open(filepath, "r", encoding="utf-8") as f:
      lines = f.readlines()
      # data = [l.strip().split(";") for l in lines]
      for i, line in enumerate(lines):
        lineData = line.strip().split(";")

        # duomenų kiekio eilutėje validacija
        if len(lineData) != 3:
          print(f"\033[31mklaida {i} eilutėje\033[0m\n    {line}    ne 3 duomenys - eilutė praleidžiama")
          continue
        
        # duomenų tipo 3 pozicijoje validacija
        try:
          float(lineData[2])
        except ValueError:
          print(f"\033[31mklaida {i} eilutėje\033[0m\n    {line}    pozicijoje 3 ne skaičius - eilutė praleidžiama")
          continue

        data.append(lineData)
  except FileNotFoundError:
        print(f'\033[31mklaida:\033[0m failas "{filepath}" nerastas')
        return []
  print(f"nuskaityti {len(data)} įrašai")
  return data

def prekiuGeneravimas(data, filepath):
  kat = sorted(set([d[1] for d in data]))
  pre = sorted(set([d[0] for d in data]))
  count = random.randint(0, 200)

  # kadangi kategorijų yra labai daug ir prekių palyginus mažai
  # t.y.:
  # print(f"unikaliu kategoriju yra: {len(kat)}")
  # print(f"unikaliu prekiu yra: {len(pre)}")
  # nesistengsiu rasti logikos ir duomenis sugeneruosiu atsitiktinai iš to kas yra pateikta
  # teoriškai būtų galima išsipirkti chatGPT api rakta tada pasikurt "pip install openai"
  # tada pateikus gudrią užklausą ir sulaukus ats. DI pagal semantiką sugrupuotu kategorijas ir daiktus. :)

  rndInts = [0 for _ in kat]
  maxIndex = len(rndInts) - 1
  for i in range(count):
    rndInts[random.randint(0, maxIndex)] += 1

  with open(filepath, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "prekė", "kategorija", "kaina", "likutis"])

    for index, k in enumerate(kat):    
      i = rndInts[index]    
      if i != 0:
        for j in range(i):
          rndPre = pre[random.randint(0, len(pre) - 1)]
          id = k[0].upper() + rndPre[0].upper() + str(index + 1) + str(j + 1).zfill(4)
          rndKaina = round(random.uniform(0.99,999.99), 2)
          rndLik = random.randint(0, 200)
          writer.writerow([id, rndPre, k, rndKaina, rndLik])

  # is pradziu bandziau duomenis pertvarkyti, turbut ne taip supratau uzduoti
  # palieku uzkomentuota dali kur pertvarko jau turima sarasa (gaila trinti)
  # t.y. grazina sarasa kuriame duomenys yra sugrupuoti, sugeneruoti id
  # ir jei papuole kaip siuksle likutis, jį irgi prideda pagal tai kas duota txt faile

  # ordered = []
  # for k in kat:
  #   filtered = list(filter(lambda d: d[1] == k, data))
  #   ordered.append(filtered)
  # finalData = []
  # for data in ordered:  
  #   for i, d in enumerate(data):
  #     id = d[0][0].upper() + d[1][0].upper() + str(kat.index(d[1]) + 1) + str(i+1).zfill(4)
  #     if len(d) < 4:
  #       likutis = 0
  #     elif len(d) == 4:
  #       likutis = d[3]
  #     finalData.append([id, *d[:3], likutis])
  # return finalData

def prekiuNuksaitymas(filepath):
  prekes = []

  with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")    
    for i, line in enumerate(lines):
      if i > 0:
        line = lines[i].strip().split(",")
        prekes.append({
          header[0]: line[0],           # ID
          header[1]: line[1],           # prekė
          header[2]: line[2],           # kategorija
          header[3]: float(line[3]),    # kaina
          header[4]: int(line[4])       # likutis
        })
  return prekes

def analizuotiA (prekes):
  brangiausiaPr = max(prekes, key=lambda p: p["kaina"])
  deficitinePr = min(prekes, key=lambda p: p["likutis"])
  kainuSum = round(sum([p["kaina"] * p["likutis"] for p in prekes]), 2)
  print(f"""
brangiausia prekė: {brangiausiaPr["prekė"]} - {brangiausiaPr["kaina"]} eur.
prekė su mažiausiu likučiu {deficitinePr["prekė"]} - {deficitinePr["likutis"]} vnt.
sandėlyje liko prekių už: {kainuSum} eur.
""")

def analizuotiB (prekes):
  kategorijos = sorted(set([p["kategorija"] for p in prekes]))
  print("\nkategorijos:")
  for i, kat in enumerate(kategorijos):
    print(f"{i + 1}. {kat}")
  pas = int(input("pasirinkite kategorijos numerį: ")) - 1
  k = kategorijos[pas]
  preSum = sum([1 for p in prekes if p["kategorija"] == k ])
  likSum = sum([p["likutis"] for p in prekes if p["kategorija"] == k])
  vidKain = round(sum([p["kaina"] for p in prekes if p["kategorija"] == k ]) / preSum, 2)
  print(f"""
kategorijoje - {k}:
skirtingų prekių kiekis: {preSum} prekės
visų prekių bendras likutis: {likSum} vnt.
vidutinė prekių kaina: {vidKain} eur.
""")

def kurtiAtaskaita(prekes, filepath):
  top10brang = sorted(prekes, key=lambda p: p["kaina"], reverse=True)[:10]
  likSar = [p for p in prekes if p["likutis"] < 5]
  sandVert = sum([p["kaina"] * p["likutis"] for p in prekes])

  def drawHorLine():
    f.write("+" + "-" * 10 + "+" + "-" * 17 + "+" + "-" * 17 + "+" + "-" * 9 + "+" + "-" * 9 + "+\n")
  def drawTable(list):
      drawHorLine()
      f.write(f"| {"ID":<8} | {"prekė":>15} | {"kategorija":>15} | {"kaina":>7} | {"likutis":>7} |\n")
      for p in list:
        drawHorLine()
        f.write(f"| {p["ID"]:<8} | {p["prekė"]:>15} | {p["kategorija"]:>15} | {p["kaina"]:>7} | {p["likutis"]:>7} |\n")
      drawHorLine()

  with open(filepath, "w", encoding="utf-8") as f:
    f.write("top 10 brangiausių prekių:\n")
    drawTable(top10brang)
    f.write("\nprekių su mažiausiu likučiu sąrašas:\n")
    if len(likSar) == 0: 
      f.write("\nprekių su mažesniu nei 5 vnt. likučiu nėra\n")
    else: 
      sortedLikSar = sorted(likSar, key=lambda p: p["likutis"])
      drawTable(sortedLikSar)
    f.write(f"\nVisų sandėlio prekių vertė: {sandVert} eur.")

# ---------atkomentuoti prasitestavimui----------

# data = duomenuNuskaitymas("./input_files/prekes250.txt")
# prekiuGeneravimas(data, "./output_files/sandėlis.csv")
# prekes = prekiuNuksaitymas("./output_files/sandėlis.csv")
# analizuotiA(prekes)
# analizuotiB(prekes)
# kurtiAtaskaita(prekes,"./output_files/sandelio_ataskaita.txt")