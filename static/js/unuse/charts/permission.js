/**
 * Created with IntelliJ IDEA.
 * User: Freeeeeeeee
 * Date: 13-8-5
 * Time: 下午3:00
 */
$(function () {
    $('#pie_chart').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Browser market shares at a specific website, 2010'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    connectorColor: '#000000',
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Browser share',
            data: [
                ['Firefox',   1.0],
                ['IE',       1],
                {
                    name: 'Chrome',
                    y: 1,
                    sliced: true,
                    selected: true
                },
                ['Safari',    1],
                ['Opera',     1],
                ['Others',   1]
            ]
        }]
    });
});
