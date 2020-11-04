from odoo import models, fields


class CreateBatch(models.Model):
    _name = 'lab.batch'
    _description = "lab.batch"

    batch_name = fields.Char(string="Name", required=True, help="batch name")
    test_record = fields.Many2many('lab.request')


    # def action_done(self):
    #    pass
