const filterPlace = $('.filter').offset().top;
const filterOffset =
  $(window).width() - $('.filter').offset().left - $('.filter').width() - 30;
const filterWidth = $(window).width() - $('.filter').offset().left;
// console.log($('.filter').offset().left);
console.log($(window).width());

$(window).click(function (e) {
  if (e.target.classList[1] != 'input') {
    $('#d1').fadeOut('fast');
    $('#d2').fadeOut('fast');
  }
}); //ком

$(window).scroll(function () {
  const scrollHeight = $(this).scrollTop();

  // console.log(filterOffset);
  console.log(filterWidth);

  if ($(window).width() > 768) {
    if (filterPlace < scrollHeight) {
      $('.filter').addClass('filter-active');
      $('.filter').css({ 'padding-right': filterOffset, width: filterWidth });
    } else {
      $('.filter').removeClass('filter-active');
      $('.filter').css({ 'padding-right': '6%', width: '33.33333%' });
    }
  }
});

$('.filter__need').click(function (e) {
  $('#d1').fadeToggle('fast');
  let position = $('.filter__need').offset();
  let top = position.top + $('.filter__need').innerHeight();
  let left = position.left;

  $('#d2').fadeOut('fast');

  $('#d1').css({
    top: top,
    left: left,
    width: $('.filter__need').innerWidth(),
  });
});

$('.filter__specialization').click(function (e) {
  $('#d2').fadeToggle('fast');
  let position = $('.filter__specialization').offset();
  let top = position.top + $('.filter__specialization').innerHeight();
  let left = position.left;
  $('#d1').fadeOut('fast');

  $('#d2').css({
    top: top,
    left: left,
    width: $('.filter__need').innerWidth(),
  });
});

$('.dropdown__item').click(function (e) {
  $('#d1').fadeOut('fast');
  $('#d2').fadeOut('fast');
  let tar = $(e.target);

  // console.log(tar.parent().attr('id'));
  // console.log(tar.text());
  if (tar.parent().attr('id') == 'd1') {
    $('.filter__need').val(tar.text());
  } else {
    $('.filter__specialization').val(tar.text());
  }
});

$('.filter__need').keyup(function (e) {
  let tar = $(e.target);
  let value = tar.val();
  $('#d1').fadeIn('fast');

  $.each($('#d1 > .dropdown__item'), function (indexInArray, valueOfElement) {
    if ($(valueOfElement).text().indexOf(value) == -1) {
      $(valueOfElement).hide();
    } else {
      $(valueOfElement).show();
    }
  });
});

$('.filter__specialization').keyup(function (e) {
  let tar = $(e.target);
  let value = tar.val();
  $('#d2').fadeIn('fast');

  $.each($('#d2 > .dropdown__item'), function (indexInArray, valueOfElement) {
    if ($(valueOfElement).text().indexOf(value) == -1) {
      $(valueOfElement).hide();
    } else {
      $(valueOfElement).show();
    }
  });
});

//reset button

$('.filter__reset').click(function (e) {
  $('.filter__specialization').val('');
  $('.filter__need').val('');
});

$('.mobile-filter').click(function (e) {
  // $('.filter').toggle();
  $('.filter').toggleClass('hidden');
});
