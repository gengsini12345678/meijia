/**
 * Created by Administrator on 2019/12/16.
 */
$(function(){

    // 当一级类型下拉列表发生变化时，触发改变事件
    $('#type1').change(function(){
        // 清空二级类型下列表中的所有子元素
        $('#type2').empty()
        $.ajax({
            url:'/goods/goodstype/',
            type:'GET',
            data:{
                'ajax_type_id':$('#type1').val()
            },
            success:function(response){
                // 将服务器返回的json字符串，转化成json对象
                json_obj = JSON.parse(response)
                for (index in json_obj){
                    //console.log(json_obj[i])
                    console.log(json_obj[index].fields.name,json_obj[index].pk)
                   //  DOM 操作，添加到网页的二级类型列表中
                    var $option = $('<option>')
                    $option.attr('value',json_obj[index].pk)
                    $option.text(json_obj[index].fields.name)
                    $('#type2').append($option)

                }

            },
            error:function(){
                console.log('请求失败')
            }
        })
    })
})