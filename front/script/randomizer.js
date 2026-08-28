const form = document.getElementById("randomizer");
const result = document.getElementById("random-result");
const nextButton = document.getElementById("next-button");

const category = form.dataset.category;
const nextPage = form.dataset.next;

let currentChoice = null;


form.addEventListener("submit", async function(event) {
    event.preventDefault();

    try {
        const response = await fetch(
            `/api/random-select.py?category=${encodeURIComponent(category)}`
        );

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();

        currentChoice = data.value;

        result.textContent = currentChoice;
        nextButton.disabled = false;
    }
    catch (error) {
        console.error(error);
        result.textContent = "Unable to generate a choice.";
    }
});


nextButton.addEventListener("click", function() {
    if (currentChoice === null) {
        return;
    }

    sessionStorage.setItem(category, currentChoice);

    window.location.href = nextPage;
});
