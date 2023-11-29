import os
import shutil
import random
import pandas as pd

from .annotation_dataset import annotation_dataset


def dataset_random_annotation(source_dir: str, name_annotation: str) -> pd.DataFrame:
    """
        Создаст аннотацию и датасет со случайными штучками
    """

    for i in range(1, 6):
        
        if not os.path.exists( os.path.join(source_dir, str(i)) ):
            raise Exception("Is doesn't live")
    
    cataloge = source_dir + ".random"
    os.mkdir(cataloge)


    data = annotation_dataset(source_dir, "ARBITRASHIK.csv")
    os.remove("ARBITRASHIK.csv")


    fieldnames = ['abs_path', 'rel_path', "class"]    

    data_2 = pd.DataFrame(columns=fieldnames)


    random_ls = data[['rel_path', 'class']].values
    
    indexes = list(range(len(random_ls)))

    random.shuffle(indexes)

    randomized_data = [random_ls[i] for i in indexes]

    index = 0

    for file in randomized_data:

    
        source = os.path.join( file[0] )

        destination = os.path.join( cataloge, str(index).rjust(5, "0") )

        new_row = [ os.path.join( os.getcwd(), destination), os.path.join(destination),  file[1]]

        data_2.loc[index] = new_row

        index += 1

        shutil.copyfile(source, destination)
    
    data_2.to_csv(name_annotation, index=False)

    return data_2
