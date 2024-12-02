{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'A Simple library management system',
    'description': """
       Manage books, loans, etc
    """,
    'category': 'Management,Books',
    "author": "Mark Kimathi",
    "license": 'LGPL-3',
    'depends': ['base', 'hr', 'contacts', 'mail',],
    'data': [
        'views/books.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}