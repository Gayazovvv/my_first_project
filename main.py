from PIL import Image
from Class import Exit, BlurFilter, BlackWhite, Enhance, RandomFilter
import os


def main():
    filter_names = [
        "Выход из приложения",
        "Блюр",
        "Конвертация изображения в чёрно-белый",
        "Затемнение",
        "Рандом"

    ]
    filters = [
        Exit(),
        BlurFilter(),
        BlackWhite(),
        Enhance(),
        RandomFilter()
    ]

    print("Добро пожаловать в консольный фоторедактор.")


    is_finished = False
    while not is_finished:
        path = input("Введите путь к файлу: ")

        while not os.path.exists(path):
            path = input("Файл не найден. Попробуй еще раз: ")


        print("Какой фильтр вы хотите применить?")

        for i in range(len(filter_names)):
            print(f"{i} - {filter_names[i]}")

        choice = input("Выберите фильтр (введите номер): ")

        while not choice.isdigit() or int(choice) >= len(filters) or int(choice) < 0:
            choice = input("Некорректный ввод. Попробуй еще раз: ")

        filt = filters[int(choice)]
        img = filt.apply_to_image(path)

        save_path = input("Введите путь, куда сохранить файл: ")

        img.save(save_path)
        answer = input("Еще раз? (да/нет): ").lower()

        while answer != "да" and answer != "нет":
            answer = input("Некорректный ввод. Попробуй еще раз: ")
        is_finished = answer == "нет"


if __name__ == "__main__":
    main()



