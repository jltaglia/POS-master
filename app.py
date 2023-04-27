import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from database import Database
from models import Product

# Initialize the database
db = Database()

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the dashboard layout
app.layout = dbc.Container([
    html.H1('Inventory Management System'),
    dbc.Row([
        dbc.Col([
            html.H2('Products'),
            html.Table([
                html.Thead([
                    html.Tr([
                        html.Th('Name'),
                        html.Th('Description'),
                        html.Th('Price'),
                        html.Th('Actions')
                    ])
                ]),
                html.Tbody(id='product-table')
            ]),
            html.A('Add Product', href='/add_product', className='btn btn-primary mt-3')
        ], md=8),
        dbc.Col([
            html.H2('Sales'),
            dcc.Graph(id='sales-graph', figure={
                'data': [
                    {'x': ['Jan', 'Feb', 'Mar'], 'y': [100, 150, 200], 'type': 'bar', 'name': 'Sales'}
                ],
                'layout': {
                    'title': 'Sales by Month'
                }
            })
        ], md=4)
    ])
])

# Define the product table callback
@app.callback(
    dash.dependencies.Output('product-table', 'children'),
    dash.dependencies.Input('interval', 'n_intervals')
)
def update_product_table(n):
    products = db.get_all_products()
    rows = []
    for product in products:
        row = html.Tr([
            html.Td(product.name),
            html.Td(product.description),
            html.Td(f'${product.price:.2f}'),
            html.Td([
                html.A('Edit', href=f'/edit_product/{product.id}', className='btn btn-sm btn-primary'),
                html.A('Delete', href=f'/delete_product/{product.id}', className='btn btn-sm btn-danger ml-1', 
                       onclick='return confirmDelete();')
            ])
        ])
        rows.append(row)
    return rows

# Define the sales graph callback
@app.callback(
    dash.dependencies.Output('sales-graph', 'figure'),
    dash.dependencies.Input('interval', 'n_intervals')
)
def update_sales_graph(n):
    return {
        'data': [
            {'x': ['Jan', 'Feb', 'Mar'], 'y': [100, 150, 200], 'type': 'bar', 'name': 'Sales'}
        ],
        'layout': {
            'title': 'Sales by Month'
        }
    }

if __name__ == '__main__':
    app.run_server(debug=True)
