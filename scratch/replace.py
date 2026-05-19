import re

with open("src/App.jsx", "r") as f:
    content = f.read()

# 1. Add isSidebarOpen state
content = content.replace(
    'const [codingError, setCodingError] = useState("");',
    'const [codingError, setCodingError] = useState("");\n  const [isSidebarOpen, setIsSidebarOpen] = useState(false);'
)

# 2. Extract everything before the main return
match = re.search(r'(if \(!loggedUser\).*?)(  return \(\n    <div\n      style=\{\{\n        minHeight: "100vh",)', content, flags=re.DOTALL)
if match:
    before_return = content[:match.end(1)]
    
    new_return = """
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #020617, #0f172a, #1e293b)",
        color: "white",
        fontFamily: "Arial",
        position: "relative",
        overflowX: "hidden"
      }}
    >
      <div style={{ padding: "40px", transition: "all 0.3s ease", opacity: isSidebarOpen ? 0.3 : 1 }}>
        <div style={{ 
          display: "flex", 
          justifyContent: "space-between", 
          alignItems: "center",
          marginBottom: "40px"
        }}>
          <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
            <span style={{ color: "#86efac", fontWeight: "bold" }}>
              {loggedUser?.email}
            </span>
            <button
              onClick={handleLogout}
              style={{
                padding: "8px 16px",
                borderRadius: "8px",
                border: "none",
                backgroundColor: "#ef4444",
                color: "white",
                cursor: "pointer",
                fontSize: "12px",
                fontWeight: "bold",
                boxShadow: "0 4px 6px rgba(239, 68, 68, 0.3)",
              }}
            >
              Logout
            </button>
          </div>

          <div style={{ textAlign: "center" }}>
            <h1 style={{ fontSize: "52px", margin: "0 0 10px 0" }}>
              Placement Prep AI Agent
            </h1>
            <p style={{ color: "#cbd5e1", margin: 0 }}>
              Practice smarter. Track weak areas. Prepare like a pro.
            </p>
          </div>

          <div>
            <button
              onClick={() => setIsSidebarOpen(true)}
              style={{
                padding: "12px 20px",
                borderRadius: "12px",
                border: "1px solid #475569",
                backgroundColor: "#1e293b",
                color: "white",
                cursor: "pointer",
                fontSize: "16px",
                fontWeight: "bold",
              }}
            >
              ☰ Menu
            </button>
          </div>
        </div>

        <div style={{ display: "flex", justifyContent: "center", gap: "10px", marginTop: "40px" }}>
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

      <div
        style={{
          position: "fixed",
          top: 0,
          right: isSidebarOpen ? "0" : "-500px",
          width: "100%",
          maxWidth: "500px",
          height: "100vh",
          backgroundColor: "#0f172a",
          boxShadow: "-5px 0 25px rgba(0,0,0,0.5)",
          transition: "right 0.3s ease-in-out",
          zIndex: 50,
          overflowY: "auto",
          borderLeft: "1px solid #334155",
          padding: "30px",
          boxSizing: "border-box"
        }}
      >
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "30px" }}>
          <h2 style={{ margin: 0, color: "white" }}>Dashboard & Tools</h2>
          <button
            onClick={() => setIsSidebarOpen(false)}
            style={{
              background: "transparent",
              border: "none",
              color: "#cbd5e1",
              fontSize: "24px",
              cursor: "pointer"
            }}
          >
            ✕
          </button>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
            gap: "20px",
            marginBottom: "40px",
          }}
        >
          <div
            style={{
              background: "rgba(30, 41, 59, 0.95)",
              padding: "20px",
              borderRadius: "15px",
              border: "1px solid #334155",
              textAlign: "center",
              boxShadow: "0 8px 20px rgba(0,0,0,0.3)",
            }}
          >
            <div style={{ fontSize: "30px", marginBottom: "10px" }}>🧠</div>
            <h3 style={{ color: "#94a3b8", fontSize: "14px", margin: "0 0 10px 0" }}>Total MCQs Practiced</h3>
            <p style={{ color: "#38bdf8", fontSize: "28px", fontWeight: "bold", margin: 0 }}>{totalMCQs}</p>
          </div>

          <div
            style={{
              background: "rgba(30, 41, 59, 0.95)",
              padding: "20px",
              borderRadius: "15px",
              border: "1px solid #334155",
              textAlign: "center",
              boxShadow: "0 8px 20px rgba(0,0,0,0.3)",
            }}
          >
            <div style={{ fontSize: "30px", marginBottom: "10px" }}>📚</div>
            <h3 style={{ color: "#94a3b8", fontSize: "14px", margin: "0 0 10px 0" }}>Topics Practiced</h3>
            <p style={{ color: "#38bdf8", fontSize: "28px", fontWeight: "bold", margin: 0 }}>{history.length}</p>
          </div>

          <div
            style={{
              background: "rgba(30, 41, 59, 0.95)",
              padding: "20px",
              borderRadius: "15px",
              border: "1px solid #334155",
              textAlign: "center",
              boxShadow: "0 8px 20px rgba(0,0,0,0.3)",
            }}
          >
            <div style={{ fontSize: "30px", marginBottom: "10px" }}>📅</div>
            <h3 style={{ color: "#94a3b8", fontSize: "14px", margin: "0 0 10px 0" }}>Study Plans Generated</h3>
            <p style={{ color: "#38bdf8", fontSize: "28px", fontWeight: "bold", margin: 0 }}>{studyPlanCount}</p>
          </div>

          <div
            style={{
              background: "rgba(30, 41, 59, 0.95)",
              padding: "20px",
              borderRadius: "15px",
              border: "1px solid #334155",
              textAlign: "center",
              boxShadow: "0 8px 20px rgba(0,0,0,0.3)",
            }}
          >
            <div style={{ fontSize: "30px", marginBottom: "10px" }}>🚀</div>
            <h3 style={{ color: "#94a3b8", fontSize: "14px", margin: "0 0 10px 0" }}>Recommended Next Topic</h3>
            <p style={{ color: "#facc15", fontSize: "22px", fontWeight: "bold", margin: 0, textTransform: "capitalize" }}>{history[0] || "Start"}</p>
          </div>
        </div>

        <div
          style={{
            background: "#1e293b",
            padding: "25px",
            borderRadius: "18px",
            marginBottom: "40px",
            border: "1px solid #334155",
            boxShadow: "0 10px 25px rgba(0,0,0,0.2)",
          }}
        >
          <h2 style={{ color: "#38bdf8", marginBottom: "10px" }}>🧠 Weak Topic Analyzer</h2>
          <p style={{ color: "#cbd5e1", marginBottom: "20px" }}>
            Add topics you find difficult. The agent will help you practice them.
          </p>

          <div style={{ display: "flex", gap: "10px", marginBottom: "20px" }}>
            <input
              type="text"
              placeholder="E.g. Dynamic Programming, SQL Joins..."
              value={weakTopicInput}
              onChange={(e) => setWeakTopicInput(e.target.value)}
              style={{
                flex: 1,
                padding: "12px",
                borderRadius: "10px",
                border: "1px solid #475569",
                backgroundColor: "#0f172a",
                color: "white",
                fontSize: "16px",
              }}
            />
            <button
              onClick={handleAddWeakTopic}
              style={{
                padding: "12px 20px",
                borderRadius: "10px",
                border: "none",
                backgroundColor: "#f97316",
                color: "white",
                fontWeight: "bold",
                cursor: "pointer",
                fontSize: "16px",
                boxShadow: "0 4px 10px rgba(249, 115, 22, 0.3)",
              }}
            >
              Add
            </button>
          </div>

          {savedWeakTopics.length === 0 ? (
            <p style={{ color: "#94a3b8", fontStyle: "italic" }}>
              No weak topics added yet.
            </p>
          ) : (
            <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
              {savedWeakTopics.map((item, index) => (
                <button
                  key={index}
                  onClick={() => {
                    setTopic(item);
                    setIsSidebarOpen(false);
                  }}
                  style={{
                    padding: "8px 16px",
                    borderRadius: "20px",
                    border: "1px solid #f97316",
                    backgroundColor: "transparent",
                    color: "#f97316",
                    cursor: "pointer",
                    fontSize: "14px",
                    fontWeight: "bold",
                    transition: "all 0.2s",
                  }}
                  onMouseOver={(e) => {
                    e.target.style.backgroundColor = "#f97316";
                    e.target.style.color = "white";
                  }}
                  onMouseOut={(e) => {
                    e.target.style.backgroundColor = "transparent";
                    e.target.style.color = "#f97316";
                  }}
                >
                  {item}
                </button>
              ))}
            </div>
          )}
        </div>

        <div style={{ marginBottom: "40px", textAlign: "center", backgroundColor: "#1e293b", padding: "20px", borderRadius: "18px", border: "1px solid #334155" }}>
          <h3 style={{ marginTop: 0 }}>Recently Practiced Topics</h3>

          {history.length === 0 ? (
            <p style={{ color: "#94a3b8" }}>No topics practiced yet.</p>
          ) : (
            <div style={{ display: "flex", justifyContent: "center", gap: "10px", flexWrap: "wrap" }}>
              {history.map((item, index) => (
                <button
                  key={index}
                  onClick={() => {
                    setTopic(item);
                    setIsSidebarOpen(false);
                  }}
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

        <div
          style={{
            background: "#1e293b",
            padding: "25px",
            borderRadius: "18px",
            marginBottom: "40px",
            border: "1px solid #334155",
            boxShadow: "0 10px 25px rgba(0,0,0,0.2)",
          }}
        >
          <h2 style={{ color: "#c084fc", marginBottom: "10px" }}>💻 Coding Question Generator</h2>
          <p style={{ color: "#cbd5e1", marginBottom: "20px" }}>
            Generate placement-level coding questions with approach and hints.
          </p>

          <div style={{ display: "flex", flexDirection: "column", gap: "10px", marginBottom: "20px" }}>
            <div style={{ display: "flex", gap: "10px" }}>
              <input
                type="text"
                placeholder="Topic..."
                value={codingTopic}
                onChange={(e) => setCodingTopic(e.target.value)}
                style={{
                  flex: 2,
                  padding: "12px",
                  borderRadius: "10px",
                  border: "1px solid #475569",
                  backgroundColor: "#0f172a",
                  color: "white",
                  fontSize: "14px",
                }}
              />
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                style={{
                  flex: 1,
                  padding: "12px",
                  borderRadius: "10px",
                  border: "1px solid #475569",
                  backgroundColor: "#0f172a",
                  color: "white",
                  fontSize: "14px",
                }}
              >
                <option value="Easy">Easy</option>
                <option value="Medium">Medium</option>
                <option value="Hard">Hard</option>
              </select>
            </div>
            
            <button
              onClick={handleCodingQuestion}
              disabled={codingLoading}
              style={{
                padding: "12px 20px",
                borderRadius: "10px",
                border: "none",
                backgroundColor: "#9333ea",
                color: "white",
                fontWeight: "bold",
                cursor: codingLoading ? "not-allowed" : "pointer",
                fontSize: "16px",
                boxShadow: "0 4px 10px rgba(147, 51, 234, 0.3)",
                opacity: codingLoading ? 0.7 : 1,
              }}
            >
              {codingLoading ? "Generating..." : "Generate"}
            </button>
          </div>

          {codingError && (
            <div
              style={{
                backgroundColor: "#7f1d1d",
                padding: "15px",
                borderRadius: "10px",
                marginBottom: "20px",
              }}
            >
              {codingError}
            </div>
          )}

          {codingQuestion && (
            <div
              style={{
                background: "rgba(30, 41, 59, 0.95)",
                padding: "20px",
                borderRadius: "15px",
                border: "1px solid #334155",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "15px" }}>
                <h3 style={{ color: "#c084fc", margin: 0, fontSize: "18px" }}>{codingQuestion.title}</h3>
                <span style={{ 
                  padding: "6px 10px", 
                  borderRadius: "20px", 
                  fontSize: "12px", 
                  fontWeight: "bold",
                  backgroundColor: codingQuestion.difficulty === "Easy" ? "#065f46" : codingQuestion.difficulty === "Medium" ? "#b45309" : "#991b1b",
                  color: "white"
                }}>
                  {codingQuestion.difficulty}
                </span>
              </div>

              <p style={{ lineHeight: "1.6", marginBottom: "20px", fontSize: "14px" }}>{codingQuestion.problem}</p>

              <div style={{ marginBottom: "15px" }}>
                <strong style={{ color: "#94a3b8", fontSize: "14px" }}>Input Format:</strong>
                <p style={{ marginTop: "5px", fontSize: "14px" }}>{codingQuestion.inputFormat}</p>
              </div>

              <div style={{ marginBottom: "20px" }}>
                <strong style={{ color: "#94a3b8", fontSize: "14px" }}>Output Format:</strong>
                <p style={{ marginTop: "5px", fontSize: "14px" }}>{codingQuestion.outputFormat}</p>
              </div>

              <div style={{ marginBottom: "20px" }}>
                <strong style={{ color: "#94a3b8", fontSize: "14px" }}>Example:</strong>
                <pre style={{ 
                  backgroundColor: "#0f172a", 
                  padding: "15px", 
                  borderRadius: "8px", 
                  overflowX: "auto",
                  marginTop: "8px",
                  border: "1px solid #1e293b",
                  fontSize: "12px"
                }}>
                  <code>{codingQuestion.example}</code>
                </pre>
              </div>

              <div style={{ marginBottom: "15px" }}>
                <strong style={{ color: "#38bdf8", fontSize: "14px" }}>💡 Approach:</strong>
                <p style={{ marginTop: "5px", color: "#cbd5e1", lineHeight: "1.5", fontSize: "14px" }}>{codingQuestion.approach}</p>
              </div>

              <div>
                <strong style={{ color: "#facc15", fontSize: "14px" }}>🔑 Hint:</strong>
                <p style={{ marginTop: "5px", color: "#cbd5e1", fontStyle: "italic", fontSize: "14px" }}>{codingQuestion.hint}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
"""
    
    final_content = before_return + new_return
    
    with open("src/App.jsx", "w", encoding="utf-8") as f:
        f.write(final_content)
    print("Success")
else:
    print("Failed to match return statement")
