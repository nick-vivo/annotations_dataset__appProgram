import os
import shutil
import pandas as pd


def dataset_aloin(source_dir: str) -> str:
    """
    Функция принимает путь к датасету и создаст в этой папке папке по соседству папочку source_dir + ".aloin"

    Заполнит папку всеми файлами вида source_dir + ".aloin"/class_0000

    :return: Название папки новой
    """

    for i in range(1, 6):
        if not os.path.exists(os.path.join(source_dir, str(i))):
            raise Exception("Is doesn't live")

    cataloge = source_dir + ".aloin"

    os.mkdir(cataloge)

    for i in range(1, 6):
        files = os.listdir(os.path.join(source_dir, str(i)))
        files.sort()

        for file in files:
            source = os.path.join(source_dir, str(i), file)

            destination = os.path.join(cataloge, str(i) + "_" + file)

            shutil.copyfile(source, destination)

    return cataloge


def annotation_aloin(source_dir: str, name_annotation: str) -> pd.DataFrame:
    """
    Функция принимает путь к датасету aloin и будущее имя папки с аннотацией"

    Создаст аннотацию
    """

    if not os.path.exists(os.path.join(source_dir)):
        raise Exception("Is doesn't live")

    fieldnames = ["abs_path", "rel_path", "class"]

    data = pd.DataFrame(columns=fieldnames)

    files = os.listdir(os.path.join(source_dir))

    files.sort()

    index = 0

    for file in files:
        new_row = {
            fieldnames[0]: os.path.join(os.getcwd(), source_dir, file),
            fieldnames[1]: os.path.join(source_dir, file),
            fieldnames[2]: file[0],
        }

        data.loc[index] = new_row

        index += 1

    data.to_csv(name_annotation, index=False)

    return data
