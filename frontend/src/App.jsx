import { useState } from "react";
import "./App.css";
import { story } from "./storyData";

export default function App() {
  const [current, setCurrent] = useState("start");

  const node = story[current];

  return (
    <div className="page">
      <h1 className="app-title">Interactive Story Generator</h1>

      <div className="story-card">
        {node.title && (
          <h2 className="story-title">{node.title}</h2>
        )}

        <p className="story-description">{node.text}</p>

        {node.options.length > 0 && (
          <>
            <h3 className="question">What will you do?</h3>

            {node.options.map((opt, i) => (
              <button
                key={i}
                className="option-btn"
                onClick={() => setCurrent(opt.next)}
              >
                {opt.text}
              </button>
            ))}
          </>
        )}

        {node.options.length === 0 && (
          <div className="actions">
            <button
              className="restart-btn"
              onClick={() => setCurrent("start")}
            >
              Restart Story
            </button>
          </div>
        )}

        <div className="new-story-container">
          <button
            className="new-story-btn"
            onClick={() => setCurrent("start")}
          >
            New Story
          </button>
        </div>
      </div>
    </div>
  );
}
