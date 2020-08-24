  function filterTable() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    var elementsLength = 0;
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
          elementsLength++
        } else {
          tr[i].style.display = "none";
        }
      }
    }
    document.getElementById("elementId").innerHTML = 'Records Count : ' +elementsLength;
  }


  function sortTable(n) {
    var table,element, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    element = document.getElementById("wrapper").querySelectorAll("a"); 
    
    table = document.getElementById("myTable");
    switching = true;
    dir = "asc";
    while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        if (dir == "asc") {
          var ii = 0;
          for (ii = 0; ii < element.length; ii++) {
            element[ii].classList.remove('fa-sort-alpha-desc')
            element[ii].classList.add('fa-sort-alpha-asc')
  }
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          var ii = 0;
          for (ii = 0; ii < element.length; ii++) {
            element[ii].classList.remove('fa-sort-alpha-asc')
            element[ii].classList.add('fa-sort-alpha-desc')}
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
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

  function animateValue(id, start, end, duration) {
    var obj = document.getElementById(id);
    if(obj){
      var range = end - start;
      var current = start;
      var increment = end > start? 1 : -1;
      var stepTime = Math.abs(Math.floor(duration / range));
      var timer = setInterval(function() {
          current += increment;
          obj.innerHTML = current;
          if (current == end) {
              clearInterval(timer);
          }
      }, stepTime);  
    }
    else{ 
    }
  }
