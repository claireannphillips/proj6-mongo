
import flask
from flask import g
from flask import render_template
from flask import request
from flask import url_for

from bson.objectid import ObjectId

import json
import logging

import sys

# Date handling
import arrow
from dateutil import tz  # For interpreting local times

# Mongo database
from pymongo import MongoClient

import configfrom flask_main import *
import arrow 

import nose



def test_regular():
	'''
	Tests creating certain memos
	'''
    memo = "this is my memo"
    date = "2016-11-01"
    assert(create_helper(memo, date)["text"] == memo)
    assert(create_helper(memo, date)["date"] == arrow.get(date).replace(tzinfo = tz.tzlocal()).isoformat())
    
    
    return None 
    
    
    
    
    
    
    
    
    
    
    