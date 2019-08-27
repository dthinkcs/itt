function start() {


  var table = document.querySelector("table");

  var row = table.insertRow(0);
  var cell0 = row.insertCell(0);
  var cell1 = row.insertCell(1);
  var cell2 = row.insertCell(2);
  cell0.innerHTML = "<b>n</b>";
  cell1.innerHTML = "<b>n<sup>2</sup></b>";
  cell2.innerHTML = "<b>n<sup>3</sup></b>";

  for (var i = 0; i <= 10;  i++) {
    var row = table.insertRow(i + 1);
    var cell0 =  row.insertCell(0);
    var cell1 = row.insertCell(1);
    var cell2 = row.insertCell(2);
    cell0.innerHTML = i;
    cell1.innerHTML = i * i;
    cell2.innerHTML = i * i * i;
  }
}
