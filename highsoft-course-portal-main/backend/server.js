import express from "express"
import courses from "./data/courses.json" assert { type: "json" };

const app = express();

app.use(express.json());

app.get("/api/courses", (req,res) => {
  res.json(courses);
});
