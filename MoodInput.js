import React, { useState } from 'react';
import 'I:/Prajwal/Vibe-Tribe/frontend/src/styles.css';  // Updated to relative path for better portability

function MoodInput() {
    const [mood, setMood] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            const response = await fetch('http://localhost:5000/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mood })
            });
            

            const data = await response.json();

            if (response.ok) {
                setMessage(`Music generated: ${data.file}`);
            } else {
                setMessage(`Error: ${data.error}`);
            }
        } catch (error) {
            setMessage('Failed to connect to the server.');
        }
    };

    return (
        <div className="mood-input-container">
            <form onSubmit={handleSubmit} className="mood-form">
                <input 
                    type="text" 
                    value={mood} 
                    onChange={(e) => setMood(e.target.value)} 
                    placeholder="Enter mood (happy, sad, calm)" 
                    className="mood-input"
                />
                <button type="submit" className="generate-btn">Generate</button>
            </form>
            {message && <p className="message">{message}</p>}
        </div>
    );
}

export default MoodInput;
