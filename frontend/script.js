    document.addEventListener('DOMContentLoaded', function() {
        const tickers = document.getElementById('tickers');
        const initialBudget = document.getElementById('budget');
        const myButton = document.getElementById('submit');
        const outputParagraph = document.getElementById('output');
        const API_URL = 'http://127.0.0.1:8000/submit-portfolio';

        myButton.addEventListener('click', function(event) {
            event.preventDefault(); // Prevents page refresh after button click
            //const tickerData = tickers.value;
            var rawTickerData = tickers.value.toUpperCase();
            const tickerDataRaw = rawTickerData.split(',');
            const modelList = ["AAPL","MSFT","NVDA","AMZN","JNJ","JPM","XOM","CAT","PG","NEE"];
            let validData = true;

            let tickerDataSet = new Set(tickerDataRaw);
            const tickerData = Array.from(tickerDataSet);
            console.log(tickerData);

            outputParagraph.textContent = "LOADING";

            for (const ticker of tickerData)
            {
                if (!modelList.includes(ticker))
                {
                    validData = false;
                    break;
                }
            }
            
            
            
            
            if (!tickerData || isNaN(initialBudget.value) || tickerData.length < 3) {
                outputParagraph.textContent = "Please enter three or more stock tickers. Comma separated with no spaces.";
                return;
            }

            if (tickerData.length > modelList.length)
            {
                outputParagraph.textContent = "Ticker list has exceeded the number of avaliable stocks.";
                return;
            }

            if (!validData)
            {
                outputParagraph.textContent = "One of the tickers entered above is not in the avaliable list above. Please enter a stock symbol from above.";
                return;
            }

            let initialMoney = initialBudget.value;
            if (initialMoney.length === 0)
            {
                outputParagraph.textContent = "Please input your initial budget.";
                return;
            }
            
        
            outputParagraph.textContent = "Sending data to API for processing...";

            fetch(API_URL, {
            method: 'POST', 
            headers: {
                
                'Content-Type': 'application/json' 
            },
            // Must match Pydantic model specified earlier
            body: JSON.stringify({
                tickers: tickerData, 
                initial_value: initialMoney,
                weights: [],
                expected_return: 0,
                expected_variance: 0,
            })
        })


        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP Error! Status: ${response.status}. Check console for details.`);
            }
            // If success re
            return response.json(); 
        })
        .then(data => {
            // 4. Handle the successful response from FastAPI
            const tickersList = data.tickers.join(', ');
            
            // Create a formatted list of tickers with their weights as percentages
            const weightsDisplay = data.tickers.map((ticker, index) => {
                const weight = (data.weights[index] * 100).toFixed(2);
                return `${ticker}: ${weight}%`;
            }).join('<br>');
            console.log(data.expected_return);
            outputParagraph.innerHTML = `**Success!** Data processed.<br>
                                         **Tickers:** ${tickersList}<br>
                                         **Budget:** $${data.initial_value.toFixed(2)}<br>
                                         <br><strong>Portfolio Weights:</strong><br>
                                         ${weightsDisplay}
                                         <br><br>Expected Portfolio Return: $${data.expected_return}</br></br>
                                         Expected Portfolio Variance: ${data.expected_variance.toFixed(5)}`;
            console.log("API Response Data:", data);
        })
        .catch(error => {
            // 5. Handle any errors (network, parsing, HTTP status error)
            outputParagraph.textContent = `ERROR: Failed to process data. ${error.message}`;
            console.error("Fetch operation failed:", error);
        });
        });
    });