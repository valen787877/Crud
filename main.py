my_pets = [
            {
                "id": 1,
                "name":"Mice",
                "species":"cat",
                "birth_year":2000,
            },
            {
                "id": 2,
                "name":"Sheba",
                "species":"cat",
                "birth_year":1990,
            },
            {
                "id": 3,
                "name":"Sandy",
                "species":"dog",
                "birth_year":1995,
            }
          ]

id_counter = 3
while True:
    print("--------------------------------------------------------------------------")
    print("1. Parodyk savo gyvunus")
    print("2. Įtraukti gyvuna")
    print("3. koreguoti irasa")
    print("4. trinti irasa")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirink:------------------------------------")
    ivestis = input()
    match ivestis:
        case "1":
            for pet in my_pets:
                print(f"{pet["id"]} vardas {pet["name"]} rusis {pet["species"]} gimimo metai {pet["birth_year"]}")
        case "2":
            print("ivesk varda")
            name = input()
            print("ivesk rusi")
            species = input()
            print("ivesk gimimo metus")
            birth_year = input()

            id_counter += 1
            pet = {
                "id":id_counter,
                "name": name,
                "species": species,
                "birth_year": birth_year,
            }
            my_pets.append(pet)
        case "3":
            print("Gyvuno koregavimas")
            print("ivesk id gyvuno kuri nori redaguoti")
            edit_id = input()
            for pet in my_pets:
                if edit_id == str(pet["id"]):
                    print(f"{pet["id"]} vardas {pet["name"]} rusis {pet["species"]} gimmo metai{pet["birth_year"]}")
                    print("ivesk varda")
                    pet["name"] = input()
                    print("ivesk rusi")
                    pet["species"] = input()
                    print("ivesk gymimo metus")
                    pet["birth_year"] = input()
        case "4":
            print("gyvuno iraso pasalinimas")
            print("ivesk id gyvuno kuri nori pasalinti")
            del_id = input()
            for pet in my_pets:
                if del_id == str(pet["id"]):
                    print(f"{pet["id"]}pasalinamas gyvunas {pet["name"]} rusis{pet["species"]}gymimo metai{pet["birth_year"]}" )
                    my_pets.remove(pet)
        case "5":
            print("iseiti is programos")
            break