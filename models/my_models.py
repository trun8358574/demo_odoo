# -*- coding: utf-8 -*-

from odoo import api, models, fields

import datetime


class IssueTicket(models.Model)

  _name = 'issue.ticket'
  _description = 'Issue Ticket'
  _order = 'name desc'
  
  name = fields.Char(string='Ticket Name', required=True)
  text = fields.Text(string='Content', required=True)
  date = fields.Datetime(string='Ticket Date', 
                         default=lambda self: datetime.datetime.now, readonly=True)
  order_number = fields.Integer(string='Order Number', required=True)
  order_id = fields.Integer(string='Order ID Number', compute='_compute_order_id', store=True)
  order_record = fields.Many2one(comodel='sale.order', string='Order', compute='_compute_order', store=True)
  issues = fields.One2many(comodel='issue.issue', 'ticket_id')
  
  
  @api.depends('order_number')
  def _compute_order_id(self):
    order_number = self.order_number
    order = self.env['sale.order'].search(domains=[('order_number', '=', order_number)], limit=1)
    self.order_id = order.id
    
  @api.depends('order_number') 
    def _compute_order(self):
    order_number = self.order_number
    order = self.env['sale.order'].search(domains=[('order_number', '=', order_number)], limit=1)
    self.order_record = order
    
    
 class Issues(model.Models)
    _name = 'issue.issue'
    
    ticket_id = fields.Many2one('issue.ticket', required=True)
    content = fields.Char(string='Content')
    
   
 
