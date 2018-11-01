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

})