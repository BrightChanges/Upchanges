//
// $(document).ready(function(){
// 		$("#Welcome_model").modal('show');
// 	});

$(document).ready(function(){
//loads when document is ready

if (document.cookie.indexOf('modal_shown=') >= 0) {
 //do nothing if modal_shown cookie is present
} else {
  $('#Welcome_model2').modal('show');  //show modal pop up
  document.cookie = 'modal_shown=seen'; //set cookie modal_shown
  //cookie will expire when browser is closed
}

});









// $(document).ready(function(){
//             setTimeout(function(){
//             if(!Cookies.get('modalShown')) {
//                 $("#Welcome_model").modal('show');
//               Cookies.set('modalShown', true);
//             } else {
//                 // alert('Your modal won\'t show again as it\'s shown before.');
//             }
//
//     },6000);
//  });







// $(document).ready(function() {
// if ($.cookie("decline") == null) {$('#Welcome_model').appendTo("body");
//
// function show_modal(){
//
// $('#Welcome_model').modal();
//
// }
//
// window.setTimeout(show_modal, 500);
//
// }
//
// $("#close").click(function() {var date = new Date();
//
//     var minutes = 1;
//
//     date.setTime(date.getTime() + (minutes * 60 * 24));
//
//     $.cookie("decline", "true", { expires: date, path: '/' });
//
//     });
//
// });

