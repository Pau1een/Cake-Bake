'use strict';
console.log("save review file")
// const saveButton = document.querySelector("#saveButton").addEventListener('submit', (evt) => {
//     evt.preventDefault();

// const reviewText = document.querySelector('#reviews').value;
//     saveReview(reviewText);
// })

const saveReview = (recipe_link) => {
    console.log("saving review")
    const reviewText = document.getElementById(recipe_link).value;
    console.log(recipe_link)
    console.log(reviewText)
    const body = {
        review: reviewText, 
        recipe_link: recipe_link
    }
    fetch('/save_review', {
        method: "POST",
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'
        },
    })
    .then((response) => response.text())
    .then((data) => console.log(data))

}

