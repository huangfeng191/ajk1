# -*- coding: utf-8 -*-
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import time
from mongo.utils import *
def doExcel(data,name="empty_book"):
    wb = Workbook()
    dest_filename = './excel/%s_%s.xlsx'%(name,YMDHMS(int(time.time()),"%Y-%m-%d%H%M%S"))
    ws1 = wb.active
    ws1.title = "range names"
    fields=["avg_price_unit", "building_area", "building_area_unit", "community", "area", "salesman",  "city", "title",   "floor", "advantage", "total_price_unit", "marked", "avg_price", "house_type", "total_price", "building_time", "url", "changed","_id","id","created", "create_time","url_md5"]
    for i in range(0, len(data)):
        if i==0:
            ws1.append(fields)
        else:
            d=  data[i]
            dt=[]
            for field in  fields:
                dt.append(d[field])
            ws1.append(dt)

    wb.save(filename = dest_filename)