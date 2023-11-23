from typing import Tuple
from PIL import Image
from math import exp, e
from random import randint
class Filter:
    def enhance(self, image, factor):
        return image

    def apply_to_pixel(self, r: int, g: int, b: int) -> Tuple[int, int, int]:
        return r, g, b

    def apply_to_image(self, path) -> Image.Image:
        img = Image.open(path).convert("RGB")

        for i in range(img.width):
            for j in range(img.height):
                r, g, b = img.getpixel((i, j))
                new_colors = self.apply_to_pixel((r, g, b))
                img.putpixel((i, j), new_colors)
        return img

class Exit(Filter):
    def apply_to_image(self, path) -> Image.Image:
        exit()

# Блюр фильтр, играем с методом resize
class BlurFilter(Filter):
    def apply_to_image(self, path) -> Image.Image:
        img = Image.open(path).convert("RGB")
        width, height = img.size
        factor = 4
        small_image = img.resize((int(width / factor), int(height / factor)), Image.BILINEAR)
        blurred_image = small_image.resize(img.size, Image.NEAREST)
        return blurred_image

# Перевод RGB картинки в чёрно-белую, через метод convert('L')
class BlackWhite(Filter):
    def apply_to_image(self, path) -> Image.Image:
        image_file = Image.open(path).convert('L')
        return image_file

class Enhance(Filter):
    def apply_to_image(self, path) -> Image.Image:
        img = Image.open(path).convert("RGB")

        # Применение затемнения к каждому пикселю
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = img.getpixel((i, j))

                # Вычисление новых значений каждого канала RGB
                new_r = int(r * 0.5)
                new_g = int(g * 0.5)
                new_b = int(b * 0.5)

                # Применение новых значений к пикселю
                img.putpixel((i, j), (new_r, new_g, new_b))

        return img
class RandomFilter(Filter):
    def apply_to_pixel(self, pixel) -> tuple:
        r, g, b = pixel[0], pixel[1], pixel[2]
        r, g, b = randint(max(r-50, 0), min(r+50, 255)), randint(max(g-50, 0), min(g+50, 255)), randint(max(b-50, 0), min(b+50, 255))
        new_pixel = (r, g, b)
        return new_pixel

class KakoytoFilter(Filter):
        def apply_to_pixel(self, pixel) -> tuple:
            r, g, b = pixel[0], pixel[1], pixel[2]
            r = min((r-50), 0)
            new_pixel = (r, g, b)
            return new_pixel


class WhataHeeellFilter(Filter):
    def apply_to_pixel(self, pixel) -> tuple:
        r, g, b = pixel[0], pixel[1], pixel[2]
        r = max((b - 70), 90)
        new_pixel = (r, g, b)
        return new_pixel













