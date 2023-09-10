const resultMessage = document.querySelector("#result");

// Function to predict car price
function predictCarPrice() {
    document.querySelector("#carForm").addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting via the browser.

        const formData = {
            "brand": [document.querySelector("#make").value],
            "year": [parseInt(document.querySelector("#year").value)],
            "fuel": [document.querySelector("#fuel").value],
            "gearbox": [document.querySelector("#transmission").value],
            "mileage (kms)": [parseInt(document.querySelector("#mileage").value)]
        };

        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        };

        fetch("http://127.0.0.1:5000/predict", requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data.predicted_price);
                resultMessage.textContent = "Predicted Price: " + data.predicted_price;
            })
            .catch(error => {
                console.log("ERROR: ", error);
                resultMessage.textContent = "Error occurred while predicting the price.";
            });
    });
}

// Initialize the prediction function
predictCarPrice();
