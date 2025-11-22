import csv
import statistics

# MARK: Studentas Class
class Studentas:
  def __init__(self, vardas: str, pavarde: str, pazymiai: list[int]):
    self.vardas = vardas
    self.pavarde = pavarde
    self.pazymiai = pazymiai

  def validus_vidurkis(self):
    return True if len(self.pazymiai) >= 3 else False
  
  def vidurkis(self):
    pCount = len(self.pazymiai)
    if pCount < 3:
      return None
    else:
      return round(sum(self.pazymiai) / pCount, 2)
  
  def __str__(self):
    paz = ", ".join(map(str, self.pazymiai))
    return f"studentas: {self.vardas} {self.pavarde}\npažymiai:  {paz}"

# MARK: csv f. nusk.

studentai = []

with open("./failai/studentai_lietuviski_INT.csv", newline="", encoding="windows 1257") as studCsvFile:
  reader = csv.DictReader(studCsvFile)
  for row in reader:
    vardas = row['Vardas']
    pavarde = row['Pavarde']
    pazymiai = []
    for i in range(1,11):
      p = row[f"paz{i}"]
      if p != "":
        pazymiai.append(int(p))
    studentai.append(Studentas(vardas, pavarde, pazymiai))

# for st in studentai:
#   print(st)
#   print("")

for st in studentai:
  valid = True
  for p in st.pazymiai:
    if p < 1 or p > 10:
      valid = False
      break
  if not valid: print(f"klaida, studento {st.vardas} {st.pavarde} ne visi pažymiai yra 1-10 diapozone")

# MARK: st. analize

def vidurkiuRikiuote():
  beSkolu = list(filter(lambda s: s.vidurkis() != None, studentai ))
  print(f"visi studentai: {len(studentai)}\nstudentai su tinkamu paž. sk.: {len(beSkolu)}\n")
  beSkolu.sort(key=lambda s: s.vidurkis(), reverse=True)
  i = 1
  for s in beSkolu:
    print(i)
    print(s)
    print(f"vidurkis: {s.vidurkis()}\n")
    i += 1

# vidurkiuRikiuote()

def skolininkuSarasas():
  skolininkai = list(filter(lambda s: s.vidurkis() == None, studentai ))
  print(f"skolininkų sąraše yra {len(skolininkai)} studentai:\n")
  for s in skolininkai:
    print(s)
    print("")

# skolininkuSarasas()

def grupesStat():
  # bendras vidurkis
  beSkolu = list(filter(lambda s: s.vidurkis() != None, studentai ))
  vidurkiai = [s.vidurkis() for s in beSkolu]
  bendrasVid = round(sum(vidurkiai) / len(vidurkiai), 2)

  # mediana
  visiPazymiai = []
  for st in studentai:
    for p in st.pazymiai:
      visiPazymiai.append(p)
  mediana = statistics.median(visiPazymiai)

  # max vidurkis
  maxVidurkis = round(max(vidurkiai), 2)

  # min vidurkis iš tų, kurie turi bent 3 pažymius
  minVidurkis = round(min(vidurkiai), 2)

  # studentų skaičius kurių vidurkis ≥ 8
  pazangiujuSk = sum([v >= 8 for v in vidurkiai])

  print(f"bendras vidurkių vidurkis: {bendrasVid}\nklasės pažimių mediana: {mediana}\ndidziausias vidurkis: {maxVidurkis}\nmažiausias vidurkis {minVidurkis}\nstudentų skaičius kurių vidurkis ≥ 8 yra: {pazangiujuSk}")

grupesStat()
