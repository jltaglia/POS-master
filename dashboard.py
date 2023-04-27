from flask import Blueprint, render_template
from flask_login import login_required, current_user

from database import Database
from models import Product

dashboard_bp = Blueprint('dashboard', __name__)

# Initialize the database
db = Database()

# Define the dashboard route
@dashboard_bp.route('/')
@login_required
def dashboard():
    products = db.get_all_products()
    return render_template('dashboard.html', products=products, user=current_user)

# Define the sales report route
@dashboard_bp.route('/reports/sales')
@login_required
def sales_report():
    # Query the database for sales data
    # Generate a report using a package like Pandas
    # Return a downloadable file or display the report in the browser
    return 'Sales report'
