def load_default_data():
    return [
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

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Parodyk savo gyvunus")
    print("2. Įtraukti gyvuna")
    print("3. koreguoti irasa")
    print("4. trinti irasa")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirink:------------------------------------")

def print_my_pets(my_pets):
    for pet in my_pets:
        print(f"{pet["id"]} vardas {pet["name"]} rusis {pet["species"]} gimimo metai {pet["birth_year"]}")

def create_pet(my_pets, id_counter):
    print("ivesk varda")
    name = input()
    print("ivesk rusi")
    species = input()
    print("ivesk gimimo metus")
    birth_year = int(input())

    id_counter += 1
    pet = {
        "id": id_counter,
        "name": name,
        "species": species,
        "birth_year": birth_year,
    }
    my_pets.append(pet)
    return id_counter

def edit_pet(my_pets):
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
            pet["birth_year"] = int(input())

def remove_pet(my_pets):
    print("gyvuno iraso pasalinimas")
    print("ivesk id gyvuno kuri nori pasalinti")
    del_id = input()
    for pet in my_pets:
        if del_id == str(pet["id"]):
            print(f"{pet["id"]}pasalinamas gyvunas {pet["name"]} rusis{pet["species"]}gymimo metai{pet["birth_year"]}")
            my_pets.remove(pet)