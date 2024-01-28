# 给定一个 URL, 形成 recycle,
# from 1970 to 2021, 10年一个周期
#
import time

import requests

method = 'listResults'
dataType = 'Production'
dateFrom = '1970'
dateTo = '1979'
commodity = '2'
agreeToTsAndCs = 'Yes'
exportToSpreadsheet = 'Yes'

url = 'https://www2.bgs.ac.uk/mineralsuk/statistics/wms.cfc?method={method}&dataType={dataType}&dateFrom={dateFrom}&dateTo={dateTo}&commodity={commodity}&country=&agreeToTsAndCs=agreed&exportToSpreadsheet=Yes'
commodity_list = [2, 4, 5, 6, 199]

for comm in commodity_list:
    for year in range(1970, 2024, 10):
        dateFrom, dateTo = year, year + 9
        dateTo = 2021 if dateTo >= 2021 else dateTo
        # print(dateFrom,dateTo)
        print(url.format(method=method, dateFrom=dateFrom, dateTo=dateTo, commodity=comm, dataType=dataType))
        down_res = requests.get(
            url.format(method=method, dateFrom=dateFrom, dateTo=dateTo, commodity=comm, dataType=dataType))
        if 'No results' not in str(down_res.content):
            with open(f'{comm}_{dateFrom}.xlsx', 'wb') as f:
                f.write(down_res.content)
            time.sleep(10)
        else:
            print('No results,so can\'t create the filesymotion-lineforward!')
