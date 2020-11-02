# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import fields
from odoo import models


class Tutor(models.Model):
    _inherit = 'res.users'
    _name = 'res.users'
    
    isTutor = fields.Boolean()
    pupils =  fields.One2many('res.users', 'res_tutor', string ="Pupils")