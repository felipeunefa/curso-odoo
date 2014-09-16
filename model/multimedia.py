# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
    _name ='co.multimedia'
    _description= 'CO Multimedia'
    
    _columns={
    'cade':fields.char('Código'),
    'title':fields.char('Titulo'),
    'release_date':fields.date('Fecha de Publicación'),
    'categoria_id':fields.many2one('co.categoria','Categoria'),
    'medios_ids':fields.many2many(
        'co.tipo.medio',
        'co_muntimedia_tipo_medio_rel',
        'multimedia_id',
        'medio_id'),
    }
    
multimedia()
