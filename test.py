import requests
import json

#loginurl = "https://my-blog-tests.herokuapp.com/users/"
#url2 = "https://my-blog-tests.herokuapp.com/posts/"
# url = "http://localhost:8000/token/"
#http post http://127.0.0.1:8000/token-auth/ username=simon password=1234
#http post http://127.0.0.1:8000/token-auth/ username=simon password=1234
# 842a77990cdca6efd3c24d66f4d56e0ccd040f03



# data1 = {"username":"amit@123","password":"123"}


# data = requests.post(url=url, data=data1)
# print(data.json())


# url = "http://localhost:8000/posts/create/"
# data = {"title":"second fsc s ww","body":"qriorrrrrrrrrrrrrrrrrrrrrrrrrrrr","status": "published",}
headers = {
"Content-Type": "application/json; charset=UTF-8",
'Authorization': 'Token 4d4ffe5a9459cd57cbe5dcee12b9efd9ade7df44',

}

# data = json.dumps(data)
# data = requests.post(url=url,headers=headers,data=data)
# print(data.json())
# data = requests.delete(url="http://localhost:8000/posts/new-post/",headers=headers)
# print(data.json())
# # print(data.json())
# #curl -X POST -d '{"username": "admin","password": "top_secret"}' -H 'Content-Type: application/json'  http post http://127.0.0.1:8000/token/
# # curl -s -H "Content-Type: application/json" \
# #    -X POST http://localhost:8000/token/  \
# #    --data '{"username":"amit@123","password":"123"}'

url =  "http://localhost:8000/logout"

data = requests.get(url=url,headers=headers)
print(data)