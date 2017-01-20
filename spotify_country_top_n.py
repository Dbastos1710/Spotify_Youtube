import requests
import webbrowser
import json
import urllib.request
import urllib.parse
import re
import time

token = "Bearer " + input("OAuth Token: ") #BQDWxOubOFzx8fjeDi9E3Npt_fd9GiGXVgdiC3tS9LWHgajM3dRe2w3DjVVtjv0ZgHZAKt6zw2cD9PEBcLf-TFxtpOnb89THvPNMH-gbAO9Ho_8eSchxzO7JdaQ1Rg6eLBmzGIPjUp-5NM9Umpk62uKuAwPw7kSB0fb_B1uYdR4YkztfMsW5_OwXJukHyN0Cp2ztHR5V4_-5oFlHuTfPmyDcKZK8yreVwFUZuYB_VMPe_4pNhmu3PwlcePsKel9irRRsw41ly0mk1FcL3XFFHHXMHBHblYEu7hSccB8sqecdVZD9-w7PdcYS"

headers = {
        'Accept': 'application/json',
        'Authorization': token}
params = {
        'country': input("Country in ISO 3166-1 alpha-2 form: "),
        'limit': input("Maximum number of tracks: "),
        'offset' : input("Mininum number of tracks: ")
        }

r = requests.get('https://api.spotify.com/v1/browse/new-releases', headers=headers, params = params)
print_json = r.json()

albums_name, videos_time = [], []

for i in range(int(params['offset']), int(params['limit'])):
    a = print_json['albums']['items'][i]['name']
    albums_name.append(a)

def youtube(s):
    query_string = urllib.parse.urlencode({"search_query" : s})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    
    query_string1 = urllib.parse.urlencode({"search_query" : s})
    html_content1 = urllib.request.urlopen("http://www.youtube.com/results?" + query_string1)
    search_results1 = re.findall(r'\d{1}:\d{2}', html_content1.read().decode())
    videos_time.append(search_results1[0])

    return("http://www.youtube.com/watch?v=" + search_results[0])    


for i in albums_name:
    webbrowser.open(youtube(i, videos_time))
    time.sleep(int(videos_time[albums_name.index(i)][0])*60 + int(videos_time[albums_name.index(i)][2:4]))

#
