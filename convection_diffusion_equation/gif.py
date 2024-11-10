import os

from PIL import Image


def clear_folder(image_folder):
    # очисить все в папке image_folder
    for filename in os.listdir(image_folder):
        if filename.endswith('.png'):
            file_path = os.path.join(image_folder, filename)
            os.remove(file_path)


def combine_images_to_gif(
        image_folder: str,
        gif_path: str,
        step: int = 1
):
    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith('.png'):
            file_path = os.path.join(image_folder, filename)
            images.append(Image.open(file_path))

    if images:
        images[0].save(
            gif_path,
            save_all=True,
            append_images=images[1::step],
            duration=1,
            loop=0
        )


def create_gif(
        image_folder: str,
        gif_path: str,
        create_images_for_gif,
        step: int = 1,
        skip_creating: bool = False,
):
    if not skip_creating:
        print('Очищаю папку...')
        clear_folder(image_folder)

        print('Создаю изображния...')
        create_images_for_gif(image_folder)

    print('Создаю gif...')
    combine_images_to_gif(image_folder, gif_path, step)

    print('Gif cоздано')
