import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple


def excel_to_list(data_file, sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    rows = sh.nrows
    cols = sh.ncols
    header = sh.row_values(0)
    for i in range(1, rows):
        row_content = []
        for j in range(0, cols):
            c_type = sh.cell(i, j).ctype  # 表格的数据类型
            cell = sh.cell_value(i, j)
            if c_type == 2 and cell % 1 == 0:  # 如果是整形
                cell = int(cell)
            elif c_type == 3:
                # 转成datetime对象
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y/%d/%m %H:%M:%S')
            elif c_type == 4:
                cell = True if cell == 1 else False
            row_content.append(cell)
        d = dict(zip(header, row_content))
        data_list.append(d)
    return data_list


