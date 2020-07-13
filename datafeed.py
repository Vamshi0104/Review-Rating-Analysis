import openpyxl
from openpyxl.styles import Alignment
def appendexcel(name,rating,review,reviewrate):
    wb_obj = openpyxl.load_workbook(r'C:\Users\mvk\PycharmProjects\Review-Rating\Review.xlsx')
    sheet_obj = wb_obj.active
    crow=sheet_obj.max_row + 1
    col1 = "A" + str(crow)
    sheet_obj[col1]=crow-1
    sheet_obj[col1].alignment = Alignment(horizontal='center')
    col2="B" + str(crow)
    sheet_obj[col2]=name
    sheet_obj[col2].alignment = Alignment(horizontal='center')
    col3="C" + str(crow)
    sheet_obj[col3]=rating
    sheet_obj[col3].alignment = Alignment(horizontal='center')
    col4="D" + str(crow)
    sheet_obj[col4]=review
    sheet_obj[col4].alignment = Alignment(horizontal='center')
    col5="E" + str(crow)
    sheet_obj[col5]=reviewrate
    sheet_obj[col5].alignment = Alignment(horizontal='center')
    wb_obj.save(r'C:\Users\mvk\PycharmProjects\Review-Rating\Review.xlsx')