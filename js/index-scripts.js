$(window).scroll(function() {
  if ($(this).scrollTop() > 50) /*height in pixels when the navbar becomes non opaque*/ {
    $('.opaque-navbar').addClass('opaque');
  } else {
    $('.opaque-navbar').removeClass('opaque');
  }
});
// $(document).ready(function() {
//   $("#profile").click(function() {
//     event.preventDefault();
//     $('html,body').animate({
//       scrollTop: 940
//     }, 'slow');
//   });
//   $("#blog").click(function() {
//     event.preventDefault();
//     $('html,body').animate({
//       scrollTop: 2000
//     }, 'slow');
//   });
// });
