from odoo import models, fields, api

class DailyProduction(models.Model):
    _name = 'daily.production'
    _description = 'Daily Production Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', required=True, default='New')
    date = fields.Date(string='Production Date', required=True, default=fields.Date.today)
    site_id = fields.Many2one('mining.site', string='Mining Site', required=True)
    shift = fields.Selection([
        ('morning', 'Morning Shift (07:00 - 15:00)'),
        ('afternoon', 'Afternoon Shift (15:00 - 23:00)'),
        ('night', 'Night Shift (23:00 - 07:00)'),
    ], string='Shift', required=True)
    supervisor_id = fields.Many2one('hr.employee', string='Shift Supervisor')
    volume_target = fields.Float(string='Target Volume (Ton)')
    volume_actual = fields.Float(string='Actual Volume (Ton)', tracking=True)
    achievement = fields.Float(string='Achievement (%)', compute='_compute_achievement', store=True)
    weather = fields.Selection([
        ('sunny', 'Sunny / Cerah'),
        ('cloudy', 'Cloudy / Berawan'),
        ('rainy', 'Rainy / Hujan'),
        ('heavy_rain', 'Heavy Rain / Hujan Lebat'),
    ], string='Weather Condition')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='Status', default='draft', tracking=True)
    notes = fields.Text(string='Notes / Kendala')

    @api.depends('volume_target', 'volume_actual')
    def _compute_achievement(self):
        for rec in self:
            if rec.volume_target > 0:
                rec.achievement = (rec.volume_actual / rec.volume_target) * 100
            else:
                rec.achievement = 0

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'