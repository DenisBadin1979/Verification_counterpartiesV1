# https://github.com/hflabs/dadata-py
import pandas as pd
from dadata import Dadata

from kontragets import translation_conragents

"""Запрос на сервисе Дадата , возвращает данные по одному контрагенту"""
def zapros_min (pth_fl):
    token = "6524fe79cd1bc844f004d4076bbb5efb4f54355f"
    dadata = Dadata(token)
    lit_cont = translation_conragents(pth_fl)
    list_cont = []
    for i_cont in lit_cont:
        inn = i_cont['ИНН']
        result = dadata.find_by_id( "party",inn)
        cont_dict = {}
        if not result:
            cont_dict = {'Контрагент' : 'Данные не найдены'}
        else:
            c_inn = result[0]
            if c_inn['data']['type'] == 'LEGAL':
                print(c_inn)
                cont_dict = {'Контрагент': c_inn.get('value'),
                         'ИНН': c_inn['data']['inn'],
                         'ОГРН': c_inn['data']['ogrn'],
                         'Статус' : c_inn['data']['state']['status'],
                         'Дата регистрации': c_inn['data']['state']['registration_date'],
                         'Дата ликвидации': c_inn['data']['state']['liquidation_date'],
                         'Причина ликвидации': c_inn['data']['state']['code'],
                         'Должность руководителя' : c_inn['data']['management']['post'],
                         'ФИО руководителя' : c_inn['data']['management']['name'],
                         'Дата вступления в должность' : c_inn['data']['management']['start_date'],
                         'Основной Код ОКВЭД' : c_inn['data']['okved'],
                         'Адрес организации' : c_inn['data']['address']['value'],
                         'Дата последних изменений': c_inn['data']['state']['actuality_date'],}
            elif c_inn['data']['type'] == 'INDIVIDUAL':
                print(c_inn)
                cont_dict = {'Контрагент': c_inn.get('value'),
                         'ИНН': c_inn['data']['inn'],
                         'ОГРН': c_inn['data']['ogrn'],
                         'Статус': c_inn['data']['state']['status'],
                         'Дата регистрации': c_inn['data']['state']['registration_date'],
                         'Дата ликвидации': c_inn['data']['state']['liquidation_date'],
                         'Причина ликвидации': c_inn['data']['state']['code'],
                         'Основной Код ОКВЭД': c_inn['data']['okved'],
                         'Адрес организации': c_inn['data']['address']['value'],
                         'Дата последних изменений': c_inn['data']['state']['actuality_date'], }
        list_cont.append(cont_dict)
    df = pd.DataFrame(list_cont)
    df['Дата вступления в должность'] = pd.to_datetime(df['Дата вступления в должность'], unit='ms')
    df['Дата регистрации'] = pd.to_datetime(df['Дата регистрации'], unit='ms')
    df['Дата ликвидации'] = pd.to_datetime(df['Дата ликвидации'], unit='ms')
    df['Дата последних изменений'] = pd.to_datetime(df['Дата последних изменений'], unit='ms')



    return df

if __name__ == "__main__":
    ff = zapros_min('data/kont2.xlsx')

    ff.to_excel('data/gotov.xlsx', index=False)