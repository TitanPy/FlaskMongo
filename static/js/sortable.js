function sortTable(tableClass, n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementsByClassName(tableClass)[0];
    switching = true;
    dir = "asc";
    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];          
            var xContent = (isNaN(x.innerText))
                ? (x.innerText.toLowerCase() === '-')
                      ? 0 : x.innerText.toLowerCase()
                : parseFloat(x.innerText);
            var yContent = (isNaN(y.innerText))
                ? (y.innerText.toLowerCase() === '-')
                      ? 0 : y.innerText.toLowerCase()
                : parseFloat(y.innerText);
            if (dir == "asc") {
                if (xContent > yContent) {
                    shouldSwitch= true;
                    break;
                }
            } else if (dir == "desc") {
                if (xContent < yContent) {
                    shouldSwitch= true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount ++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
     }
  }