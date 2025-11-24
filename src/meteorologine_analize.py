from datetime import date, timedelta
from statistics import median

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

def duomenuNuskaitymas(filepath):
  matavimai = []
  with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
      if i > 0:
        data = line.strip().split(";")
        matavimai.append(Matavimas(*data))
  return matavimai

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

def krituliuAnalize(filepath, matavimai):
  def dKK(nuo, iki=None): # dienos kai krituliai buvo nuo iki
    return len([m for m in matavimai if m.krituliai[0] >= nuo and (iki is None or m.krituliai[0] < iki)])
  krDienuSk = [dKK(0,5), dKK(5,15), dKK(15,30), dKK(30)]
  diapozonas = ["0-5","5-15","15-30","≥30"]
  with open(filepath, "w", encoding="utf-8") as f:
    f.write("2023 metų kritulių statistika:\n\n")
    for i, s in enumerate(krDienuSk):
      f.write(f"{diapozonas[i]:>5} mm {"█" * int(s / max(krDienuSk) * 50):<50} ({s} d.)\n")
    



matavimai = duomenuNuskaitymas("./input_files/meteo365_no_date.txt")
bendraStatistika("./output_files/bendra_statistika.txt", matavimai)
krituliuAnalize("./output_files/krituliai.txt", matavimai)

# print("---------")
# print(matavimai[0].temperatura[0])