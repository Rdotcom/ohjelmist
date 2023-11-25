'use strict';
function calculate() {
  const num1 = parseInt(document.getElementById('num1').value);
  const num2 = parseInt(document.getElementById('num2').value);
  const operator = document.getElementById('operation').value;

  let result;
  switch (operator) {
    case 'addition':
      result = num1 + num2;
      break;
    case 'subtraction':
      result = num1 - num2;
      break;
    case 'multiplication':
      result = num1 * num2;
      break;
    case 'division':
      if (num2 !== 0) {
        result = num1 / num2;
      } else {
        result = 'Cannot divide by zero';
      }
      break;
    default:
      result = 'Invalid operator';
  }

  document.getElementById('result').textContent = 'Result: ' + result;
}
