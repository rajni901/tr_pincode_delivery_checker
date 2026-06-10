from odoo import http
from odoo.http import request


class PincodeDeliveryController(http.Controller):

    @http.route('/shop/check_delivery_pincode', type='json', auth='public', website=True)
    def check_delivery_pincode(self, pincode=None, **kwargs):
        pincode = (pincode or '').strip()
        if not pincode:
            return {
                'success': False,
                'message': request.env._('Please enter a pincode.'),
            }

        record = request.env['delivery.pincode'].sudo().search([
            ('pincode', '=', pincode),
            ('company_id', 'in', [request.env.company.id, False]),
        ], limit=1)

        if not record or not record.is_serviceable:
            return {
                'success': True,
                'serviceable': False,
                'message': request.env._('Sorry, we currently do not deliver to pincode %s.', pincode),
            }

        estimated_date = record._get_estimated_delivery_date()

        return {
            'success': True,
            'serviceable': True,
            'city': record.city or '',
            'state': record.state_id.name or '',
            'delivery_days': record.delivery_days,
            'estimated_date': estimated_date.strftime('%d %b %Y'),
            'cod_available': record.cod_available,
            'message': request.env._('Delivery available! Estimated delivery by %s.', estimated_date.strftime('%d %b %Y')),
        }
