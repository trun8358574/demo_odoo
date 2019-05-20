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
  order_name = fields.Integer(string='Order Name', required=True)
  order_id = fields.Integer(string='Order ID Number', compute='_compute_order_id', store=True)
  order_record = fields.Many2one(comodel='sale.order', string='Order', compute='_compute_order', store=True)
  issues = fields.One2many(comodel='issue.issue', 'ticket_id')
  
  
  @api.depends('order_name')
  def _compute_order_id(self):
    order_name = self.order_name
    order = self.env['sale.order'].search(domains=[('name', '=', order_name)], limit=1)
    self.order_id = order.id
    
  @api.depends('order_name') 
    def _compute_order(self):
    order_name = self.order_name
    order = self.env['sale.order'].search(domains=[('name', '=', order_name)], limit=1)
    self.order_record = order
    
    
 class Issues(model.Models)
    _name = 'issue.issue'
    
    ticket_id = fields.Many2one('issue.ticket', required=True)
    content = fields.Char(string='Content')
    
   
 
