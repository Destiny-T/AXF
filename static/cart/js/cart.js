$(function () {
    $('cart').width(innerWidth)


    total()


    $('.confirm-wrapper').on('click',function(){
        var cartid = $(this).attr('cartid')
        var $that = $(this)

        $.get('/axf/changecartstatus/',{'cartid':cartid},function(response){

            if (response['status'] == '1'){
                var isselect = response['isselect']
                $that.attr('isselect',isselect)

                $that.children().remove()
                if(isselect){
                    $that.append('<span class="glyphicon glyphicon-ok"></span>')
                    console.log($(this))
                }else{
                    $that.append('<span class="no"></span>')
                }

                total()
            }
        })
    })


    function total(){
        var sum = 0


        $('.goods').each(function () {
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')


            if ($confirm.find('.glyphicon-ok').length){
                var price = parseInt($content.find('.price').attr('str'))
                var num = parseInt($content.find('.num'),attr('str'))
                sum += num * price
            }
        })


        $('.bill .total b').html(sum)
    }
})