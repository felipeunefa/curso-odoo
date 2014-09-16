# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tiendas(osv.osv):
    _name ='co.tiendas'
    _description= 'CO Tiendas'
    
    _columns={
    'name':fields.char('Nombre de la tienda'),
    'address':fields.char('Dirección'),
    }
    
tiendas()
