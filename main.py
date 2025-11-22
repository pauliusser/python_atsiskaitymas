from src import studentai as st
import os

def stOptionsMenu():
  print("""
1. išrikiuoti studentų duomenis pagal vidurkį
2. skolininkų sąrašas
3. grupės statistika
4. sukurti pažangių studentų sarašą 'pazangus.csv'
5. sukurti grupės duomenų ataskaitą 'ataskaita.txt'
x. grįžti
""")

def clnCons():
  os.system('cls')

def main():
  clnCons()
  exit = False
  while not(exit):
    print("\n1. Studentai\nx. išeiti\n")
    inp = input("pasirinkite programą: ")
    if inp == "x":
       exit = True
    else:
      match inp:
        case"1":
          stList = st.studNusk("./files/studentai_lietuviski_INT.csv")
          exitStud = False
          clnCons()
          print("Studentų analizė:")
          while not(exitStud):
            print("\n\n--- pasirinkimai ---")
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
        case _:
          print("neteisingas pasirinkimas")
if __name__ == "__main__":
    main()