# Automation of Number Plate Detection

# Images of frontend

<img width="500" alt="Screenshot 2023-05-04 at 2 10 46 PM" src="https://user-images.githubusercontent.com/132324275/236158607-dfbe6d16-ecb2-46ba-83ee-a36da83e9b3e.png">


<img width="500" alt="Screenshot 2023-05-04 at 2 13 17 PM" src="https://user-images.githubusercontent.com/132324275/236158649-5da4c770-a59d-407a-8567-5b96798ba8f1.png">

<img width="500" alt="Screenshot 2023-05-04 at 2 13 27 PM" src="https://user-images.githubusercontent.com/132324275/236158642-16567aa5-bc9f-4a40-ba9c-8a6f911ee0b5.png">

<img width="500" alt="Screenshot 2023-05-04 at 2 14 06 PM" src="https://user-images.githubusercontent.com/132324275/236158985-efc749d4-2d27-4c42-9e86-3f233f4d9c40.png">


# python work
This is a Python script that detects number plates in a video and saves the corresponding images to a specified folder. Additionally, it sends the saved images to a server using HTTP requests.

Prerequisites This script requires the following Python libraries to be installed:

1. number.py OpenCV Numpy Requests os

2. api.py sqlite3 flask config pandas

Getting Started

To get started, follow these steps:

1. Clone the repository to your local machine.

make extra folder in this file

1.core
inside  make "media" folder in this file
 

2. Install the required libraries using pip: pip install all #import file

        pip install opencv
 
        pip install numpy
 
        pip install Requests
 
        pip instal sqlight3
 
        pip install flask
 
        pip install flask_cors
 
        pip install pandas
 
        pip install config

3. save photo in Internal on machine and using flask frame work store photo in sqlite3 database table

4. Run api then make user in api 
        
     user name = admin user
    
     email = admin@gmail.com 
      
     user passwors = admin

     Start API then write on your search engine this command

         http://127.0.0.1:5000/admin/admin@gmail.com/admin

5. Update the save_folder variable in the script to specify the folder where you want to save the detected number plate images.

6. Update the send_img function in the script to specify the URL of the server where you want to send the images.

7. set your path of where your program work store image in only core/media folder video file name is IMG_1891.mp4

8. Run the script using the commands:

       python api.py
 
       python number.py

License : 
This script is distributed under the GNU General Public License

Acknowledgements: 
This project uses the haarcascade_russian_plate_number.xml file from the OpenCV,GitHub repository.

# React js Work 

This is a React JS program that demonstrates the use of various React components and libraries. The program displays a simple user interface that allows users to perform various actions, such as adding and deleting items from a list, filtering and searching items, and displaying charts.

1. Requirements :
        This app is run online react-bootstrapt so internet and some offline images 

2. Installation of React js : 

 1. create wab app using Terminal :

        1. npx create-react-app number

        2. cd number

        3. npm start

 2. Installation commands: 

        npm axios
  
        npm Modal

        npm Button 

        npm react-toastify

        npm menu
 
 3. And install other Requirements 


3. Features : 

This program demonstrates the following features of React JS:

1. Components: The program is built using various React components, such as buttons, forms, and charts.
2. State management: The program uses state to manage the data displayed on the user interface.
3. Props: The program passes data between components using props.
4. Hooks: The program uses various React hooks, such as useState and useEffect.
5. React Router: The program uses React Router to handle navigation between different pages.

License: 
This program is licensed under the MIT License. See the LICENSE file for more information.
