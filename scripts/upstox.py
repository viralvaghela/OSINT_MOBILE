import requests

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
