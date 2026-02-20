from odoo import models, fields, api

class HeavyEquipment(models.Model):
    _name = 'heavy.equipment'
    _description = 'Heavy Equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Equipment Name', required=True)
    code = fields.Char(string='Equipment Code', required=True)
    equipment_type = fields.Selection([
        ('excavator', 'Excavator'),
        ('dump_truck', 'Dump Truck'),
        ('bulldozer', 'Bulldozer'),
        ('drill', 'Drilling Machine'),
        ('crusher', 'Crusher'),
        ('conveyor', 'Conveyor'),
        ('loader', 'Wheel Loader'),
    ], string='Equipment Type', required=True)
    brand = fields.Char(string='Brand')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Year of Manufacture')
    site_id = fields.Many2one('mining.site', string='Mining Site', required=True)
    operator_id = fields.Many2one('hr.employee', string='Operator')
    status = fields.Selection([
        ('operational', 'Operational'),
        ('maintenance', 'Under Maintenance'),
        ('breakdown', 'Breakdown'),
        ('standby', 'Standby'),
    ], string='Status', default='operational', tracking=True)
    last_maintenance = fields.Date(string='Last Maintenance Date')
    next_maintenance = fields.Date(string='Next Maintenance Date')
    notes = fields.Text(string='Notes')