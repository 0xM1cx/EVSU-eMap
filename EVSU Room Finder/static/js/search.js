// Rooms List in Array
const engBuilding = ["EB215", "EB216", "EB219"];



const searchedRoom = document.getElementById('search');
const searchButton = document.getElementById('search-button');


const search = () => {

    const room = searchedRoom.value;  // Assigns the value of the searched room 

    if(engBuilding.includes(room)) {
        
    }
}

searchButton.addEventListener('click', search);