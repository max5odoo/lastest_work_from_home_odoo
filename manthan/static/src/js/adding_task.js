function myCreateFunction(){
var table_ref=document.getElementById('myTable');
var tr_create=document.createElement('tr');
var course_cnt_ref = document.getElementById('record_cnt');
var tr_cnt = table_ref.rows.length;
console.log(`this is the table length: ${tr_cnt}`)
var td_create,inputs
for (var i=0;i<2;i++)
{
    td_create=document.createElement('td');
    inputs=document.createElement('input');
    if (i==0)
    {
        inputs.setAttribute('name',`task_name${tr_cnt}`);
    }
    else
    {
     inputs.setAttribute('name',`task_description${tr_cnt}`);
    }
    td_create.appendChild(inputs);
    tr_create.appendChild(td_create);
}
cnt_val = parseInt(course_cnt_ref.value)  + parseInt(1);
console.log(`this is the count value: ${cnt_val}`)
course_cnt_ref.setAttribute('value',cnt_val);
var last_table=table_ref.appendChild(tr_create);
cell = last_table.insertCell(-1);
var btnRemove = document.createElement("INPUT");
btnRemove.type = "button";
btnRemove.value = "Remove";
btnRemove.setAttribute("onclick", "Remove(this)");
cell.appendChild(btnRemove);
};
function Remove(button) {
console.log("this is the delete button")
            //Determine the reference of the Row using the Button.
            var row = button.parentNode.parentNode;
            console.log(`this is the row  value: ${row}`)
            var name = row.getElementsByTagName("TD")[0].innerHTML;
            console.log(`this is the row  name: ${name}`)
            if (confirm("Do you want to delete: " + name)) {

                //Get the reference of the Table.
                var table = document.getElementById("myTable");

                //Delete the Table row using it's Index.
                table.deleteRow(row.rowIndex);
            }
        }