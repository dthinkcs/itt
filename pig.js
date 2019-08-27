


function printLatinWord() {
  var inputWords = document.getElementsByTagName("input")[0].value.split(" ");

  var outputString = "";


  for (var word of inputWords) {
    outputString += convertIntoPigLating(word) + " ";
  }
  document.write(outputString);
}


function convertIntoPigLating(s) {
  return s.substring(1) + s[0] + "ay";
}

function returnFalse() {
  return false;
}

// jump the computer
