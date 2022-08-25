$(function (){
    $("#searchBtn").click(function (ev) {
        console.info("reload");
        alert("lala")
        var conditionSelect = $("#conditionSelect").val();
        var conditionInput = $("#conditionInput").val();
        table.reload('reloadTb', {
            url: 'http://localhost:8080/ConditionSelect'
            , where: {
                conditionSelect: conditionSelect,
                conditionInput: conditionInput
            } //设定异步数据接口的额外参数

        });
    })

})