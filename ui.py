import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Inventory Management System"),
    html.Div([
        html.Label("Product Name"),
        dcc.Input(id="product-name", type="text")
    ]),
    html.Div([
        html.Label("Quantity"),
        dcc.Input(id="quantity", type="number")
    ]),
    html.Button("Add Product", id="add-product-button"),
    html.Table([
        html.Thead([
            html.Tr([
                html.Th("Product Name"),
                html.Th("Quantity")
            ])
        ]),
        html.Tbody(id="product-table")
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
