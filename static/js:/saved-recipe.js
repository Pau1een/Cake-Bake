const saveRecipe = async (event) => {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const response = await fetch("/save_recipe", {
        method: "POST",
        body: formData,
    });
    const recipe = await response.json();
    // your code here to display the recipe on the HTML page
};

const form = document.querySelector("#recipes/search");
form.addEventListener("submit", saveRecipe);

<script>
    document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    // get the form data
    const formData = new FormData(event.target);

    // make the fetch call
    fetch("/save_recipe", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
        throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        // do something with the response data
    })
    .catch(error => {
        console.error("There was a problem with the fetch call:", error);
    });
    });
</script>