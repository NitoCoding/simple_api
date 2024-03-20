def appconfig(app):
    app.config['SECRET_KEY'] = '9OLWxND4o83j358uK4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/db_repositori'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app