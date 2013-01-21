# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, flash
from flask import Blueprint

shop_cart = Blueprint('shop_cart', __name__)

@shop_cart.route('/', methods=['GET'])
def index():
    T = {'name':'hello'}
    return render_template('shop_cart.html',T=T)
    
