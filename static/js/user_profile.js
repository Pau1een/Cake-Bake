'use strict';
const headers = {
    'Content-Type': 'application/json'
}

const updateProfile = (user) => {
    const body = {
        fname: user.user.fname,
        lname: user.user.lname,
        email: user.user.email,
        password: user.user.password,
    }
    fetch('/update_profile', {
        method: "POST",
        body: JSON.stringify(body),
        headers: headers
    })
    .then((response) => response.text())
    .then((data) => console.log(data))
    const usernameElement = document.getElementById('username');
    usernameElement.textContent = user.user.fname;
}

