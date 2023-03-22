'use strict';

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
    .then((data) => alert(data))

}


function removeFromFavorite(recipe_link) {
    console.log(recipe_link)
    const removed_recipe = {
    recipe_link: recipe_link,
    }
    
    fetch('/remove_saved_recipe', {
    method: 'POST',
    body: JSON.stringify(removed_recipe),
    headers: {'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then((data) => {
    if (data.success) {
        alert('Sucessfully removed recipe!');  
    } 
    // console.log(data)
    
    })
}
