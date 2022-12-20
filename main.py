import http.client, urllib
import time
import random
sleep = 30
key = "8EG81WT1IS9HS5NP"

def randomgen():
    while(True):
        random1 = random.randint(50, 100)
        params = urllib.parse.urlencode({'field1':random1, 'key':key})
        headers = {'Content-type':"application/x-ww-form-urlencoded", "Accept":"text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(random1)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("Connection Failed")
        break

while(True):
    randomgen()
    time.sleep(sleep)