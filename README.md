# FullStackExercise

# Backend

To launch the backend, make sure to follow these steps:

#1: 
  In the FullStackExercise folder, run the following command in cmd to activate the python virtual environment:
 
       source aphp/bin/activate
       
 #2 Once the virtual environment is activated, cd to the AirportProject folder and run the backend django server by doing:
 
 
       cd AirportProject
       python manage.py runserver
       
   -> If any python modules is not installed, you can check which modules is used in the virtual environment with the requirements.txt file in AirportProject
   
  #3 Once the backend server is launched, make sure that it is working by going to :
  
    http://localhost:8000/admin/
    
   #4 You can check that we load the correct json by either going to :
   
      http://localhost:8000/api/original/
      
      or
      
      http://localhost:8000/api/load_original/
      
   The first route links to the original json, while the second one routes toward another json format file with indices for each instance of the original json file
   
   
# frontend

#1 To launch the frontend, make sure that npm is installed, then cd to the following folder:
      
       FullStackExercise/AirportProject/finalfront
 #2  And run:
      
      npm start
      
 The server is in development deployment, but you can still access to the datatable when loading this url:
 
    http://localhost:3000/
    




