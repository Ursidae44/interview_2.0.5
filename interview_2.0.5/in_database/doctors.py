from flask import Blueprint, jsonify, request

from in_database import db

bp = Blueprint('doctors', __name__, url_prefix='/doctors')


def get_doctor(doctor_id):
    """
    Helper to get doctor
    :param doctor_id: id of the doctor
    :return: doctor row
    """
    cursor = db.get_db().cursor()

    result = cursor.execute(
        'SELECT id, first_name, last_name '
        'FROM doctors '
        'WHERE id = ?',
        (doctor_id,)
    ).fetchone()
    cursor.close()

    return result


@bp.route('', methods=['GET'])
def list_doctors():
    """
    Get all doctors

    :return: List of full doctor rows
    """
    cursor = db.get_db().cursor()

    result = cursor.execute(
        'SELECT id, first_name, last_name '
        'FROM doctors'
    ).fetchall()

    doctors = [dict(row) for row in result]

    cursor.close()

    return jsonify(doctors), 200


@bp.route('<int:doctor_id>', methods=['GET'])
def list_doctor(doctor_id):
    """
    Get one doctor

    :param doctor_id: The id of the doctor
    :return: Full doctor row
    """
    result = get_doctor(doctor_id)

    if result is None:
        return jsonify({'error_detail': 'Doctor not found'}), 404

    doctor = dict(result)

    return jsonify(doctor), 200


# Note: Must set the content type to JSON
@bp.route('<int:doctor_id>', methods=['POST'])
def update_doctor(doctor_id):
    """
    Update doctor information

    :param doctor_id: The id of the doctor
    :param (payload) first_name: First name of the doctor
    :param (payload) last_name: Last name of the doctor
    :return: 204 if doctor updated
    """
    req_data = request.get_json()

    try:
        first_name = req_data['first_name']
        last_name = req_data['last_name']
    except KeyError:
        return jsonify({'error_detail': 'Missing required field'}), 400

    try:
        cursor = db.get_db().cursor()
        cursor.execute(
            'UPDATE doctors SET first_name = ?, last_name = ?'
            ' WHERE id = ?',
            (first_name, last_name, doctor_id)
        )

        cursor.close()
        db.get_db().commit()
        return '', 204
    except Exception as e:
        return jsonify({'error_detail': e.message}), 400


# Note: Must set the content type to JSON. Use something like:
# curl -X POST -H "Content-Type: application/json" --data '{"first_name": "Joe", "last_name": "Smith"}' http://localhost:5000/doctors
@bp.route('', methods=['POST'])
def add_doctor():
    """
    Create a doctor

    :param first_name: The doctor's first name
    "param last_name: The doctor's last name

    :return: The id of the newly created doctor
    """
    req_data = request.get_json()

    try:
        first_name = req_data['first_name']
        last_name = req_data['last_name']
    except KeyError:
        return jsonify({'error_detail': 'Missing required field'}), 400

    try:
        cursor = db.get_db().cursor()

        cursor.execute(
            'INSERT INTO doctors (first_name, last_name) '
            'VALUES (?, ?)',
            (first_name, last_name)
        )

        doctor_id = cursor.lastrowid

        cursor.close()
        db.get_db().commit()
    except Exception as e:
        return jsonify({'error_detail': e.message}), 400

    return jsonify({'id': doctor_id}), 200


@bp.route('<int:doctor_id>/locations', methods=['GET'])
def list_doctor_locations(doctor_id):
    """
    Get the locations for a single doctor

    :param doctor_id: The id of the doctor
    :return: List of full location rows
    """

    cursor = db.get_db().cursor()

    result = cursor.execute(
        'SELECT l.id, l.address '
        'FROM doctor_locations dl '
        'INNER JOIN locations l ON dl.location_id = l.id '
        'WHERE dl.doctor_id = ?',
        (doctor_id,)
    ).fetchall()

    # See https://medium.com/@PyGuyCharles/python-sql-to-json-and-beyond-3e3a36d32853
    locations = [dict(zip([key[0] for key in cursor.description], row)) for row in result]

    cursor.close()

    return jsonify(locations), 200


@bp.route('<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    """
    Delete doctor
    :param doctor_id:  The id of the doctor
    :return: 204 if successful
    """
    doctor = get_doctor(doctor_id)
    if doctor is None:
        return jsonify({'error_detail': 'Doctor not found'}), 404

    try:
        cursor = db.get_db().cursor()

        cursor.execute(
            'DELETE from doctors WHERE id = ?',
            (doctor_id,)
        )

        cursor.close()
        db.get_db().commit()
        return '', 204
    except Exception as e:
        return jsonify({'error_detail': e.message}), 400
