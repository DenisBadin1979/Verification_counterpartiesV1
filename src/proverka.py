import pandas as pd

from kontragets import translation_conragents
from zapros_api import zapros_min


def proverka_cont (pth_fl):
    lit_cont = translation_conragents(pth_fl)
    list_cont = []
    for i_cont in lit_cont:
        inn_cont = i_cont['ИНН']
        dict_prov = zapros_min(inn_cont)
        list_cont.append(dict_prov)
        df = pd.DataFrame(list_cont)
        df['Дата вступления в должность'] = pd.to_datetime(df['Дата вступления в должность'], unit='ms')
        df['Дата регистрации'] = pd.to_datetime(df['Дата регистрации'], unit='ms')
        df['Дата ликвидации'] = pd.to_datetime(df['Дата ликвидации'], unit='ms')
        df['Дата последних изменений'] = pd.to_datetime(df['Дата последних изменений'], unit='ms')


    return df


if __name__ == '__main__':
    ff = proverka_cont('data/kont.xlsx')

    ff.to_excel('data/gotov.xlsx', index=False)


