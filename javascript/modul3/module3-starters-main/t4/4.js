'use strict';
let targetelement = document.getElementById("target");
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

for (let student of students) {
  let optionElement = document.createElement("option");
  optionElement.value = student.id;
  optionElement.textContent = student.name;
  targetelement.appendChild(optionElement);
}