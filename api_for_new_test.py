import requests


class ApiPets:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_key(self, password, email):
        response = requests.get(f"{self.base_url}/api/key", params={'status': 'available'},
                                headers={'accept': 'application/json',
                                         "password": password,
                                         "email": email})
        status = response.status_code
        try:
            res_key = response.json()
        except:
            res_key = response.text
        return status, res_key

    def get_pets(self, key):
        response = requests.get(f"{self.base_url}/api/pets",
                                params={'filter': "my_pets"},
                                headers={'auth_key': key})
        status = response.status_code
        try:
            info_pets = response.json()
        except:
            info_pets = response.text
        return status, info_pets

    def create_pet(self, name, type_pet, age, photo):
        file = {'pet_photo': (photo, open(photo, 'rb'), 'image/jpg')}
        response = requests.post(f"{self.base_url}/api/pets",
                                 headers={'auth_key': '47c19fcdb9a680fc597ef5bb10346fc6a3e3e6404cd14d28470a5307'},
                                 data={"name": name,
                                       "animal_type": type_pet,
                                       "age": age},
                                 files=file)
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def update_pet(self, pet_id, name, type_pet, age):
        response = requests.put(f"{self.base_url}/api/pets/{pet_id}",
                                headers={'auth_key': '47c19fcdb9a680fc597ef5bb10346fc6a3e3e6404cd14d28470a5307'},
                                data={"name": name,
                                      "animal_type": type_pet,
                                      "age": age})
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def delete_pet(self, pet_id):
        response = requests.delete(f"{self.base_url}/api/pets/{pet_id}",
                                   headers={'auth_key': '47c19fcdb9a680fc597ef5bb10346fc6a3e3e6404cd14d28470a5307'})
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def create_pet_simple(self, name, type_pet, age):
        response = requests.post(f"{self.base_url}/api/create_pet_simple",
                                 headers={'auth_key': '47c19fcdb9a680fc597ef5bb10346fc6a3e3e6404cd14d28470a5307'},
                                 data={"name": name,
                                       "animal_type": type_pet,
                                       "age": age})
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response

    def set_photo_for_pet(self, photo, pet_id):
        """Функция добавления фота"""
        file = {'pet_photo': (photo, open(photo, 'rb'))}
        response = requests.post(f"{self.base_url}/api/pets/set_photo/{pet_id}",
                                 headers={'auth_key': '47c19fcdb9a680fc597ef5bb10346fc6a3e3e6404cd14d28470a5307'},
                                 files=file)
        status = response.status_code
        try:
            response = response.json()
        except:
            response = response.text
        return status, response


a = ApiPets()
# (a.get_key("Lion163163", "dqwdqw2d@dwdwd.tr"))
print(a.get_pets("47c19fcdb9a680fc597ef5bb10346fc6a3e3e6404cd14d28470a5307"))
# print(a.create_pet())
# print(a.update_pet())
# print(a.delete_pet())
# print(a.create_pet_simple())
# print(a.set_photo_for_pet())
