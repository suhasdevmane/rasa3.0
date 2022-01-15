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
roomoccupancypirsensorid = '1bshakS5QjmWE1FEQ3r1em2OxZ5Pvbv6BNTjv1aG-3vg'
tableoccupancypirsensorid = '1ncnsGnaYR10hly_eqpaccdFK3NP-qvX-2oyRbPwIx2E'
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
        mintemp = round(mintemp,2)
        if not mintemp:
            dispatcher.utter_message(text= "could'nt get right minimum temperature. please try again")
        else:
            dispatcher.utter_message(text= " the minimum temperature was about {} degrees".format(mintemp))

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
        maxtemp = round(maxtemp,2)

        if not maxtemp:
            dispatcher.utter_message(text= "could'nt get right maximum temperature. please try again")
        else:
            dispatcher.utter_message(text= " the maximum temperature was about {} degrees".format(maxtemp))

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
                                            range="Under-Desk-Sensor!a1:h40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['motionDetected Value']
        a = df.iloc[-1]
       
        if not a:
            dispatcher.utter_message(text= "Sorry, i am not sure about the chair availability. Please try again later. Thank you for using RaSa.")
        elif a == 'TRUE':
            dispatcher.utter_message(text= "Sorry. Chair is already taken. Please check for other chairs.")
        else:
            dispatcher.utter_message(text= "Hey.It looks like no one is using the chair. You can use the place for your work. thank you.")

        return []


class action_gives_table_status(Action):

    def name(self) -> Text:
        return "action_asked_table_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  tableoccupancypirsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Occupancy-PIR!a1:h40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['motionDetected Value']
        a = df.iloc[-1]
       
        if not a:
            dispatcher.utter_message(text= "Sorry, i am not sure about the desk availability. Please try again later. Thank you for using RaSa.")
        elif a == 'TRUE':
            dispatcher.utter_message(text= "Sorry. This Desk is already taken. Please check for other desks.")
        else:
            dispatcher.utter_message(text= "Hey.It looks like no one is using the Desk. You can use the place for your work. thank you.")

        return []


class action_gives_room_status(Action):

    def name(self) -> Text:
        return "action_asked_occupancy_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  roomoccupancypirsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Ceiling-Mount-PIR!a1:h40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['motionDetected Value']
        a = df.iloc[-1]
       
        if not a:
            dispatcher.utter_message(text= "Sorry, could'nt load the data at the moment. Please try again later. Thank you for using RaSa.")
        elif a == 'TRUE':
            dispatcher.utter_message(text= "It looks like motion is detected in the room. The room is occupied.")
        else:
            dispatcher.utter_message(text= "Hey. No motion detected in the room. the room is vacant. thank you.")

        return []



class action_gives_co2_lavel(Action):

    def name(self) -> Text:
        return "action_asked_co2_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        co2 = df['concentration Value'].iloc[-1]
        #temp = df['temperature Value'].iloc[-1]
        #hum = df['humidity Value'].iloc[-1]
       
        if not co2:
            dispatcher.utter_message(text= "Sorry, could'nt load the data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The CO2 level in the smartlab is {} PPM now.".format(co2))

        return []




class action_gives_average_co2(Action):

    def name(self) -> Text:
        return "action_asked_average_co2_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        avgco2 = df['concentration Value'].astype('int').mean()
        avgco2 = int(avgco2)
        if not avgco2:
            dispatcher.utter_message(text= "Sorry, could'nt load the data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The average CO2 level in the smartlab is {} PPM now.".format(avgco2))

        return []


class action_gives_minimum_co2(Action):

    def name(self) -> Text:
        return "action_asked_minimum_co2_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        minco2 = df['concentration Value'].min()
       
        if not minco2:
            dispatcher.utter_message(text= "Sorry, could'nt load the data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The minimum CO2 level was {} PPM in the smartlab.".format(minco2))

        return []


class action_gives_maximum_co2(Action):

    def name(self) -> Text:
        return "action_asked_maximum_co2_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        maxco2 = df['concentration Value'].max()
       
        if not maxco2:
            dispatcher.utter_message(text= "Sorry, could'nt load the data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The maximum CO2 level was {} PPM in the smartlab.".format(maxco2))

        return []


class action_gives_humidity(Action):

    def name(self) -> Text:
        return "action_asked_humidity_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        hum = df['humidity Value'].iloc[-1]
       
        if not hum:
            dispatcher.utter_message(text= "Sorry, could'nt load the humidity data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The humidity level is {} percent in the smartlab.".format(hum))

        return []

    
class action_gives_average_humidity(Action):

    def name(self) -> Text:
        return "action_asked_average_humidity_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df["humidity Value"] = df["humidity Value"].astype('str').astype('float').astype('int')
        avghum = round(df["humidity Value"].mean(),2)
        if not avghum:
            dispatcher.utter_message(text= "Sorry, could'nt load the humidity data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The average humidity level is {} percent in the smartlab.".format(avghum))

        return []


    
class action_gives_minimum_humidity(Action):

    def name(self) -> Text:
        return "action_asked_minimum_humidity_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df["humidity Value"] = df["humidity Value"].astype('str').astype('float').astype('int')
        minhum = round(df["humidity Value"].min(),2)
       
        if not minhum:
            dispatcher.utter_message(text= "Sorry, could'nt load the data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The minimum humidity level was found {} percent in the smartlab.".format(minhum))

        return []



class action_gives_maximum_humidity(Action):

    def name(self) -> Text:
        return "action_asked_maximum_humidity_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  co2temphumiditysensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="CO2-Temperature-And-Humidity!a1:k40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df["humidity Value"] = df["humidity Value"].astype('str').astype('float').astype('int')
        maxhum = round(df["humidity Value"].max(),2)
       
        if not maxhum:
            dispatcher.utter_message(text= "Sorry, could'nt load the data at the moment. Please try again later. Thank you for using RaSa.")
        else:
            dispatcher.utter_message(text= " The maximum humidity level found is {} percent in the smartlab.".format(maxhum))

        return []



class action_gives_window_status(Action):

    def name(self) -> Text:
        return "action_asked_window_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  doorandwindowsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Door-and-Window!a1:f40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        status = df['contact Value'].iloc[-1]
       
        if status == 'open':
            dispatcher.utter_message(text= "I have confirmed that, the window is open. you are getting fresh air.Thank you.")
        else:
            dispatcher.utter_message(text= " I have confirmed that, the window is closed. stay warm.")
        return []





class action_gives_all_channel_temp(Action):

    def name(self) -> Text:
        return "action_asked_multi_channel_temperatures"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        ch1 = df['channel1 Value'].iloc[-1]
        ch2 = df['channel2 Value'].iloc[-1]
        ch3 = df['channel3 Value'].iloc[-1]
        
        if ch1 == 'fault':
            dispatcher.utter_message(text= "there is some fault in accessing channel 1 temperature")
        else:
            dispatcher.utter_message(text= "the channel 1 is temperature is {} degrees".format(ch1))

        if ch2 == 'fault':
            dispatcher.utter_message(text= "there is some fault in accessing channel 2 temperature")
        else:
            dispatcher.utter_message(text= "the channel 2 is temperature is {} degrees".format(ch2))

        if ch3 == 'fault':
            dispatcher.utter_message(text= "there is some fault in accessing channel 3 temperature")
        else:
            dispatcher.utter_message(text= "the channel 3 is temperature is {} degrees".format(ch3))
        return []








#==================================================================================================






class action_gives_channel_1_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_one_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        ch1 = df['channel1 Value'].iloc[-1]
        
        if ch1 == 'fault':
            dispatcher.utter_message(text= "there is some fault in accessing channel 1 temperature")
        else:
            dispatcher.utter_message(text= "the channel 1 is temperature is {} degrees".format(ch1))
        return []

class action_gives_channel_2_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_two_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        ch2 = df['channel2 Value'].iloc[-1]
        
        if ch2 == 'fault':
            dispatcher.utter_message(text= "there is some fault in accessing channel 2 temperature")
        else:
            dispatcher.utter_message(text= "the channel 2 is temperature is {} degrees".format(ch2))
        return []

    

class action_gives_channel_3_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_three_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        ch3 = df['channel3 Value'].iloc[-1]
        
        if ch3 == 'fault':
            dispatcher.utter_message(text= "there is some fault in accessing channel 3 temperature")
        else:
            dispatcher.utter_message(text= "the channel 3 is temperature is {} degrees".format(ch3))
        return []





class action_gives_channel_1_mean_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_one_mean_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel1 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch1mean = round(a.mean(),2)
        if not ch1mean:
            dispatcher.utter_message(text= "couldn't load the channel 1 average temperature")
        else:
            dispatcher.utter_message(text= "the channel 1 average temperature is {} degrees".format(ch1mean))
        return []





class action_gives_channel_2_mean_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_two_mean_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel2 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch2mean = round(a.mean(),2)
        if not ch2mean:
            dispatcher.utter_message(text= "couldn't load the channel 2 average temperature")
        else:
            dispatcher.utter_message(text= "the channel 2 average temperature is {} degrees".format(ch2mean))
        return []







class action_gives_channel_3_mean_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_three_mean_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel3 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch3mean = round(a.mean(),2)
        if not ch3mean:
            dispatcher.utter_message(text= "couldn't load the channel 3 average temperature")
        else:
            dispatcher.utter_message(text= "the channel 3 average temperature is {} degrees".format(ch3mean))
        return []



class action_gives_channel_1_min_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_one_minimum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel1 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch1min = round(a.min(),2)
        if not ch1min:
            dispatcher.utter_message(text= "couldn't load the channel 1 average temperature")
        else:
            dispatcher.utter_message(text= "the channel 1 had minimum temperature was {} degrees".format(ch1min))
        return []



class action_gives_channel_2_min_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_two_minimum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel2 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch2min = round(a.min(),2)
        if not ch2min:
            dispatcher.utter_message(text= "couldn't load the channel 2 minimum temperature")
        else:
            dispatcher.utter_message(text= "the channel 2 had minimum temperature was {} degrees".format(ch2min))
        return []




class action_gives_channel_3_min_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_three_minimum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel3 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch3min = round(a.min(),2)
        if not ch3min:
            dispatcher.utter_message(text= "couldn't load the channel 3 minimum temperature")
        else:
            dispatcher.utter_message(text= "the channel 3 had minimum temperature was {} degrees".format(ch3min))
        return []














































class action_gives_channel_1_max_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_one_maximum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel1 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch1max = round(a.max(),2)
        if not ch1max:
            dispatcher.utter_message(text= "couldn't load the channel 1 average temperature")
        else:
            dispatcher.utter_message(text= "the channel 1 had maximum temperature was {} degrees".format(ch1max))
        return []



class action_gives_channel_2_max_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_two_maximum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel2 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch2max = round(a.max(),2)
        if not ch2max:
            dispatcher.utter_message(text= "couldn't load the channel 2 maximum temperature")
        else:
            dispatcher.utter_message(text= "the channel 2 had maximum temperature was {} degrees".format(ch2max))
        return []




class action_gives_channel_3_max_temp(Action):

    def name(self) -> Text:
        return "action_asked_channel_three_maximum_temperature"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        SERVICE_ACCOUNT_FILE = 'keys.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
        SAMPLE_SPREADSHEET_ID =  threechanneltempsensorid
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range="Multichannel-Temp-Sensor-3Ch-20to100!a1:j40000").execute()
        values = result.get('values', [])
        df = pd.DataFrame(values)
        ls= list(df.iloc[0])
        df.drop(index=df.iloc[:1, :].index.tolist(), inplace=True)
        df.columns = ls
        df = df['channel3 Value']
        a = df.apply(pd.to_numeric, errors='coerce').dropna()
        ch3max = round(a.max(),2)
        if not ch3max:
            dispatcher.utter_message(text= "couldn't load the channel 3 minimum temperature")
        else:
            dispatcher.utter_message(text= "the channel 3 had minimum temperature was {} degrees".format(ch3max))
        return []