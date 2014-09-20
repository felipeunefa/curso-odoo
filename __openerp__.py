# -*- coding: utf-8 -*-

{
  'name':'curso openerp',
  'description':'Este módulo es para  aprender openerp',
  'author':'Felipe villamizar',
  'version':'dia1',
  'depends':['base','mail', ],
  'data':[
        'security/curso_odoo_security.xml',
        'views/curso_odoo_view.xml',
        'views/multimedia_view.xml',
        'views/tipo_medio_view.xml',
        'views/categoria_view.xml',
        'views/tienda.xml',
        'views/suscriptor.xml',
        'views/suscripcion.xml',
        'views/solicitud.xml',
        'views/tipo_suscripcion.xml',
        'security/menu_sucurity.xml',
        'data/suscripcion_data.xml',
        'security/ir.model.access.csv',
        'report/listado_multimedia_report.xml',
       
  ],
  'demo':[],

}
