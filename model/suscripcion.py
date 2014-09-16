# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
TIPOS=[
    ('oro','Plan Oro'),
    ('plata','Plan Plata'),
    ('Bronce','plan Bronce')
]

class suscripcion(osv.osv):
    _name ='co.suscripcion'
    _description= 'CO Suscripcion'
    
    _columns={
    'code':fields.char('Código'),
    'type':fields.selection(TIPOS,'Tipo de Suscripción',),
    'date_start':fields.date('Inicio de Suscripción'),
    'date_end':fields.date('Fin Suscripción'),
    'active':fields.boolean('Activo'),
    'suscriptor_id':fields.many2one('co.suscriptor','Afiliado'),
    }
    
suscripcion()
