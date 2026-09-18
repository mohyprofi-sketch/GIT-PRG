import json
import random
from nicegui import ui





with open("sample.json") as f:
    seznam = json.load(f)

    print("Aktualní seznam", seznam)

    barvy = {1: "green",
             2: "lightgreen",
             3: "yellow",
             4: "orange",
             5: "red"
         
    }
    emoji = {1: "😁",
             2: "😊",
             3: "😐",
             4: "😔",
             5: "😭"
             
        }

    jmeno_input = ui.input("Jméno studenta")
    krabicka = ui.label("Zde bude známka")

    def pridat_znamku():
         student = jmeno_input.value
         if not student:
              return
            
         znamka = random.randint(1, 5)

         seznam[student] = znamka 
         with open("sample.json", "w", encoding="utf-8") as f:
                 json.dump(seznam, f, indent=4)
         krabicka.text = f"{student}: {znamka} {emoji[znamka]}"
         krabicka.style(f"background-color: {barvy[znamka]}; padding: 10px; font-size: 20px;")
         print("Ahoj")

    ui.button("Udělit známku", on_click = pridat_znamku)
    
    ui.run()



        

         
    #znamka2 = random.randint(1, 5)

    #student = input("jakýmu studentovi?")
    #if student not in seznam:
        #print("Chcete přidat studenta?")
    #elif student in seznam:
            #seznam[student] = znamka2
            #print (f"Studentovi {student} byla zapsána známka {znamka2}.")

    
    #with open("sample.json", "w", encoding="utf-8") as f:
        #json.dump(seznam, f, indent=4, ensure_ascii=False)

    #znamka2 = random.randint(1, 5)


    #import random

    #znamka = random.randint(1, 5)

    #seznam = {"Radek" : znamka, "Mohamed" : znamka, "Petr" : znamka, "Ayanokoji" : znamka}

    #student = input("jakýmu studentovi?")
    #if student not in seznam:
        #print("Chcete přidat studenta?")
    #elif student in seznam:
        #print(znamka)
        #average = sum(list)/len(list)