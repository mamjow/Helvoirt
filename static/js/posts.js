$(document).ready(function () {

    /* Functions */
    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);// Button that triggered the modal
        var objectid = button.data('whatever'); // Extract info from data-* attributes
        var formurl = button.data('formurl');
        var form = $(this);
        form.submit(function () {
            $.ajax({
                url: formurl,
                type: 'POST',
                dataType: 'json',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function (data) {
                    console.log(data)
                }
            });
        });
        var modal = $(this);
        modal.find('.modal-body strong').html(objectid)
    });

    var loadNewsForm = function () {
        var btn = $(this);
        var formurl = btn.data('formurl');
        $.ajax({
            url: formurl,
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#Form-Modal .modal-content").html("");
                $("#Form-Modal").modal("show");
            },
            success: function (data) {
                $("#Form-Modal .modal-content").html(data.html_form);
                $("#Form-Modal").find('form').attr('data-url', formurl);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        var formdata = new FormData(this);
        $.ajax({
            url: form.attr("data-url"),
            data: formdata,
            processData: false,
            contentType: false,
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#data-table tbody").html(data.html_book_list);
                    $("#Form-Modal").modal("hide");

                }
                else {
                    $("#Form-Modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book
    $("#OpenAddArticle").click(loadNewsForm);

    //edit
    $("#data-table").on("click", ".js-update-news", loadNewsForm);

    // Save
    $("#Form-Modal").on("submit", ".js-news-create-form", saveForm);

    // Create intro
    $("#OpenAddIntro").click(loadNewsForm);

    //edit intro
    $("#data-table").on("click", ".js-update-intro", loadNewsForm);

    // Save intro
    $("#Form-Modal").on("submit", ".js-intro-create-form", saveForm);
});