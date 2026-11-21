function classifyImage() {
    const file = document.getElementById("imageInput").files[0];

    if (!file) {
        alert("Please upload an image");
        return;
    }

    document.getElementById("type").innerText = "Plastic";
    document.getElementById("category").innerText = "Non-Biodegradable";
    document.getElementById("disposal").innerText = "Recycle";
}