function animateText(inputElement) {
    const value = inputElement.value; // Obtén el texto ingresado
    const animatedText = value
        .split("")
        .map(
            (char, index) => `
                <span style="
                    animation-delay: ${index * 50}ms;
                " class="glow-letter">${char}</span>
            `
        )
        .join(""); // Divide las letras, agrega animación y vuelve a unirlas
    
    inputElement.style.position = "relative"; // Asegura que la posición no rompa el layout
    inputElement.innerHTML = animatedText;
    console.log(animatedText)
}

function placeCaretAtEnd(element) {
    element.focus();
    if (typeof window.getSelection !== "undefined"
        && typeof document.createRange !== "undefined") {
        const range = document.createRange();
        range.selectNodeContents(element);
        range.collapse(false);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
    }
}


