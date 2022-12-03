
prod_db = {
    "1000" : "com ga",
    "1001" : "com rang dua bo",
    "1002" : "bun ngan",
    "1003" : "pho thin 69",
    "1004" : "bun dau mam tom",
    "1005" : "com suon ",
    "1006" : "lau ca keo"
}


def prod_infor(prod_db, prod_id):
    if prod_id in prod_db:
        return prod_db[prod_id]
    else:
        print("Not found")

def prod_add(prod_db, id_new, name):
    prod_db[id_new] = name
    
def prod_update(prod_db, prod_id, new_name):
    if prod_id in prod_db:
        prod_db[prod_id] = new_name
#     for k in prod_db:
#         if prod_id == k:
#             prod_db[prod_id] = name
#         else:
#             prod_db[prod_id] = {}
#             prod_db[prod_id]['name'] = name
#             print(prod_db)
        
def prod_delete(prod_db, prod_id):
    if prod_id in prod_db:
        del prod_db[prod_id]

def prod_display(prod_db):
    for key, value in prod_db.items():
        print(key, " : ", value)

# nguoi dung lua chon:
while True:
    print("\
please make your choice: 1: for all product information,\
2: for add new product, \
3: for delete a product, \
4: for update a product, \
0: for cancel " )
                                 
    choice = int(input())
    if choice == 1:
        xem = prod_display(prod_db)
        print(xem)
    elif choice == 2:
        id_new = int(input("please input id for new product: "))
        name = input("please input new product name: ")
        them = prod_add(prod_db, id_new, name)
        print(prod_db)
    elif choice == 3:
        prod_id = int(input("please input id of product you want to delete: "))
        xoa = prod_delete(prod_db, prod_id)
        print(prod_db)
    elif choice == 4:
        prod_id = int(input("please input id of product you want to update: "))
        name = input("please input new name for product: ")
        sua = prod_update(prod_db, prod_id, name)
        print(prod_db)
    else: 
        choice == 0
        break
                      
               







