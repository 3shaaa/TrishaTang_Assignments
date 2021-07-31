products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):

    return(products[code])

get_product("espresso")

def get_property(code,property):

    return(products[code][property])

get_property("espresso", "price")

def main():

    total_1=0
    total_2=0
    total_3=0
    total_4=0
    total_5=0
    total_6=0
    ordered_food={}
    americano = 0
    brewedcoffee = 0
    cappuccino = 0
    dalgona = 0
    espresso = 0
    frappuccino = 0
    while True:
        productquantity=str(input('Input your product and quantity: '))

        if productquantity == "/":
            break
        product_code, quantity=productquantity.split(",")
        name_product= (products[product_code]["name"])
        quantity= int(quantity)
        if product_code == 'americano':
            americano+=quantity
            quantity = americano
            subtotal= americano*(products[product_code]["price"])
            total_1 = americano*(products[product_code]["price"])
        if product_code == 'brewedcoffee':
            brewedcoffee+=quantity
            quantity = brewedcoffee
            subtotal= brewedcoffee*(products[product_code]["price"])
            total_2 = brewedcoffee*(products[product_code]["price"])
        if product_code == 'cappuccino':
            cappuccino+=quantity
            quantity = cappuccino
            subtotal= cappuccino*(products[product_code]["price"])
            total_3 = cappuccino*(products[product_code]["price"])
        if product_code == 'dalgona':
            dalgona+=quantity
            quantity = dalgona
            subtotal= dalgona*(products[product_code]["price"])
            total_4 = dalgona*(products[product_code]["price"])
        if product_code == 'espresso':
            espresso+=quantity
            quantity = espresso
            subtotal= espresso*(products[product_code]["price"])
            total_5 =  espresso*(products[product_code]["price"])
        if product_code == 'frappuccino':
            frappuccino+=quantity
            quantity = frappuccino
            subtotal= frappuccino*(products[product_code]["price"])
            total_6 = frappuccino*(products[product_code]["price"])
        ordered_food.update({product_code:{'name_product':name_product,'quantity':quantity,'subtotal':subtotal}})
        total = total_1+total_2+total_3+total_4+total_5+total_6
    ordered_food=dict(sorted(ordered_food.items()))

    with open("receipt.txt", "w") as f:
        f.write('''
    ==
    CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')

        for k in ordered_food:
            f.write(f'''
            {k}\t\t{ordered_food[k]['name_product']}\t\t{ordered_food[k]['quantity']}\t\t\t\t{ordered_food[k]['subtotal']}
            ''')

        f.write(f'''
        Total:\t\t\t\t\t\t\t\t\t\t{total}
        ==
        ''')

main()
