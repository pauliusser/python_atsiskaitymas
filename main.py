from src import studentai as st
from src import e_shop_warehouse as eShop
from src import meteorologine_analize as met
from src.menu import mainMenu, stOptionsMenu, eShopOptionsMenu, metOptionsMenu
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
      # MARK: studentai
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
              
            case "4": # sukurti pažangių studentų sarašą 'pazangus.csv'
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

      # MARK: eshop
      case"2":
        exitEShop = False
        isval()
        print("e-parduotuvės sandėlio valdymas:")
        data = []
        prekes = []
        dataDir = "./input_files/prekes250.txt"
        sarasoDir = "./output_files/sandelis.csv"
        ataskDir = "./output_files/sandelio_ataskaita.txt" 
        file_path = Path(sarasoDir) # cia tam kad po to butu galima patikrinti ar failas egzistuoja
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
                input("paspauskite enter")
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
      
      # MARK: meteo
      case"3":
        exitMet = False
        matavimai = None
        isval()
        print("meteorologinių duomenų analizė:")
        inpMetDPath = "./input_files/meteo365_no_date.txt"
        outBendStPath = "./output_files/bendra_statistika.txt"
        outKrAnPath = "./output_files/krituliai.txt"
        outEkstDPath = "./output_files/audra.txt"
        outMenStPath = "./output_files/menesiai.txt"
        outSezAtPath = "./output_files/metai.txt"
        while not(exitMet):
          if matavimai == None:
            input(f'paspauskite enter, kad nuskaitytumėte duomenis iš "{inpMetDPath}"')
            matavimai = met.duomenuNuskaitymas("./input_files/meteo365_no_date.txt")
            print(f'meteorologiniai duomenys iš: "{inpMetDPath}" nuskaityti')
          print("\n\n---pasirinkimai---")
          metOptionsMenu()
          metOpt = input("pasirinkite veiksmą: ")
          print("")
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
              isval()
              exitMet = True

            case _: # klaidos atvejis meteo programoje
              print("neteisingas pasirinkimas")

      # MARK: išėjimas
      case"x": 
        exit = True
        isval()
        print("pabaiga")
      
      # klaidos atvejis pagrindiniame meniu
      case _: 
        print("neteisingas pasirinkimas")

if __name__ == "__main__":
  main()