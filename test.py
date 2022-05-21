#CLIENT FILE
import requests

BASE='http://127.0.0.1:5000/'

data=[
    {'likes':100,'views':50,'name':'title1'},
    {'likes':300,'views':20,'name':'title2'},
    {'likes':400,'views':60,'name':'title3'}
]

# for i in range(len(data)):
#     response=requests.put(BASE + 'video/'+str(i),data[i])
#     print(response.json())

# input()

response=requests.get(BASE+'video/1')
print(response.json())




# response=requests.delete(BASE+'video/1')
# print(response)

# input()

# response=requests.get(BASE+'video/1')
# print(response.json())\



# response=requests.get(BASE+'helloworld')
# print(response.json())

# response=requests.post(BASE+'helloworld')
# print(response.json())



# response=requests.get(BASE+'hello')
# print(response.json())

# response=requests.post(BASE+'world')
# print(response.json())


# response=requests.get(BASE+'helloworld/pooja/10')
# print(response.json())

# response=requests.get(BASE+'helloworld/jess')
# print(response.json())

# response=requests.put(BASE+'video/1',{'name':'tv','likes':10,'views':100})
# print(response.json())

# input() #This will help us like jab upper print function run hone ke baad it will take some time and when we will press enter then only below print function will work

# response=requests.get(BASE+'video/2')
# print(response.json())


# input()

# response=requests.put(BASE+'video/1',{'name':'tv','likes':10,'views':100})
# print(response.json())

