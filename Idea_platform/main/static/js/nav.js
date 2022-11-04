$('.header__profile-link').click(function (e) { 
    e.preventDefault();
    console.log("123");
    $('.profile-dropdown').slideToggle('fast');
    $('.header__profile-link').toggleClass('header__profile-link--active');
  });