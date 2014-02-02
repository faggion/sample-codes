# coding: utf-8
from flask import Blueprint, render_template
import logging, sys, os, traceback
import models
from google.appengine.ext.db import GqlQuery

app = Blueprint('admin_editor', __name__, url_prefix='/admin/editor')

@app.route('', methods=['GET'])
def admin_editor():
    name = 'foo'
    return render_template('admin_editor.html', name=name)

