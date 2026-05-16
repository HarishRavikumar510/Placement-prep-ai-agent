import { useState } from "react";
import { generateMCQs, generateStudyPlan } from "./gemini";

function App() {
  const [topic, setTopic] = useState(localStorage.getItem("lastTopic") || "");
  const [mcqs, setMcqs] = useState([]);
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState(
    JSON.parse(localStorage.getItem("topicHistory")) || []
  );

  const [company, setCompany] = useState("");
  const [days, setDays] = useState("");
  const [weakTopics, setWeakTopics] = useState("");
  const [studyPlan, setStudyPlan] = useState([]);
  const [planError, setPlanError] = useState("");
  const [planLoading, setPlanLoading] = useState(false);

  async function handleGenerate() {
    if (!topic.trim()) {
      alert("Enter a topic");
      return;
    }

    setLoading(true);
    setOutput("");
    setMcqs([]);

    localStorage.setItem("lastTopic", topic);

    const updatedHistory = [
      topic,
      ...history.filter((item) => item !== topic),
    ];

    localStorage.setItem("topicHistory", JSON.stringify(updatedHistory));
    setHistory(updatedHistory);

    try {
      const result = await generateMCQs(topic);
      setMcqs(result);
    } catch (error) {
      console.error(error);
      setOutput(error.message || "Something went wrong while generating MCQs");
    } finally {
      setLoading(false);
    }
  }

  async function handleStudyPlan() {
  if (!company.trim() || !days.trim() || !weakTopics.trim()) {
    alert("Enter company, days, and weak topics");
    return;
  }

  setPlanLoading(true);
  setStudyPlan([]);
  setPlanError("");

  try {
    const result = await generateStudyPlan(company, days, weakTopics);
    setStudyPlan(result);
  } catch (error) {
    console.error("Study plan error:", error);
    setPlanError(error.message || "Something went wrong");
  } finally {
    setPlanLoading(false);
  }
}

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #020617, #0f172a, #1e293b)",
        color: "white",
        padding: "40px",
        fontFamily: "Arial",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          fontSize: "52px",
          marginBottom: "25px",
        }}
      >
         Placement Prep AI Agent
      </h1>

      <p style={{ textAlign: "center", color: "#cbd5e1", marginBottom: "35px" }}>
        Practice smarter. Track weak areas. Prepare like a pro.
      </p>

      <div style={{ display: "flex", justifyContent: "center", gap: "10px" }}>
        <input
          type="text"
          placeholder="Enter topic: SQL, DSA, OOP..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          style={{
            padding: "15px",
            width: "420px",
            borderRadius: "12px",
            border: "1px solid #475569",
            fontSize: "16px",
            backgroundColor: "#1e293b",
            color: "white",
          }}
        />

        <button
          onClick={handleGenerate}
          disabled={loading}
          style={{
            padding: "15px 24px",
            borderRadius: "12px",
            border: "none",
            background: "linear-gradient(135deg, #2563eb, #7c3aed)",
            color: "white",
            cursor: "pointer",
            fontSize: "16px",
            fontWeight: "bold",
          }}
        >
          {loading ? "Generating..." : "Generate MCQs"}
        </button>
      </div>

      <div
        style={{
          marginTop: "22px",
          display: "flex",
          justifyContent: "center",
          gap: "12px",
          flexWrap: "wrap",
        }}
      >
        {["SQL", "DSA", "OOP", "Aptitude", "Gen AI"].map((item) => (
          <button
            key={item}
            onClick={() => setTopic(item)}
            style={{
              padding: "10px 16px",
              borderRadius: "999px",
              border: "1px solid #475569",
              cursor: "pointer",
              backgroundColor: topic === item ? "#2563eb" : "#334155",
              color: "white",
            }}
          >
            {item}
          </button>
        ))}
      </div>

      <div style={{ marginTop: "25px", textAlign: "center" }}>
        <h3>Recently Practiced Topics</h3>

        {history.length === 0 ? (
          <p style={{ color: "#94a3b8" }}>No topics practiced yet.</p>
        ) : (
          <div style={{ display: "flex", justifyContent: "center", gap: "10px", flexWrap: "wrap" }}>
            {history.map((item, index) => (
              <button
                key={index}
                onClick={() => setTopic(item)}
                style={{
                  padding: "8px 13px",
                  borderRadius: "8px",
                  border: "none",
                  cursor: "pointer",
                  backgroundColor: "#475569",
                  color: "white",
                }}
              >
                {item}
              </button>
            ))}
          </div>
        )}
      </div>

      {loading && (
        <p style={{ textAlign: "center", marginTop: "30px", color: "#38bdf8" }}>
          ⚡ AI is preparing your questions...
        </p>
      )}

      {output && (
        <div
          style={{
            marginTop: "35px",
            backgroundColor: "#7f1d1d",
            padding: "20px",
            borderRadius: "12px",
          }}
        >
          {output}
        </div>
      )}

      <div
        style={{
          marginTop: "40px",
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
          gap: "22px",
        }}
      >
        {mcqs.map((mcq, index) => (
          <div
            key={index}
            style={{
              background: "rgba(30, 41, 59, 0.95)",
              padding: "24px",
              borderRadius: "18px",
              border: "1px solid #334155",
              boxShadow: "0 10px 25px rgba(0,0,0,0.35)",
            }}
          >
            <h2 style={{ color: "#38bdf8", marginBottom: "12px" }}>
              Question {index + 1}
            </h2>

            <p style={{ fontSize: "18px", fontWeight: "bold", lineHeight: "1.5" }}>
              {mcq.question}
            </p>

            <div style={{ marginTop: "18px" }}>
              {mcq.options.map((option, i) => (
                <div
                  key={i}
                  style={{
                    backgroundColor: "#0f172a",
                    padding: "12px",
                    borderRadius: "10px",
                    marginBottom: "10px",
                    border: "1px solid #334155",
                  }}
                >
                  {option}
                </div>
              ))}
            </div>

            <div
              style={{
                marginTop: "18px",
                backgroundColor: "#052e16",
                padding: "12px",
                borderRadius: "10px",
                color: "#86efac",
              }}
            >
              ✅ Correct Answer: {mcq.answer}
            </div>

            <p style={{ marginTop: "15px", color: "#cbd5e1", lineHeight: "1.6" }}>
              💡 {mcq.explanation}
            </p>
          </div>
        ))}
      </div>

      <div
        style={{
          marginTop: "45px",
          backgroundColor: "#1e293b",
          padding: "25px",
          borderRadius: "18px",
        }}
      >
        <h2>📅 AI Study Plan Generator</h2>

        <input
          type="text"
          placeholder="Target company"
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          style={{ padding: "12px", width: "100%", marginBottom: "10px", borderRadius: "8px" }}
        />

        <input
          type="number"
          placeholder="Preparation days"
          value={days}
          onChange={(e) => setDays(e.target.value)}
          style={{ padding: "12px", width: "100%", marginBottom: "10px", borderRadius: "8px" }}
        />

        <input
          type="text"
          placeholder="Weak topics"
          value={weakTopics}
          onChange={(e) => setWeakTopics(e.target.value)}
          style={{ padding: "12px", width: "100%", marginBottom: "10px", borderRadius: "8px" }}
        />

        <button
          onClick={handleStudyPlan}
          disabled={planLoading}
          style={{
            padding: "12px 18px",
            borderRadius: "8px",
            border: "none",
            backgroundColor: "#16a34a",
            color: "white",
            cursor: "pointer",
          }}
        >
          {planLoading ? "Generating..." : "Generate Study Plan"}
        </button>

        {planLoading && (
  <p style={{ color: "#38bdf8", marginTop: "20px" }}>
    ⚡ AI is building your personalized plan...
  </p>
)}

{planError && (
  <div
    style={{
      marginTop: "20px",
      backgroundColor: "#7f1d1d",
      padding: "15px",
      borderRadius: "10px",
    }}
  >
    {planError}
  </div>
)}

<div
  style={{
    marginTop: "25px",
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
    gap: "18px",
  }}
>
  {studyPlan.map((plan, index) => (
    <div
      key={index}
      style={{
        background: "linear-gradient(135deg, #0f172a, #1e293b)",
        border: "1px solid #334155",
        borderRadius: "18px",
        padding: "22px",
        boxShadow: "0 10px 25px rgba(0,0,0,0.35)",
      }}
    >
      <h2 style={{ color: "#38bdf8" }}>📌 {plan.day}</h2>

      <h3 style={{ color: "#facc15" }}>{plan.focus}</h3>

      <ul style={{ lineHeight: "1.8" }}>
        {plan.tasks.map((task, i) => (
          <li key={i}>{task}</li>
        ))}
      </ul>

      <p>
        <strong>🎯 Practice:</strong> {plan.practice}
      </p>

      <p style={{ color: "#86efac" }}>
        💡 {plan.tip}
      </p>
    </div>
  ))}
</div>
      </div>
    </div>
  );
}

export default App;