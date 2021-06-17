console.log("Welcome to student controler 😅😅😅!!!");


//tr(no of rows) of tbody
tables_rows = document.getElementById('courseTable').children;

console.log(tables_rows)


sum = 0;

//based upon length of tr(no rows) - loop iterate for loop
for(var row=0;row < tables_rows.length ; row++)
{
	// td[4].innerHTML //price 
	priceColVal = tables_rows[row].children[3].children[0].innerHTML;
	console.log(priceColVal);
	//sum + sum + td[4] 
	sum +=  parseFloat(priceColVal);

}


console.log(`Total Price : ${sum.toFixed(2)}`)


//add totalPrice to HTML
document.getElementById("totalPrice").innerHTML = sum.toFixed(2);
