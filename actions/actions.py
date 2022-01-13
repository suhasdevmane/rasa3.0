#pip install gspread oauth2client
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



#!pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import numpy as np
from googleapiclient.discovery import build
from google.oauth2 import service_account


class action_give_temp(Action):
    def name(self) -> Text:
        return "action_give_temperature"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = '1rL3uVcxRHtqORqwpbXnWvAIE6Pad6376YFxx7LQ245U'
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Temperature-Sensor!a1:g40000").execute()
        #rows = result.get('values', [])
        #print('{0} rows retrieved.'.format(len(rows)))
        df = pd.DataFrame.from_dict(result.get('values', []))
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df['temperature Value'] = df['temperature Value'].astype(float)
        #meantemp = df['temperature Value'].mean()
        temp = df.iloc[-1, 5]
        temp = round(temp,2)
        #temp = tracker.get_slot("temp")
        if not temp:
            dispatcher.utter_message(text= "could'nt get right temperature. please try again")
        else:
            dispatcher.utter_message(text= " temperature is {} degrees".format(temp))
        return []



class action_give_average_temp(Action):

    def name(self) -> Text:
        return "action_give_average_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SERVICE_ACCOUNT_FILE = 'keys.json'        
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = '1rL3uVcxRHtqORqwpbXnWvAIE6Pad6376YFxx7LQ245U'
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Temperature-Sensor!a1:g40000").execute()
        #rows = result.get('values', [])
        #print('{0} rows retrieved.'.format(len(rows)))
        df = pd.DataFrame.from_dict(result.get('values', []))
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df['temperature Value'] = df['temperature Value'].astype(float)
        avgtemp = df['temperature Value'].mean()
        avgtemp = round(avgtemp,2)
        #temp = df.iloc[-1, 5]
        #temp = tracker.get_slot("temp")
        if not avgtemp:
            dispatcher.utter_message(text= "could'nt get right temperature. please try again")
        else:
            dispatcher.utter_message(text= " the mean temperature is about {} degrees".format(avgtemp))

        return []