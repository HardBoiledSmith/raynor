$(document).ready(function () {
    var control_btn_list = ['id-create-all', 'id-create-vpc', 'id-create-nova', 'id-create-rds', 'id-terminate-all',
        'id-terminate-vpc', 'id-terminate-nova', 'id-terminate-rds', 'id-terminate-eb-old-env'];

    for (var i = 0; i < control_btn_list.length; i++) {
        var btn_id = '#' + control_btn_list[i];
        var btn = $(btn_id);

        (function (btn) {
            $(btn_id).on('click', function () {
                $('.btn-control').addClass('disabled');

                $('#log-content').empty();
                $('#view-title').text('Running : ' + btn.text());

                create_socket();

                var request_url = btn.data('url');

                $.ajax({
                    url: request_url,
                    dataType: 'json',
                    success: function (resp) {
                        console.log("Success!");
                    },
                    error: function (error) {
                        console.log(error);
                    }
                });
            });
        })(btn);
    }
});

var create_socket = function () {
    var socket_scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
    var socket_path = socket_scheme + '://' + window.location.host + window.location.pathname + 'stream/';

    console.log('Connecting to ' + socket_path);

    var socket = new ReconnectingWebSocket(socket_path);

    socket.onopen = function () {
        console.log('Connected to stream socket');
    }
    socket.onclose = function () {
        console.log('Disconnected to stream socket');
    }
    socket.onmessage = function (message) {
        console.log('Got message ' + message.data);

        var data = JSON.parse(message.data);
        var code = data.code;
        var log = data.log;

        if (code == 0) {
            socket.close();

            $('#view-title').text('No Running');
            $('.btn-control').removeClass('disabled');

            return;
        }

        var content = '<p>' + log + '</p>';

        $('#log-content').append(content);
        $('#log-panel').animate({
            scrollTop: $('#log-content').height()
        }, "fast");
    };
}