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
    .then((data) => alert(data))

}
