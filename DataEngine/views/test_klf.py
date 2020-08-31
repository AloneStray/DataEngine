from flask import Blueprint, request, Response, render_template, session, jsonify, redirect, url_for
#from PIL import Image,ImageDraw,ImageFont

testObj = Blueprint("test", __name__)
@testObj.route('/')
def Index():
    return "hello world"

@testObj.route('/add')
def add():
    return "add"








