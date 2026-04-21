from flask import Flask, jsonify, request
import json
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
COURSES_FILE = BASE_DIR / "data" / "courses.json"
QUIZ_FILE = BASE_DIR / "data" / "quiz-cards.json"
MODULES_FILE = BASE_DIR / "data" / "modules.json"


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = load_json(COURSES_FILE)

    skill_level = request.args.get("skillLevel")
    duration = request.args.get("duration")
    topic = request.args.get("topic")

    if skill_level:
        courses = [
            course for course in courses
            if course.get("skillLevel", "").lower() == skill_level.lower()
        ]

    if duration:
        courses = [
            course for course in courses
            if course.get("duration", "").lower() == duration.lower()
        ]

    if topic:
        courses = [
            course for course in courses
            if course.get("topic", "").lower() == topic.lower()
        ]

    return jsonify(courses)


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    courses = load_json(COURSES_FILE)
    course = next((course for course in courses if course["id"] == course_id), None)

    if not course:
        return jsonify({"error": "Course not found"}), 404

    return jsonify(course)


@app.route("/api/courses/<int:course_id>/modules", methods=["GET"])
def get_course_modules(course_id):
    modules = load_json(MODULES_FILE)
    course_modules = [module for module in modules if module["courseId"] == course_id]
    return jsonify(course_modules)


@app.route("/api/courses/<int:course_id>/modules/<int:module_id>", methods=["GET"])
def get_single_module(course_id, module_id):
    modules = load_json(MODULES_FILE)
    module = next(
        (
            module for module in modules
            if module["courseId"] == course_id and module["id"] == module_id
        ),
        None
    )

    if not module:
        return jsonify({"error": "Module not found"}), 404

    return jsonify(module)


@app.route("/api/quiz", methods=["GET"])
def get_quiz():
    quiz = load_json(QUIZ_FILE)
    return jsonify(quiz)


@app.route("/api/quiz/results", methods=["POST"])
def get_quiz_results():
    answers = request.json.get("answers", [])
    courses = load_json(COURSES_FILE)

    answer_tags = set(answer.lower() for answer in answers)

    scored_courses = []
    for course in courses:
        course_tags = set(tag.lower() for tag in course.get("tags", []))
        score = len(answer_tags.intersection(course_tags))
        scored_courses.append((score, course))

    scored_courses.sort(key=lambda item: item[0], reverse=True)
    recommended = [course for score, course in scored_courses if score > 0][:3]

    return jsonify(recommended)


@app.route("/api/courses/<int:course_id>/complete", methods=["POST"])
def complete_course(course_id):
    return jsonify({
        "message": f"Course {course_id} marked as completed",
        "completed": True
    })


if __name__ == "__main__":
    app.run(debug=True, port=4000)
