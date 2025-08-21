# https://github.com/hflabs/dadata-py

from dadata import Dadata
"""Запрос на сервисе Дадата , возвращает данные по одному контрагенту"""
def zapros_min (inn):
    token = "6524fe79cd1bc844f004d4076bbb5efb4f54355f"
    dadata = Dadata(token)
    result = dadata.find_by_id( "party",inn)
    c_inn = result[0]
    print (c_inn)
    cont_dict = {'Контрагент': c_inn.get('value'),
                 'ИНН': c_inn['data']['inn'],
                 'ОГРН': c_inn['data']['ogrn'],
                 'Дата выдачи ОГРН': c_inn['data']['ogrn_date'],
                 'Должность руководителя' : c_inn['data']['management']['post'],
                 'ФИО руководителя' : c_inn['data']['management']['name'],
                 'Дата вступления в должность' : c_inn['data']['management']['start_date'],}
    return cont_dict

if __name__ == "__main__":
    cp_inn = zapros_min('025002442172')


    print (cp_inn)
