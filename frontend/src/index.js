import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

// Find the root element in the DOM
const rootElement = document.getElementById("root");

// Create a root
const root = ReactDOM.createRoot(rootElement);

// Render the App component into the root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
