from typing import Dict, List
import pandas as pd

def convert_dict_to_df(import_dict: Dict) -> pd.DataFrame:

    # convert to DataFrame
    df = (pd.DataFrame.from_dict(import_dict, 
                                        orient='index', 
                                        columns=['temperature', 'feels_like',
                                                  'rain', 'description', 'city'])
                  .reset_index()
                  .rename(columns={"index": "date"})
                  .assign(date = lambda x: pd.to_datetime(x['date']))
                  )

    return df


def convert_list_to_df(import_list: List[Dict]) -> pd.DataFrame:
    '''
    Converst a list with dictionaries to a Pandas DatFrame

    Parameters:

    * import_list: List to be converted
    '''

    # define list to collect the DataFrames with predictions
    df_list = []

    # convert to a DataFrame
    for prediction in import_list:
        prediction_df = convert_dict_to_df(prediction)
        df_list.append(prediction_df)


    # combine list to a single DataFrame
    df_predictions = pd.concat(df_list)
    
    return df_predictions
