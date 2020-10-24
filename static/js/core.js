let ctx;

$(document).ready(() => {
    ctx = document.getElementById('plot-canvas').getContext('2d');
    // new Chart(ctx, {type: 'line'});
    Chart.defaults.line.spanGaps = true;
    $('#submit-btn').click(calculate);
})

function calculate() {
    let form = {
        function: $('#function-input').val(),
        var: parseFloat($('#var-value').val()),
        tab: {
            from: parseFloat($('#tab-from').val()),
            to: parseFloat($('#tab-to').val()),
            step: parseFloat($('#tab-step').val()),
        }
    }
    $.post('/calc', {data: JSON.stringify(form)})
        .done(res => {
            $('#result-output').text(res.result.toFixed(2));

            $('#tokens').empty();
            $('#tokens').append(res.tokens);
            $('#rpn').empty();
            $('#rpn').append(res.rpn);
            let tab = res.tab.map(item => {
                return {x: item[0], y: item[1]}
            });
            let labels = res.tab.map(item => item[0]);
            new Chart(ctx, {
                type: 'line', data: {
                    labels: labels,
                    datasets: [{
                        label: 'chart',
                        data: tab
                    }]
                }
            });
            $('.result-block').css('visibility', 'visible');
        })
        .fail(err => {
            new Noty({theme: 'mint', text: err.responseText, type: 'error', timeout: 5000}).show();
        })
}


