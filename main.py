from src import studentai as st
from src import e_shop_warehouse as eShop
from src.menu import mainMenu, stOptionsMenu, eShopOptionsMenu
from pathlib import Path
import os

def isval(): # konsoles isvalymas
  os.system('cls')

def main():
  isval()
  exit = False
  while not(exit):
    mainMenu()
    inp = input("pasirinkite programą: ")
    match inp:
      # MARK: stidemtai
      case"1":
        pazangusOut = "./output_files/pazangus.csv"
        ataskaitaOut = "./output_files/ataskaita.txt"
        stList = st.studNusk("./input_files/studentai_lietuviski_INT.csv")
        exitStud = False
        isval()
        print("Studentų analizė:")
        while not(exitStud):
          print("\n\n---pasirinkimai---")
          stOptionsMenu()
          anOption = input("pasirinkite veiksmą: ")
          print("")
          match anOption:
            case "1": # išrikiuoti studentų duomenis pagal vidurkį
              st.prntVidurkiuRikiuote(stList)

            case "2": # skolininkų sąrašas
              st.prntSkolininkuSarasas(stList)

            case "3": # grupes statistika
              st.prntGrupesStat(stList)
              
            case "4": # ukurti pažangių studentų sarašą 'pazangus.csv'
              st.pazangiujuFailas(pazangusOut, stList)
              print(f'pažangių studentų sarašas sukurtas {pazangusOut}')
              
            case "5": # sukurti grupės duomenų ataskaitą 'ataskaita.txt'
              st.ataskaita(ataskaitaOut, stList)
              print(f'grupės duomenų ataskaita sukurta {ataskaitaOut}')

            case "x": # grįžti
              isval()
              exitStud = True

            case _: # klaidos atvejis
              print("neteisingas pasirinkimas")

          input("paspauskite enter")
      case"2":
        # MARK: eshop
        exitEShop = False
        isval()
        print("e-parduotuvės sandėlio valdymas:")
        data = []
        prekes = []
        dataDir = "./input_files/prekes250.txt"
        sarasoDir = "./input_files/sandėlis.csv"
        ataskDir = "./input_files/sandelio_ataskaita.txt" 
        file_path = Path(sarasoDir)         
        while not(exitEShop):
          if len(data) == 0:
            input(f'paspauskite enter, kad nuskaitytumėte duomenis iš "{dataDir}"')
            data = eShop.duomenuNuskaitymas(dataDir)
            print(f'duomenys iš: "{dataDir}" nuskaityti')
          print("\n\n---pasirinkimai---")
          eShopOptionsMenu()
          eShopOption = input("pasirinkite veiksmą: ")
          print("")
          match eShopOption:
            case "1": # sugeneruoti atsitiktinių prekių sąrašo failą ir jo nuskaitymas
              eShop.prekiuGeneravimas(data, sarasoDir)
              prekes = eShop.prekiuNuksaitymas(sarasoDir)
              print(f'prekių sąrašas sugeneruotas "{sarasoDir}"\nir prekės nuskaitytos')
              
            case "2": # prekių analizė
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
              else:
                if  len(prekes) == 0:
                  prekes = eShop.prekiuNuksaitymas(sarasoDir)
                eShop.kurtiAtaskaita(prekes, ataskDir)
                print(f'ataskaita "{ataskDir}" sugeneruota')
                input("paspauskite enter")

            case "x": # išėjimas iš eshop programos
              isval()
              exitEShop = True

            case _: # klaidos atvejis eshop programoje
              print("neteisingas pasirinkimas")

      case"x": # išėjimas iš programos
        exit = True
        isval()
        print("pabaiga")

      case _: # klaidos atvjeis pagrindiniame meniu
        print("neteisingas pasirinkimas")

if __name__ == "__main__":
  main()