import json
with open("DATA/users.json","r") as file:
    users = json.load(file)
    user = {}
    for x in users:
        if (x.id == 5):
            user = x
            index = users.index(x)
            break
with open("DATA/users.json","r") as p:
    products = json.load(file)
    product = {}
    for x in products :
        if(x.id == 5):
            user.cart.append(x)
            users[index] = user
            break
    
    user.cart.append(product)
    users[index] = user
  
    