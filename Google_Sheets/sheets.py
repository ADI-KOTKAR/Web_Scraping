import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file',"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('Edisha-9fa188955318.json', scope)

client = gspread.authorize(creds)

''' Spreadsheet '''
sheet = client.open("Dataset")

''' Calculate sheets of Spreadsheet '''
worksheet = sheet.worksheets()
# print(worksheet)

''' Sheets of Spreadsheet '''
harvard = sheet.worksheet("Harvard")

''' Functions '''
def insertRow(rowArrray, sheetName):
    sheetName.insert_row(rowArrray)

def displayRows(sheetName):
    print(sheetName.get_all_values)

