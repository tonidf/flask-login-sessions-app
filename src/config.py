class Config():
    SECRET_KEY= '0496e42bba9162479b5de73396632e2b2de9f543dc62ab586c891c7436a066cc'

class DevelopmentConfig(Config):

    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='Aleixgarcia'
    MYSQL_DB='flask_login_2024_2025'

class ProductionConfig(Config):

    DEBUG=False
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='Aleixgarcia'
    MYSQL_DB='flask_login_2024_2025'


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}