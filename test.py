# import requests
# import json

# # loginurl = "https://my-blog-tests.herokuapp.com/users/"
# #url2 = "https://my-blog-tests.herokuapp.com/posts/"
# # base_url = "https://blog-1-api-test.herokuapp.com"
# # url = "https://blog-1-api-test.herokuapp.com/token/"
# #http post http://127.0.0.1:8000/token-auth/ username=simon password=1234
# #http post http://127.0.0.1:8000/token-auth/ username=simon password=1234
# # 842a77990cdca6efd3c24d66f4d56e0ccd040f03



# # data1 = {"username":"amit@123","password":"123"}


# # data = requests.post(url=url, data=data1)
# # print(data.json())


# # url = "https://blog-1-api-test.herokuapp.com/logout/"
# url = "http://localhost:8000/posts/search/?search=fir"
# # data = {"body":"good jsahhhhhhhhhhhhhhhhhhhhhhhhhhhhhh sa sahjkas sksahkjas boy"}
# # headers = {
# # "Content-Type": "application/json; charset=UTF-8",
# # 'Authorization': 'Token fa93180e4be31710e0fa8d1629b3c285b0d16f4c',

# # }

# # data = json.dumps(data)
# data = requests.get(url=url)
# print(data.json())
# # data = requests.delete(url="http://localhost:8000/posts/new-post/",headers=headers)
# # print(data.json())
# # # print(data.json())
# # #curl -X POST -d '{"username": "admin","password": "top_secret"}' -H 'Content-Type: application/json'  http post http://127.0.0.1:8000/token/
# # # curl -s -H "Content-Type: application/json" \
# # #    -X POST http://localhost:8000/token/  \
# # #    --data '{"username":"amit@123","password":"123"}'

# # headers = {
# # 'Authorization':'Token ce405b864949acf415be52ab54d8a5d0fef0ad95',
# # }

# # url = base_url + "/logout/"

# # data = requests.get(url=url, headers=headers)
# # print(data)







# # #For example, In following series
# # #1       5      2     8   9     3    7    9     15    20     20     7    7    1


# # x = [1,5,2,8,9,3,7,9,15,20,20,7,7,1,100,200,300,400,500,6000]
# # max_lenth =1

# # for i in range(len(x)):
# #     mx=1
# #     count =i + 1
# #     temp = x[i]

# #     while count<len(x) and temp< x[count]:
# #         mx=mx+1
# #         temp= x[count]

# #         count +=1
# #     if mx>max_lenth:
# #         max_lenth=mx
# # print(max_lenth)
# # token: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


# # bdcwiwmmcervyxyu


def print_revarse(n):
    """Printing series ..."""
    for i in range(len(n) - 1, -1, -1):
        print(n[i], end=" ")

arr = [10,223,44,35,56,35,44,223,10]

print_revarse(arr)
