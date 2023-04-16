import numpy as np
import pandas as pd
from sqlalchemy import create_engine

from .models import GraphVisRefugeeData

'''
This file contains functions of that deal with data 
of Asylum-seeker data between 2015-2022 from UNHCR website 
'''


def convert_csv_to_df(file_path):
    '''
    Auxiliary function that converts csv file to pandas dataframe format,
    used in combination with the "add_data" command to for constructing the database,
    see "add_data.py" for more detail

    NOTE: this is a brute-force implementation which only works for this particular dataset
    '''

    with open(file_path) as fp:
        # Trim down the description text
        pop_df = pd.read_csv(fp, skip_blank_lines=True,
                             skiprows=range(14), on_bad_lines="error", sep=",")

    pop_df.head()

    # We ignore the IDPs in this scenarios, as this would complicate our graph visualisation

    pop_df = pop_df[pop_df["Country of origin (ISO)"]
                    != pop_df["Country of asylum (ISO)"]]

    pop_df.drop(columns=["IDPs of concern to UNHCR"], inplace=True)

    # key_feat_df = pop_df.filter(
    #     items=["Year", "Country of origin", "Country of asylum", "Asylum-seekers"])

    refugee_types = ["Country of asylum (ISO)", "Refugees under UNHCR's mandate", "Asylum-seekers",
                     "Other people in need of international protection", "Stateless persons", "Host Community", "Others of concern"]

    pop_df["total_refugees"] = pop_df[refugee_types].sum(axis=1)

    # Lastly, adding the indices for each record so they could be used as primary keys
    pop_df.insert(0, "id", range(1, len(pop_df) + 1))
    
    return pop_df
