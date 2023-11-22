import requests
import gzip
import json
import csv
import logging

def http_request():
    url = "https://httpbin.org/anything"
    params = {"isadmin": 1}
    headers = {"User-Agent": "CustomUserAgent"}

    # Sending the first request with default User-Agent
    response_default = requests.post(url, params=params)
    body_default = response_default.json() if response_default.ok else None

    # Sending the second request with a custom User-Agent
    response_custom_ua = requests.post(url, params=params, headers=headers)
    body_custom_ua = response_custom_ua.json() if response_custom_ua.ok else None

    return body_default, body_custom_ua




# Question 2

class ProductProcessor:
    def __init__(self):
        self.data_file_path = "third_part/data/data.json.gz"
        self.output_csv_file = "output_products.csv"

    def read_data(self):
        try:
            with gzip.open(self.data_file_path, "rt", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            logging.error(f"Error: File {self.data_file_path} not found.")
            return None
        except json.JSONDecodeError:
            logging.error(f"Error: Unable to decode JSON data from {self.data_file_path}.")
            return None

    def process_products(self, products):
        available_products = []
        for product_id, product_info in products.items():
            if not isinstance(product_info, dict):
                logging.warning(f"Invalid product information for ID: {product_id}, Info: {product_info}")
                continue

            product_name = product_info.get("name", "")
            product_price = product_info.get("price", None)

            if product_name and product_price is not None:
                truncated_name = self.truncate_product_name(product_name)
                rounded_price = round(product_price, 1)
                available_products.append((truncated_name, rounded_price))
                print(f"You can buy {truncated_name} at our store at {rounded_price}")
            else:
                logging.warning(f"Product information incomplete for ID: {product_id}, Name: {product_name}")

        return available_products

    def truncate_product_name(self, product_name, max_length=30):
        return product_name[:max_length]

    def save_to_csv(self, data):
        try:
            with open(self.output_csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Product Name', 'Product Price'])
                writer.writerows(data)
            print(f"Available products saved to {self.output_csv_file}")
        except IOError:
            logging.error(f"Error: Unable to write to {self.output_csv_file}")

    def process_and_save(self):
        product_data = self.read_data()
        if product_data:
            available_products = self.process_products(product_data)
            self.save_to_csv(available_products)
