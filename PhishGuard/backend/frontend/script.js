const button = document.getElementById("analyzeBtn");

console.log("Script Loaded!");

button.addEventListener("click", async () => {

    console.log("Button Clicked!");

    const url = document.getElementById("urlInput").value;

    try {

        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();

const result = document.getElementById("result");

result.innerHTML = data.prediction;

if (data.prediction.includes("SAFE")) {
    result.style.color = "#22c55e";
}
else {
    result.style.color = "#ef4444";
}

    } catch (error) {

        console.error(error);

        document.getElementById("result").innerHTML =
            "Error connecting to Flask API";
    }

});