from tugas1 import db
from . import bp
from ..models import DataDosen,DataProdi
# import jsonify
from flask import request,jsonify

@bp.route("/get-dosen")
def get_dosen():
    # try:
        nip = request.args.get('nip', None)
        nama_lengkap = request.args.get('nama_lengkap', None)
        prodi_id = request.args.get('prodi_id', None)

        filters = {
            key: value
            for key, value in (
                ('nip', nip),
                ('nama_lengkap', nama_lengkap),
                ('prodi_id', prodi_id)
            )
            if value is not None
        }

        filtered_dosens = DataDosen.query.filter(
            *[getattr(DataDosen, key) == value for key, value in filters.items()]
        )

        dosen_list = [
            {
                'nip': dosen.nip,
                'nama_lengkap': dosen.nama_lengkap,
                'prodi': {
                    'id': dosen.prodi.id,
                    'kode_prodi': dosen.prodi.kode_prodi,
                    'nama_prodi': dosen.prodi.nama_prodi
                }
            }
            for dosen in filtered_dosens
        ]

        if not dosen_list:
            return jsonify({'message': 'Data not found'}), 404

        return jsonify(dosen_list)
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500



@bp.route('/create-dosen',methods=['POST'])
def create_dosen():
    try:
        nip = request.form.get('nip')
        nama_lengkap = request.form.get('nama_lengkap')
        prodi_id = request.form.get('prodi_id')

        if not (prodi_id and nama_lengkap and nip):
            return jsonify({'error': 'No nip, prodi_id and nama_lengkap provided'}), 400

        try:
            prodi_id = int(prodi_id)
        except ValueError:
            return jsonify({'error': 'Invalid prodi_id provided'}), 400

        prodi = DataProdi.query.get(prodi_id)
        if prodi is None:
            return jsonify({'error': 'Prodi with the provided prodi_id does not exist'}), 404
        
        dosen = DataDosen.query.get(nip)
        if dosen is not None:
            return jsonify({'error': 'Dosen with the provided NIP already exists'}), 400

        dosen = DataDosen(nip=nip,nama_lengkap=nama_lengkap, prodi_id=prodi_id)
        # print(dosen)
        db.session.add(dosen)
        db.session.commit()
        
        return jsonify({'message': 'Dosen created successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/update-dosen',methods=['PUT'])
def update_dosen():
    try:
        nip = request.args.get('nip')
        nama_lengkap = request.form.get('nama_lengkap')
        prodi_id = request.form.get('prodi_id')

        if not nip:
            return jsonify({'error': 'no nip provided'}), 400

        if not any([nama_lengkap,prodi_id]):
            return jsonify({'error': 'At least one of the fields nama_lengkap or prodi_id must be provided'}), 400

        dosen = DataDosen.query.get(nip)
        if dosen is None:
            return jsonify({'error': 'Dosen not found'}), 404

        if nama_lengkap:
            dosen.nama_lengkap = nama_lengkap
        if prodi_id:
            dosen.prodi_id = prodi_id

        db.session.commit()
        
        return jsonify({'message': 'Dosen Updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/delete-dosen',methods=['DELETE'])
def delete_dosen():
    try:
        nip = request.args.get('nip')

        if not nip:
            return jsonify({'error': 'No nip provided'}), 400

        dosen = DataDosen.query.get(nip)
        if dosen is None:
            return jsonify({'error': 'Dosen not found'}), 404

        db.session.delete(dosen)
        db.session.commit()

        return jsonify({'message': 'Dosen deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
