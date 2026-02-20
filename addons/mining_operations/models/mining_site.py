from odoo import models, fields, api

class MiningSite(models.Model):
    _name = 'mining.site'
    _description = 'Mining Site'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Site Name', required=True, tracking=True)
    code = fields.Char(string='Site Code', required=True)
    location = fields.Char(string='Location', required=True)
    mineral_type = fields.Selection([
        ('coal', 'Coal / Batubara'),
        ('gold', 'Gold / Emas'),
        ('nickel', 'Nickel / Nikel'),
        ('tin', 'Tin / Timah'),
        ('copper', 'Copper / Tembaga'),
        ('bauxite', 'Bauxite / Bauksit'),
    ], string='Mineral Type', required=True, tracking=True)
    area_hectare = fields.Float(string='Area (Hectare)')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ], string='Status', default='active', tracking=True)
    responsible_id = fields.Many2one('hr.employee', string='Site Manager')
    date_start = fields.Date(string='Operation Start Date')
    notes = fields.Text(string='Notes')
    equipment_ids = fields.One2many('heavy.equipment', 'site_id', string='Equipment')
    production_ids = fields.One2many('daily.production', 'site_id', string='Production Records')

    equipment_count = fields.Integer(compute='_compute_equipment_count', string='Equipment Count')
    production_count = fields.Integer(compute='_compute_production_count', string='Production Count')

    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        for rec in self:
            rec.equipment_count = len(rec.equipment_ids)

    @api.depends('production_ids')
    def _compute_production_count(self):
        for rec in self:
            rec.production_count = len(rec.production_ids)