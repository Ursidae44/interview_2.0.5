-- Everything here will get rolled back at the end of a test run
-- Populate everything with known data

DELETE FROM doctors;
INSERT INTO doctors(id, first_name, last_name) VALUES (0, 'Testy', 'McTestFace');
INSERT INTO doctors(id, first_name, last_name) VALUES (1, 'Julius', 'Hibbert');

DELETE FROM locations;
INSERT INTO locations(id, address) VALUES (0, '1 Park St');
INSERT INTO locations(id, address) VALUES (1, '2 University Ave');

DELETE FROM doctor_locations;
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (0, 0, 0);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (1, 0, 1);
INSERT INTO doctor_locations(id, doctor_id, location_id) VALUES (2, 1, 1);

DELETE FROM schedules;
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

DELETE FROM doctor_schedules;
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

DELETE FROM appointments;
INSERT INTO appointments(id, doctor_id, location_id, appointment_time)
  VALUES (0, 0, 0, '2019-12-11 09:00:00');