'''
use this file to transfer csv to xlsx dataformat
'''
import pyexcel


def from_csv_to_xlsx(from_file,to_file):
    pyexcel.save_as(file_name=from_file,dest_file_name=to_file)
def getSheet(file_name):
    sheet = pyexcel.get_sheet(file_name=file_name)
    return sheet
def getDict(file_name):
    sheet = pyexcel.get_book_dict(file_name=file_name)
    return sheet
def getRecords(file_name):
    sheet = pyexcel.iget_records(file_name=file_name)
    return sheet




