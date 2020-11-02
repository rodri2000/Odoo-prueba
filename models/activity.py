
from odoo import fields
from odoo import models
from odoo import api
from odoo.exceptions import ValidationError

class Activity(models.Model):
    _name = 'retofinal.activity'
    
    
    date = fields.Date(default=fields.Date.today)
    description = fields.Text()
    duration = fields.Float(digits=(6,2))
    remarks = fields.Char(string="Remarks")
    res_pupil = fields.Many2one('res.users', ondelete='set null', string="Owner")
    
    
    
    
    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration>8:
                raise ValidationError("You can not do so extended activity: %s" % record.duration)
            