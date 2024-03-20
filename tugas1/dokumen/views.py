from tugas1 import db
from . import bp
from ..models import DataDosen,DataDokuman
# import jsonify
from flask import request,jsonify

from flask import request, jsonify
from flask import request, jsonify

@bp.route("/get-dokumen")
def get_dokumen():
    try:
        id = request.args.get('id', None)
        nip = request.args.get('nip', None)
        type_dokumen = request.args.get('type_dokumen', None)
        nama_dokumen = request.args.get('nama_dokumen', None)
        nama_file = request.args.get('nama_file', None)

        filters = {
            key: value
            for key, value in (
                ('id', id),
                ('nip', nip),
                ('type_dokumen', type_dokumen),
                ('nama_dokumen', nama_dokumen),
                ('nama_file', nama_file)
            )
            if value is not None
        }

        filtered_dokumens = DataDokuman.query.filter(
            *[getattr(DataDokuman, key) == value for key, value in filters.items()]
        )

        dokumen_list = [
            {
                'id': dokumen.id,
                'dosen': {
                    'nama_lengkap': dokumen.data_dosen.nama_lengkap,
                    'nip': dokumen.data_dosen.nip
                },
                'type_dokumen': dokumen.type_dokumen,
                'nama_dokumen': dokumen.nama_dokumen,
                'nama_file': dokumen.nama_file
            }
            for dokumen in filtered_dokumens
        ]

        if not dokumen_list:
            return jsonify({'message': 'Data not found'}), 404

        return jsonify(dokumen_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/create-dokumen',methods=['POST'])
def create_dokumen():
    try:
        nip = request.form.get('nip')
        type_dokumen = request.form.get('type_dokumen')
        nama_dokumen = request.form.get('nama_dokumen')
        nama_file = request.form.get('nama_file')

        if not (nip and type_dokumen and nama_dokumen and nama_file):
            return jsonify({'error': 'NIP, type_dokumen, nama_dokumen and nama_file are required'}), 400

        dosen = DataDosen.query.filter_by(nip=nip).first()
        if dosen is None:
            return jsonify({'error': 'DataDosen with the provided NIP does not exist'}), 404

        dokumen = DataDokuman(nip=nip, type_dokumen=type_dokumen, nama_dokumen=nama_dokumen, nama_file=nama_file)
        db.session.add(dokumen)
        db.session.commit()
        
        return jsonify({'message': 'Dokumen created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/update-dokumen',methods=['PUT'])
def update_dokumen():
    try:
        id = request.args.get('id')
        nip = request.form.get('nip')
        type_dokumen = request.form.get('type_dokumen')
        nama_dokumen = request.form.get('nama_dokumen')
        nama_file = request.form.get('nama_file')

        if not id:
            return jsonify({'error': 'No ID provided'}), 400
        
        try:
            id = int(id)
        except ValueError:
            return jsonify({'error': 'Invalid ID provided'}), 400
        
        if not any([nip, type_dokumen, nama_dokumen,nama_file]):
            return jsonify({'error': 'At least one of the fields nip, type_dokumen, nama_dokumen and nama_file must be provided'}), 400
        
        if type_dokumen not in ['file', 'url'] and type_dokumen is not None:
            return jsonify({'error': 'Type dokumen harus "file" atau "url"'}), 400

        dokumen = DataDokuman.query.get(id)
        if dokumen is None:
            return jsonify({'error': 'Dokumen not found'}), 404

        if nip:
            dokumen.nip = nip
        if type_dokumen:
            dokumen.type_dokumen = type_dokumen
        if nama_dokumen:
            dokumen.nama_dokumen = nama_dokumen
        if nama_file:
            dokumen.nama_file = nama_file

        db.session.commit()
        
        return jsonify({'message': 'Dokumen updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/delete-dokumen',methods=['DELETE'])
def delete_dokumen():
    try:
        id = request.args.get('id')

        if not id:
            return jsonify({'error': 'No ID provided'}), 400
        
        try:
            id = int(id)
        except ValueError:
            return jsonify({'error': 'Invalid ID provided'}), 400

        dokumen = DataDokuman.query.get(id)
        if dokumen is None:
            return jsonify({'error': 'Dokumen not found'}), 404

        db.session.delete(dokumen)
        db.session.commit()

        return jsonify({'message': 'Dokumen deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
