from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)

DATA_FILE = Path(__file__).parent / "data" / "courses.json"


def load_courses():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = load_courses()
    return jsonify(courses)


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    courses = load_courses()
    course = next((course for course in courses if course["id"] == course_id), None)

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    return jsonify(course)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
