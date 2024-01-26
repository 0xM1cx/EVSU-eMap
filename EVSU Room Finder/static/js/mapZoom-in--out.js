// Zoom-in-Zoom-Out function for the map

let currentZoom = 1;

function zoomIn() {
    currentZoom += 0.2;
    applyZoom();
}

function zoomOut() {
    currentZoom -= 0.2;
    applyZoom();
}


function applyZoom() {
    const map = document.querySelector('.map');
    map.style.transform = `scale(${currentZoom})`;
}