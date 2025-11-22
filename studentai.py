import csv
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
    return f"studentas: {self.vardas} {self.pavarde}\npazymiai:  {paz}"

# studentas1 = Studentas("Paulius", "Sermuksnis",[10,9,8,9,1,8,7,7,3,7,6,5,3,3,3,3,3])
# print(studentas1)
# valVid = studentas1.validus_vidurkis()
# vid = studentas1.vidurkis()
# print(f"vidurkio validumas: {valVid}, vidurkis: {vid}")

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

for st in studentai:
  print(st)
  print("")

for st in studentai:
  valid = True
  for p in st.pazymiai:
    if p < 1 or p > 10:
      valid = False
      break
  if not valid: print(f"klaida, studento {st.vardas} {st.pavarde} ne visi pazymiai yra 1-10 diapozone")