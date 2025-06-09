import requests

# CREATE a product -> POST
new_product = {"title": "notebook", "price": 19.99}
response = requests.post("https://dummyjson.com/products/add", data=new_product)
print(response.status_code, response.text)

# READ a product -> GET
product_id = 100
response = requests.get(f"https://dummyjson.com/products/{product_id}")
print(response.status_code, response.text)

# READ multiple products -> GET (Optional with limit and skip)
response = requests.get("https://dummyjson.com/products/", params={"skip": 50, "limit": 5})
response_json = response.json()
for product in response_json["products"]:
    print(product["title"])

# UPDATE a product PUT / PATCH
updated_product = {"id": 100, "title": "Notebook", "price": 59.99}
response = requests.put("https://dummyjson.com/products/100", data=updated_product)
print(response.status_code, response.text)

updated_product = {"price": 100.99}
response = requests.patch("https://dummyjson.com/products/100", data=updated_product)
print(response.status_code, response.text)

# DELETE a product
response = requests.delete("https://dummyjson.com/products/100")
print(response.status_code, response.text)

# Authentication with username and password
credentials = {"username": "emilys", "password": "emilyspass"}
response = requests.post("https://dummyjson.com/auth/login", data=credentials)
print(response.status_code, response.text)
token = response.json()["accessToken"]

# GET with token authorization
response = requests.get("https://dummyjson.com/auth/me", headers={"Authorization": f"Bearer {token}"})
print(response.status_code, response.text)