console.log("loaded..");



$.ajax({
  url: '/studentdata',
  type: 'get',
  success: function(response){
  	console.log(typeof(response));
    res = JSON.parse(response); 
    console.log(typeof(res));

    console.log(res.msg);
    //console.log(res["msg"]);


    console.log(res.students); 


    //table update

    tr = ''
   $.each(res.students, function(i, item) {  



      
      tr += "<tr><td>" + 
      item.name + "</td><td>" +
       item.email_id + "</td><td>" +
        item.gender + "</td><td>"
         item.address_line + "</td></tr>";
    });

    
    $('#tbody').append(tr);
  
  

    }


 
});