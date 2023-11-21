'use strict';
let targetelement = document.getElementById("target");
    let listitem1 = document.createElement("li");
    let listitem2 = document.createElement("li");
    let listitem3 = document.createElement("li");

    listitem1.textContent= "First item";
    listitem2.textContent= "Second item";
    listitem2.classList.add("my-item");

    listitem3.textContent= "Third item";

    targetelement.appendChild(listitem1);
    targetelement.appendChild(listitem2);
    targetelement.appendChild(listitem3);