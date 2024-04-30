#a = {
    #"car" : "tayota",
    #"model":"camry",
   # "image": ["https://ai2.appinventor.mit.edu/?locale=ru#5974014489067520","https://some-lm"],
   # "price" : 25000000,
    #"is_published" : True
    #}

a = {"name": "Erbol", "surname": "Ascarov"}
b = a ["name"]
print("b=", b)
b = a.get("name")
b = None

a["middle_name"] = "Erzhanuly"
print("a", a)


с= {"name":"Askar", "last_name":"Erlanov"}
for k,v in с.items():
    print("key", k)
    print("value", v)




list_1 = [

     {
        "name" :"Kanat",
        "last_name":"Erbolov",
        "age": 20
    },
    {
        "name" :"Askar",
        "last_name":"Erzhanov",
        "age":15

    },
    {
        "name":"Kairat",
        "last_name":"Zhandosov",
        "age":45
    }
]


total=0
for n in list_1:
    total += n["age"]

count=len(list_1)

age = total/count
print(age)




#dictionary = словарь,dict