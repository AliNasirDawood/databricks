from faker import Faker
import random
import time
import json

fake = Faker()

def generate_transaction():
    # Generate customer details
    customer_name = fake.name()
    customer_email = fake.email()

    # Generate shipping address with city and country
    shipping_address = fake.street_address()
    shipping_city = fake.city()
    shipping_country = fake.country()
    full_shipping_address = f"{shipping_address}, {shipping_city}, {shipping_country}"

    # Generate product details
    product_name = fake.word()
    product_price = round(random.uniform(10, 1000), 2)
    quantity = random.randint(1, 5)

    # Calculate total amount
    total_amount = product_price * quantity

    # Generate transaction details in a dictionary
    transaction_details = {
        "Transaction ID": str(fake.uuid4()),
        "Date": str(fake.date_time_this_month()),
        "Customer Name": customer_name,
        "Customer Email": customer_email,
        "Shipping Address": full_shipping_address,
        "Product Name": product_name,
        "Quantity": quantity,
        "Product Price": product_price,
        "Total Amount": total_amount
    }

    # Convert dictionary to JSON format
    json_transaction = json.dumps(transaction_details, indent=2)
    print(json_transaction)

if __name__ == "_main_":
    while True:
        generate_transaction()
        time.sleep(2)  # Sleep for 10 seconds before generating the next transaction