<h1>Rethink Backend Tasks:</h1>

<h3>Making Backend for Clinic Management System:</h3>

**Task(completed):**
Completed making all the proper endpoints for Admin, Doctors and Visitors
Added Error handling

**Tasks(Remaining):**
Couldn’t make the swagger interface for the endpoints as swagger doesn’t come in-built with django. Django rest swagger can be used, but it's obsolete with its support ended for versions > django 3.0.5, while django is currently 3.1.6. But I have used API Viewsets, we can get a near-swagger like output in the browser

**Kindly ignore the dummy names used in the API Schemas.
**Kindly ignore the word “PRACTITIONER” mentioned as “PRACTIONER” several times.



**How to Start/Setup the Project:**

<h2>In the terminal:</h2>

- Fork The Repo
- git clone https://github.com/sd2001/Rethink-Backend.git
- cd Rethink-Backend

```
 pip install virtualenv
 
 virtualenv env
 
 source env/bin/activate
 
 pip install -r requirements.txt
 
 python manage.py createsuperuser
   (To access the django-admin)
   
 python manage.py makemigrations
 
 python manage.py migrate
 
 python manage.py runserver

```

In the .env file, kindly add desired email and password(with smtp enabled to use the mail feature)








**ADMIN:

*URL : 127.0.0.1:8000/manage/admin

      -    Get list of Practitioners(get)
      -    Add a Practitioner(post)
      -    
Schema: 
{
        "name": "Dr 1",
        "picture_link": "aws.s3.123456789",
        "specialization": "Heart",
        "phone_number": 9836088355,
        "available": false,
        "PAN_number": "121xyz",
        "Account_number": "334xyz",
        "IFSC_number": "456xyz"
    }










**PRACTITIONERS:

Profile Endpoints for Doctors:

*URL:  127.0.0.1:8000/doctors/profile/<uuid:pk>

     -    Get a particular profile(post)
     -  Update a particular profile(put - update the values to be changed here)
     
   {
    "id": "367884a0-2bc3-48dd-8950-4c436a565e15",
    "name": "Dr 1",
    "picture_link": "n/a",
    "specialization": "Heart",
    "phone_number": 9836088355,
    "available": false,
     "PAN_number": "121xyz",
     "Account_number": "334xyz",
      "IFSC_number": "456xyz"
   }









Availability Endpoints for Doctors:

*URL: 127.0.0.1:8000/doctors/avail/<uuid:pk>

     -     Get particular doctor’s time(get)
     -     Update time(put - update the values to be changed here)
     -     
{
    "id": "98fded74-9775-4348-9505-7a9a1a60634e",
    "name": "Dr2",
    "start1": "10:00:00",
    "end1": "12:00:00",
    "maxtime": 25
}



*URL: 127.0.0.1:8000/doctors/avail

    -     Get all doctors available times(get)
    -    Post doctors available time(slots get created via this)
    -    
   {
        "id": "367884a0-2bc3-48dd-8950-4c436a565e15",
        "name": "Dr1",
        "start1": "13:00:00",
        "end1": "15:00:00",
        "maxtime": 20
    }



Slot Checking for booking:

*URL: http://127.0.0.1:8000/doctors/slots

    -   Get all the slots as selected by the doctors(get)


Check Booked Slots:(FORGOT TO SHOW THIS IN VIDEO)
*URL: http://127.0.0.1:8000/doctors/booking/<uuid:pk>

    -  Get the bookings for a particular doctor(get)






**VISITORS:

Registering Patients:

*URL: http://127.0.0.1:8000/patients/register

     -  Getting the list of all visitors(get)
     -  Add a visitor(post)
     
{
        "name": "Patient1",
        "email": "im.swarnabha2001@gmail.com",
        "address": "96/2, Bangur Avenue, 3rd floor",
        "postal": "700055",
        "city": "Kolkata",
        "state": "West Bengal",
        "country": "India",
        "nationality": "Indian",
        "dob": "21/12/2001",
        "verify": false
    }


Getting Details of a patient:

*URL: http://127.0.0.1:8000/patients/register/<uuid:pk>

    -  Get the patient details(get)




Verifying the patient email using OTP

URL: http://127.0.0.1:8000/patients/verify

    -   Get the otp(s) for all the patient from database(get)
    -   Post the otp to verify user = True(post)[this set the user.verify = True]
    -   
{
    "id": "5326ce22-b027-4289-8457-569518c14944",
    "otp": "eb130"
}

URL: http://127.0.0.1:8000/patients/verify/<uuid:pk>

     -  Get verification details for a single patient


Booking Slots:

*URL: http://127.0.0.1:8000/patients/bookslot

     -   Get the booked slots(get)
     -   Post booking slots(post - booking as per empty slots(false))
   
{
        "id": "461b2709-122e-4465-bc66-c1a56b0186dc",
        "patient_id": "324553d7-af74-4c6f-bb71-7c67d8e3c8f3",
        "name": "Voldemort",
        "email": "im.swarnabha2001@gmail.com",
        "dr_id": "a4d9a89e-6add-4294-b6be-e737e2c6d5a0",
        "slot": "15:00:00",
        "mode": "offline",
        "payment": false
    }

Payment for Booking/:

*URL: http://127.0.0.1:8000/patients/bookverify

    -  Get all the payment info for the users who’ve paid(get)
    -  Post the payment schema to make payment = true(post)
    
{
        "id": "1a14a38c-f5e8-4241-ad63-3a5d7fe6c4ae",
        "patient_id": "324553d7-af74-4c6f-bb71-7c67d8e3c8f3",
        "name": "Voldemort",
        "dr_id": "a4d9a89e-6add-4294-b6be-e737e2c6d5a0",
        "amount" : 500
    }

 

