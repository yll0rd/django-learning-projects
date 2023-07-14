# Ecommerce API

This is an API for an ecommerce platform that allows customers to browse products, add items to their cart, and check out their orders. The API is built using the Django Rest Framework and includes endpoints for managing user accounts, products, orders, and payments.
Getting Started

To get started with the Ecommerce API, you will need to have Python 3.8 or higher installed on your system. You will also need to install the required Python packages by running the following command:

`pip install -r requirements.txt`

Once you have installed the required packages, you can start the development server by running the following command:

`python manage.py runserver`

This will start the server on http://localhost:8000/. You can then use a tool like `curl` or a web browser to make requests to the API.
  
## API Endpoints

The Ecommerce API includes the following endpoints:  
### Authentication
```
    POST /auth/register1/: Register a new user with basic information
    POST /auth/register2/: Register a new user with admin privileges
    POST /auth/login/: Authenticate a user and get an access token
    POST /auth/logout/: Log out a user and revoke their access token
```
### Users  
```
    GET /auth/: Get a list of all users (requires admin privileges)
    PUT /auth/:id/: Update user details (requires admin privileges)
    DELETE /auth/:id/: Delete a user (requires admin privileges)  
``` 
### Products
```
    GET /products/: Get a list of all products
    POST /products/: Create a new product (requires admin privileges)
    PUT /products/:id/: Update details for a product (requires admin privileges)
    DELETE /products/:id/: Delete a product (requires admin privileges)
```
### Orders
```
    GET /orders/: Get a list of all orders (requires admin privileges)
```
### Cart
```
    POST /addCart/: Add a product to the user's cart
    PUT /cart/: Update the quantity of the product in cart
```
### Checkout
```
    POST /checkout/: Checkout the user's current cart and place an order
```

## Authentication and Authorization

The Ecommerce API uses token-based authentication and authorization. When a user logs in or registers, the API returns an access token that can be used to authenticate subsequent requests. This access token is included in the Authorization header of the request, like so:

`Authorization: Token <access_token>`

Some endpoints require admin privileges, which are indicated in the endpoint documentation. To access these endpoints, the user must have an admin account and include the access token in their request header.  

## Error Handling
The Ecommerce API returns error responses with appropriate HTTP status codes and error messages in the response body. Error messages include a message field that describes the error, like so:

```
{
    "message": "Invalid credentials"
}
```

## Environment Variables

This project uses environment variables to store sensitive information, such as database credentials and secret keys. These variables are stored in an `.env` file in the root directory of the project.

To set up the environment variables, you should create a copy of the `.env`.example file and rename it to `.env`. Then, open the file and replace the placeholder values with your own values.

```
cp .env.example .env
nano .env
```