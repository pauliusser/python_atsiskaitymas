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
def studNusk(path):
  studentai = []

  try:
    with open(path, newline="", encoding="utf-8") as studCsvFile:
      reader = csv.DictReader(studCsvFile)
      for i, row in enumerate(reader):
        if len(row) != 12:
          print(f"\033[31mklaida {i + 1} eilutėje\033[0m turi būti 12 duomenų, o yra {len(row)}")
          continue
        vardas = row['Vardas']
        pavarde = row['Pavarde']
        pazymiai = []
        error = False
        for j in range(1,11):
          p = row[f"paz{j}"]
          if p != "":
            try:
              pazymys = int(p)
            except ValueError:
              print(f'\033[31mklaida {i + 1} eiluteje\033[0m pozicijoje "paz{j}" ne pažymys: "{p}"')
              error = True
              continue
            if pazymys < 1 or pazymys > 10:
              print(f'\033[31mklaida {i + 1} eiluteje\033[0m pozicijoje "paz{j}" pažymys: "{p}" nėra nuo 1 iki 10')
              error = True
              continue
            pazymiai.append(pazymys)
        if error: continue
        studentai.append(Studentas(vardas, pavarde, pazymiai))
  except FileNotFoundError:
        print(f'\033[31mklaida:\033[0m failas "{path}" nerastas')
        return []
  print(f"nuskaityti {len(studentai)} įrašai")
  return studentai

# MARK: st. analize

def vidurkiuRikiuote(studentai):
  beSkolu = list(filter(lambda s: s.vidurkis() != None, studentai ))
  beSkolu.sort(key=lambda s: s.vidurkis(), reverse=True)
  return beSkolu

def prntVidurkiuRikiuote(st):
    i = 1
    for s in vidurkiuRikiuote(st):
      print(i)
      print(s)
      print(f"vidurkis: {s.vidurkis()}\n")
      i += 1

# skolininku sarasas

def skolininkuSarasas(studentai):
  return [s for s in studentai if s.vidurkis() is None]

def prntSkolininkuSarasas(st):
  skolininkai = skolininkuSarasas(st)
  print(f"skolininkų sąraše yra {len(skolininkai)} studentai:\n")
  for s in skolininkai:
    print(s)
    print("")

# grup stat

def grupesStat(studentai):
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
  pazangiujuSk = sum(v >= 8 for v in vidurkiai) # arba: sum(1 for v in vidurkiai if v >= 8)
  stat = dict(
    bendrasVid=bendrasVid,
    mediana=mediana,
    maxVidurkis=maxVidurkis,
    minVidurkis=minVidurkis,
    pazangiujuSk=pazangiujuSk
    )

  return stat

def prntGrupesStat(st):
  stat = grupesStat(st)
  print(f"""
grupės statistika:
bendras vidurkių vidurkis: {stat["bendrasVid"]}
klasės pažimių mediana: {stat["mediana"]}
didziausias vidurkis: {stat["maxVidurkis"]}
mažiausias vidurkis {stat["minVidurkis"]}
studentų skaičius kurių vidurkis ≥ 8 yra: {stat["pazangiujuSk"]}""")

# MARK: filtr ir rez

def pazangiujuFailas( path, studentai):
  beSkolu = list(filter(lambda s: s.vidurkis() != None, studentai ))
  pazangieji = list(filter(lambda s: s.vidurkis() >= 8, beSkolu ))
  with open(path, "w", newline="", encoding="UTF-8") as file:
    antrastes = ["Vardas", "Pavarde", "Vidurkis"]
    writer = csv.DictWriter(file, fieldnames=antrastes)
    writer.writeheader()

    for st in pazangieji:
      writer.writerow({
        "Vardas": st.vardas,
        "Pavarde": st.pavarde,
        "Vidurkis": st.vidurkis()
      })

# MARK: ataksaita

def ataskaita(path, studentai):
  with open(path, "w", encoding="utf-8") as ataskaita:

    ataskaita.write("ATASKAITA\n\n")

    # 10 geriausiai besimokanciu studentu
    ataskaita.write("10 pažangiausiųjų studentų:\n\n")
    nr = 1
    for st in vidurkiuRikiuote(studentai)[:10]:
      ataskaita.write(f"{nr}. {st.vardas} {st.pavarde} - {st.vidurkis()}\n")
      nr += 1
    
    # studentai kurių vidurkis neskaičiuojamas
    ataskaita.write("\nstudentai kurių vidurkis neskaičiuojamas:\n\n")
    for st in skolininkuSarasas(studentai):
      ataskaita.write(f"{st.vardas} {st.pavarde} - vidurkis neskaičiuojamas (trūksta {3 - len(st.pazymiai)} pažimių(o))\n")
    
    #grupės statistika
    stat = grupesStat(studentai)
    ataskaita.write("\ngrupės statistika:\n\n")
    ataskaita.write(f"bendras vidurkių vidurkis: {stat['bendrasVid']}\n")
    ataskaita.write(f"klasės pažimių mediana: {stat['mediana']}\n")
    ataskaita.write(f"didziausias vidurkis: {stat['maxVidurkis']}\n")
    ataskaita.write(f"mažiausias vidurkis {stat['minVidurkis']}\n")
    ataskaita.write(f"studentų skaičius kurių vidurkis ≥ 8 yra: {stat['pazangiujuSk']}\n")


# ---------atkomentuoti prasitestavimui----------

# stList = studNusk("./input_files/studentai_lietuviski_INT.csv")
# prntVidurkiuRikiuote(stList)
# prntSkolininkuSarasas(stList)
# prntGrupesStat(stList)
# pazangiujuFailas("./output_files/pazangus.csv", stList)
# ataskaita("./output_files/ataskaita.txt", stList)