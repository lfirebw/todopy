document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("create-collection-form");
    const colorPicker = document.getElementById("color-picker");
    const colorInput = document.getElementById("color");

    colorPicker.addEventListener("input", function () {
        colorInput.value = colorPicker.value;
    });

    colorInput.addEventListener("input", function () {
        if (/^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/.test(colorInput.value)) {
            colorPicker.value = colorInput.value;
        }
    });
    colorInput.dispatchEvent(new Event("input"));
});