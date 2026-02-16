from product_sql import insert_order
import traceback

try:
    print("Attempting to insert dummy order...")
    order_data = {
        'customer_name': 'Test User',
        'grand_total': 100.0,
        'order_details': [
            {
                'product_id': 1,
                'quantity': 1,
                'total_price': 100.0
            }
        ]
    }
    order_id = insert_order(order_data)
    print("Success! Order ID:", order_id)
except Exception:
    traceback.print_exc()
