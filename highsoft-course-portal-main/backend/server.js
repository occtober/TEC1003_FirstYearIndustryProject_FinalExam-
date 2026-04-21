import express from "express"
import courses from "./data/courses.json" assert { type: "json" };

const app = express();

app.get("/api/courses", (req, res => {
  res.json(courses); 
});

app.listen(3000, () => {
  console.log("Server running on port 3000); 
});
