from tugas1 import db
from . import bp
from ..models import DataProdi
# import jsonify
from flask import request,jsonify



@bp.route("/get-prodi")
def get_prodi():
    try:
        id = request.args.get('id', None)
        kode_prodi = request.args.get('kode_prodi', None)
        nama_prodi = request.args.get('nama_prodi', None)


        filters = {
            key: value
            for key, value in (
                ('id', id),
                ('kode_prodi', kode_prodi),
                ('nama_prodi', nama_prodi)
            )
            if value is not None
        }

        filtered_prodis = DataProdi.query.filter(
            *[getattr(DataProdi, key) == value for key, value in filters.items()]
        )

        prodi_list = [
            {
                'id': prodi.id,
                'kode_prodi': prodi.kode_prodi,
                'nama_prodi': prodi.nama_prodi
            }
            for prodi in filtered_prodis
        ]

        if not prodi_list:
            return jsonify({'message': 'Data not found'}), 404


        return jsonify(prodi_list),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/create-prodi',methods=['POST'])
def create_prodi():
    try:
        kode_prodi = request.form.get('kode_prodi')
        nama_prodi = request.form.get('nama_prodi')

        if not (kode_prodi and nama_prodi):
            return jsonify({'error': 'No kode_prodi and nama_prodi provided'}), 400

        prodi = DataProdi(kode_prodi=kode_prodi,nama_prodi=nama_prodi)
        db.session.add(prodi)
        db.session.commit()
        return jsonify({'message': 'Dokumen created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@bp.route('/update-prodi',methods=['PUT'])
def update_prodi():
    try:
        id = request.args.get('id')
        kode_prodi = request.form.get('kode_prodi')
        nama_prodi = request.form.get('nama_prodi')

        if not id:
            return jsonify({'error': 'no ID provided'}), 400
        
        try:
            id = int(id)
        except ValueError:
            return jsonify({'error': 'Invalid ID provided'}), 400

        if not any([kode_prodi, nama_prodi]):
            return jsonify({'error': 'At least one of the fields kode_prodi or nama_prodi must be provided'}), 400

        prodi = DataProdi.query.get(id)
        if prodi is None:
            return jsonify({'error': 'Prodi not found'}), 404

        if kode_prodi:
            prodi.kode_prodi = kode_prodi
        if nama_prodi:
            prodi.nama_prodi = nama_prodi

        db.session.commit()
        
        return jsonify({'message': 'Dokumen updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/delete-prodi',methods=['DELETE'])
def delete_prodi():
    try:
        id = request.args.get('id')

        if id is None:
            return jsonify({'error': 'No ID provided'}), 400

        try:
            id = int(id)
        except ValueError:
            return jsonify({'error': 'Invalid ID provided'}), 400

        prodi = DataProdi.query.get(id)
        if prodi is None:
            return jsonify({'error': 'Prodi not found'}), 404

        db.session.delete(prodi)
        db.session.commit() 

        return jsonify({'message': 'Prodi deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    # return "delete prodi"