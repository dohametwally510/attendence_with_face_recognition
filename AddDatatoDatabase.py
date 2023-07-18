import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-597f0-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')



data = {
    "234789":
        {
            "name":"Mohamed",
            "major":"AI" ,
            "starting_year":2022,
            "total_attendance": 2,
            "standing":"G",
            "year":3,
            "last_attendance_time":"2022-12-11 00:54:34"
        },
    "235679":
        {
            "name": "Mohaned",
            "major": "Open source",
            "starting_year": 2017,
            "total_attendance": 2,
            "standing": "G",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"254318":
        {
            "name": "Manar",
            "major": ".Net",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"314526":
        {
            "name": "Amira",
            "major": ".Python",
            "starting_year": 2020,
            "total_attendance": 3,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"564312":
        {
            "name": "Adel",
            "major": "AI",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"653189":
        {
            "name": "Alaa",
            "major": "Front end",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"2654789":
        {
            "name": "Mahmoud",
            "major": "Flutter",
            "starting_year": 2018,
            "total_attendance": 5,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-8-9 00:54:34"
        },
"731901":
        {
            "name": "Daren",
            "major": "Graphic",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-10-3 00:54:34"
        },
"764904":
        {
            "name": "Doha",
            "major": "AI",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"784329":
        {
            "name": "Bassant",
            "major": "AI & ML",
            "starting_year": 2022,
            "total_attendance": 1,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"843168":
        {
            "name": "Ahmed",
            "major": "IT",
            "starting_year": 2020,
            "total_attendance": 1,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"852741":
        {
            "name": "Sendi",
            "major": "Motion",
            "starting_year": 2023,
            "total_attendance": 1,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"954168":
        {
            "name": "yousef",
            "major": "Electicain",
            "starting_year": 2015,
            "total_attendance": 2,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"963852":
        {
            "name": "Omer",
            "major": "Bussines",
            "starting_year": 2014,
            "total_attendance": 2,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}


for key ,value in data.items():
    ref.child(key).set(value)