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
            }
            $("#id_magic_number").val(new_result)
        }
    });

    $("#magic_form").submit(function (event) {
        magic_day = $("#id_magic_day").val();
        magic_month = $("#id_magic_month").val();
        magic_year = $("#id_magic_year").val();
        console.log('magic_button clicked');
        if (magic_day === 'День' || magic_month === 'Месяц' || magic_month === 'Год') {
            event.preventDefault();
            alert("Для поиска по магическому числу необходимо обязательно выбрать день, месяц и год вашего рождения")
        } else {
            console.log('all ok')
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