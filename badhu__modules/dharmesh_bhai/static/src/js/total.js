 var rows = document.getElementById('t_body').children;
 var total = 0;
 console.log(rows.length);

 for (var i = 0; i < rows.length; i++) {
     //  priceColVal = tables_rows[row].children[3].children[0].innerHTML;

     total += parseFloat(rows[i].children[3].children[0].innerHTML);

 }
 console.log(total);
 console.log(total.toFixed(2));


 document.getElementById('total').innerHTML = total.toFixed(2);