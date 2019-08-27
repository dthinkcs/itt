var inputString = prompt("Enter US Phone Number");

var areaCode = inputString.substring(inputString.indexOf("(") + 1, inputString.indexOf(")"));
var lastFourDigits = inputString.substring(inputString.indexOf("-") + 1);

var inputTagArr = document.getElementsByTagName("input");
inputTagArr[0].value = areaCode
inputTagArr[1].value = lastFourDigits
