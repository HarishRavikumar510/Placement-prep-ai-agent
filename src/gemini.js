import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(
  import.meta.env.VITE_GEMINI_API_KEY
);

const models = [
  "gemini-2.5-flash",
  "gemini-2.0-flash",
  "gemini-1.5-flash",
];

async function tryModels(prompt) {
  for (const modelName of models) {
    try {
      console.log("Trying model:", modelName);

      const model = genAI.getGenerativeModel({
        model: modelName,
      });

      const result = await model.generateContent(prompt);

      return result.response.text();
    } catch (error) {
      console.error(`${modelName} failed`, error);
    }
  }

  throw new Error(
    "The AI is currently experiencing high demand. Please try again in a few moments."
  );
}

export async function generateMCQs(topic, questionLimit) {
  const prompt = `
Generate exactly ${questionLimit} placement MCQs on ${topic}.

Return ONLY valid JSON.
No markdown.
No explanation outside JSON.

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

  try {
    const text = await tryModels(prompt);

    const cleanText = text.replace(/```json|```/g, "").trim();

    return JSON.parse(cleanText);
  } catch (error) {
    console.error(error);

    return [
      {
        question: "Which SQL clause is used to filter rows?",
        options: [
          "A. ORDER BY",
          "B. GROUP BY",
          "C. WHERE",
          "D. HAVING",
        ],
        answer: "C. WHERE",
        explanation:
          "WHERE filters rows before grouping or aggregation.",
      },
    ];
  }
}

export async function generateStudyPlan(company, days, weakTopics) {
  const prompt = `
Create a placement preparation study plan.

Target Company: ${company}
Preparation Days: ${days}
Weak Topics: ${weakTopics}

Return ONLY valid JSON.

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

  try {
    const text = await tryModels(prompt);

    const cleanText = text.replace(/```json|```/g, "").trim();

    return JSON.parse(cleanText);
  } catch (error) {
    console.error(error);

    return [
      {
        day: "Day 1",
        focus: "SQL Basics",
        tasks: [
          "Learn SELECT queries",
          "Practice WHERE clause",
          "Revise GROUP BY",
        ],
        practice: "Solve 10 SQL MCQs",
        tip: "Consistency beats intensity.",
      },
    ];
  }
}

export async function generateCodingQuestion(codingTopic, difficulty) {
  const prompt = `
Generate exactly ONE coding interview practice question.

Topic: ${codingTopic}
Difficulty: ${difficulty}

Return ONLY valid JSON.
No markdown. No extra text.

Format:
{
  "title": "Problem Title",
  "difficulty": "Easy/Medium/Hard",
  "problem": "Detailed problem description.",
  "inputFormat": "Description of input format.",
  "outputFormat": "Description of output format.",
  "example": "Input: ... Output: ... Explanation: ...",
  "approach": "A brief approach to solve the problem.",
  "hint": "A small hint to help get started."
}
`;

  try {
    const text = await tryModels(prompt);

    const cleanText = text.replace(/```json|```/g, "").trim();

    return JSON.parse(cleanText);
  } catch (error) {
    console.error("Coding question generation failed:", error);

    return {
      title: "Two Sum",
      difficulty: difficulty || "Easy",
      problem: "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
      inputFormat: "An array of integers 'nums' and an integer 'target'.",
      outputFormat: "An array containing two integers representing the indices.",
      example: "Input: nums = [2,7,11,15], target = 9 | Output: [0,1] | Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].",
      approach: "Use a hash map to store the numbers and their indices as you iterate. For each number, check if the complement (target - number) exists in the map.",
      hint: "Try to solve it in one pass using a hash map.",
    };
  }
}