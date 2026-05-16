import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(
  import.meta.env.VITE_GEMINI_API_KEY
);

export async function generateMCQs(topic) {
  const model = genAI.getGenerativeModel({
    model: "gemini-2.5-flash",
  });

  const prompt = `
Generate exactly 10 placement MCQs on ${topic}.

Return ONLY valid JSON.
No markdown. No explanation outside JSON.

Format:
[
  {
    "question": "Question text",
    "options": ["A. option", "B. option", "C. option", "D. option"],
    "answer": "C. correct option",
    "explanation": "Short explanation"
  }
]
`;

  const result = await model.generateContent(prompt);
  const text = result.response.text();

  const cleanText = text.replace(/```json|```/g, "").trim();

  return JSON.parse(cleanText);
}

export async function generateStudyPlan(company, days, weakTopics) {
  const model = genAI.getGenerativeModel({
    model: "gemini-2.5-flash",
  });

  const prompt = `
Create a placement preparation study plan.

Target Company: ${company}
Preparation Days: ${days}
Weak Topics: ${weakTopics}

Return ONLY valid JSON.
No markdown.
No extra text.

Format:
[
  {
    "day": "Day 1",
    "focus": "Main topic",
    "tasks": [
      "Task 1",
      "Task 2",
      "Task 3"
    ],
    "practice": "Practice activity",
    "tip": "Short motivational tip"
  }
]
`;

  const result = await model.generateContent(prompt);

  const text = result.response.text();

  const cleanText = text.replace(/```json|```/g, "").trim();

  return JSON.parse(cleanText);
}