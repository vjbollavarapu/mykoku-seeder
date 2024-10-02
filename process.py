import json
import requests
import random
from datetime import datetime
import os

import logging

log_directory = 'logs'

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
log_filepath = os.path.join(log_directory, log_filename)

def log_message(message):
    with open(log_filepath, 'a') as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

# logging.basicConfig(filename='process.log', level=log_message, format='%(asctime)s - %(levelname)s - %(message)s')

# URL for API endpoint
#url = 'http://staging-api.mykokurikulum.com/api/v1/'
#BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsInVubSI6Im5lcnNlZHV0ZWNoIiwiZXhwIjoxNzI0ODQxMzYwfQ.jnzxXzI84lcJSUtxV1vTRsB5TmzNStwsos--pWWt1Fc'
url = 'http://localhost:8000/api/v1'
BEARER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEsInVubSI6Im5lcnNlZHV0ZWNoIiwiZXhwIjoxNzI0OTQ5NTEwfQ.v7sweoYnqWl3Btm5ZKrvfCuP_yn-1CWnR0HUoE2mN4I'
def get_data(endpoint, id=None, params=None):
    headers = {
        'Authorization': f'{BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }

    try:
        if id is None:
            url_to_call = f'{url}/{endpoint}'
            log_message(f"Getting multiple rows for {endpoint}")
        else:
            url_to_call = f'{url}/{endpoint}/{id}'
            log_message(f"Getting a row for {endpoint} of ID: {id}")
        
        response = requests.get(url_to_call, headers=headers, params=params)
        if response.status_code == 200:
            if id is None:
                log_message(f'Success: {endpoint} - Params: {json.dumps(params,indent=4)} - {response.status_code} - {json.dumps(response.json(), indent=4)}')
            else:
                log_message(f'Success: {endpoint} - {response.status_code} - {json.dumps(response.json(), indent=4)}')
        else:
            log_message(f"Error: {response.status_code}, {json.dumps(response.text, indent=4)}")
    except requests.exceptions.HTTPError as http_err:
        log_message(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        log_message(f"Error occurred: {req_err}")
    except ValueError as json_err:
        log_message(f"Error parsing JSON: {json_err}")


def post_data(endpoint, payload):
    headers = {
        'Authorization': f'{BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(f'{url}/{endpoint}/add', json=payload, headers=headers)
        if response.status_code == 200:
            log_message(f'Success: {endpoint} - {json.dumps(payload, indent=4)} - {response.status_code} - {json.dumps(response.text, indent=4)}')
        else:
            log_message(f"Error: {response.status_code}, {json.dumps(response.text, indent=4)}")
        # log_message(data)
    except requests.exceptions.HTTPError as http_err:
        log_message(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        log_message(f"Error occurred: {req_err}")
    except ValueError as json_err:
        log_message(f"Error parsing JSON: {json_err}")

def post_data_custom(endpoint, payload):
    headers = {
        'Authorization': f'{BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(f'{url}/{endpoint}', json=payload, headers=headers)
        if response.status_code == 200:
            log_message(f'Success: {endpoint} - {json.dumps(payload, indent=4)} - {response.status_code} - {json.dumps(response.text, indent=4)}')
        else:
            log_message(f"Error: {response.status_code}, {json.dumps(response.text, indent=4)}")
        # log_message(data)
    except requests.exceptions.HTTPError as http_err:
        log_message(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        log_message(f"Error occurred: {req_err}")
    except ValueError as json_err:
        log_message(f"Error parsing JSON: {json_err}")


def put_data(endpoint, payload, id):
    headers = {
        'Authorization': f'{BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:

        response = requests.put(f'{url}/{endpoint}/edit/{id}', json=payload, headers=headers)
        if response.status_code == 200:
            log_message(f'Success: {endpoint} - {json.dumps(payload, indent=4)} - {response.status_code} - {json.dumps(response.text, indent=4)}')
        else:
            log_message(f"Error: {response.status_code}, {json.dumps(response.text, indent=4)}")
        # log_message(data)
    except requests.exceptions.HTTPError as http_err:
        log_message(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        log_message(f"Error occurred: {req_err}")
    except ValueError as json_err:
        log_message(f"Error parsing JSON: {json_err}")

def delete_data(endpoint, id):
    headers = {
        'Authorization': f'{BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:

        response = requests.delete(f'{url}/{endpoint}/{id}', headers=headers)
        if response.status_code == 200:
            log_message(f'Success: {endpoint} -  {response.status_code} - {json.dumps(response.text, indent=4)}')
        else:
            log_message(f"Error: {response.status_code}, {json.dumps(response.text, indent=4)}")
        # log_message(data)
    except requests.exceptions.HTTPError as http_err:
        log_message(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        log_message(f"Error occurred: {req_err}")
    except ValueError as json_err:
        log_message(f"Error parsing JSON: {json_err}")


def put_data_custom(endpoint, payload, id):
    headers = {
        'Authorization': f'{BEARER_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:

        response = requests.put(f'{url}/{endpoint}/{id}', json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            log_message(f'Success: {endpoint} - {data} - {id} - {payload} - {response.status_code} - {response.data}')
        else:
            log_message(f"Error: {response.status_code}, {response.text}")
            data = response.json()
        # log_message(data)
    except requests.exceptions.HTTPError as http_err:
        log_message(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        log_message(f"Error occurred: {req_err}")
    except ValueError as json_err:
        log_message(f"Error parsing JSON: {json_err}")



# Posting schools
def post_schools():
    for inc in range(1, 4):
        payload = {
            "name": "School " + str(inc),
            "schoolid": str(inc),
            "address1": "Address 1 " + str(inc),
            "address2": "Address 2 " + str(inc),
            "city": "City " + str(inc),
            "postcode": "1234" + str(inc),
            "state": 1,
            "country": 1,
            "num_student": 1000,
            "email": "nersschool" + str(inc) + "@yopmail.com",
            "phone": "03" + str(inc),
            "school_type": 1,
            "is_active": True,
            "business_name": "School Business Name " + str(inc),
            "registration_id": "Regn ID " + str(inc),
            "bank_account_number": "12344455" + str(inc),
            "bank_name": "CIMB Bank",
            "profile_pic": "https://picsum.photos/200/300"
        }    
        post_data('school', payload)

# Posting academies
def post_academies():
    for inc in range(1, 13):
        payload = {
            "name": "Academy " + str(inc),
            "founder": "Founder " + str(inc),
            "phone": "03 1 " + str(inc),
            "bio": "Academy " + str(inc) + " Bio",
            "business_name": "Academy Business Name " + str(inc),
            "business_reg_number": "12342343 " + str(inc),
            "bank_account_number": "12312312 " + str(inc),
            "bank_name": "May Bank " + str(inc),
            "company_website": "https://www.academy" + str(inc) + ".com",
            "email": "nersacademy" + str(inc) + "@yopmail.com",
            "is_active": True,
            "is_verified": True,
            "address1": "Academy Addr1 " + str(inc),
            "address2": "Academy Addr2 " + str(inc),
            "city": "Academy Ciry " + str(inc),
            "postcode": "1231 " + str(inc),
            "state": 1,
            "country": 1,
            "course_type": 1,
            "commission": 10
        }
        post_data('academy', payload)

# Posting parents
def post_parents():
    for inc in range(1, 4):
        payload = {
            "name": "Parent" + str(inc),
            "profile_pic": "https://picsum.photos/200/300",
            "ic_number": "Parent IC " + str(inc),
            "ic_proof_image": "https://picsum.photos/200/300",
            "birthday": "2024-08-17",
            "email": "nersparent"+ str(inc) + "@yopmail.com",
            "age": 40,
            "gender": "M",
            "is_active": True,
            "is_approved": True,
            "is_subparent": True,
        }

        post_data('parent', payload)

# Posting branches
def post_branches():
    for inc in range(1, 12):
        school_id = random.randint(1, 3)
        payload = {
            "name": "Branch " + str(inc),
            "profile_pic": "https://picsum.photos/200/300",
            "pic": "Branch " + str(inc),
            "school_type": 1,
            "if_external": False,
            "address1": "Branch Addr1 " + str(inc),
            "address2": "Branch Addr2 " + str(inc),
            "city": "Branch City " + str(inc),
            "postcode": "1231" + str(inc),
            "state": 1,
            "country": 1,
            "school": school_id,
            "academy": random.randint(1, 12),
            "commission_rate": 122,
            "student_amount": 10,
            "slogan": "Slogan",
            "images": [
                "https://picsum.photos/200/300", "https://picsum.photos/200/300", "https://picsum.photos/200/300"
            ]
        }
        
        post_data('branch', payload)

# Posting courses
def post_courses():
    for inc in range(1, 11):
        payload = {
            "name": "Course " + str(inc),
            "description": "Course " + str(inc) + "description",
            "cta": "Course " + str(inc) + "cta",
            "price": 100 * inc,
            "billing_type": {
                "id": 1,
                "classCount": 0
            },
            "academy": random.randint(1, 12),
            "images": [
                "https://picsum.photos/200/300", "https://picsum.photos/200/300", "https://picsum.photos/200/300"
            ],
            "max_students_per_class": 20,
            "replaceable": True,
            "max_replacements_per_month": 5,
            "youtube_link": "https://youtube.com",
            "website_link": "https://website.com",
            "who_can_join": [
                5, 6, 7
            ],
            "course_type": [
                1, 2
            ],
            "assigned_branches": [
                {
                    "branch_id": 1,
                    "day": "Monday",
                    "start_time": "10:00",
                    "end_time": "11:00"
                },
                {
                    "branch_id": 2,
                    "day": "Thursday",
                    "start_time": "9:00",
                    "end_time": "10:00"
                }
            ]
        }

        post_data('course', payload)

# Posting coaches
def post_coaches():
    for inc in range(1, 12):
        branch_id = random.randint(1, 11)
        payload = {
            "name": "Coach " + str(inc),
            "ic_number": "IC No " + str(inc),
            "bank_account_number": "1231232 " + str(inc),
            "bank_name": "CIMB Bank " + str(inc),
            "mailing_address": "Mailing Address " + str(inc),
            "phone": "03 " + str(inc),
            "categories": [1],
            "gender": "M",
            "profile_pic": "https://picsum.photos/200/300",
            "bio": "Bio Coach " + str(inc),
            "ic_proof_image": "https://picsum.photos/200/300",
            "birth_date": "2024-08-17",
            "email": "nerscoach" + str(inc) + "@yopmail.com",
            "city": "City " + str(inc),
            "is_active": True,
            "is_approved": True,
            "salary_amount": 1000,
            "billing_type": {
                "id": 1,
                "classCount": 0
            },
            "assignedInfo": [
                {
                    "branchId": branch_id,
                    "courseIds": [4, 5]
                }
            ],
            "title": "Mr"
        }
        post_data('coach', payload)

# Posting students
def post_students():
    for inc in range(1,13):
        payload = {
            "name": "Student " + str(inc),
            "email": "student" + str(inc) + "@yopmail.com",
            "ic_number": "12312312" + str(inc),
            "birthday": "2024-08-17",
            "profile_pic": "https://picsum.photos/200/300",
            "ic_proof_image": "https://picsum.photos/200/300",
            "id_number": "S0012" + str(inc),
            "id_proof_image": "https://picsum.photos/200/300",
            "is_active": True,
            "is_approved": True,
            "payment_status": True,
            "payment_value": 300,
            "school_classroom": "1B",
            "relationship": "Son",
            "school": random.randint(1, 3),
            "student_standard": random.randint(1, 12),
            "parent": random.randint(1, 3),
            "assignedInfo": [
                {
                    "branchId": random.randint(1, 11),
                    "courseIds": [
                        4,5 
                    ]
                }
            ]
        }

        post_data('student', payload)
    
# Posting items
def post_items():
    for inc in range(1, 12):
        payload = {
            "name": "Item" + str(inc),
            "cta": "Item CTA" + str(inc),
            "price": 230,
            "billing_type": {
                "id": 1,
                "classCount": 0
            },
            "academy": random.randint(1, 12),
            "description": "Item Description " + str(inc),
            "youtube_link": "https://youtube.com",
            "website_link": "https://website.com",
            "images": [
                "https://picsum.photos/200/30", "https://picsum.photos/200/30", "https://picsum.photos/200/30"
            ],
            "applicable_branches": [1,2,5],
            "is_active": True
        }

        post_data('item', payload)


# Posting schedules
def post_schedules():
    for inc in range(1, 10):
        payload = {
            "day": "Monday",
            "event_date": "2024-08-21",
            "start_stime": "10:00",
            "end_time": "12:00",
            "event_name": "Event " + str(inc),
            "event_description": "Event " + str(inc),
            "event_type": "Class Event",
            "course": 1,
            "branch": 1,
            "venue_name": "Venue " + str(inc),
            "address": "Address " + str(inc),
            "city": "Subang Jaya",
            "postcode": "6637" + str(inc),
            "attendees": [
                "Coach", "Student",
            ]
        }

        post_data('schedule', payload)

# Posting announcements
def post_announcements():
    for inc in range(1, 10):
        payload = {
            "title": "Announcement " + str(inc),
            "description": "Description " + str(inc),
            "start_date": "2024-08-21",
            "end_date": "2024-08-21",
            "attachments": [
                "https://picsum.photos/200/300", "https://picsum.photos/200/300", "https://picsum.photos/200/300"
            ]
        }   

        post_data('announcement', payload)


# Posting attendance
def post_attendance():
    for inc in range(1, 100):
        attendance_status = [ "Present", "Absent", "Late", "Excused", "Leave"]
        payload = {
            "class_info": "ABC " + str(inc),
            "date": "2024-08-21",
            "time": datetime.now().strftime("%H:%M:%S"),  # Current time
            "attendance_status": random.choice(attendance_status),  # Choose a single status
            "notes": "Notes " + str(inc),
            "student_id": random.randint(1,13),
            "schedule": random.randint(1, 10),
        }

        post_data('attendance', payload)

# Posting checkin
def post_checkin():
    for inc in range(1, 20):
        payload = {
            "present": True,
            "coach": random.randint(1, 11),
            "schedule": random.randint(1, 9),
        }

        post_data('checkin', payload)

# Posting notifications
def post_notifications():
    for inc in range(1, 100):
        payload = {
            "title": "Notification " + str(inc),
            "description": "Description of Notification " + str(inc),
            "status": True,
            "reason": "Reason of Notification " + str(inc),
        }

        post_data('notification', payload)


# Put school
def put_school(id):
    payload = {
        "name": "School ",
        "address1": "Address 1 " ,
        "address2": "Address 2 " ,
        "city": "City " ,
        "postcode": "1234" ,
        "state": 1,
        "country": 1,
        "num_student": 1000,
        "email": "nersschool"  + "@yopmail.com",
        "phone": "03" ,
        "school_type": 1,
        "is_active": True,
        "business_name": "School Business Name " ,
        "registration_id": "Regn ID " ,
        "bank_account_number": "12344455" ,
        "bank_name": "CIMB Bank",
        "profile_pic": "https://picsum.photos/200/300"
    }

    put_data('school', payload, id)    

# Put academy
def put_academy(id):
    payload = {
        "name": "Academy " ,
        "founder": "Founder " ,
        "phone": "03 1 " ,
        "bio": "Academy "  + " Bio",
        "business_name": "Academy Business Name " ,
        "business_reg_number": "12342343 " ,
        "bank_account_number": "12312312 " ,
        "bank_name": "May Bank " ,
        "company_website": "https://www.academy"  + ".com",
        "email": "nersacademy"  + "@yopmail.com",
        "is_active": True,
        "is_verified": True,
        "address1": "Academy Addr1 " ,
        "address2": "Academy Addr2 " ,
        "city": "Academy Ciry " ,
        "postcode": "1231 " ,
        "state": 1,
        "country": 1,
        "course_type": 1,
        "commission": 10
    }
    put_data('academy', payload, id)

# Put parent
def put_parent(id):
    payload = {
        "name": "Parent" + " Edited",
        "profile_pic": "https://picsum.photos/200/300",
        "ic_number": "Parent IC " + " Edited" ,
        "ic_proof_image": "https://picsum.photos/200/300",
        "birthday": "2024-08-17",
        "email": "nersparent" + "@yopmail.com",
        "age": 40,
        "gender": "M",
        "is_active": True,
        "is_approved": True,
        "is_subparent": True,
    }

    put_data('parent', payload, id)

# Put branch
def put_branch(id):
    payload = {
        "name": "Branch "  + " Edited",
        "profile_pic": "https://picsum.photos/200/300",
        "pic": "Branch " ,
        "school_type": 1,
        "if_external": False,
        "address1": "Branch Addr1 "  + " Edited",
        "address2": "Branch Addr2 "  + " Edited",
        "city": "Branch City "  + " Edited",
        "postcode": "1231"  + " Edited",
        "state": 1,
        "country": 1,
        "school": 1,
        "academy": 1,
        "commission_rate": 50,
        "student_amount": 10,
        "slogan": "Slogan" + " Edited",
        "images": [
            "https://picsum.photos/200/300", "https://picsum.photos/200/300", "https://picsum.photos/200/300"
        ]
    }
    
    put_data('branch', payload, id)

# Put course
def put_course(id):
    payload = {
        "name": "Course "  + " Edited",
        "description": "Course "  + "description" + " Edited",
        "cta": "Course "  + "cta",
        "price": 1200,
        "billing_type": {
            "id": 1,
            "classCount": 0
        },
        "academy": 5,
        "images": [
            "https://picsum.photos/200/300", "https://picsum.photos/200/300", "https://picsum.photos/200/300"
        ],
        "max_students_per_class": 20,
        "replaceable": True,
        "max_replacements_per_month": 5,
        "youtube_link": "https://youtube.com" + "Edited",
        "website_link": "https://website.com" + "Edited",
        "who_can_join": [
            5, 6, 7
        ],
        "course_type": [
            1, 2
        ],
        "assigned_branches": [
            {
                "branch_id": 1,
                "day": "Monday",
                "start_time": "10:00",
                "end_time": "11:00"
            },
            {
                "branch_id": 2,
                "day": "Thursday",
                "start_time": "9:00",
                "end_time": "10:00"
            }
        ]
    }

    put_data('course', payload, id)

# Put coach
def put_coach(id):
    payload = {
        "name": "Coach "  + " Edited",
        "ic_number": "IC No "  + " Edited",
        "bank_account_number": "1231232 " + " Edited" ,
        "bank_name": "CIMB Bank "  + " Edited",
        "mailing_address": "Mailing Address "  + " Edited",
        "phone": "03 "  + " Edited",
        "categories": [1],
        "gender": "M",
        "profile_pic": "https://picsum.photos/200/300",
        "bio": "Bio Coach "  + " Edited",
        "ic_proof_image": "https://picsum.photos/200/300",
        "birth_date": "2024-08-17",
        "email": "nerscoach"  + "@yopmail.com",
        "city": "City "  + " Edited",
        "is_active": True,
        "is_approved": True,
        "salary_amount": 1000,
        "billing_type": {
            "id": 1,
            "classCount": 0
        },
        "assignedInfo": [
            {
                "branchId": 5,
                "courseIds": [4, 5]
            }
        ],
        "title": "Mr"
    }
    put_data('coach', payload, id)

# Put student
def put_student(id):
    payload = {
        "name": "Student " + " Edited" ,
        "email": "student"  + "@yopmail.com",
        "ic_number": "12312312" + " Edited",
        "birthday": "2024-08-17",
        "profile_pic": "https://picsum.photos/200/300",
        "ic_proof_image": "https://picsum.photos/200/300",
        "id_number": "S0012" ,
        "id_proof_image": "https://picsum.photos/200/300",
        "is_active": True,
        "is_approved": True,
        "payment_status": True,
        "payment_value": 300,
        "school_classroom": "1B",
        "relationship": "Son" + " Edited",
        "school": 2,
        "student_standard": 5,
        "parent": 2,
        "assignedInfo": [
            {
                "branchId": 4,
                "courseIds": [
                    4,5 
                ]
            }
        ]
    }

    put_data('student', payload, id)
    
# Put item
def put_item(id):
    payload = {
        "name": "Item"  + " Edited",
        "cta": "Item CTA"  + " Edited",
        "price": 230,
        "billing_type": {
            "id": 1,
            "classCount": 0
        },
        "academy": random.randint(1, 12),
        "description": "Item Description "  + " Edited",
        "youtube_link": "https://youtube.com",
        "website_link": "https://website.com",
        "images": [
            "https://picsum.photos/200/30", "https://picsum.photos/200/30", "https://picsum.photos/200/30"
        ],
        "applicable_branches": [1,2,5],
        "is_active": True
    }

    put_data('item', payload, id)


# Put schedule
def put_schedule(id):
    payload = {
        "day": "Monday",
        "event_date": "2024-08-21",
        "start_stime": "10:00",
        "end_time": "12:00",
        "event_name": "Event " + " Edited" ,
        "event_description": "Event "  + " Edited",
        "event_type": "Class Event" + " Edited",
        "course": 1,
        "branch": 1,
        "venue_name": "Venue "  + " Edited",
        "address": "Address "  + " Edited",
        "city": "Subang Jaya" + " Edited",
        "postcode": "6637"  + "Edit",
        "attendees": [
            "Coach", "Student", "All"
        ]
    }

    put_data('schedule', payload, id)

# Put announcement
def put_announcement(id):
    payload = {
        "title": "Announcement "  + " Edited",
        "description": "Description "  + " Edited",
        "start_date": "2024-08-21",
        "end_date": "2024-08-21",
        "attachments": [
            "https://picsum.photos/200/300", "https://picsum.photos/200/300", "https://picsum.photos/200/300"
        ]
    }   

    put_data('announcement', payload, id)


# Put attendance
def put_attendance(id):
    payload = {
        "class_info": "ABC "  + " Edited",
        "date": "2024-08-21",
        "time": datetime.now().strftime("%H:%M:%S"),  # Current time
        "attendance_status": 'Present',  # Choose a single status
        "notes": "Notes "  + " Edited",
        "student_id": 11,
        "schedule": 8,
    }

    put_data('attendance', payload, id)

# Put checkin
def put_checkin(id):
    payload = {
        "present": True,
        "coach": 2,
        "schedule": 6,
    }

    put_data('checkin', payload, id)

# Put notification
def put_notification(id):
    payload = {
        "title": "Notification "  + " Edited",
        "description": "Description of Notification "  + " Edited",
        "status": False,
        "reason": "Reason of Notification "  + " Edited",
    }

    put_data('notification', payload, id)


post_schools()
post_academies()
post_parents()
post_branches()
post_courses()
post_coaches()
post_students()
post_items()
post_schedules()
post_announcements()
post_attendance()
post_checkin()
post_notifications()

get_data('school')
get_data('academy')
get_data('parent')
get_data('branch')
get_data('course')
get_data('coach')
get_data('student')
get_data('item')
get_data('schedule')
get_data('announcement')
get_data('attendance')
get_data('checkin')
get_data('notification')

get_data('school', params={
    'page': 1,
    'page_size': 10,
    'name': 'Edited',
    'course_type': 1,
})

get_data('academy',params={
    'page': 1,
    'page_size': 10,
    'name': 'Edited',
    'course_type': 1,
})

get_data('parent',params={
    'page': 1,
    'page_size': 10,
    'name': 'Edited',
    'is_active': True,
    'is_approved': True,
})
get_data('branch',params={
    'page': 1,
    'page_size': 10,
    'location_type': None,
    'name': 'Edited',
})
get_data('course',params={
    'page': 1,
    'page_size': 10,
    'course_type_id': 1,
    'name': 'Edited',
    'sort_price': 'asc'
})
get_data('coach',params={
    'page': 1,
    'page_size': 10,
    'name': 'Edited',
    'course_type': 1,
})
get_data('student',params={
    'page': 1,
    'page_size': 10,
    'branch_id': '',
    'is_active': 1,
    'payment_status': True,
    'name': 'Edited',
})
get_data('item',params={
    'page': 1,
    'page_size': 10,
    'name': 'Edited',
    'academy_id': 1,
})
get_data('schedule',params={
    'page': 1,
    'page_size': 10,
    #'branch_id': 1,
    #'event_type': 'Edited',
    'event_date_from': '2024-01-01',
    'event_date_to': '2024-05-10',
})
get_data('announcement',params={
    'page': 1,
    'page_size': 10,
    'start_date_from': '2024-01-01',
    'start_date_to': '2024-08-20',
})
get_data('attendance',params={
    'page': 1,
    'page_size': 10,
    'from_date': '2024-10-10',
    'to_date': '2024-10-10',
})
get_data('checkin', params={
    'page': 1,
    'page_size': 10,
    'from_date': '2024-10-10',
    'to_date': '2024-10-10',
})
get_data('notification', params ={
    'page': 1,
    'page_size': 10,
    'from_date': '2024-10-10',
    'to_date': '2024-10-10',
})

put_parent(1)
put_branch(1)
put_course(1)
put_coach(1)
put_student(1)
put_item(1)
put_schedule(1)
put_announcement(1)
put_attendance(1)
put_checkin(1)
put_notification(3)

"""
get_data('school', 1)
get_data('academy', 1)
get_data('parent', 1)
get_data('branch', 1)
get_data('course', 1)
get_data('coach', 1)
get_data('student', 1)
get_data('item', 1)
get_data('schedule', 1)
get_data('announcement',1)
get_data('attendance', 1)
get_data('checkin', 1)
get_data('notification', 3)

get_data('billingtype', 1)
get_data('category', 1)
get_data('schooltype',1)
get_data('state',1)

get_data('school/dd', 1)
get_data('academy/dd', 1)
get_data('parent/dd', 1)
get_data('branch/dd', 1)
get_data('course/dd', 1)
get_data('coach/dd', 1)
get_data('student/dd', 1)
get_data('item/dd', 1)
get_data('billingtype/dd', 1)
get_data('category/dd', 1)
get_data('schooltype/dd',1)
get_data('state/dd',1)

post_data_custom('academy/profile', 1)

put_data_custom('academy/verify-business', 1)

delete_data('academy',1)
delete_data('announcement',1)
delete_data('attendance',1)
delete_data('billingtype',1)
delete_data('branch',1)
delete_data('category',1)
delete_data('checkin',1)
delete_data('coach',1)
delete_data('course',1)
delete_data('item',1)
delete_data('notification',1)
delete_data('parent',1)
delete_data('schedule',1)
delete_data('school',1)
delete_data('schooltype',1)
delete_data('state',1)
delete_data('student',1)


post_data_custom('user/change-password', params={'old_password': 'password', 'new_password': 'password'})
post_data_custom('user/create', params={'name': 'name', 'ic': 'ic', 'email': 'email', 'password': 'password', 'confirm_password': 'password', 'group': 'group'})
post_data_custom('user/generate-otp', params={'email': 'email'})
post_data_custom('user/logout')
post_data_custom('user/validate-otp', params={'email': 'email', 'otp': 'otp'})
"""

