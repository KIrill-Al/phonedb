$(document).ready(function () {
    $(".onlyNumber").keypress(function (e) {
        if (e.which < 48 || e.which > 57) {
            return false;
        }
    });
    $(".small-input").keyup(function () {
        console.log(this.maxLength);
        console.log(this.value.length);
        if (this.value.length === this.maxLength) {
            $(this).next('.small-input').focus();
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