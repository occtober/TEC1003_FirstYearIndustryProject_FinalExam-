# Highsoft Course Portal

This project is part of the First Year Industry Project.

The goal is to design and develop a digital course portal for Highsoft.

## Project Structure

The project is divided into two main parts:

### Frontend
Located in `/frontend`

Contains HTML, CSS, JavaScript, assets, and design system documentation.

### Backend
Located in `/backend`

Contains the Python Flask API and course data handling.

## Backend Features

The backend provides course data for the frontend through API endpoints.

### Endpoints

- `GET /api/courses`  
  Returns all courses

- `GET /api/courses/<id>`  
  Returns a single course by id

## Example URLs

- `http://127.0.0.1:4000/api/courses`
- `http://127.0.0.1:4000/api/courses/1`

## Backend Structure

    backend/
      app.py
      requirements.txt
      README.md
      .gitignore
      data/
        courses.json

## How to Run the Backend

1. Open a terminal in the `backend` folder
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
