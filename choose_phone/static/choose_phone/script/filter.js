$(document).ready(function () {
    $(".onlyNumber").keypress(function (e) {
        console.log(e.which);
        if (e.which < 48 || e.which > 57) {
            return false;
        }
    });
    // $('.submitForm').submit(function (event) {
    //
    //     const formData = $(this).serialize();
    //     const formUrl = $(this).attr('action');
    //
    //     $.ajax({
    //         method: 'POST',
    //         url: formUrl,
    //         data: formData,
    //         dataType: 'json',
    //         success: function (data) {
    //             if (data['result'] === 'error') {
    //                 event.preventDefault();
    //                 event.stopImmediatePropagation();
    //                 console.log('errors')
    //             }
    //         },
    //         error: function () {
    //             console.log('can\'t connect to server')
    //         }
    //     });
    //
    //     return false;
    // })
});