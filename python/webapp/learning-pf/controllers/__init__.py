# coding: utf8
import os, jinja2, ConfigParser, logging

from webapp2_extras import i18n
from webapp2_extras.i18n import lazy_gettext as _

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(['templates'], encoding="utf8"),
    autoescape=True,
    extensions=[
        'jinja2.ext.autoescape',
        'jinja2.ext.with_',
        'jinja2.ext.i18n',
        ],
    )

env.install_gettext_translations(i18n)
