'use strict';


function removeFromFavorite(recipe_link, user_id) {
    const removed_recipe = {
    recipe_link: recipe_link,
    user_id: user_id,
    }
    
    fetch('/remove_saved_recipe', {
    method: 'POST',
    body: JSON.stringify(removed_recipe)
    })
    .then((response) => response.json())
    .then((data) => {
    if (data.success) {
        alert('Sucessfully removed recipe!');  
    } 
    
    })
}
