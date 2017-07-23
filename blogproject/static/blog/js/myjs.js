/**
 * Created by Administrator on 2017/7/22.
 */
//页面加载完毕之后执行  js写法
// window.onload = function ()
// {
// var btn = document.getElementById('top');
// var timer = null;
// var isTop = true;
// // var osTop = document.documentElement.scrollTop || document.body.scrollTop;
// var osTop = document.body.scrollTop;
// var clientheight = document.documentElement.clientHeight  //获取页面可视区域的高度
//   window.onscroll = function () {
//       if(osTop>=clientheight){
//             btn.style.display = "block";
//         }else{
//              btn.style.display = "none";
//         };
//       if(!isTop){
//           clearInterval(timer);
//       }isTop=false;
//   }
//
//         btn.onclick = function () {
//             timer = setInterval(function(){
//                 var osTop = document.documentElement.scrollTop || document.body.scrollTop;  //获取滚动条距离顶部的距离
//                 var ispeed= Math.floor(-osTop/6);
//                 document.documentElement.scrollTop = document.body.scrollTop = osTop+ispeed;
//                 if (osTop == 0){
//                     clearInterval(timer);
//                     isTop = false;
//                 }
//             },30);
//
//         }
// }

// jquery写法
$(function () {
    var btn = document.getElementById('top');
    var timer = null;
    var osTop = document.documentElement.scrollTop || document.body.scrollTop;
    var clientheight = document.documentElement.clientHeight  //获取页面可视区域的高度
    $(window).scroll(function () {
        if($(window).scrollTop()>1.5*clientheight){
            $("#top").css('display','block');
           // $("#top").style.display="block";
           //  alert($(window).scrollTop());
        }
     else{
            $("#top").css('display','none');
     }
    })
        btn.onclick = function () {
            timer = setInterval(function(){
                var osTop = document.documentElement.scrollTop || document.body.scrollTop;  //获取滚动条距离顶部的距离
                var ispeed= Math.floor(-osTop/6);
                document.documentElement.scrollTop = document.body.scrollTop = osTop+ispeed;
                if (osTop == 0){
                    clearInterval(timer);
                }
            },30);
        }
})