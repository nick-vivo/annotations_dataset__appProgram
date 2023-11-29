import os
import pandas as pd

def annotation_dataset(source_dir: str, name_annotation: str) -> pd.DataFrame:
    """
    Функция принимает путь к датасету и будущее имя папки с аннотацией

    Создаст аннотацию на оригинальный датасет
    """

    for i in range(1, 6):
        
        if not os.path.exists( os.path.join(source_dir, str(i)) ):
            raise Exception("Is doesn't live")


    fieldnames = ['abs_path', 'rel_path', "class"]
    
    data = pd.DataFrame(columns=fieldnames)

    index = 0
    
    for i in range(1, 6):


        files = os.listdir( os.path.join(source_dir, str(i)) )

        files.sort()


        for file in files:
            

            new_row = { fieldnames[0]:os.path.join( os.getcwd(), source_dir, str(i), file), fieldnames[1]:os.path.join(source_dir, str(i), file), fieldnames[2]:str(i) }

            data.loc[index] = new_row

            index += 1

    data.to_csv(name_annotation, index=False)

    return data