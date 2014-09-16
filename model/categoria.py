# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class categoria(osv.osv):
    _name ='co.categoria'
    _description= 'CO Categoria'
    
    _columns={
    'name':flields.char('Nombre'),
    'Descripción':flields.text('Descripción'),
    'perent_id':fields.many2one('co.categoria','Padre'),
    'child_id':fields.one2many('co.categoria','perent_id','Sub Categoria'),
    }
    
categoria()
