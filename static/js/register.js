$(document).ready(function () {
    $('#register-button').click(function () {

        var NewUsername = $('#NewUserName').val();
        var password1 = $('#NewUserPass1').val();
        var password2 = $('#NewUserPass2').val();
        var NewUserEmail = $('#NewUserEmail').val;
        let UserError = $('#username-errors');
        var register_button = $('#register-button-msg');
        register_button.html('Aanmelden ...');

        var register_icon = $('#register-button-icon');
        register_icon.removeClass(' fa-user-plus').addClass('fa-spinner fa-spin');

        $('#SignUpForm').submit(function (e) {

            var register_button = $('#register-button-msg');
            var register_icon = $('#register-button-icon');

            event.preventDefault();
            var form = $(this).closest("form");

            $.ajax({
                url: form.attr("data-validate-existing-username-url"),
                data: form.serialize(),
                dataType: 'json',
                success: function () {
                    UserError.css('display', 'none');
                    $.ajax({
                        url: '/signup/',
                        type: "POST", // GET or POST
                        data: {
                            username: NewUsername,
                            password: password1,
                            'csrfmiddlewaretoken': csrfmiddlewaretoken
                        },
                        success: function (signup_response) {
                            if (signup_response.message == "Success") {

                                $.ajax({
                                    type: "post",
                                    url: '/login/',
                                    data: {
                                        username: NewUsername,
                                        password: password1,
                                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                                    },
                                    success: function () {
                                        register_button.html('ingelogged');
                                        register_icon.removeClass('fa-spinner fa-spin').addClass(' fa-user-plus');
                                        $('#SignUpModal').modal('hide');
                                        console.log(signup_response.message.toString());
                                        location.reload();
                                    },
                                    error: function () {
                                        var ajax_err = $('#ajax-errors');
                                        ajax_err.css('display', 'block');
                                        ajax_err.find('span').html('Ops. Something went wrong. Please try again!')
                                    },

                                })

                            }

                            if (signup_response.message == "Password-must-match") {
                                var ajax_err = $('#register-errors');

                                ajax_err.css('display', 'block');
                                ajax_err.find('span').html('Password must match');
                            }

                        }, /* end of Success */
                        error: function (signup_response) {
                            var ajax_err = $('#register-errors');
                            ajax_err.css('display', 'block');
                            ajax_err.find('span').html(signup_response.message)
                            console.log(signup_response)
                        }/*  end of error */
                    });
                    /*./ajax*/

                },
                error: function () {
                    var ajax_err = $('#register-errors');
                    ajax_err.css('display', 'block');
                    ajax_err.find('span').html('Gebruikersnaam "' + Newusername + '" is al in gebruik. Probeer even een andere gebruikersnaam.');
                    register_button.html('Aanmelden.');
                    register_icon.removeClass('fa-spinner fa-spin').addClass('fa-user-plus');

                }

            });


        });

    })


    let logUser = document.getElementById('NewUserName');
    logUser.oninput = handleInput;

    function handleInput(e) {

        var register_button = $('#register-button-msg');
        var register_icon = $('#register-button-icon');
        var form = $(this).closest("form");
        var Newusername = $('#NewUserName').val();
        $.ajax({
            url: form.attr("data-validate-existing-username-url"),
            data: form.serialize(),
            dataType: 'json',
            success: function (response) {
                {
                    var ajax_err = $('#username-errors');
                    ajax_err.css('display', 'none');

                }

            },
            error: function (response) {
                var ajax_err = $('#username-errors');
                console.log('Username already exist.');
                ajax_err.css('display', 'block');
                ajax_err.find('span').html('Gebruikersnaam "' + Newusername + '" is al in gebruik. Probeer even een andere gebruikersnaam.');
                register_button.html('Aanmelden');
                register_icon.removeClass('fa-spinner fa-spin').addClass('fa-user-plus');
            }

        });
    }

});






