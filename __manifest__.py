# -*- coding: utf-8 -*-
{
    'name': 'Croix-Rouge Tenues',
    'version': '0.1',
    'sequence': 150,
    'category': 'custom',
    'author': 'Croix-Rouge',
    'website': 'http://croix-rouge.fr',
    'depends': [
        'base',
		'web',
    ],
    'data': [
        'view/vetement.xml',
		'view/unite_locale.xml',
		'view/benevole.xml',
		'view/responsable.xml',
		'view/affectation_tenue.xml',
		'view/mission.xml',
		'view/menu.xml',
		'view/theme.xml',
		'security/ir.model.access.csv',
    ],
    'test': [
    ],
    'demo': [
    ],
    'js': [
    ],
    'qweb': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
