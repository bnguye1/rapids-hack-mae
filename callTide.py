import requests
 
#https://api.tidelift.com/external-api/v1/packages/maven/<PACKAGE>/releases/<VERSION>/dependencies
url = "https://api.tidelift.com/external-api/v1/packages/maven/org.springframework:spring-webmvc/releases/6.0.8/dependencies"
 
headers = {
    "Content-Type": "application/json",
    #Auth Token
    "Authorization": "Bearer v2/user/eJwty0ELgjAUAOD/snOj9VS0bkUFRdsuA6mLPPecbWXF1FP035Po/PG92fC8NQ+2YmPfxPnFqCBLmeltO2jTZtILoWDvT+VBqPI8SLPptDneVdilMqwXbPZ7U++x93TFiFWHMeJr/FPlaVILlCKA4xbyhKdAjtcOiBeQYNHk1i0Fsc8XoyosZw=="
    }
 
proxies = {
   'http': 'http://zsproxy.fanniemae.com:10479',
   'https': 'http://zsproxy.fanniemae.com:10479',
   }
 
try:
 
    response = requests.get( url, headers=headers,proxies=proxies)
 
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Failed:",response.status_code)
except requests.exceptions.RequestExceptions as e:
    print("Error:",str(e))
