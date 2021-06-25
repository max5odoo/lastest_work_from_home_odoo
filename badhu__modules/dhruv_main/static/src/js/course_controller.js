function addRow() {
			var course_cnt_ref = document.getElementById('record_cnt');
		


           //get table id for insert row
            var tableRef = document.getElementById('course_tb_1'); 
            //tr,td->input

            //get tr cnt
            tr_cnt = tableRef.rows.length;

            console.log(tr_cnt);

            var myTr =  document.createElement('tr');
            var myTd,myInput;
            for(var i=0;i<3;i++)
            {
                myTd = document.createElement('td');
                myInput = document.createElement('input');

                if(i==0)
                {
                	myInput.setAttribute('name',`course${tr_cnt}`); 

                }
                else if(i == 1)
                {
                	myInput.setAttribute('name',`created_by${tr_cnt}`);
                }
                else 
                {
                	myInput.setAttribute('name',`desc${tr_cnt}`);
                }

                myTd.appendChild(myInput);

                myTr.appendChild(myTd);
            }
            cnt_val = parseInt(course_cnt_ref.value)  + parseInt(1);
            course_cnt_ref.setAttribute('value',cnt_val);
            tableRef.appendChild(myTr);
}