function myFunction() {
    console.log('star function creation');
    var mytr, mytd, myinput, tr_cnt;
    var table = document.getElementById("myTable");
    var total_rows = document.getElementById("total_row");
    tr_cnt = table.rows.length;
    tr_cnt += 1;
    console.log(tr_cnt);
    mytr = document.createElement('tr');
    for (var i = 0; i < 3; i++) {

        console.log('star collom creation');
        // createcolumn object
        mytd = document.createElement('td');

        // inside column create input object
        myinput = document.createElement('input');

        // set atribute to input name couum by colum
        if (i == 0) {
            myinput.setAttribute('name', `course${tr_cnt}`);
        } else if (i == 1) {
            myinput.setAttribute('name', `length${tr_cnt}`);
        } else if (i == 2) {
            myinput.setAttribute('name', `amount${tr_cnt}`);
        }

        // inside column input tag as child

        mytd.appendChild(myinput);

        // inside row place column tag as child
        mytr.appendChild(mytd);
        // for add delete colum child

    }
    var onerow = table.appendChild(mytr);
    // colum add at last 
    var cell = onerow.insertCell(-1);
    button_del = document.createElement('button');
    // button_del.type = 'button';
    button_del.value = 'remove';
    console.log('del step1');
    button_del.setAttribute('onclick', 'remove_row(this)');

    console.log('del step2');
    cell.appendChild(button_del);
    console.log('end collom creation');
    total_rows.setAttribute('value', tr_cnt);

}

function remove_row(del) {
    var table = document.getElementById("myTable");
    var find_row = del.parentNode;
    currnt_row = find_row.parentNode
    table.deleteRow(currnt_row);
    // find_row.deleteRow();
    console.log(find_row.parentNode);
}

function course_select(data) {
    console.log(data.value);
    myFunction();

    var table = document.getElementById("myTable");
    rowlen = table.rows.length;
    values = document.querySelector(`
            input[name = "course${rowlen}"]
            `);
    // find by name in tag 
    emelements = document.querySelector(`
            select[name = "courses_selection"]
            `);
    values.value = data.value;
    console.log(rowlen);
    console.log(emelements.value);

}