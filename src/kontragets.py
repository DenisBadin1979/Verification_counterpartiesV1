import pandas as pd

def translation_conragents (file_pah):
    """Функция, которая формирует из готового excel файла данные в список словарей, возвращает список словарей"""
    df = pd.read_excel(file_pah)
    df_dict = df.to_dict(orient="records")
    for i_dict in df_dict:
        t = str(i_dict['ИНН'])
        if len(t) == 9 or len(t) == 11:
            inn_str = '0' + t
        else:
            inn_str =  t
        i_dict['ИНН'] = inn_str

    return df_dict

if __name__ == "__main__":
    ss = "data/kont.xlsx"
    sd = translation_conragents(ss)
    for i in sd:


        print(i)

