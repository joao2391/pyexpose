import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1DGlAztQcah4N_1S1YgnfFxOsrMcG8ymbqrmtyJ1Z3yw"
SAMPLE_RANGE_NAME = "2024 AWS Tracker!L4:L"


def main():

  try:
    creds = service_account.Credentials.from_service_account_file("C:\\Users\\joaolima\\Downloads\\credentials.json", scopes=SCOPES)
    service = build("sheets", "v4", credentials=creds)
    # = open("C:\Users\joaolima\Downloads\testgs-413601-4507bd41709a.json", "r")   

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return
    
    range_body_values = {
            'value_input_option': 'USER_ENTERED',
            'data': []
           }
    smarts = ['30000',
            '30029',
            '30030',
            '30031',
            '30032',
            '30033',
            '30034',
            '30035',
            '30036',
            '30037',
            '30038',
            '30039',
            '30040',
            '30041',
            '30042',
            '30043',
            '30044',
            '30045',
            '30046',
            '30047',
            '30048',
            '30049',
            '30050',
            '30051',
            '30052',
            '30053',
            '30054',
            '30055',
            '30056',
            '30057',
            '30058',
            '30059',
            '30060',
            '30061',
            '30062',
            '30063',
            '30064',
            '30065',
            '30066',
            '30067',
            '30068',
            '30069',
            '30070',
            '30071',
            '30072',
            '30073',
            '30074',
            '30075',
            '30076',
            '30077',
            '30078',
            '30079',
            '30080',
            '30081',
            '30082',
            '30083',
            '30084',
            '30085',
            '30086',
            '30087',
            '30088',
            '30089',
            '30090',
            '30091',
            '30092',
            '30093',
            '30094',
            '30095',
            '30096',
            '30097',
            '30098',
            '30099',
            '30100',
            '30101',
            '30102',
            '30103',
            '30104',
            '30105',
            '30106',
            '30107',
            '30108',
            '30109',
            '30110',
            '30111',
            '30112',
            '30113',
            '30114',
            '30115',
            '30116',
            '30117',
            '30118',
            '30119',
            '30120',
            '30121',
            '30122',
            '30123',
            '30124',
            '30125',
            '30126']
    #print(values)
    values = [ele for ele in values if ele != []]    

    for row in values:
      for x in smarts:        
        if row[0] == x:
           range_body_values['data'].append(
                    [{
                        'majorDimension': 'ROWS',
                        'range': 'M4',
                        'values': [['TESTE'+x]]
                    },
                    {
                       'majorDimension': 'ROWS',
                        'range': 'P4',
                        'values': [['TESTE111'+x]]
                    }])
         
         
    request = service.spreadsheets().values().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=range_body_values)
    response = request.execute()
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()