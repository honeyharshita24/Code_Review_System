import React, { useState } from 'react';
import axios from 'axios';

function App() {
  // State to track the code input and feedback
  const [code, setCode] = useState('');
  const [feedback, setFeedback] = useState('');

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();  // Prevents page reload
    try {
      // Send code to the backend API
      const response = await axios.post('http://localhost:8000/review', { code });
      setFeedback(response.data.feedback);  // Update feedback state
    } catch (error) {
      setFeedback('Error: Could not get feedback.');
    }
  };

  return (
    <div>
      <h1>AI Code Reviewer</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}  // Update code state as user types
          placeholder="Paste your code here..."
          rows={10}
          cols={50}
        />
        <button type="submit">Get Feedback</button>
      </form>
      {feedback && (  
        <div>
          <h2>Feedback:</h2>
          <pre>{feedback}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
