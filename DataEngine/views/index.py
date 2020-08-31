from flask import Blueprint, request, Response, render_template, session, jsonify, redirect, url_for
#from PIL import Image,ImageDraw,ImageFont

indexObj = Blueprint("index1", __name__)
@indexObj.route('/')
def Index():
    #
    return render_template('Index.html')

@indexObj.route('/login_welcome')
def login_welcome():
    return  render_template('login_welcome.html')