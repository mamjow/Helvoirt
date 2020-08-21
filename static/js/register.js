$(document).ready(function () {
    $('#register-button').click(function () {

        var register_button = $('#register-button-msg');
        register_button.html('Aanmelden ...');

        var register_icon = $('#register-button-icon');
        register_icon.removeClass(' fa-user-plus').addClass('fa-spinner fa-spin');

        $('#SignUpForm').submit(function (e) {
            var NewUserName = $('#NewUserName').val();
            var password1 = $('#NewUserPass1').val();
            var password2 = $('#NewUserPass2').val();
            var NewUserEmail = $('#NewUserEmail').val();
            var UserError = $('#username-errors');
            var register_button = $('#register-button-msg');
            var register_icon = $('#register-button-icon');
            var ajax_err = $('#register-errors');
            $("#email-errors").css('display', 'none');
            $("#password-errors").css('display', 'none');

            event.preventDefault();
            var form = $(this).closest("form");

            $.ajax({
                type: "POST",
                url: form.attr("data-validate-existing-username-url"),
                data: form.serialize(),
                dataType: 'json',
                success: function () {
                    UserError.css('display', 'none');
                    // console.log('vlidate shod', NewUserEmail, NewUserName, password2, password1);
                    $.ajax({
                        type: "POST", // GET or POST
                        url: '/signup/',
                        data: {
                            username: NewUserName,
                            email: NewUserEmail,
                            password1: password1,
                            password2: password2,
                            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                        },
                        success: function (data) {
                            // console.log(data.message);
                            if (data['message'] == "Success") {
                                // console.log('berim login ?');
                                $.ajax({
                                    type: "POST",
                                    url: '/login/',
                                    data: {
                                        username: NewUserName,
                                        password: password1,
                                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                                    },
                                    success: function () {
                                        register_button.html('ingelogged');
                                        register_icon.removeClass('fa-spinner fa-spin').addClass(' fa-user-plus');
                                        $('#SignUpModal').modal('hide');
                                        // console.log(data);
                                        location.reload();
                                    },
                                    error: function () {
                                        var ajax_err = $('#ajax-errors');
                                        ajax_err.css('display', 'block');
                                        ajax_err.find('span').html('Ops. Something went wrong. Please try again!')
                                    },

                                })

                            }
                            else {

                                if ("email" in data['message']) {
                                    $("#email-errors").html(data['message']['email'][0]);
                                    $("#email-errors").css('display', 'block');
                                }

                                if ("password2" in data['message']) {
                                    $("#password-errors").html(data['message']['password2'][0]);
                                    $("#password-errors").css('display', 'block');
                                }

                            }
                            register_button.html('Aanmelden');
                            register_icon.removeClass('fa-spinner fa-spin').addClass('fa-user-plus');

                        }, /* end of Success */
                        error: function (data) {
                            // console.log(data.message);
                            var ajax_err = $('#register-errors');
                            ajax_err.css('display', 'block');
                            ajax_err.find('span').html(data.message)
                        }/*  end of error */
                    });
                    /*./ajax*/

                },
                error: function () {
                    $('#username-errors').css('display', 'block');
                    ajax_err.css('display', 'block');
                    ajax_err.find('span').html('Gebruikersnaam "' + NewUserName + '" is al in gebruik. Probeer even een andere gebruikersnaam.');
                    register_button.html('Aanmelden');
                    register_icon.removeClass('fa-spinner fa-spin').addClass('fa-user-plus');

                }

            });


        });


    });


    let logUser = document.getElementById('NewUserName');
    logUser.oninput = handleInput;

    function handleInput(e) {

        var register_button = $('#register-button-msg');
        var register_icon = $('#register-button-icon');
        var form = $(this).closest("form");
        var NewUserName = $('#NewUserName').val();
        var ajax_err = $('#register-errors');
        $.ajax({
            url: form.attr("data-validate-existing-username-url"),
            data: form.serialize(),
            dataType: 'json',
            type: "POST",
            success: function () {
                {
                    $('#username-errors').css('display', 'none');
                    ajax_err.css('display', 'none');

                }

            },
            error: function () {
                $('#username-errors').css('display', 'block');
                ajax_err.css('display', 'block');
                ajax_err.find('span').html('Gebruikersnaam "' + NewUserName + '" is al in gebruik. Probeer even een andere gebruikersnaam.');
                register_button.html('Aanmelden');
                register_icon.removeClass('fa-spinner fa-spin').addClass('fa-user-plus');
            }

        });
    }

});






