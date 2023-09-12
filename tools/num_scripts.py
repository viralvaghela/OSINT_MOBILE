import requests

def check_flipkart(num):
    num = "+91"+num 
    
    burp0_url = "https://1.rome.api.flipkart.com:443/api/6/user/signup/status"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Referer": "https://www.flipkart.com/", "X-User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0 FKUA/website/42/website/Desktop", "Origin": "https://www.flipkart.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "close"}
    burp0_json={"loginId": [num], "supportAllStates": True}
    
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    jsonData= response.json()
    jsonData['RESPONSE']['userDetails'][num]
    
    if(jsonData['RESPONSE']['userDetails'][num]=="GUEST"):
        print("Flipkart : False")

    elif(jsonData['RESPONSE']['userDetails'][num]=="VERIFIED"):
        print("Flipkart : True")

    elif(jsonData['RESPONSE']['userDetails'][num]=="VERIFIED"):
        print("Flipkart : True")
    else:
        print("Flipkart : False")

       

def check_instagram(num):

    burp0_url = "https://www.instagram.com:443/api/v1/web/accounts/account_recovery_send_ajax/"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "X-Csrftoken": "bShw46OB35NJxqZhWDt3WWBwq3ZjfIlX", "X-Instagram-Ajax": "1008400429", "X-Ig-App-Id": "936619743392459", "X-Asbd-Id": "129477", "X-Ig-Www-Claim": "0", "X-Web-Device-Id": "4946C9B5-839D-4132-B16E-76DEF3ED9FF9", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.instagram.com", "Referer": "https://www.instagram.com/accounts/password/reset/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp0_data = {"email_or_username":num}
    res=requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
    jsonData= res.json()
    if(jsonData['status']=="ok"):
        print("Instagram : True")
    else:
        print("Instagram : False")

 
def check_snapdeal(num):
    burp0_url = "https://www.snapdeal.com:443/isUserExists"
    burp0_cookies = {"AWSALB": "+YkqG4rZwezyidTaRusAaervVKSC6fTrOLjWdr5KxFry+pm4jWVuEqERjbHP6b9HaDq8zHKDfXXL+Ubb+SxvLiHedplGidEZqYGvnzLNiQbVweIPi7LW8PwCnDLo", "AWSALBCORS": "+YkqG4rZwezyidTaRusAaervVKSC6fTrOLjWdr5KxFry+pm4jWVuEqERjbHP6b9HaDq8zHKDfXXL+Ubb+SxvLiHedplGidEZqYGvnzLNiQbVweIPi7LW8PwCnDLo", "SCOUTER": "z3ke8p582ns36h", "JSESSIONID": "A71FB7412A43ADAD4C46EF34AD358C1A", "versn": "v1", "u": "169449250362352196", "sd.zone": "NO_ZONE", "xg": "eyJ3YXAiOnsiYWUiOiIxIn0sIm1hcGkiOnsidHBmIjoiQTIifSwicHMiOnsiYXQiOiJvIiwiY2IiOiJCIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiOWU1Zjk2NDQtMzcyYy00YmI2LWI3MWUtZjE3MTg3NWM5NWNiIn19fHwxNjk0NDk0MzAzNjI1", "xc": "eyJ3YXAiOnsiYWUiOiIxIn0sIm1hcGkiOnsidHBmIjoiQTIifSwicHMiOnsiYXQiOiJvIiwiY2IiOiJCIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19", "alps": "akm", "_gcl_au": "1.1.888232672.1694492549", "_sdDPPageId": "1694492584944_7380_169449250362352196", "isWebP": "true", "st": "utm_source%3Dadmitad_846%7Cutm_content%3Dadmitad_846%7Cutm_medium%3Dnull%7Cutm_campaign%3Dd86262e77696277dbdf80abc67039a31%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C", "vt": "utm_source%3Dadmitad_846%7Cutm_content%3Dadmitad_846%7Cutm_medium%3Dnull%7Cutm_campaign%3Dd86262e77696277dbdf80abc67039a31%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C", "lt": "utm_source%3Dadmitad_846%7Cutm_content%3Dadmitad_846%7Cutm_medium%3Dnull%7Cutm_campaign%3Dd86262e77696277dbdf80abc67039a31%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C", "_uetsid": "fee6e4b0512311eeba3c33c85d935e4b", "_uetvid": "fee6fbd0512311ee98885dab8561a01b", "s_sess": "%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_ppv%3D100%3B", "s_pers": "%20s_vnum%3D1697084561621%2526vn%253D1%7C1697084561621%3B%20gpv_pn%3DLoginPage%7C1694494402305%3B%20s_invisit%3Dtrue%7C1694494402306%3B", "_fbp": "fb.1.1694492569935.1703251362", "lang": "en"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.snapdeal.com", "Referer": "https://www.snapdeal.com/login", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp0_json={"userName": num}
    res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    if res.status_code == 200:
        jsonData = res.json()
        if jsonData['userExist'] == True:
            print(f"Snapdeal: True")
        else:
            print(f"Snapdeal: False")
 
def check_swiggy(num):
    burp0_url = "https://www.swiggy.com:443/dapi/auth/signup"
    burp0_cookies = {"__SW": "47GnsdAO63a2sNdrRrrcv6oinPbzTUKr", "_device_id": "0f6b717f-fc91-09c8-bfab-4aff074b7f28", "WZRK_G": "c7c6022d99ef41b2b3d778c0e739598c", "_ga_34JYJ0BCRN": "GS1.1.1693569437.2.0.1693569444.0.0.0", "_ga": "GA1.2.166954299.1680838951", "_guest_tid": "07f1bff4-df93-4bbe-abac-77833ddf1075", "_is_logged_in": "", "_sid": "9355984f-0b0d-4c06-9a3d-ff05fcf323b3", "fontsLoaded": "1", "WZRK_S_W86-ZZK-WR6Z": "%7B%22s%22%3A1693569438%2C%22t%22%3A1693569437%7D", "_gcl_au": "1.1.2067118175.1693569436", "_gid": "GA1.2.571477607.1693569438", "_gat_0": "1"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.swiggy.com/", "Content-Type": "application/json", "__fetch_req__": "true", "Origin": "https://www.swiggy.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp0_json={"_csrf": "O2sXih6dADEF-XT5X2Rs-IvmalAhE29w_KE8tMMQ", "email": "randomtest@test.com", "mobile": num, "name": "test", "otp": "", "referral": ""}
    response = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)

    jsonData= response.json()
    if(jsonData['statusMessage']=="Mobile number already exists"):
        print("Swiggy : True")
    else:
        print("Swiggy : False")
    
 

### Doesn't work as expected, sends OTP for all valid num(registred or not)
def check_upstox(num):
   

    burp0_url = "https://service.upstox.com:443/login/open/v5/auth/1fa/otp/generate?requestId=WPRO-46cb9b177b"
    burp0_cookies = {"_ga_CLCPGTZJXV": "GS1.1.1692441881.1.1.1692441954.50.0.0", "_gcl_au": "1.1.1902378256.1692441881", "_ga": "GA1.2.598873318.1692441882", "_ga_VFG6NNXYGT": "GS1.1.1692441881.1.1.1692441954.0.0.0", "_fbp": "fb.1.1692441883025.403003868", "_clck": "ryv6w7|2|fea|0|1326", "_uetvid": "64c722a03e7d11ee8f0fcda295cc8256", "WZRK_S_88W-7Z6-676Z": "%7B%22p%22%3A1%7D", "_gid": "GA1.2.1117413322.1693572435", "_dc_gtm_UA-80300668-1": "1", "_gat_UA-80300668-1": "1", "lead_phone_number": "7485994073", "_cfuvid": "ZB9rSWeAxQRRQLG_v1FVOoaH6Q.cYU.JmPuCzh.41DQ-1693572444978-0-604800000", "mp_62597aa51842e6e2c56b97d96e4c5f8a_mixpanel": "%7B%22distinct_id%22%3A%20%2218a0d65a32e68-0c4431d09781f8-d535429-144000-18a0d65a32f460%22%2C%22%24device_id%22%3A%20%2218a0d65a32e68-0c4431d09781f8-d535429-144000-18a0d65a32f460%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://login.upstox.com/", "Content-Type": "application/json", "X-Device-Details": "platform=WEB|osName=Windows/10|osVersion=Firefox/117.0|appVersion=4.0.0|modelName=Firefox|manufacturer=unknown", "Origin": "https://login.upstox.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers"}
    burp0_json={"data": {"mobileNumber": num}}
    res= requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)

    jsonData= res.json()
    if(jsonData['success']=="true"):
        print("Upstox : True")
    else:
        print("Upstox : False")
