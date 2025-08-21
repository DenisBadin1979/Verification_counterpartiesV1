# https://github.com/hflabs/dadata-py

from dadata import Dadata
"""Запрос на сервисе Дадата , возвращает данные по одному контрагенту"""
def zapros_min (inn):
    token = "6524fe79cd1bc844f004d4076bbb5efb4f54355f"
    dadata = Dadata(token)
    result = dadata.find_by_id( "party",inn)
    cont_dict = {}
    if not result:
        cont_dict = {'Контрагент' : 'Данные не найдены'}
    else:
        c_inn = result[0]
        if c_inn['data']['type'] == 'LEGAL':

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
    return cont_dict

if __name__ == "__main__":
    cp_inn = zapros_min('027318179556')


    print (cp_inn)