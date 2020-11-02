# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import fields
from odoo import models

class FCTPartner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    
    isFCTPartner = fields.Boolean()
    pupils = fields.One2many('res.users', 'res_company', string="Pupils")
    
    