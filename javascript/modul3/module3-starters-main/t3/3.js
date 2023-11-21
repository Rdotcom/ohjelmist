'use strict';
const targetElement = document.getElementById("target");
    const names = ["John", "Paul", "Jones"];
    let htmlcontent = "";

    for (let name of names) {
        htmlcontent += "<li>" + name + "</li>";
    }
    targetElement.innerHTML = htmlcontent;