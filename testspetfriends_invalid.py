from api_for_new_test import *
import pytest

a = ApiPets()


class TestPets:
    def test_getkey_invalid_password(self):
        """Невалидный пароль"""
        status, res_key = a.get_key("Lion163", "dqwdqw2d@dwdwd.tr")
        assert status == 403
        with pytest.raises(AssertionError):
            assert "key" in res_key

    def test_getkey_invalid_email(self):
        """Невалидынй емаил"""
        status, res_key = a.get_key("Lion163163", "dqwdqw2d")
        assert status == 403
        with pytest.raises(AssertionError):
            assert "key" in res_key

    def test_get_pets_invalid_key(self):
        """Невалидынй ключ доступа"""
        status, info_pets = a.get_pets("qwe123")
        assert status == 403
        with pytest.raises(AssertionError):
            assert "pets" in info_pets
        with pytest.raises(TypeError):
            assert len(info_pets["pets"]) > 0

    def test_create_pet_not_value(self):
        """Создание питомца с пустыми полями"""
        status, info = a.create_pet("", "", "", "cezar.jpg")
        assert status == 200

    def test_create_pet_not_photo(self):
        """Создание питомца без указания фото"""
        with pytest.raises(FileNotFoundError):
            a.create_pet("Chips", "Dog", "3", "")

    def test_update_pet(self):
        """Изменение данных на пустые поля"""
        status, info = a.update_pet("fbbda9da-0c6e-42cb-98a6-2abd8f14fb6f", "", "", "")  # указать свой pet_id
        assert status == 200

    def test_delete_pet(self):
        """Удаление питомца с несуществующим pet_id"""
        status, info = a.delete_pet("123123")
        assert status == 200

    @pytest.mark.parametrize("value_age", [-1, 0, 1, "qwe", "q1w2e3"])
    def test_create_pet_simple(self, value_age):
        """Создание питомца с невалидными данными поля age"""
        status, info = a.create_pet_simple("Сима", "Корги", value_age)
        assert status == 200
        assert info["pet_photo"] == ''

    @pytest.mark.parametrize("formfile", ["text.txt", "viki.PDF", "corg.doc", "run_file.exe"])
    def test_set_photo_for_pet(self, formfile):
        """Отправка файла другого формата"""
        status, info = a.set_photo_for_pet(formfile, "fbbda9da-0c6e-42cb-98a6-2abd8f14fb6f")  # указать свой pet_id
        assert status == 500 or 200

    def test_set_photo_for_pet_large(self):
        """Отправка файла большого размера"""
        status, info = a.set_photo_for_pet("video.jpg", "9fccfd15-cdef-4d65-8571-831365e2cd56")  # размер файла ~300mb
        assert status == 502
