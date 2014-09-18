# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class lineas_stock(osv.osv):
    _name ='co.lineas.stock'
    _description= 'CO Lineas Stock'
    
    
    _columns={
    'mutimendia_id':fields.many2one('co.multimedia','Multimendia',required=True),
    'medio_id':fields.many2one('co.tipo.medio','tipo de Medio',required=True),
    'tienda_id':fields.many2one('co.tiendas','Tienda'),
    'quantity':fields.integer('Cantidad',required=True),
    }
    def onchange_med(self,cr,uid,ids,medios_id):
        return {
         'value':{
            'mutimendia_id':'',
            'quantity':0,
                }
            }
    def _check_qty(self,cr,uid,ids,context=None):
        if isinstance(ids,(int,long)):
            ids=[ids]
        for s in self.browse(cr,uid,ids,context=context):
            if s.quantity<0:
                return False
        return True
    _constraints=[
        (_check_qty,'La Cantidad no puede ser Negativa',
         ['quantity']),
    ]
    _sql_constraints=[('stock_media_tienda',
                    'unique(medio_id,tienda_id,mutimendia_id)',
                    'no se pueden guardar dos iguales')]
    
lineas_stock()

class tiendas(osv.osv):
    _inherit='co.tiendas'
    
    
    _columns={
    'line_id':fields.one2many('co.lineas.stock','tienda_id','Stock'),
    }
    def unlink(self,cr,uid,ids,context=None):
        if isinstance(ids,(int,long)):
            ids=[ids]
        for t in self.browse(cr,uid,ids,context=context):
            line_ids=[l.id for l in t.line_id]
            if self.pool.get('co.lineas.stock').unlink(cr,uid,line_ids):
                if super(tiendas,self).unlink(cr,uid,t.id,context=context):
                    continue
            return False
        return True
tiendas()
