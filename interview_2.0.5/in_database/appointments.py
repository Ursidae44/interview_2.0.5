from flask import Blueprint, jsonify, request

from in_database import db
from in_database import doctors

bp = Blueprint('appointments', __name__, url_prefix='/appointments')


def get_appointment(appointment_id):
    """
    Helper method to get a single appointment
    :param appointment_id: id of appointment
    :return: appointment row
    """
    cursor = db.get_db().cursor()

    result = cursor.execute(
        'SELECT id, doctor_id, location_id, appointment_time '
        'FROM appointments '
        'WHERE id = ?',
        (appointment_id,)
    ).fetchone()
    cursor.close()

    return result


@bp.route('', methods=['POST'])
def add_appointment():
    """
    Add an appointment
    :param doctor_id: Doctor's id
    :param location_id: Location id
    :param time: Time - datetime string default iso8601 format

    :return: the id of the newly created appointment
    """
    req_data = request.get_json()

    try:
        doctor_id = req_data['doctor_id']
        location_id = req_data['location_id']
        time = req_data['time']
    except KeyError:
        return jsonify({'error_detail': 'Missing required field'}), 400

    # Validate doctor exists
    doctor = doctors.get_doctor(doctor_id)
    if doctor is None:
        return jsonify({'error_detail': "That doctor doesn't exist"}), 400

    # TODO: Validate doctor at location
    # TODO: Validate time in doctor's schedule
    # TODO: Validate time slot not filled

    # Create appointment
    try:
        cursor = db.get_db().cursor()

        cursor.execute(
            'INSERT INTO appointments (doctor_id, location_id, appointment_time)'
            'VALUES (?, ?, ?)',
            (doctor_id, location_id, time)
        )

        appointment_id = cursor.lastrowid

        cursor.close()
        db.get_db().commit()
    except Exception as e:
        return jsonify({'error_detail': e.message}), 400

    return jsonify({'id': appointment_id}), 200


@bp.route('', methods=['GET'])
def list_appointments():
    """
    Get all appointments
    :return: List of appointment rows
    """
    cursor = db.get_db().cursor()

    result = cursor.execute(
        'SELECT id, doctor_id, location_id, appointment_time '
        'FROM appointments'
    ).fetchall()

    appointments = [dict(row) for row in result]

    cursor.close()

    return jsonify(appointments), 200


@bp.route('<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    """
    Cancel / delete an appointment
    :param appointment_id: id of appointment
    :return: 204 if successful
    """

    # Validate appointment exists
    appointment = get_appointment(appointment_id)
    if appointment is None:
        return jsonify({'error_detail': 'Appointment not found'}), 404

    # Delete appointment
    try:
        cursor = db.get_db().cursor()

        cursor.execute(
            'DELETE from appointments WHERE id = ?',
            (appointment_id,)
        )

        cursor.close()
        db.get_db().commit()
        return '', 204
    except Exception as e:
        return jsonify({'error_detail': e.message}), 400
