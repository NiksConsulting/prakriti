/*
var hair = getElement('.hair')

$('.skin').on('click', skin_func(){
        var skin_val = document.getElementById('skin').attr('value');
        //.attr('value');

        $.ajax({
                cache: false,
                type: "GET",
                url: "http://127.0.0.1:5000/avatar",
                data: { skin: skin, b: No2 },
                contentType: "application/json; charset=ytf-8",
                success: function (result) {
                    alert("data");
                },
                error: function (xhr, textStatus, errorThrown) { alert(textStatus + ':' + errorThrown); }
            });
});

$(document).ready(function () {
        $('#BtnRegister').click(function () {
            debugger;

            var skin = document.getElementById('TxtFirstNumber').value;
            var No2 = document.getElementById('TxtSecondNumber').value;

            $.ajax({
                cache: false,
                type: "GET",
                async: false,
                url: "http://localhost:22727/Service1.svc/Display",
                data: 'a=' +No1+'&b='+No2,
                contentType: "application/json; charset=ytf-8",
                dataType: "json",
                processData: true,
                success: function (result) {
                    alert("data");
                },
                error: function (xhr, textStatus, errorThrown) { alert(textStatus + ':' + errorThrown); }
            });
        });
    });


$('.skin').each(function () {
    var skin_val = $(this).attr('value');
    $(this).attr('src', src + '&showinfo=1&autohide=1');
});
 */