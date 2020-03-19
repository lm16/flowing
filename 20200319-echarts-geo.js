myChart.showLoading();

$.get('https://geo.datav.aliyun.com/areas/bound/441200_full.json', function () {
    myChart.hideLoading();

    option = {
        title: {
            text: '20200319-肇庆',
            subtext: '百度一下',
            sublink: 'http://baidu.com',
            left: 'right'
        },
        
        tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter: function (params) {
                var value = (params.value + '').split('.');
                value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');
                return params.seriesName + '<br/>' + params.name + ': ' + value;
            }
        },
        
        visualMap: {
            left: 'right',
            min: 500000,
            max: 38000000,
            inRange: {
                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
            },
            text: ['High', 'Low'],           // 文本，默认为数值文本
            calculable: true
        },
        
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
                dataView: {readOnly: false},
                restore: {},
                saveAsImage: {}
            }
        },
        
        series: [
            {
                name: null,
                type: 'map',
                roam: true,
                map: 'USA',
                emphasis: {
                    label: {
                        show: true
                    }
                },
                // 文本位置修正
                textFixed: {
                    Alaska: [20, -20]
                },
                data:[
                    {name: '封开县', value: 4822023},
                    {name: '怀集县', value: 731449},
                    {name: '德庆县', value: 6553255},
                    {name: '高要区', value: 2949131},
                    {name: '端州区', value: 38041430},
                    {name: '鼎湖区', value: 5187582},
                    {name: '四会市', value: 3590347},
                    {name: '广宁县', value: 917092}
                ]
            }
        ]
    };

    myChart.setOption(option);
});