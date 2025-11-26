from datetime import date, timedelta
from statistics import median

# MARK: Class
class Matavimas:
  def __init__(self, diena, temperatura, krituliai, vejas):
    # print(diena, temperatura, krituliai, vejas)
    self.diena = [int(diena), diena]
    self.data = date(2023, 1, 1) + timedelta(int(diena) - 1)
    match self.data.weekday():
      case 0: savD = "pirmadienis"
      case 1: savD = "antradienis"
      case 2: savD = "trečiadienis"
      case 3: savD = "ketvirtadienis"
      case 4: savD = "penktadienis"
      case 5: savD = "šeštadienis"
      case 6: savD = "sekmadienis"
    self.savaitesDiena = savD
    m = self.data.month
    match m:
      case 1: men = "sausis"
      case 2: men = "vasaris"
      case 3: men = "kovas"
      case 4: men = "balandis"
      case 5: men = "gegužė"
      case 6: men = "birželis"
      case 7: men = "liepa"
      case 8: men = "rubpjūtis"
      case 9: men = "rugsėjis"
      case 10: men = "spalis"
      case 11: men = "lapkritis"
      case 12: men = "gruodis"
    self.menuo = men
    if 3 <= m <= 5: mL = "pavasaris"
    elif 6 <= m <= 8: mL = "vasara"
    elif 9 <= m <= 11: mL = "ruduo"
    else: mL = "žiema"
    self.metuLaikas = mL
    self.temperatura = [float(temperatura), temperatura + " °C"]
    self.krituliai = [float(krituliai), krituliai + " mm"]
    self.vejas = [float(vejas), vejas + " m/s"]

  def menesiai():
    return ["sausis","vasaris","kovas","balandis","gegužė","birželis","liepa","rubpjūtis","rugsėjis","spalis","lapkritis","gruodis"]

  def metuLaikai():
    return ["pavasaris","vasara","ruduo","žiema"]

  def __str__(self):
    return f"""
Diena: {self.diena[1]}
Data: {self.data}
Savaitės diena: {self.savaitesDiena}
Mėnuo: {self.menuo}
Metų laikas: {self.metuLaikas}
Temperatūra: {self.temperatura[1]}
Krituliai: {self.krituliai[1]}
Vėjas: {self.vejas[1]}"""
  
# MARK: nuskaitymas
def duomenuNuskaitymas(filepath):
  matavimai = []
  try:
    with open(filepath, "r", encoding="utf-8") as f:
      lines = f.readlines()
      for i, line in enumerate(lines):
        if i > 0: # tiesiog ignoruojama pirma eilutė
          data = line.strip().split(";")
          if len(data) != 4:
            print(f'\033[31mklaida {i} eilutėje\033[0m turi būti 4 duomenys')
          try:
            int(data[0])
            float(data[1])
            float(data[2])
            float(data[3])
          except ValueError:
            print(f'\033[31mklaida {i} eilutėje\033[0m netinkami duomenys: {line.strip("\n")}')
            continue
          matavimai.append(Matavimas(*data))
  except FileNotFoundError:
    print(f'\033[31mklaida:\033[0m failas "{filepath}" nerastas')
    return []
  print(f"nuskaityti {len(matavimai)} įrašai")
  return matavimai

# MARK: bendr stat
def bendraStatistika(filepath, matavimai):
  temps = [m.temperatura[0] for m in matavimai]
  metuVidTemp = round(sum(temps) / len(matavimai), 2)
  mteuTempMed = median(temps)
  maxTempDiena = max(matavimai, key=lambda m: m.temperatura[0])
  minTempDiena = min(matavimai, key=lambda m: m.temperatura[0])
  karstuDienSk = len([m for m in matavimai if m.temperatura[0] > 25])
  saltuDienuSk = len([m for m in matavimai if m.temperatura[0] < -10])

  with open(filepath, "w", encoding="utf-8") as f:
    f.write("2023 metų temperatūrų statistika:\n\n")
    f.write(f"metų vidutinė tepmeratūra: {metuVidTemp} °C\n")
    f.write(f"metų tepmeratūros mediana: {mteuTempMed} °C\n")
    f.write(f"karščiausia diena: {maxTempDiena.data} {maxTempDiena.savaitesDiena} {maxTempDiena.temperatura[1]}\n")
    f.write(f"šalčiausia diena: {minTempDiena.data} {minTempDiena.savaitesDiena} {minTempDiena.temperatura[1]}\n")
    f.write(f"dienų skaičius, kai temperatūra buvo > +25°C: {karstuDienSk}\n")
    f.write(f"dienų skaičius, kai temperatūra buvo < –10°C: {saltuDienuSk}\n")

# MARK: krit an
def krituliuAnalize(filepath, matavimai):
  def dKK(nuo, iki=None): # dienos kai krituliai buvo nuo iki
    return len([m for m in matavimai if m.krituliai[0] >= nuo and (iki is None or m.krituliai[0] < iki)])
  krDienuSk = [dKK(0,5), dKK(5,15), dKK(15,30), dKK(30)]
  diapozonas = ["0-5","5-15","15-30","≥30"]
  with open(filepath, "w", encoding="utf-8") as f:
    f.write("2023 metų kritulių statistika:\n\n")
    for i, s in enumerate(krDienuSk):
      f.write(f"{diapozonas[i]:>5} mm {"█" * int(s / max(krDienuSk) * 50):<50} ({s} d.)\n")

# MARK: audros
def ekstremaliosDienos(filepath, matavimai):
  audros = [m for m in matavimai if m.vejas[0] >= 15 and m.krituliai[0] >= 10]
  with open(filepath, "w", encoding="utf-8") as f:
    f.write("2023 metais kilusios audros:\n\n")
    for a in audros:
      f.write(f"{a.data} {"(" + a.savaitesDiena :>17}) - AUDRA: krituliai {a.krituliai[1] :<4}, vėjas {a.vejas[1] :<4}\n")

# MARK: men stat
def menesiuStatistika(filepath, matavimai):
  menesiai = Matavimas.menesiai()
  with open(filepath, "w", encoding="utf-8") as f:
    f.write("2023 metų mėnesinė oro sąlygų ataskaita:\n")
    for men in menesiai:
      tempList = [m.temperatura[0] for m in matavimai if m.menuo == men]
      kritList = [m.krituliai[0] for m in matavimai if m.menuo == men]
      vejoList = [m.vejas[0] for m in matavimai if m.menuo == men]
      f.write(f"\n{men.upper()}:\n")
      f.write(f"Vid. temperatūra: {round(sum(tempList) / len(tempList), 1)} °C\n")
      f.write(f"Max temp:         {max(tempList)} °C\n")
      f.write(f"Min temp:         {min(tempList)} °C\n")
      f.write(f"Viso kritulių:    {round(sum(kritList), 1)} mm\n")
      f.write(f"Vid. vėjas:       {round(sum(vejoList) / len(vejoList), 1)} m/s\n")

# MARK: sezonu stat
def metuLaikuStatistika(filepath, matavimai):
  metuLaikai = Matavimas.metuLaikai()
  with open(filepath, "w", encoding="utf-8") as f:
    f.write("2023 metų sezoninė oro sąlygų ataskaita:\n")
    for ml in metuLaikai:
      mlMatav = [m for m in matavimai if m.metuLaikas == ml]
      tempList = [m.temperatura[0] for m in matavimai if m.metuLaikas == ml]
      kritList = [m.krituliai[0] for m in matavimai if m.metuLaikas == ml]
      vejoList = [m.vejas[0] for m in matavimai if m.metuLaikas == ml]
      minTempDiena = min(mlMatav, key=lambda m: m.temperatura[0])
      maxTempDiena = max(mlMatav, key=lambda m: m.temperatura[0])
      maxKritDiena = max(mlMatav, key=lambda m: m.krituliai[0])
      f.write(f"\n=== {ml.upper()} ===\n")
      f.write(f"Vid. temperatūra: {round(sum(tempList) / len(tempList), 1)} °C\n")
      f.write(f"Viso kritulių:    {round(sum(kritList), 1)} mm\n")
      f.write(f"Vid. vėjas:       {round(sum(vejoList) / len(vejoList), 1)} m/s\n")
      f.write(f"\n-- šalčiausia diena --{str(minTempDiena)}\n")
      f.write(f"\n-- šilčiausia diena --{str(maxTempDiena)}\n")
      f.write(f"\n-- daugiausia krit. diena --{str(maxKritDiena)}\n\n")

# MARK: print day
def isspausdintiDiena(diena, matavimai):
  if 0 > diena > 365:
    print ("metuose tokios dienos nėra")
  else:
    print (matavimai[diena - 1])


# ---------atkomentuoti prasitestavimui----------

# matavimai = duomenuNuskaitymas("./input_files/meteo365_no_date.txt")
# bendraStatistika("./output_files/bendra_statistika.txt", matavimai)
# krituliuAnalize("./output_files/krituliai.txt", matavimai)
# ekstremaliosDienos("./output_files/audra.txt", matavimai)
# menesiuStatistika("./output_files/menesiai.txt", matavimai)
# metuLaikuStatistika("./output_files/metai.txt", matavimai)
# isspausdintiDiena(74, matavimai)