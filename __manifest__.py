# -*- coding: utf-8 -*-
###############################################################################
#
#    ITL Bangladesh Limited
#
###############################################################################
{
    'name': "User Friendly Automatically Database Backup To Local Server, Remote Server,"
            "Google Drive, Dropbox, Onedrive, Nextcloud and Amazon S3",
    'version': '16.0.6.0.2',
    'live_test_url': 'https://youtu.be/Q2yMZyYjuTI',
    'category': 'Extra Tools',
    'summary': 'Odoo Database Backup, Automatic Backup, Database Backup, Automatic Backup,Database auto-backup, odoo backup'
               'google drive, dropbox, nextcloud, amazon S3, onedrive or '
               'remote server, Odoo17, Backup, Database, Odoo Apps',
    'description': 'This module has been developed for creating database '
                   'backups automatically and store it to the different '
                   'locations,database backup, backup, Google Drive, Dropbox, Onedrive, Nextcloud, Amazon S3, automatic backup',
    'author': "ITL Bangladesh Limired",
    'maintainer': 'Md. Aminul Islam',
    'company': 'ITL-Gorup.com',
    'website': "https://www.itl-group.com",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
        'views/db_backup_configure_views.xml',
        'wizard/dropbox_auth_code_views.xml',
    ],
    'external_dependencies': {
        'python': ['dropbox', 'pyncclient', 'boto3', 'nextcloud-api-wrapper','paramiko']},
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
