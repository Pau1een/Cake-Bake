function replaceFact(results) {
    document.querySelector('#facts-text').innerHTML = results;
    }
    
    function showFact(evt) {
        fetch('/facts')
        .then((response) => response.text())
        .then(replaceFact);
    }
    
    document.querySelector('#get-fact-button').addEventListener('click', showFact);
