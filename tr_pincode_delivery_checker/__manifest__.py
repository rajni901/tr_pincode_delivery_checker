{
    'name': 'Pincode Delivery Checker & Estimated Delivery Date',
    'version': '19.0.1.0.0',
    'category': 'Website/eCommerce',
    'summary': 'Let customers check delivery availability and estimated delivery date by pincode on the product page',
    'description': """
Pincode Delivery Checker & Estimated Delivery Date — by Technical Rajni
=========================================================================
Add a "Check Delivery" widget on your product pages so customers can
instantly know if you deliver to their area, and when to expect it.

Features:
- Pincode input + "Check" button on the product page
- Maintain a serviceable pincode database (city, state, COD availability, delivery days)
- Instant AJAX check without reloading the page
- Estimated delivery date calculation (skips Sundays)
- COD availability shown per pincode
- Manage pincodes from Website > eCommerce > Delivery Pincodes
- Import pincodes in bulk via standard CSV import
    """,
    'author': 'Technical Rajni',
    'website': 'https://www.technicalrajni.com',
    'license': 'OPL-1',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_pincode_views.xml',
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'tr_pincode_delivery_checker/static/src/css/pincode_checker.css',
            'tr_pincode_delivery_checker/static/src/js/pincode_checker.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 15.00,
    'currency': 'USD',
}
