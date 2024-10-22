creating a virtual environment for this project, all the dependecies that are present only be there for this project, it will not affect any other modules and dependecies i add to other projects

1.
python3 -m venv venv -> creates a new virtual environment in the folder VNV
-m venv  (runs vnv module)
venv (directory name)
[got error while running python3 so used python -m venv venv]

2.activate the virtual environment
source ./venv/bin/activate 
source - shell command to execute the script
./venv/bin/activate - path to activate the virtual environment
[ i jsut tired to run it using this command but the venv folder has Scripts folder which contains activate command and i changed the directory to the scripts and activated the virtual environment]
whenever we install any dependency it will only be present for this particular folder 

3. Create a API
- Using Fast API
- pip3 install fastapi
- created a simple api route
- fastapi dev main.py (to run the app in developer mode(dev))
- 127.0.0.1 (local host)
- anything after a question mark is a query in url

day 2:
- I have done the route for the signup validation and installed postgres sql. 

day 3:
- SQLAlchemy - to connect backend framework to external database
- installed SQLAlchemy
- importing engine 
- called the function with specefic url 
- creating a session 
- sqlalchemy has session maker
- session created 
- initialized database
- 

