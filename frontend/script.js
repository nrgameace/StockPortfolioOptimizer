    document.addEventListener('DOMContentLoaded', function() {
        const tickers = document.getElementById('tickers');
        const initialBudget = document.getElementById('budget');
        const myButton = document.getElementById('submit');
        const outputParagraph = document.getElementById('output');
        const API_URL = 'http://127.0.0.1:8000/submit-portfolio';

        myButton.addEventListener('click', function() {
            event.preventDefault();
            const tickerData = tickers.value;

            outputParagraph.textContent = "LOADING ...";
            console.log("Text from textbox: " + tickerData); // Optional: log to console

            if (!tickerData || isNaN(initialBudget.value)) {
            outputParagraph.textContent = "Please enter stock tickers and a valid initial budget.";
            return;
        }
        
            outputParagraph.textContent = "🚀 Sending data to API for processing...";

            fetch(API_URL, {
            // CRITICAL: Must use the POST method
            method: 'POST', 
            headers: {
                // Tells the server that the data being sent is in JSON format
                'Content-Type': 'application/json' 
            },
            // The body must be a JSON string, and the keys MUST match your Pydantic model
            body: JSON.stringify({
                tickers: tickerData, 
                initial_value: initialBudget.value 
            })
        })


        .then(response => {
            // Check if the server responded with an error status (e.g., 404, 500, 422)
            if (!response.ok) {
                // Throw an error if the status is not successful (2xx)
                throw new Error(`HTTP Error! Status: ${response.status}. Check console for details.`);
            }
            // If successful, parse the JSON response body
            return response.json(); 
        })
        .then(data => {
            // 4. Handle the successful response from FastAPI
            const tickersList = data.tickers.join(', ');
            outputParagraph.innerHTML = `✅ **Success!** Data processed.<br>
                                         **Tickers:** ${tickersList}<br>
                                         **Budget:** $${data.initial_value.toFixed(2)}`;
            console.log("API Response Data:", data);
        })
        .catch(error => {
            // 5. Handle any errors (network, parsing, HTTP status error)
            outputParagraph.textContent = `❌ ERROR: Failed to process data. ${error.message}`;
            console.error("Fetch operation failed:", error);
        });
        });
    });