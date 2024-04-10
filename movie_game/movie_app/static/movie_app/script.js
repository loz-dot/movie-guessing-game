document.addEventListener('DOMContentLoaded', function() {
function fetchDataAndRender() {
    console.log("pressed");
    fetch('/refresh/')
        .then(response => response.text())
        .then(data => {
            document.getElementById('home-screen').innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

document.getElementById('startButton').addEventListener('click', fetchDataAndRender);
document.getElementById('continue').addEventListener('click', fetchDataAndRender);
});