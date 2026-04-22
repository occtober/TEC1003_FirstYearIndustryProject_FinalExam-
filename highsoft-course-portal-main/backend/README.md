Highsoft Course Portal Backend
This backend is part of the First Year Industry Project for the Highsoft course portal.

It provides course, quiz, and module data for the frontend.

Tech Stack
Python
Flask
JSON
Project Structure
app.py
requirements.txt
README.md
.gitignore
data/
  courses.json
  quiz-cards.json
  modules.json
How to Run
Open the project in VS Code
Open a terminal in the project folder
Install dependencies:
python -m pip install -r requirements.txt
Start the backend:
python app.py
The backend runs locally at:

http://127.0.0.1:4000

Working Endpoints
GET /api/courses
Returns the available courses

GET /api/courses?skillLevel=beginner
Returns filtered courses based on query parameters

GET /api/courses/1
Returns the course details for lesson 1

GET /api/quiz
Returns the quiz card data

POST /api/quiz/results
Returns recommended courses based on quiz answers

GET /api/courses/1/modules
Returns the modules for lesson 1

GET /api/courses/1/modules/1
Returns module 1

GET /api/courses/1/modules/2
Returns module 2

GET /api/courses/1/modules/3
Returns module 3

POST /api/courses/1/complete
Marks the course as completed for the current session

Example URLs
http://127.0.0.1:4000/api/courses
http://127.0.0.1:4000/api/courses?skillLevel=beginner
http://127.0.0.1:4000/api/courses/1
http://127.0.0.1:4000/api/quiz
http://127.0.0.1:4000/api/courses/1/modules
http://127.0.0.1:4000/api/courses/1/modules/1
Notes
The backend currently supports one main course flow
Data is stored in JSON files inside the data folder
The frontend can use these endpoints to fetch course, quiz, and module data
