from functools import lru_cache
import csv


@lru_cache
def read(path):
    # """Reads a file from a given path and returns its contents

    # Parameters
    # ----------
    # path : str
    #     Full path to file

    # Returns
    # -------
    # list
    #     List of rows as dicts
    # """
    # return []
    data_list = []
    with open(path, mode="r") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for row in reader:
            data_list.append(row)
    return data_list
