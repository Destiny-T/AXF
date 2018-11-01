$(function(){
    $('.register').width(innerWidth)

    // 失去焦点
    // 用户名输入完成，发起ajax请求，验证用户名是否能用
    $('#account').blur(function(){
        console.log($(this).val())
        $.get('/axf/checkuser/',{'account':$(this).val()},function(response){
            console.log(response)
            if(response['status'] == '-1'){
                $('#accounterr').show().html(response['msg'])
            }else{
                $('#accounterr').hide()
            }

        })
    })


    $('#password').blur(function () {
        var password = $(this).val()
        if(password.length<6 || password.length>12){
            $('#passworderr').show()
        }else{
            $('#passworderr').hide()
        }
    })
})