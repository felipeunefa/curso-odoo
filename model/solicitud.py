# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class solicitud(osv.osv):
    _name ='co.solicitud'
    _description= 'CO Solicitud'
    
    _columns={
    'code':fields.char('Codigo'),
    'suscriptor_id':fields.many2one('co.suscriptor','Afiliado'),
    'multimedia_id':fields.many2one('co.multimedia','Multimendia'),
    'medio_id':fields.many2one('co.tipo.medio','Tipo de Medio'),
    'tienda_id':fields.many2one('co.tiendas','Tienda'),
    'requested_date':fields.date('Fecha Solicitada'),
    'qty_days':fields.integer('Duración (en Dias)'),
    }
    
    
solicitud()
