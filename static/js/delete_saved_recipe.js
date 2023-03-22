'use strict';


// const removeFavoriteButton = document.querySelector('.remove-favorite');

// removeFavoriteButton.addEventListener('click', () => {
//     const recipeLink = 'Favorite_recipe.recipe_link'; 
//     const userId = 'Favorite_recipe.user_id'; 
//     removeFromFavorite(recipeLink, userId);
//     });

function removeFromFavorite(recipe_link, user_id) {
    const removed_recipe = {
    recipe_link: recipe_link,
    user_id: user_id,
    }
    console.log(recipe_link);
    console.log(user_id);
    
    fetch('/remove_saved_recipe', {
    method: 'POST',
    body: JSON.stringify(removed_recipe)
    })
    .then((response) => response.json())
    .then((data) => {
    if (data.success) {
        alert('Sucessfully removed recipe!');  
    } else {
        alert('Error removing recipe.');
    console.log();
    }
    })
    // .catch(function(error) {
    // console.error('Error from removing recipe:', error);
    // alert('Error removing recipe.');
    // });
}
