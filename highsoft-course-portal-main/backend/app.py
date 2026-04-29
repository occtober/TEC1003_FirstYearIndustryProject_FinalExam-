from flask import Flask, jsonify, send_from_directory

import json
from pathlib import Path

app = Flask(__name__, static_folder="../Frontend", static_url_path="")

BASE_DIR = Path(__file__).parent
COURSES_FILE = BASE_DIR / "data" / "courses.json"
QUIZ_FILE = BASE_DIR / "data" / "quiz-cards.json"
MODULES_FILE = BASE_DIR / "data" / "modules.json"


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/api/quiz", methods=["GET"])
def get_quiz():
    return jsonify(load_json(QUIZ_FILE))


@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(load_json(COURSES_FILE))


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    courses = load_json(COURSES_FILE)
    course = next((course for course in courses if course["id"] == course_id), None)

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    return jsonify(course)


@app.route("/api/courses/<int:course_id>/modules", methods=["GET"])
def get_course_modules(course_id):
    modules = load_json(MODULES_FILE)
    return jsonify([module for module in modules if module["courseId"] == course_id])


@app.route("/api/courses/<int:course_id>/modules/<int:module_id>", methods=["GET"])
def get_module(course_id, module_id):
    modules = load_json(MODULES_FILE)
    module = next(
        (
            module for module in modules
            if module["courseId"] == course_id and module["id"] == module_id
        ),
        None
    )

    if module is None:
        return jsonify({"error": "Module not found"}), 404

    return jsonify(module)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
