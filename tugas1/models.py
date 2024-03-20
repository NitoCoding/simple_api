
from flask_sqlalchemy import SQLAlchemy
from tugas1 import db

class DataDokuman(db.Model):
    __tablename__ = 'data_dokumen'

    id = db.Column(db.Integer, primary_key=True)
    nip = db.Column(db.ForeignKey('data_dosen.nip'), index=True)
    type_dokumen = db.Column(db.Enum('file', 'url'), nullable=False)
    nama_dokumen = db.Column(db.String(255))
    nama_file = db.Column(db.String(255))

    data_dosen = db.relationship('DataDosen', primaryjoin='DataDokuman.nip == DataDosen.nip', backref='data_dokumen')



class DataDosen(db.Model):
    __tablename__ = 'data_dosen'

    nip = db.Column(db.String(30), primary_key=True)
    nama_lengkap = db.Column(db.String(100))
    prodi_id = db.Column(db.ForeignKey('data_prodi.id'), index=True)

    prodi = db.relationship('DataProdi', primaryjoin='DataDosen.prodi_id == DataProdi.id', backref='data_dosens')



class DataProdi(db.Model):
    __tablename__ = 'data_prodi'

    id = db.Column(db.Integer, primary_key=True, index=True)
    kode_prodi = db.Column(db.String(5))
    nama_prodi = db.Column(db.String(100))
