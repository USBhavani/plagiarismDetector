Install all packages (use the versions suitable for the system)
https://github.com/abhimanyutherobot/rpi_interview_app/blob/master/Interview_App/requirements.txt

abhimanyu -> with access_id, service_id (sky*)
$ aws configure

To use speech services: google credentials -> check for 'abhimanyu-google.json' file in html folder if yes, run the below command in temrinal
$ export GOOGLE_APPLICATION_CREDENTIALS="/var/www/html/abhimanyu-google.json"

-------------------------------------------
if html folder is not present
var$ sudo mkdir www/
www$ sudo mkdir html/


for file read and write permissions
var$ sudo chmod 777 www/
www# ls -l

www$ sudo chmod html/
html$ ls -l
-------------------------------------------

in rpi_interview_App

constants.py: QUESTION_ID_FIELD = "questionbank_id"
constants.py: DJANGO_SERVER_ADDR = 'http://202.53.13.21:5002/'
** session_id need to be created by admin before starting the interview and also update the session id in interview.py
interview.py: session_id (cross check with /admin/interview_app/session/)

If all the above mentioned requirements are satisfied then run main.py file
interview_App$ python3 main.py
