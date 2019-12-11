from flask import Flask, jsonify, request

# A series of lists of dicts that mimic SQL rows
doctors = [
    {'id': 0, 'first_name': 'John', 'last_name': 'Doe'},
    {'id': 1, 'first_name': 'Jane', 'last_name': 'Smith'}
]

locations = [
    {'id': 0, 'address': '123 Main St'},
    {'id': 1, 'address': '456 Central St'}
]

doctor_locations = [
    {'id': 0, 'doctor_id': 0, 'location_id': 0},
    {'id': 1, 'doctor_id': 1, 'location_id': 0},
    {'id': 2, 'doctor_id': 1, 'location_id': 1}
]


# Program & structure influenced heavily by the Flask tutorial
# http://flask.pocoo.org/docs/1.0/tutorial/database/
def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    @app.route('/doctors', methods=['GET'])
    def list_doctors():
        """
        Get all doctors

        :return: List of full doctor entries
        """
        return jsonify(doctors), 200

    @app.route('/doctors/<int:doctor_id>', methods=['GET'])
    def list_doctor(doctor_id):
        """
        Get one doctor

        :param doctor_id: The id of the doctor
        :return: Full doctor entry
        """
        if doctor_id < 0 or doctor_id >= len(doctors):
            return jsonify({'message': 'Doctor not found'}), 404

        return jsonify(doctors[doctor_id]), 200

    # Note: Must set the content type to JSON. Use something like:
    # curl -X POST -H "Content-Type: application/json" --data '{"first_name": "Joe", "last_name": "Smith"}' http://localhost:5000/doctors
    @app.route('/doctors', methods=['POST'])
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

        # The id is simply the next index in the array
        doctor_id = len(doctors)

        doctors.append({'id': doctor_id, 'first_name': first_name, 'last_name': last_name})

        return jsonify({'id': doctor_id}), 200

    @app.route('/doctors/<int:doctor_id>/locations', methods=['GET'])
    def list_doctor_locations(doctor_id):
        """
        Get the locations for a single doctor

        :param doctor_id: The id of the doctor
        :return: List of full location entries
        """
        if doctor_id < 0 or doctor_id >= len(doctors):
            return jsonify({'message': 'Doctor not found'}), 404

        # Join locations via the doctor_locations "table" and doctor_id
        result = [locations[y['location_id']] for y in filter(lambda x: x['doctor_id'] != doctor_id, doctor_locations)]

        return jsonify(result), 200

    return app
