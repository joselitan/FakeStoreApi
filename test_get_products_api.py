import requests
import logging

logging.basicConfig(level=logging.INFO)
def test_products_returns_200_status_code():
    response = requests.get("https://fakestoreapi.com/products")
    logging.info(f"Response Status Code: {response.status_code}")
    assert response.status_code == 200, "Expected status code 200"

def test_assert_amount_of_products():
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()
    logging.info(f"Number of Products: {len(products)}")
    assert len(products) == 20, "Expected 20 products in the response"

def test_assert_specific_product_return_fields():
    product_id = 2
    response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    product = response.json()
    logging.info(f"Title: {product['title']}, Price: {product['price']}, Category: {product['category']}")
    assert "title" in product, "Product title is missing"
    assert "price" in product, "Product price is missing"
    assert "category" in product, "Product category is missing"
  
    

def test_assert_specific_productId_correct_data():
    product_id = 2
    response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    product = response.json()
    logging.info(f"Product Data: {product}")
    assert product["id"] == product_id, f"Expected product ID to be {product_id}"
