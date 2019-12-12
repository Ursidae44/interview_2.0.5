import json
from in_database.db import get_db


def test_create_appointment(client):
    rv = client.post('/appointments',
                     data=json.dumps(dict(doctor_id=0, location_id=1, time='2019-12-11 10:00:00')),
                     content_type='application/json')

    assert rv.status_code == 200

    data = json.loads(rv.data)
    assert data['id'] == 1


def test_create_appointment_invalid_doctor(client):
    # If the doctor does not exist
    rv = client.post('/appointments',
                     data=json.dumps(dict(doctor_id=9, location_id=1, time='2019-12-11 10:00:00')),
                     content_type='application/json')

    assert rv.status_code == 400

    data = json.loads(rv.data)
    assert data['error_detail'] == "That doctor doesn't exist"


def test_get_all_appointments(client):
    rv = client.get('/appointments')
    assert rv.status_code == 200

    # Can't guarantee order, so test that we get the expected count and fields seem to make sense
    data = json.loads(rv.data)
    assert len(data) == 1
    for field in ['id', 'doctor_id', 'location_id', 'appointment_time']:
        assert field in data[0]


def test_cancel_appointment(client, app):
    rv = client.delete('appointments/0')
    assert rv.status_code == 204

    # Check if really deleted
    with app.app_context():
        cursor = get_db().cursor()
        result = cursor.execute(
            'SELECT * FROM appointments where id = ?',
            (0,)
        ).fetchone()
        cursor.close()

        assert result is None


def test_cancel_appointment_does_not_exist(client):
    rv = client.delete('/appointments/999')
    assert rv.status_code == 404

    data = json.loads(rv.data)
    assert data['error_detail'] == 'Appointment not found'
