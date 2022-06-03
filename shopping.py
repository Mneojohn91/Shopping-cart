import json


file = open("shopping_info.json", "r")
shopping_data = json.load(file)
file.close()


def get_customer_baskets(email):
    return [basket for basket in shopping_data if basket["email"] == email]


def get_all_customers():
    return [email for email in set(customer["email"] for customer in shopping_data)]


def stock():
    shopping_list = []
    _ = [
        [
            shopping_list.append({"name": item["name"], "quantity": item["quantity"]})
            for item in status["items"]
            if item["name"] not in shopping_list
        ]
        for status in shopping_data
        if status["status"] == "PAID"
    ]

    return shopping_list


def required_stock():
    shopping_cart = stock()
    result = {}
    for item in shopping_cart:
        if item["name"] not in result:
            result.update({item["name"]: item["quantity"]})
        else:
            result[item["name"]] = result[item["name"]] + item["quantity"]

    return [{"name": key, "quantity": value} for key, value in result.items()]


def total_spent(email):
    customer_basket = get_customer_baskets(email)
    customers = [
        [
            {
                "email": status["email"],
                "total": sum(
                    [item["price"] * item["quantity"] for item in status["items"]]
                ),
            }
        ]
        for status in customer_basket
        if status["status"] == "DELIVERED" or status["status"] == "PAID"
    ]
    totals = []

    for shopping_data in customers:
        for customer in shopping_data:
            if customer["email"] == email:
                totals.append(customer["total"])
    return sum(totals)


def get_customers_with_open_baskets():
    return [
        customer_item["email"]
        for customer_item in shopping_data
        if customer_item["status"] == "OPEN"
    ]


def top_customer():
    customer = get_all_customers()
    totals = [{"email": email, "total": total_spent(email)} for email in customer]
    return sorted(totals, key=lambda value: value["total"], reverse=True)