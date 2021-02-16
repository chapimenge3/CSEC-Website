$(document).ready(function () {
  $('.dropdown-toggle').dropdown();
  $('.toast').toast('show');
  
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    // console.log(scroll);
    if (scroll > 2000) {
      $(".navbar").css("background", "#E8DBC3");
    } else if (scroll > 1425) {
      $(".navbar").css("background", "#ebece7");
    } else if (scroll > 500) {
      $(".navbar").css("background", "#dcd7d3");
    } else if (scroll > 10) {
      $(".navbar").css("background", "#e4e0dd");
    } else {
      $(".navbar").css("background", "#eeebdf");
    }
  });
});
