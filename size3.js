var inputString = prompt("Enter String: ");
for (var i = 0; i < inputString.length - 2; i++)
{
  for (var j = i + 1; j < inputString.length - 1; j++)
  {
    for (var k = j + 1; k < inputString.length; k++)
    {
      document.write(inputString[i] + inputString[j] + inputString[k] + "<br>");
    }
  }
}
