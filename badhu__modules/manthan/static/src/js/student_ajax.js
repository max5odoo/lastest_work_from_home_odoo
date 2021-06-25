// $.ajax({url: "/studentajax",   type: 'GET',
//    dataType: 'dict',success: function(result){
//		console.log(result)
//    }});


$.getJSON('/studentajax')
    .done(function() { alert('request successful'); })
    .fail(function() { alert('request failed'); });