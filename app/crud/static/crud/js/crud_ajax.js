$('#btnsubmit').click(function() {
    output = "";
    let sid = $('#stuid').val();
    let nm = $('#nameid').val();
    let em = $('#emailid').val();
    let pw = $('#passid').val();
    let csr = $('input[name=csrfmiddlewaretoken]').val();

    // Check if empty
    if(nm == ""){
        console.log('Enter Your name')
    } else if(em == ""){
        console.log('Enter Your email')
    } else if(pw == ""){
        console.log('Enter Your pw')
    }

    mydata = {id:sid, name:nm, email:em, password:pw, csrfmiddlewaretoken:csr}

    // AJAX GET & POST
    $.ajax({
        url: "/crud/",
        method: "POST",
        data: mydata,
        success: function(data) {
            stu = data.stu_deta
            if (data.status == 'save'){
                console.log('submited')
                $('#stuid').val('')
                $('form')[0].reset();
                for (i=0; i<stu.length; i++){
                    output += `<tr><td>` + stu[i].id + `</td>
                                <td>` + stu[i].name + `</td>
                                <td>` + stu[i].email + `</td>
                                <td>` + stu[i].password + `</td>
                                
                                <td><button type="button" data-sid="` + stu[i].id + `" class="btn btn-warning btn-sm btn-edit">Edit</button></td>
                                <td><button type="button" data-sid="` + stu[i].id + `" class="btn btn-danger btn-sm btn-del">Delete</button></td>`
                }
                $('#tbody').html(output);
            }
            if (data.status == 0){
                console.log('faild')
            }
        }
    });
});

// DELETE
$('tbody').on('click', '.btn-del', function() {
    console.log('clicked')
    let id = $(this).attr('data-sid')
    let csr = $('input[name=csrfmiddlewaretoken]').val();
    mydata = {sid:id, csrfmiddlewaretoken:csr}
    mythis = this;
    console.log(id)
    $.ajax({
        url: "/crud/delete",
        method: "POST",
        data: mydata,
        success: function(data) {
            if(data.status == 'delete'){
                $(mythis).closest('tr').fadeOut();
            }
            if(data.status == 0){
                console.log('not deleted')
            }
        }
    })
})

// EDIT
$('tbody').on('click', '.btn-edit', function() {
    let id = $(this).attr('data-sid')
    let csr = $('input[name=csrfmiddlewaretoken]').val();
    mydata = {sid:id, csrfmiddlewaretoken:csr}
    $.ajax({
        url: "/crud/update",
        method: "POST",
        data: mydata,
        success: function(data) {
            if(data.status == 'ok'){
                console.log(data.stu_deta.id)
                $('#stuid').val(data.stu_deta.id);
                $('#nameid').val(data.stu_deta.name);
                $('#emailid').val(data.stu_deta.email);
                $('#passid').val(data.stu_deta.pass); 
            }
            if(data.status == 0){
            }
        }
    
    })
})