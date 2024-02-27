//데탑용 마우스 올리면 슬라이드토클
document.querySelector('.menu1').addEventListener('mouseenter', () => {
	$('.sub1').slideDown()
});
document.querySelector('.menu1').addEventListener('mouseleave', () => {
	$('.sub1').slideUp()
});
document.querySelector('.menu2').addEventListener('mouseenter', () => {
	$('.sub2').slideDown()
});
document.querySelector('.menu2').addEventListener('mouseleave', () => {
	$('.sub2').slideUp()
});


//모바일용 아이콘 누르면 
const icon = document.querySelector('.toggle-btn');

$(document).ready(function(){
  $('.toggle-btn').click(function(){
    $('.nav_menu').slideToggle()
    icon.classList.toggle('active')
  });
});

$(document).ready(function(){
  $('.login-btn').click(function(){
    $('.sub1').slideToggle()
  });
});

$(document).ready(function(){
  $('.join-btn').click(function(){
    $('.sub2').slideToggle()
  });
});