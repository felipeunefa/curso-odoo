# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class lineas_stock(osv.osv):
    _name ='co.lineas.stock'
    _description= 'CO Lineas Stock'
    
    
    _columns={
    'mutimendia_id':flields.many2one('co.multimedia','Multimendia'),
    'medio_id':flields.many2one('co.tipo.medio','tipo de Medio'),
    'tienda_id':flields.many2one('co.tiendas','Tienda'),
    'quantity'fields.integer('Cantidad'),
    }
    
lineas_stock()

class tiendas(osv.osv):
    inherit='co.tiendas'
    
    
    _columns={
    'line_id':flields.one2many('co.lineas.stock','tienda_id','Stock'),
    }
tiendas()
