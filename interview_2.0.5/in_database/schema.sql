-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS doctor_locations;
DROP TABLE IF EXISTS schedules;
DROP TABLE IF EXISTS doctor_schedules;

CREATE TABLE doctors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL
);

CREATE TABLE locations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT NOT NULL
);

CREATE TABLE doctor_locations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  doctor_id INTEGER NOT NULL,
  location_id INTEGER NOT NULL,
  FOREIGN KEY (doctor_id) REFERENCES doctors (id),
  FOREIGN KEY (location_id) REFERENCES locations (id)
);

CREATE TABLE schedules (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  day INTEGER NOT NULL CHECK(day >= 0 and day <= 7),
  start_hour INTEGER NOT NULL CHECK(start_hour >= 0 and start_hour <= 23),
  end_hour INTEGER NOT NULL CHECK(end_hour >= 0 and start_hour <= 23)
);

CREATE TABLE doctor_schedules (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  doctor_id INTEGER NOT NULL,
  schedule_id INTEGER NOT NULL,
  FOREIGN KEY (doctor_id) REFERENCES doctors (id),
  FOREIGN KEY (schedule_id) REFERENCES schedules (id)
);


INSERT INTO doctors(id, first_name, last_name) VALUES (0, 'John', 'Doe');
INSERT INTO doctors(id, first_name, last_name) VALUES (1, 'Jane', 'Smith');

INSERT INTO locations(id, address) VALUES (0, '123 Main St');
INSERT INTO locations(id, address) VALUES (1, '456 Central St');

INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (0, 0, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (1, 1, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (2, 1, 1);

INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (0, 1, 9, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (1, 2, 9, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (2, 3, 9, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (3, 4, 9, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (4, 5, 9, 17);

INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (5, 1, 13, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (6, 2, 13, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (7, 3, 13, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (8, 4, 13, 17);
INSERT INTO schedules(id, day, start_hour, end_hour) VALUES (9, 5, 13, 17);

INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(0, 0, 0);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(1, 0, 1);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(2, 0, 2);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(3, 0, 3);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(4, 0, 4);

INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(5, 1, 5);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(6, 1, 6);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(7, 1, 7);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(8, 1, 8);
INSERT INTO doctor_schedules(id, doctor_id, schedule_id) VALUES(9, 1, 9);

