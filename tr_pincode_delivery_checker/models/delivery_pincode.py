from datetime import date, timedelta

from odoo import api, fields, models


class DeliveryPincode(models.Model):
    _name = 'delivery.pincode'
    _description = 'Serviceable Delivery Pincode'
    _order = 'pincode'
    _rec_name = 'pincode'

    pincode = fields.Char(string='Pincode', required=True, index=True)
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one(
        'res.country', string='Country',
        default=lambda self: self.env.ref('base.in', raise_if_not_found=False),
    )
    is_serviceable = fields.Boolean(string='Serviceable', default=True)
    cod_available = fields.Boolean(string='COD Available', default=True)
    delivery_days = fields.Integer(string='Delivery Days', default=5, required=True)
    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company,
    )
    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            'pincode_company_uniq',
            'unique (pincode, company_id)',
            'A pincode entry already exists for this company.',
        ),
    ]

    def _get_estimated_delivery_date(self):
        """Return the estimated delivery date, skipping Sundays."""
        self.ensure_one()
        current_date = date.today()
        days_added = 0
        while days_added < self.delivery_days:
            current_date += timedelta(days=1)
            if current_date.weekday() != 6:  # Sunday
                days_added += 1
        return current_date
