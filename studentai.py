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

studentas1 = Studentas("Paulius", "Sermuksnis",[10,9,8,9,1,8,7,7,3,7,6,5,3,3,3,3,3])

studentas1.__str__()
valVid = studentas1.validus_vidurkis()
vid = studentas1.vidurkis()

print(f"vidurkio validumas: {valVid}, vidurkis: {vid}")