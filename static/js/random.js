'use strict';
console.log("connected file")

    const displayFact = () => {
        const factContainer = document.querySelector('#facts-text');
        console.log("connected fact")
        
        fetch('/facts', {
            method: "GET",
            headers: {'Content-Type': 'application/json'
            },
        })
        .then((response) => response.text())
        .then((data) => factContainer.innerHTML=data)
    }
    
    