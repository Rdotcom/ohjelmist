document.addEventListener("DOMContentLoaded", function () {
let targetelement = document.getElementById("target");
    let htmlcode = "<li>First</li><li>Second item</li><li>Third item</li>";
    targetelement.innerHTML = htmlcode;
    targetelement.classList.add("my-list")
});