class PurchaseOrder(models.Model):
    _name = 'procure.purchase.order'
    _description = 'Procure to Pay - Purchase Order'

    name = fields.Char(string="Order Reference", required=True)
    vendor_id = fields.Many2one('res.partner', string="Vendor", required=True)
    order_date = fields.Date(string="Order Date", default=fields.Date.today)
    total_amount = fields.Float(string="Total Amount", compute="_compute_total")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string="Status", default='draft')

    @api.depends('order_line_ids.price_total')
    def _compute_total(self):
        for record in self:
            record.total_amount = sum(line.price_total for line in record.order_line_ids)
