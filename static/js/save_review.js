'use strict';

const saveButton = document.querySelector("saveButton").addEventListener('submit', (evt) => {
    evt.preventDefault();

const reviewText = document.querySelector('#review').value;
    saveReview(reviewText);
})

const saveReview = (review) => {
    const body = {
        reviews: review,
    }
    fetch('/save_review', {
        method: "POST",
        body: JSON.stringify(body),
        recipe_link: JSON.stringify(body),
    })
    .then((response) => response.text())
    .then((data) => console.log(data))

}


// const saveReview = (review) => {
//     const body = {
//         reviews: review,
//     }
//     fetch('/save_review', {
//         method: "POST",
//         body: JSON.stringify(body),
        
//     })
//     .then((response) => response.text())
//     .then((data) => alert(data))

// }