document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/halloween_data")
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
        })
        .catch(error => console.error("error fetching data:", error));
});
