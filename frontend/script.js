    document.addEventListener('DOMContentLoaded', function() {
        const tickers = document.getElementById('tickers');
        const initialValue = 
        const myButton = document.getElementById('submit');
        const outputParagraph = document.getElementById('output');

        myButton.addEventListener('click', function() {
            event.preventDefault();
            const tickerData = tickers.value;

            outputParagraph.textContent = "You entered: " + tickerData;
            console.log("Text from textbox: " + tickerData, ); // Optional: log to console
        });
    });