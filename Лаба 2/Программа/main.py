import pandas as pd
import os
import numpy as np
import argparse

def get_all_file_paths(directory):
    file_paths = []

    # Проход по всем папкам и файлам в заданной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Получаем полный путь к файлу
            full_path = os.path.join(root, file)
            file_paths.append(full_path)

    return file_paths

def main():
    parser = argparse.ArgumentParser(description='Программа для создания таблиц из файлов .res статистики')
    parser.add_argument('--bin', type=str, required=True, help='Укажите путь к папке откуда считываются файлы')
    parser.add_argument('--bout', type=str, required=False, default=".\Table", help="Укажите путь для вывода таблицы. По умолчанию выводится в эту же папку")
    
    args = parser.parse_args()

    if args.bin is None:
        raise ValueError("Use '--bin' <path> to specify the folder from which the files will be taken")

    directory = os.path.abspath(args.bin.replace('"', ""))
    path_out = os.path.join(os.path.abspath(args.bout.replace('"', "")), os.path.basename(directory) + "_result.xlsx")

    files_result = get_all_file_paths(directory)

    df = pd.DataFrame(columns=np.array(["a(1)","n","S", "P"])).astype(float)

    for file_path in files_result:
        #Получим имя файла
        ind = file_path.rfind("\\");
        file_name = file_path[ind+1:]
        ind = file_name.rfind(".")
        file_name = file_name[:ind]
        ind = file_name.split("_")
        form, n = ind[0], int(ind[1])
        form = 0.5 if form == "05" else float(form)
        with open(file_path) as file:
            text = file.read()
        ind_s = text.find("S=")
        ind_p = text.find("P=", ind_s)
        val_S = float(text[ind_s+2:ind_p-1])
        ind = text.find("\n", ind_p)
        val_P = float(text[ind_p+2:ind])
        df.loc[len(df)] = np.array([form, n, val_S, val_P])
    df = df.sort_values(["a(1)","n"])
    if not os.path.exists(os.path.dirname(path_out)):
        os.makedirs(os.path.dirname(path_out))
    with pd.ExcelWriter(path_out) as writter:
        df.to_excel(writter, float_format="%.4f", index=False)
if __name__ == "__main__":
    main()