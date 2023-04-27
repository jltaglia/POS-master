from dash.dependencies import Input, Output, State
import database
import ui

from utils import generate_id

# Define a Product class with an ID field
class Product:
    def __init__(self, name, price):
        self.id = generate_id()
        self.name = name
        self.price = price

# Create a new product with a unique ID
new_product = Product("Widget", 19.99)
print(new_product.id)  # prints a random string like "A2B4C6"


db = database.Database()

@ui.app.callback(
    Output("product-table", "children"),
    [Input("add-product-button", "n_clicks")],
    [State("product-name", "value"), State("quantity", "value")]
)
def add_product(n_clicks, product_name, quantity):
    if n_clicks is not None:
        db.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (product_name, quantity))
    products = db.fetch("SELECT name, quantity FROM products")
    rows = []
    for product in products:
        rows.append(html.Tr([
            html.Td(product[0]),
            html.Td(product[1])
        ]))
    return rows

if __name__ == '__main__':
    ui.app.run_server(debug=True)
