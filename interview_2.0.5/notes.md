# Notes # 

### Prioritization / Workflow

1. Finish Doctor CRUD (it was mostly done already!)
1. Add availability model (schedules, doctor_schedules tables)
1. Look at time and realize I don't have time to do schedule CRUD API
1. Freak out and look at requirements
1. Create appointment model (appointments table)
1. Start creating appointment CRUD, beginning with listed requirements
1. Stopped after getting a few appointment methods done and realizing the time

### Trade Offs
* Skipped doctor schedule CRUD, just put in example data for now
* Because there wasn't a location or schedule CRUD, couldn't validate those when making appointments (just assumed valid data for now)

### Assumptions
#### Doctor Schedules:
* Assuming doctors work the same hours each week
* Model is to list day of the week and hours on that day
* Planned on allowing multiple schedules for the same day (to account for lunch blocks: example 8-12, 14-17)

#### Appointments:
* Appointments are made with doctor, location, and time (as in requirements)
* Time is just the start time
* Doctor can't have multiple appointments at the same time
* But this way time can be any hour/minute which may be silly

### Call Outs:
* I'm on a Windows laptop so I created different start and init scripts
* Created a test script just because I was creating scripts (but I usually just use Pycharm's testrunner)
* Refactored to use blueprints (for clarity and ease of having up in multiple windows)

### Next steps:
1. Finish up appointment CRUD API, TODOs in places that need validation from schedule, location API 
1. Create schedule API
1. Create location API
1. Fill in TODOs

### Questions:
* Returning 204 on delete? Or better to return 200?
* Missing required field? Don't want to call out which fields are required?
