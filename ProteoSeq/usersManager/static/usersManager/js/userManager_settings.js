$('#register_link').on('click',function(){
    var register_url = $(this).attr('name');
    window.location.replace(register_url);
});

$('#login_link').on('click',function(){
    var login_url = $(this).attr('name');
    window.location.replace(login_url);
});
