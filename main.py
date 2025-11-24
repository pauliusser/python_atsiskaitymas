from src import studentai as st
from src import e_shop_warehouse as eShop
from src.menu import mainMenu, stOptionsMenu, eShopOptionsMenu
from pathlib import Path
import os


def clnCons():
  os.system('cls')

def main():
  clnCons()
  exit = False
  while not(exit):
    mainMenu()
    inp = input("pasirinkite programą: ")
    if inp == "x":
       exit = True
    else:
      match inp:
        # MARK: stidemtai
        case"1":
          stList = st.studNusk("./files/studentai_lietuviski_INT.csv")
          exitStud = False
          clnCons()
          print("Studentų analizė:")
          while not(exitStud):
            print("\n\n---pasirinkimai---")
            stOptionsMenu()
            anOption = input("pasirinkite veiksmą: ")
            print("")
            match anOption:
              case "1":
                st.prntVidurkiuRikiuote(stList)
              case "2":
                st.prntSkolininkuSarasas(stList)
              case "3":
                st.prntGrupesStat(stList)
              case "4":
                filePath = "./files/pazangus.csv"
                st.pazangiujuFailas(filePath, stList)
                print(f'pažangių studentų sarašas sukurtas {filePath} ')
              case "5":
                filePath = "./files/ataskaita.txt"
                st.ataskaita("./files/ataskaita.txt", stList)
                print(f'grupės duomenų ataskaita sukurta {filePath} ')
              case "x":
                clnCons()
                exitStud = True
              case _:
                print("neteisingas pasirinkimas")
            input("paspauskite bet kurį klavišą")
        case"2":
          # MARK: eshop
          exitEShop = False
          clnCons()
          print("e-parduotuvės sandėlio valdymas:")
          data = []
          prekes = []
          dataDir = "./files/prekes250.txt"
          sarasoDir = "./files/sandėlis.csv"
          ataskDir = "./files/sandelio_ataskaita.txt" 
          file_path = Path(sarasoDir)         
          while not(exitEShop):
            if len(data) == 0:
              input(f'paspauskite bet kurį klavišą, kad nuskaitytumėte duomenis iš "{dataDir}"')
              data = eShop.duomenuNuskaitymas(dataDir)
              print(f'duomenys iš: "{dataDir}" nuskaityti')
            print("\n\n---pasirinkimai---")
            eShopOptionsMenu()
            eShopOption = input("pasirinkite veiksmą: ")
            print("")

            match eShopOption:
              case "1":
                eShop.prekiuGeneravimas(data, sarasoDir)
                prekes = eShop.prekiuNuksaitymas(sarasoDir)
                print(f'prekių sąrašas sugeneruotas "{sarasoDir}"\n ir prekės nuskaitytos')
              case "2":
                if not(file_path.exists()):
                  print(f'failas {sarasoDir} neegzistuoja, pirma sugeneruokite sąrašą\n')
                else:
                  if  len(prekes) == 0:
                    prekes = eShop.prekiuNuksaitymas(sarasoDir)
                  exitAnalize = False
                  while not(exitAnalize):
                    print ("---pasirinkimai---\n1. sandėlio statistika\n2. analizuoti kategorijas\nx. grįžti")
                    optAnalize = input(f"pasirinkite veiksmą: ")
                    match optAnalize:
                      case "1":
                        eShop.analizuotiA(prekes)
                      case "2":
                        eShop.analizuotiB(prekes)
                      case "x":
                        exitAnalize = True
                      case _:
                        print("neteisingas pasirinkimas")
              case "3":
                if not(file_path.exists()):
                  print(f'failas {sarasoDir} neegzistuoja, pirma sugeneruokite sąrašą\n')
                else:
                  if  len(prekes) == 0:
                    prekes = eShop.prekiuNuksaitymas(sarasoDir)
                  eShop.kurtiAtaskaita(prekes, ataskDir)
                  print(f'ataskaita "{ataskDir}" sugeneruota')
              case "x":
                clnCons()
                exitEShop = True
              case _:
                print("neteisingas pasirinkimas")
        case _:
          print("neteisingas pasirinkimas")
if __name__ == "__main__":
  main()