from django.shortcuts import render

import datetime

Time = datetime.datetime.now()


import pandas as pd
data = pd.ExcelFile('excel.xls')

print(data.sheet_names)


TotalOrdersPandas=data.parse(data.sheet_names[-1])

TotalOrders=[]
for i in range(1,len(TotalOrdersPandas)):
    TotalOrders.append([TotalOrdersPandas['Total Orders:'][i],TotalOrdersPandas['Count'][i]])
print(TotalOrders)    

def index(request):
    global Time
    Time = str(datetime.datetime.now()) + datetime.datetime.now().strftime("%S") 
    print(Time)
    return render(request,'webpages/index.html', {"Total":TotalOrders})

 