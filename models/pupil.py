# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import fields
from odoo import models

class Pupil(models.Model):
    _inherit = 'res.users'
    _name = 'res.users'
    
    
    isPupil = fields.Boolean()
    res_tutor = fields.Many2one('res.users',ondelete='set null', string="Responsible tutor")
    activity = fields.One2many('retofinal.activity', 'res_pupil', string="Activities")  
    res_company = fields.Many2one('res.partner',ondelete='set null', string="Responsible company")
        