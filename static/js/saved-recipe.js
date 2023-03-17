const buttons = document.querySelectorAll('button');

for(const button of buttons) {
    button.addEventListener('click', (evt) => {
        evt.preventDefault();

        const info = evt.target.value;
        const new_array = info.split(",)");
        console.log(new_array);
    });
    
}


const saveRecipe = async (event) => {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const response = await fetch("/save_recipe", {
        method: "POST",
        body: formData,
    });
    const recipe = await response.json();
    
};

const form = document.querySelector("#recipe-search-results");
form.addEventListener("submit", saveRecipe);


    document.getElementById("myForm").addEventListener("submit", function(event) {
    Event.preventDefault()} 

    // make the fetch call
    
    )
