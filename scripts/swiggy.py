import requests

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
    
 