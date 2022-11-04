const filterPlace = $('.filter').offset().top;
const filterOffset =
  $(window).width() - $('.filter').offset().left - $('.filter').width() - 30;
const filterWidth = $(window).width() - $('.filter').offset().left;

$(window).click(function (e) {
  if (e.target.classList[1] != 'input') {
    $('#d1').fadeOut('fast');
    $('#d2').fadeOut('fast');
  }
});

$(window).scroll(function () {
  const scrollHeight = $(this).scrollTop();

  // console.log(filterOffset);
  // console.log(filterWidth);

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
    let filter = $('.filter__need');
    console.log(filter.val);

    if (filter.val() == "") {
      filter.val(tar.text())

    } else if (filter.val().indexOf(tar.text())==-1) {
      filter.val(filter.val() + ", " + tar.text())
    }
  } else {
    let filter = $('.filter__specialization');
    console.log(filter.val);
    if (filter.val() == "") {
      filter.val(tar.text())
    } else if (filter.val().indexOf(tar.text())==-1) {
      filter.val(filter.val() + ", " + tar.text())
    }
  }
});

$('.filter__need').keyup(function (e) {
  let tar = $(e.target);
  let value = tar.val();
  $('#d1').fadeIn('fast');

  $.each($('#d1 > .dropdown__item'), function (indexInArray, valueOfElement) {
    if ($(valueOfElement).text().toUpperCase().indexOf(value.toUpperCase()) == -1) {
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
    if ($(valueOfElement).text().toUpperCase().indexOf(value.toUpperCase()) == -1) {
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


// SEARCH

$('.filter__accept').click(function (e) { 
  e.preventDefault()

  // console.log(window.location.pathname);

  if (window.location.pathname == "/") {
    urll = "ajax";
  } else {
    urll = "../ajax";
  }

  $.ajax({
    url: urll,
    success: function (response) {
      data = JSON.parse(response.data);
      let data2 = [];
      for (let i = 0; i < Object.keys(data).length; i++) {
        const element = data[i].fields.name;
        data2.push(element);
      }
      const cat = $('.filter__need').val().split(', ')

      let cats = ''

      for (let i = 0; i < cat.length; i++) {
        g = i
        item = data2.indexOf(cat[i]) + 1
        if (i == 0){
          cats = cats + item
        } else{
          cats = cats + ',' + item
        }
      }

      const host = response.host
      const link = `http://${host}/search/?cats=${cats}`;
      if (cats == 0) {
        return
      }
      window.location.replace(link);
    },
    error: function (response) {
      console.log(response)
      console.log("fail");
    }
  });

  // $.ajax({
  //   data: $(this).serialize(), // получаяем данные формы
  //   url: "{% url 'validate_username' %}",
  //   // если успешно, то
  //   success: function (response) {
  //       if (response.is_taken == true) {
  //           $('#id_username').removeClass('is-valid').addClass('is-invalid');
  //           $('#id_username').after('Это имя пользователя недоступно!')
  //       }
  //       else {
  //           $('#id_username').removeClass('is-invalid').addClass('is-valid');
  //           $('#usernameError').remove();
  //       }
  //   },
  //   // если ошибка, то
  //   error: function (response) {
  //       // предупредим об ошибке
  //       console.log(response.responseJSON.errors)
  //   }
  // });

  // path = `http://127.0.0.1:8000/search/?cats=${},16`
  // window.location.replace(path);
});