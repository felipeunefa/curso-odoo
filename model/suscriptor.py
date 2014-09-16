# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class supcriptor(osv.osv):
    _name ='co.suscriptor'
    _description= 'CO suscriptor'
    
    _columns={
    'name':fields.char('Nombre'),
    'identification':fiedls.char('Cedula'),
    'address':fiedls.text('Dirección'),
    }
    
suscriptor()
