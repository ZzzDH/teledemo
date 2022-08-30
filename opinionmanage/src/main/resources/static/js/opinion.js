$(function (){
    $("#searchBtn").click(function (ev) {
        console.info("reload");
        var conditionSelect = $("#conditionSelect").val();
        var conditionInput = $("#conditionInput").val();
        var table=layui.table
        table.reload('reloadTb', {
            url: 'http://47.92.23.6:7002/ConditionSelect'
            , where: {
                conditionSelect: conditionSelect,
                conditionInput: conditionInput
            } //设定异步数据接口的额外参数

        });
    })

    $("#spiderBtn").click(function (ev){
        console.info("spider");
        var spiderContent=$("#spiderContent").val();
        console.log(spiderContent)
        $.ajax({
            type:'GET',
            url: 'http://47.92.23.6:7002/spider',
            async: true,
            cache: false,
            data: {'spiderContent':spiderContent},
            beforeSend:function (){
                return layer.msg('爬取中...');
            },
            success:function(res){
                if(res==='finish'){
                    layer.close()
                    layer.msg('完成！')
                }else{
                    layer.close()
                    layer.alert(res)
                }
            }
        })
    })


})