import random

def duomenuNuskaitymas(filepath):
  with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()
    data = [l.strip().split(";") for l in lines]
  return data

data = duomenuNuskaitymas("./files/prekes250.txt")
# print(data)


def prekiuGeneravimas(data, count):
  kat = sorted(set([d[1] for d in data]))
  pre = sorted(set([d[0] for d in data]))

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

  c = 0
  dataList = []
  for index, k in enumerate(kat):
    
    i = rndInts[index]
    
    if i != 0:
      for j in range(i):
        if c == count: break
        rndPre = pre[random.randint(0, len(pre) - 1)]
        id = k[0].upper() + rndPre[0].upper() + str(index + 1) + str(j + 1).zfill(4)
        rndKaina = round(random.uniform(0.99,999.99), 2)
        rndLik = random.randint(0, 200)
        dataList.append([id, rndPre, k, rndKaina, rndLik])
        c += 1

  for d in dataList:
    print(d)

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

prekiuGeneravimas(data, 20)