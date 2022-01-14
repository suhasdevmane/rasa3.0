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

tempsensorid = '1rL3uVcxRHtqORqwpbXnWvAIE6Pad6376YFxx7LQ245U'
temphumiditysensorid = '1xBEGf2P7V2rAO4Q2WGkykHBdpD4x146ME6b8bRGoZcA'
threechanneltempsensorid = '1ZTgQDcPEStSoBhXzDxoEfS2Q3VdZvfzsPykaM3FeNhc'
doorandwindowsensorid = '1uzrdL3zkqvDranD2yVrSvDKq_PGR7c59Gj3N77m_i7o'
co2temphumiditysensorid = '1qpKWUY1QNfluLns_1pQOlm9xUWi93vmfvbuNQR08HYc'
ceilingmountpirsensorid = '1bshakS5QjmWE1FEQ3r1em2OxZ5Pvbv6BNTjv1aG-3vg'
occupancypirsensorid = '1ncnsGnaYR10hly_eqpaccdFK3NP-qvX-2oyRbPwIx2E'
underdesksensorid = '116ylJlx1fDiBT-JtkJi2IjTpk-zt4lhoDEGjBsx-YSc'
singledoorpeopleflowsensorid = '1x230Vvkv75oRlksu5-5X4QSdSyHMwyjfAxoJ6SCHysI'
drycontactsensorid = '1BK-SLLOwv2ewXZP2gaHad8MEPETgCERRTuosILls0Fc'


class action_give_temp(Action):
    def name(self) -> Text:
        return "action_asked_temperature"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = tempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Temperature-Sensor!a1:g40000").execute()
        df = pd.DataFrame.from_dict(result.get('values', []))
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df['temperature Value'] = df['temperature Value'].astype(float)
        temp = df.iloc[-1, 5]
        temp = round(temp,2)
        if not temp:
            dispatcher.utter_message(text= "could'nt get right temperature. please try again")
        else:
            dispatcher.utter_message(text= " temperature is {} degrees".format(temp))
        return []



class action_give_average_temp(Action):

    def name(self) -> Text:
        return "action_asked_average_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SERVICE_ACCOUNT_FILE = 'keys.json'        
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = tempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Temperature-Sensor!a1:g40000").execute()

        df = pd.DataFrame.from_dict(result.get('values', []))
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df['temperature Value'] = df['temperature Value'].astype(float)
        avgtemp = df['temperature Value'].mean()
        avgtemp = round(avgtemp,2)
 
        if not avgtemp:
            dispatcher.utter_message(text= "could'nt get right temperature. please try again")
        else:
            dispatcher.utter_message(text= " the mean temperature is about {} degrees".format(avgtemp))

        return []


class action_give_Min_temp(Action):

    def name(self) -> Text:
        return "action_asked_minimum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SERVICE_ACCOUNT_FILE = 'keys.json'        
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = tempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Temperature-Sensor!a1:g40000").execute()
        df = pd.DataFrame.from_dict(result.get('values', []))
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df['temperature Value'] = df['temperature Value'].astype(float)
        mintemp = df['temperature Value'].min()
        mintemp = round(avgtemp,2)
   
        if not mintemp:
            dispatcher.utter_message(text= "could'nt get right minimum temperature. please try again")
        else:
            dispatcher.utter_message(text= " the minimum temperature was about {} degrees".format(avgtemp))

        return []


class action_give_Max_temp(Action):

    def name(self) -> Text:
        return "action_asked_maximum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SERVICE_ACCOUNT_FILE = 'keys.json'        
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = tempsensorid
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
        maxtemp = df['temperature Value'].max()
        maxtemp = round(avgtemp,2)

        if not maxtemp:
            dispatcher.utter_message(text= "could'nt get right maximum temperature. please try again")
        else:
            dispatcher.utter_message(text= " the maximum temperature was about {} degrees".format(avgtemp))

        return []


        

class gives_dry_contact_status(Action):

    def name(self) -> Text:
        return "action_asked_dry_contact_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = drycontactsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Dry-Contact-Sensor!a1:f40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['contact Value'].map({'closed':False, 'open':True})
        contact = df.iloc[-1]
        
        if contact != True:
            dispatcher.utter_message(text= "Your dry contact is closed. Alarm action is taken and Machine is set to off. Please solve machine problem. ")
        else:
            dispatcher.utter_message(text= " Machine is working fine and dry contact is Open. Do not worry ")

        return []


    
class action_give_noOfVisitosVisited(Action):

    def name(self) -> Text:
        return "action_asked_number_of_visited"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = singledoorpeopleflowsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Single-Door-People-Flow!a1:f40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        i = df['flow Value'].value_counts(dropna=True)['in']

        if not i:
            dispatcher.utter_message(text= "Couldn't calculate number of visitors at the moment. Please try after some time. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= "Hey. There are {} people visited to the smartlab untill this moment.".format(i))

        return []




class action_give_noOfPeopleAvailable(Action):

    def name(self) -> Text:
        return "action_asked_number_of_people_present_in_smartlab"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = singledoorpeopleflowsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Single-Door-People-Flow!a1:f40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        i = df['flow Value'].value_counts(dropna=True)['in']
        j = df['flow Value'].value_counts(dropna=True)['out']

        k = int(i-j)

        if not k:
            dispatcher.utter_message(text= "Couldn't calculate number of people available in the smart lab. Please try after some time. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= "Hey. As per my math, there may be {} people present in the smartlab".format(k))

        return []


class action_gives_chair_status(Action):

    def name(self) -> Text:
        return "action_asked_chair_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID = underdesksensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Under-Desk-Sensor!a1:f40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['motionDetected Value']
        a = df.iloc[-1]
       
        if not a:
            dispatcher.utter_message(text= "Sorry, i am not sure about the chair availability. Please try again later. Thank you for using RaSa.")
        elif a == TRUE:
            dispatcher.utter_message(text= "Sorry. Chair is already taken. Please check for others desks.")
        else:
            dispatcher.utter_message(text= "Hey.It looks like no one is using the chair. You can use the place for your work. thank you.")

        return []
