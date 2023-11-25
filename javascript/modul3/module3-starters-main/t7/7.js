'use strict';
const triggerElement = document.getElementById('trigger');
const targetImage = document.getElementById('target');
const image = 'img/picA.jpg';
const hoverimage = 'img/picB.jpg';

triggerElement.addEventListener('mouseover', function() {
  targetImage.src = hoverimage;
});

triggerElement.addEventListener('mouseout', function() {
  targetImage.src = image;
});