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



});