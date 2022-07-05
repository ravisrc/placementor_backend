import os


class Config(object):
    SECRET_KEY = 'sasds9wn'
    SQLALCHEMY_DATABASE_URI = "postgres://nnauzcjyivqwzv:6d5bd2bc62ec8ee47a39e258387d9443d90e5381065b2fad625b223f159c6ab5@ec2-107-22-245-82.compute-1.amazonaws.com:5432/d3rgv4n1d09e20"
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    CORS_HEADERS = 'Content-Type'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')