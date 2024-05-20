async function calculate() {
  const a = document.getElementById("a").value;
  const b = document.getElementById("b").value;

  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = '';

  if (a === '' || b === '') {
      resultsDiv.innerHTML = 'Please enter both numbers.';
      return;
  }

  const operations = ["add", "subtract", "multiply", "divide"];
  const promises = operations.map(op => fetch(`http://127.0.0.1:8000/${op}`, {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({ a: parseFloat(a), b: parseFloat(b) })
  }).then(response => response.json()));

  try {
      const results = await Promise.all(promises);

      results.forEach((result, index) => {
          if (result.detail) {
              resultsDiv.innerHTML += `<p>${operations[index]}: ${result.detail}</p>`;
          } else {
              resultsDiv.innerHTML += `<p>${operations[index]}: ${result.result}</p>`;
          }
      });
  } catch (error) {
      resultsDiv.innerHTML = 'An error occurred while processing your request.';
  }
}