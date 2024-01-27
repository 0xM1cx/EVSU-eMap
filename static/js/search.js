// Rooms List in Array
const engBuilding = ["EB215", "EB216", "EB219"];

// Get elements by ID
const searchedRoom = document.getElementById('search');
const searchButton = document.getElementById('search-button');

// Common coordinates for all rooms in the building
const commonCoordinates = { x: 100, y: 200 };

// Get canvas and context
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

// Image object
const image = new Image();
image.src = 'path/to/your/image.jpg';

// Once the image is loaded, draw it on the canvas
image.onload = function() {
  ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
};

// Search function
const search = () => {
  const room = searchedRoom.value.toUpperCase();  // Assigns the value of the searched room 

  if (engBuilding.includes(room)) {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the image at the specified coordinates
    ctx.drawImage(image, commonCoordinates.x, commonCoordinates.y, canvas.width, canvas.height);
  }
};

// Event listener for the search button
searchButton.addEventListener('click', search);