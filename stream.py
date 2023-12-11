# from faker import Faker
# import random
# import time
# import json

# fake = Faker()

# def generate_transaction():
    
#     # Generate customer details
#     customer_id =  fake.uuid4()
#     customer_name = fake.name()
#     customer_email = fake.email()
    

#     # Generate shipping address with city and country
#     shipping_address = fake.street_address()
#     shipping_city = fake.city()
#     shipping_country = fake.country()
#     full_shipping_address = f"{shipping_address}, {shipping_city}, {shipping_country}"

#     # Generate product details
#     product_id = fake.uuid4()
#     product_name = fake.word()
#     product_brand = fake.company()
#     product_category = fake.word()
#     product_price = round(random.uniform(10, 1000), 2)
#     quantity = random.randint(1, 5)

#     # Calculate total amount
#     total_amount = product_price * quantity

#     # Generate transaction details in a dictionary
#     transaction_details = {
#         "Transaction ID": str(fake.uuid4()),
#         "Date": str(fake.date_time_this_month()),
#         "Customer ID": customer_id,
#         "Customer Name": customer_name,
#         "Customer Email": customer_email,
#         "Shipping Address": full_shipping_address,
#         "Product ID":product_id,
#         "Product Name": product_name,
#         "Product Brand":product_brand,
#         "Product_Category":product_category,
#         "Quantity": quantity,
#         "Product Price": product_price,
#         "Total Amount": total_amount
#     }

#     # Convert dictionary to JSON format
#     json_transaction = json.dumps(transaction_details, indent=2)
#     print(json_transaction)
#     return json_transaction

# if __name__ == "__main__":
#     while True:
#         generate_transaction()
#         time.sleep(2)  # Sleep for 10 seconds before generating the next transaction

# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

from flask import Flask, jsonify
from faker import Faker
import random
import json
import time

app = Flask(__name__)
fake = Faker()

def generate_transaction():
    # Generate customer details
    customer_id =  fake.uuid4()
    customer_name = fake.name()
    customer_email = fake.email()

    # Generate shipping address with city and country
    shipping_address = fake.street_address()
    shipping_city = fake.city()
    shipping_country = fake.country()
    full_shipping_address = f"{shipping_address}, {shipping_city}, {shipping_country}"

    # Generate product details
    product_id = fake.uuid4()
    product_name = fake.word()
    product_brand = fake.company()
    product_category = fake.word()
    product_price = round(random.uniform(10, 1000), 2)
    quantity = random.randint(1, 5)

    # Calculate total amount
    total_amount = product_price * quantity

    # Generate transaction details in a dictionary
    transaction_details = {
        "Transaction ID": str(fake.uuid4()),
        "Date": str(fake.date_time_this_month()),
        "Customer ID": customer_id,
        "Customer Name": customer_name,
        "Customer Email": customer_email,
        "Shipping Address": full_shipping_address,
        "Product ID": product_id,
        "Product Name": product_name,
        "Product Brand": product_brand,
        "Product_Category": product_category,
        "Quantity": quantity,
        "Product Price": product_price,
        "Total Amount": total_amount
    }

    # Convert dictionary to JSON format
    json_transaction = json.dumps(transaction_details, indent=2)
    return json_transaction

@app.route('/generate_transaction', methods=['GET'])
def get_transaction():
    transaction_data = generate_transaction()
    print(trasaction_data)
    return jsonify({'transaction': transaction_data})

if __name__ == "__main__":
    app.run(debug=True)
