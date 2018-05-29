'''
Created on May 30, 2016

@author: Michael
'''

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:flask_Test@flasktest.ctpmzyz1nhfs.us-west-1.rds.amazonaws.com:3306/flasktestdb'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://HostPostTest:XXX@hostpost.ctpmzyz1nhfs.us-west-1.rds.amazonaws.com:3306/hostpost?charset=utf8mb4'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'XXX'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
MYSQL_CHARSET = 'utf8mb4'