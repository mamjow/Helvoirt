$(document).ready(function () {

    $('#login-button').click(function () {
        var username = $('#user_name').val();
        var password = $('#user_password').val();

        var login_button = $('#login-button-msg');
        login_button.html('inloggen...');

        var login_icon = $('#login-button-icon');
        login_icon.removeClass(' fa-sign-in-alt').addClass('fa-spinner fa-spin');

    });

    $('#LoginForm').on('submit', function (event) {
        var username = $('#user_name').val();
        var password = $('#user_password').val();
        var login_icon = $('#login-button-icon');
        var login_button = $('#login-button-msg');
        var ajax_err = $('#ajax-errors');

        event.preventDefault();
        var form = $(this).closest("form");
        $.ajax({
            url: form.attr("data-validate-username-url"),
            data: form.serialize(),
            dataType: 'json',
            success: function (response) {
                if (response.message == "username") {

                    ajax_err.css('display', 'block');
                    ajax_err.find('span').html('Ops. Your username does not exits!')
                    login_button.html('inloggen');
                    login_icon.removeClass('fa-spinner fa-spin').addClass('fa-arrow-circle-right');
                }
                if (response.message == "password") {

                    ajax_err.css('display', 'block');
                    ajax_err.find('span').html('Ops. Your password is wrong!')
                    login_button.html('inloggen');
                    login_icon.removeClass('fa-spinner fa-spin').addClass('fa-arrow-circle-right');
                }

                if (response.message == "success") {
                    $.ajax({
                        type: "POST",
                        url: '/login/',
                        data: {
                            username: username,
                            password: password,
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                        },
                        success: function () {

                            login_button.html('ingelogged');
                            login_icon.removeClass('fa-spinner fa-spin').addClass(' fa-sign-in-alt');
                            $('#LoginModal').modal('hide');
                            location.reload();

                        },
                        error: function () {
                            var ajax_err = $('#ajax-errors');
                            ajax_err.css('display', 'block');
                            ajax_err.find('span').html('Ops. Something went wrong. Please try again!')
                        },

                    })
                }


                console.log(response.message);
            },
            error: function (response) {
                var ajax_err = $('#ajax-errors');
                console.log(response.status.toString());
                ajax_err.css('display', 'block');
                ajax_err.find('span').html('Wrong combination of username and password');
                login_button.html('inloggen');
                login_icon.removeClass('fa-spinner fa-spin').addClass('fa-arrow-circle-right');
            }

        });


    });


});