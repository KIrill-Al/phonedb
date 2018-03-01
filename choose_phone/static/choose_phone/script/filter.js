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
    $(".magic").on('change', function () {
        magic_day = $("#id_magic_day").val();
        magic_month = $("#id_magic_month").val();
        magic_year = $("#id_magic_year").val();
        console.log(magic_day);
        console.log(magic_month);
        console.log(magic_year);
        if (magic_day && magic_month && magic_year) {
            result = magic_day + magic_month + magic_year;
            result_length = result.length;
            while (result_length > 1) {
                new_result = 0;
                for (var i = 0; i < result_length; i++) {
                    new_result += +result.charAt(i)
                }
                result = new_result.toString();
                result_length = result.length;
                console.log(result);
                console.log(result_length);
                console.log(new_result);
            }
            $("#id_magic_number").val(new_result)
        }
    })
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