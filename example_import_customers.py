import pandas as pd
from typing import Dict


def create_contact(row: pd.Series) -> Dict:

    # convert row to dictionary
    contact_dict = row.to_dict()
    
    return contact_dict


if __name__ == "__main__":
    # import dataframe
    df_customer = pd.read_csv("data/customer.csv")

    # list to collect dictionaries
    contacts_list = []

    #  iterate over the rows
    for index, row in df_customer.iterrows():
        # remove columns with NaN's
        row.dropna(inplace=True) 

        # add contact
        contact_1 = create_contact(row)
        
        # add contact to the list
        contacts_list.append(contact_1)

    
    pass

