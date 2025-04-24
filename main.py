import csv

# Inicializē tukšu sarakstu, lai saglabātu produktu datus
grozs = []

# Atver CSV failu, kurā ir produktu dati
with open('barbora.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

    # Nolasīt katru rindu no CSV faila un pievienot to sarakstam
    for row in file_reader:
        grozs.append(row)

grozs.pop(0)

while True:
    # Parādīt izvēlnes opcijas
    print("1. Visi produkti")
    print("2. Produkts pēc indeksa")
    print("3. Meklēt pēc zīmola")
    print("4. Top 3 dargākie produkti")
    print("5. Top 3 produkti ar mazāku atlaidi")
    print("6. Pievienot jaunu produktu")
    print("7. Gala summa ar atlaidi")
    
    # Aicināt lietotāju ievadīt komandu
    choice = input("Ievadi komandu: ")

    # Opcija 1: Parādīt visus produktus
    if choice == "1":
        # ar ciklu iziet cauri produktiem un izdrukā katru no tiem
        # katram produktam izdrukā nosaukumu, atlaidi un cenu ar atlaidi
        pass

    # Opcija 2: Parādīt produktu pēc kārtas numura
    elif choice == "2":
        # pajautā lietotājam ievadīt kārtas numuru
        # paņem produktu no saraksta ar norādīto kārtas numuru izmantot saraksta indeksu
        pass

    # Opcija 3: Meklēt produktus pēc zīmola
    elif choice == "3":
        # pajautā lietotājam ievadīt zīmolu
        # ar ciklu iziet cauri produktiem un pārbauda, vai zīmols atbilst meklējamajam izmantojot "in" operatoru
        pass
    
    # Opcija 4: Parādīt top 3 dargākus produktus
    elif choice == "4":
        # izmanto kārtošanu un sarakta griešanu, lai iegūtu 3 dargākus produktus
        pass
    
    # Opcija 5: Parādīt top 3 produktus ar mazāku atlaidi
    elif choice == "5":
        # izmanto kārtošanu un sarakta griešanu, lai produktus ar mazāku atlaidi
        pass

    # Opcija 6: Pievienot jaunu produktu sarakstam
    elif choice == "6":
        # pajauta lietotājam ievadīt produkta datus
        # izveido jaunu produktu - sarakstu ar ievadītajiem datiem
        # pievieno to grozam
        pass
    
    # Opcija 7: Aprēķināt un parādīt katram produktam gala summu ar atlaidēm un kopējo atlaižu summu izmantojot cenu, cenu ar atlaidi un atlaidi procentos
    elif choice == "7":
        # ar ciklu un summēšanu aprēķina katram produktam noradītas summas
        pass

    # Apstrādāt nederīgas komandas
    else:
        break
    
    # Izdrukāt atdalītāju labākai lasāmībai
    print("==========================")
