# https://github.com/hflabs/dadata-py

from dadata import Dadata
def zapros_min (inn):
    token = "6524fe79cd1bc844f004d4076bbb5efb4f54355f"
    dadata = Dadata(token)
    result = dadata.find_by_id( "party",inn)
    return result



print (i_inn)