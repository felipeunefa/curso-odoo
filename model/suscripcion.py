# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime
TIPOS=[
    ('oro','Plan Oro'),
    ('plata','Plan Plata'),
    ('Bronce','plan Bronce')
]
class tipo_suscripcion(osv.osv):
    _name ='co.tipo.suscripcion'
    _description= 'CO Tipo Suscripcion'
    _rec_name='name'
    
    
    _columns={
    'name':fields.char('Nombre',required=True),
    'medio_ids':fields.many2many(
            'co.tipo.suscripcion',
            'tipo_suscripcion_medio_rel',
            'tipo_id',
            'medio_id'),
    
    }
    
    _sql_constraints=[
        ('name_uniq',
         'unique(name)',
         'El nombre no se puede repetir'),
         
        ]
        
        
class suscripcion(osv.osv):
    _name ='co.suscripcion'
    _description= 'CO Suscripcion'
    _rec_name='code'
    
    _columns={
    'code':fields.char('Código'),
    'type':fields.many2one('co.tipo.suscripcion',
    'Tipo de Suscripción',required=True),
    'date_start':fields.date('Inicio de Suscripción',required=True),
    'date_end':fields.date('Fin Suscripción',required=True),
    'active':fields.boolean('Activo'),
    'suscriptor_id':fields.many2one('co.suscriptor','Afiliado',required=True),
    }
    
    #
    _defaults={
        'active':True,
        'date_start':datetime.now().strftime('%Y-%m-%d'),
        #'code':lambda self,cr,uid,context:self.pool.get('ir.sequence').get(cr,uid,'seq.suscripcion')
        
    }
    #aquí se convierte el id iterable, por que cuando es un es un entero
    def _ckeck_date(self,cr,uid,ids,context=None):
        if isinstance(ids,(int,long)):
            ids=[ids]
        for s in self.browse(cr,uid,ids,context=context):
            if s.date_end <= s.date_start:
                return False
        return True
    _constraints=[
        (_ckeck_date,'Fecha de inicio debe ser menor',
         ['Fecha de inicio','Fecha fina']),
    ]
    def create(self,cr,uid,values,context=None):
        values.update({
            'code':self.pool.get('ir.sequence').get(cr,uid,'seq.suscripcion')})
        return super(suscripcion,self).create(cr,uid,values,context=context)
    
suscripcion()


class suscriptor(osv.osv):
    _inherit='co.suscriptor'
     
    _columns={
        'suscripcion_ids':fields.one2many(
             'co.suscripcion',
            'suscriptor_id',
        ),
    }
    
suscriptor()
