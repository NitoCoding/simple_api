from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import appconfig

app = Flask(__name__,static_url_path='/api')
app = appconfig(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    print('test')
    return 'asdqweas'

from .prodi import bp as bp_prodi
app.register_blueprint(bp_prodi,url_prefix = '/prodi')

from .dosen import bp as bp_dosen
app.register_blueprint(bp_dosen,url_prefix = '/dosen')

from .dokumen import bp as bp_dokumen
app.register_blueprint(bp_dokumen,url_prefix = '/dokumen')

