dictionary_products_amount = int(input("Insert the amount of products in the dictionary: "))

product_dictionary = {}
products_with_zero_stock = []
for _ in range(dictionary_products_amount):
    code = input("Insert the code of your product: ")
    name = input("Insert the name of your product: ")
    price = int(input("Insert the price of your product: "))
    stock = int(input("Insert the stock of your product: "))
    product_dictionary[code] = [name, price, stock]
    if(stock == 0):
        products_with_zero_stock.append(code)

print("List of products: \n")
for product in product_dictionary.keys():
    print(product)

product_code = input("Insert the code of the product you are looking for: ")

product = product_dictionary.get(product_code)
if(product):
    name = product[0]
    price = product[1]
    stock = product[2]
    print(f"Product: {name}. Price: {price}. Amount in stock: {stock}")
else:
    print("The product was not found")

if(len(products_with_zero_stock)):
    if(len(products_with_zero_stock) == 1):
        print("The products with amount equals to zero is: ")
    else:    
        print("The products with amount equals to zero are: ")
    for code in products_with_zero_stock:
        print(f"Product with the code: {code}")
else:
    print("All the products have stock!")
    
