'use strict';
const headers = {
    'Content-Type': 'application/json'
}

const saveToFavorite = (recipe) => {
    const body = {
        favorite_name: recipe.recipe.label,
        favorite_img: recipe.recipe.image,
        favorite_ingredients: recipe.recipe.ingredientLines,
        favorite_source: recipe.recipe.source,
        recipe_link: recipe.recipe.url
    }
    fetch('/save_recipe', {
        method: "POST",
        body: JSON.stringify(body),
        headers: headers
    })
    .then((response) => response.text())
    .then((data) => console.log(data))

}

// function selectRecipeButton(new_array) {
// const buttons = document.querySelectorAll('button');

// for(const button of buttons) {
//     button.addEventListener('click', (evt) => {
//         evt.preventDefault();

//         const info = evt.target.value;
//         const new_array = info.split(",)");
//         console.log(new_array);
//     });
//     fetch('/save_recipe')
//     .then((response) => response.text())
//     .then(selectRecipeButton);

// }}

// const saveRecipe = async (event) => {
//     document.querySelector('#recipe_box');
//     event.preventDefault();
//     const form = event.target;
//     const formData = new FormData(form);
//     const response = await fetch("/save_recipe", {
//         method: "POST",
//         body: formData,
//     });
//     const recipe = await response.json();
    
// };

