from src import studentai as st
from src import e_shop_warehouse as eShop
from src import meteorologine_analize as met
from src.menu import mainMenu, stOptionsMenu, eShopOptionsMenu, metOptionsMenu
from pathlib import Path
import os

path = "./output_files"
if not os.path.exists(path):
  os.makedirs(path)

def isval(): # konsoles isvalymas
  os.system('cls')

def main():
  exit = False
  while not(exit):
    isval()
    mainMenu()
    inp = input("pasirinkite programą: ")
    isval()
    match inp:
      # MARK: studentai
      case"1":
        inputFile = "./input_files/studentai_lietuviski_INT.csv"
        pazangusOut = "./output_files/pazangus.csv"
        ataskaitaOut = "./output_files/ataskaita.txt"
        stList = st.studNusk(inputFile)
        if len(stList) == 0 :
          input("duomenų nėra: paspauskite enter\n")
          continue
        print(f'failas "{inputFile}" nuskaitytas')
        input("paspauskite enter\n")
        exitStud = False
        while not(exitStud):
          isval()
          print("Studentų analizė:\n\n---pasirinkimai---")
          stOptionsMenu()
          anOption = input("pasirinkite veiksmą: ")
          isval()
          match anOption:
            case "1": # išrikiuoti studentų duomenis pagal vidurkį
              st.prntVidurkiuRikiuote(stList)
              input("paspauskite enter")

            case "2": # skolininkų sąrašas
              st.prntSkolininkuSarasas(stList)
              input("paspauskite enter")

            case "3": # grupes statistika
              st.prntGrupesStat(stList)
              input("paspauskite enter")
              
            case "4": # sukurti pažangių studentų sarašą 'pazangus.csv'
              st.pazangiujuFailas(pazangusOut, stList)
              print(f'pažangių studentų sarašas sukurtas {pazangusOut}')
              input("paspauskite enter")
              
            case "5": # sukurti grupės duomenų ataskaitą 'ataskaita.txt'
              st.ataskaita(ataskaitaOut, stList)
              print(f'grupės duomenų ataskaita sukurta {ataskaitaOut}')
              input("paspauskite enter")

            case "x": # iseiti is studentu programos
              exitStud = True

            case _: # klaidos atvejis
              print("neteisingas pasirinkimas")
              input("paspauskite enter")

      # MARK: eshop
      case"2":
        exitEShop = False
        prekes = []
        dataDir = "./input_files/prekes250.txt"
        sarasoDir = "./output_files/sandelis.csv"
        ataskDir = "./output_files/sandelio_ataskaita.txt" 
        file_path = Path(sarasoDir) # cia tam kad po to butu galima patikrinti ar failas egzistuoja
        isval()
        data = eShop.duomenuNuskaitymas(dataDir)
        if len(data) == 0:
          input("duomenų nėra, paspauskite enter\n")
          continue
        print(f'duomenys iš: "{dataDir}" nuskaityti')
        input("paspauskite enter\n")
        while not(exitEShop):
          isval()
          print("e-parduotuvės sandėlio valdymas:\n\n---pasirinkimai---")
          eShopOptionsMenu()
          eShopOption = input("pasirinkite veiksmą: ")
          isval()
          match eShopOption:
            case "1": # sugeneruoti atsitiktinių prekių sąrašo failą ir jo nuskaitymas
              eShop.prekiuGeneravimas(data, sarasoDir)
              prekes = eShop.prekiuNuksaitymas(sarasoDir)
              print(f'prekių sąrašas sugeneruotas "{sarasoDir}"\nir prekės nuskaitytos')
              input("paspauskite enter")
              
            case "2": # prekių analizė
              if not(file_path.exists()):
                print(f'failas {sarasoDir} neegzistuoja, pirma sugeneruokite sąrašą\n')
                input("paspauskite enter")
              else:
                if  len(prekes) == 0:
                  prekes = eShop.prekiuNuksaitymas(sarasoDir)
                exitAnalize = False
                while not(exitAnalize):
                  isval()
                  print ("---pasirinkimai---\n1. sandėlio statistika\n2. analizuoti kategorijas\nx. grįžti")
                  optAnalize = input(f"pasirinkite veiksmą: ")
                  isval()
                  match optAnalize:
                    case "1": # sandėlio statistika
                      eShop.analizuotiA(prekes)
                      input("paspauskite enter")

                    case "2": # analizuoti kategorijas
                      eShop.analizuotiB(prekes)
                      input("paspauskite enter")

                    case "x": # grįžti
                      exitAnalize = True
                      
                    case _: # klaidos atvejis
                      print("neteisingas pasirinkimas")

            case "3": # kurti ataskaitą txt faile
              if not(file_path.exists()): # patikrinama ar duomenu failas egzistuoja
                print(f'failas {sarasoDir} neegzistuoja, pirma sugeneruokite sąrašą\n')
                input("paspauskite enter")
              else:
                if  len(prekes) == 0:
                  prekes = eShop.prekiuNuksaitymas(sarasoDir)
                eShop.kurtiAtaskaita(prekes, ataskDir)
                print(f'ataskaita "{ataskDir}" sugeneruota')
                input("paspauskite enter")

            case "x": # išėjimas iš eshop programos
              exitEShop = True

            case _: # klaidos atvejis eshop programoje
              print("neteisingas pasirinkimas")
      
      # MARK: meteo
      case"3":
        exitMet = False
        matavimai = None
        inpMetDPath = "./input_files/meteo365_no_date.txt"
        outBendStPath = "./output_files/bendra_statistika.txt"
        outKrAnPath = "./output_files/krituliai.txt"
        outEkstDPath = "./output_files/audra.txt"
        outMenStPath = "./output_files/menesiai.txt"
        outSezAtPath = "./output_files/metai.txt"
        isval()
        matavimai = met.duomenuNuskaitymas("./input_files/meteo365_no_date.txt")
        print(f'meteorologiniai duomenys iš: "{inpMetDPath}" nuskaityti')
        input(f'paspauskite enter')
        while not(exitMet):
          isval()
          print("meteorologinių duomenų analizė:\n\n---pasirinkimai---")
          metOptionsMenu()
          metOpt = input("pasirinkite veiksmą: ")
          isval()
          match metOpt:
            case "1": # isspausdina pasirinktos dienos duomenis
              diena = input("pasirinkite sk. dienai nuo 1 iki 365: ")
              if not(diena.isdigit()): print("klaida - tai turi būti skaičius nuo 1 iki 365")
              elif 1 > int(diena) > 365: print("klaida - tai turi būti skaičius nuo 1 iki 365")
              else:
                met.isspausdintiDiena(int(diena), matavimai)
                input("paspauskite enter")

            case "2": # bendra statistika
              met.bendraStatistika(outBendStPath, matavimai)
              print(f"sukurta bendra metinė oro salygų statistika ir išsaugota į {outBendStPath}")
              input("paspauskite enter")
            
            case "3": # krituliu analize
              met.krituliuAnalize(outKrAnPath, matavimai)
              print(f"sukurta kritulių statistika ir išsaugota į {outKrAnPath}")
              input("paspauskite enter")
            
            case "4": # ekstremalios dienos
              met.ekstremaliosDienos(outEkstDPath, matavimai)
              print(f"sukurta ekstremalaus oro statistika ir išsaugota į {outEkstDPath}")
              input("paspauskite enter")
            
            case "5": # menesine oro salygu statistika
              met.menesiuStatistika(outMenStPath, matavimai)
              print(f"sukurta menesine oro salygu statistika ir išsaugota į {outMenStPath}")
              input("paspauskite enter")
            
            case "6": # sezonine oro salygu statistika
              met.metuLaikuStatistika(outSezAtPath, matavimai)
              print(f"sukurta sezonine oro salygu statistika ir išsaugota į {outMenStPath}")
              input("paspauskite enter")
            
            case "x": # isejimas is meteo programos
              exitMet = True

            case _: # klaidos atvejis meteo programoje
              print("neteisingas pasirinkimas")

      # MARK: išėjimas
      case"x": 
        exit = True
        isval()
        print(
        "              pabaiga\n\n" \
        "Programą parašė: Paulius Šermukšnis\n\n" \
        "            2025 11 27\n\n")
      
      # klaidos atvejis pagrindiniame meniu
      case _: 
        print("neteisingas pasirinkimas")

if __name__ == "__main__":
  main()