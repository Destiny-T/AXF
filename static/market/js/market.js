$(function(){

    $('.market').width(innerWidth)
    // 获取下标 typeIndex
    typeIndex = $.cookie('typeIndex')
    console.log(typeIndex)
    if(typeIndex){ //存在 ，对应分类
         $('.type-slider .type-item').eq(typeIndex).addClass('active')

    }
    else{  // 不存在，默认就是热销榜
        $('.type-slider .type-item:first').addClass('active')
    }



    // 侧边栏点击处理
    $('.type-slider .type-item').click(function () {
        // 保存下标
        // console.log($(this).index())
        $.cookie('typeIndex',$(this).index(),{exprires:3,
        path:'/'})
    })



    // 分类 和 排序
    var alltypeBt = false
    var sortBt = false
    $('#allBt').click(function () {
        // 取反
        alltypeBt = !alltypeBt

        if (alltypeBt){
            $('.bounce-view.type-view').show()
            $('#allBt b').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')


            sortBt = false
            $('.bounce-view.sort-view').hide()
            $('#sortBt b').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        }else{
            $('.bounce-view.type-view').hide()
            $('#allBt b').removeClass('glyphicon-chevron-down').addClass('glyohicon-chevron-up')
        }
    })


    $('#sortBt').click(function () {
        // 取反
        sortBt = !sortBt

        if (sortBt){
            $('.bounce-view.sort-view').show()
            $('#sortBt b').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')


            alltypeBt = false
            $('.bounce-view.type-view').hide()
            $('#allBt b').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        }else{
            $('.bounce-view.sort-view').hide()
            $('#sortBt b').removeClass('glyphicon-chevron-down').addClass('glyohicon-chevron-up')
        }

    })




    // 购物车操作
    // 默认隐藏
    $('.bt-wrapper>.glyphicon-minus').hide()
    $('.bt-wrapper>.num').hide()

    //购物车数据不为0显示
    $('.bt-wrapper>.num').each(function () {
        if(parseInt($(this).html())){
            $(this).show()
            $(this).prev().show()
        }
    })





    // 加操作
    $('.bt-wrapper>.glyphicon-plus').click(function () {

        // console.log($(this))
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)

        //发起ajax请求
        $.get('/axf/addtocart/',{'goodsid':goodsid},function (response) {
            // console.log(response)

            if (response['status'] == '-1'){

                window.open('/axf/login/',target='_self')

            }else{
                console.log(response)
                // console.log($(this).prev())
                $that.prev().html(response['number']).show()
                $that.prev().prev().show()
            }
        })
    })

    $('.bt-wrapper>.glyphicon-minus').click(function () {
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)

        $.get('/axf/subtocart/',{'goodsid':goodsid},function (response) {

            if (response['status'] == '1'){
                var number = parseInt(response['number'])
                if (number>0){
                    $that.next().html(response['number'])
                }else{
                    $that.next().hide()
                    $that.hide()
                }
            }
        })
    })

})