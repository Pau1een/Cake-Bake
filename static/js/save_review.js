
'use strict';

const saveButton = document.querySelector("#saveButton").addEventListener('submit', (evt) => {
    evt.preventDefault();

const reviewText = document.querySelector('#reviews').value;
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
        headers: {'Conten-Type': 'application/json'
        },
    })
    .then((response) => response.text())
    .then((data) => console.log(data))

}

