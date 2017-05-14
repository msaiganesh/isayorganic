import pandas as pd

import datetime as dt

from pandas import ExcelWriter

#import data from the

datap = pd.read_csv("check.csv")

bigdata = datap

#applying lamda evaluation

bigdata['ORDER_DT'] = bigdata['ORDER_DT'].apply(lambda x:  dt.datetime.strptime(x,'%d-%b-%y'))

bigdata['DELIVERY_DATE'] = bigdata['DELIVERY_DATE'].apply(lambda x:  dt.datetime.strptime(x,'%d-%b-%y'))

bigdata1 = bigdata

#input date in format 2017-03-13

#input ending date in same form 2017-03-17

a = input("ENTER THE STARING DATE IN YEAR-MONTH-DATE FORMAT")

m = input("ENTER THE ENDING DATE IN YEAR-MONTH-DATE FORMAT")

#input the product items that users brought

no_of_input=int(input(' no of products that you want to filter  '))

#filtering users list

for i in range(0,no_of_input):

    data = datap

    l=input("enter the item keys to match the products ")

    if i == 0:

        bigdata = data[(data['ITEM_CODE']==l) & (data['ORDER_DT']>=a) &(data['DELIVERY_DATE']<=m) ]

    else:

        data= data[(data['ITEM_CODE'] == l) & (data['ORDER_DT']>=a) &(data['DELIVERY_DATE']<=m)]

        bigdata = bigdata.append(data, ignore_index=True)

#filtering user who has brough t products that is not needed

no_of_input_not = int(input('enter the products that are not brought'))

if no_of_input_not!=0:

    for i in range(0, no_of_input_not):

        data = datap

        l = (input('enter the product'))

        if i == 0:

            bigdata1 = data[data['ITEM_CODE'] == l]

        else:

            data = data[data['ITEM_CODE'] == l]

            bigdata1 = bigdata1.append(data, ignore_index=True)

    temp = set(bigdata1['CUSTOMER'])

    for i in temp:

        bigdata = bigdata[bigdata['CUSTOMER'] != i]

#pushing data into the excel sheet
bigdata=bigdata.drop_duplicates()

writer = ExcelWriter('PythonExport.xlsx')

bigdata.to_excel(writer,'Sheet1')

writer.save()

writer = ExcelWriter('PythonExportusers.xlsx')

bigdata['CUSTOMER'].drop_duplicates().to_excel(writer,'Sheet2')

writer.save()

bigdat =bigdata['CUSTOMER'].drop_duplicates()

print(bigdat.count())
