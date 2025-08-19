# https://github.com/hflabs/dadata-py

from dadata import Dadata
token = "6524fe79cd1bc844f004d4076bbb5efb4f54355f"
dadata = Dadata(token)
result = dadata.find_by_id( "party","7726454328")

print (result)