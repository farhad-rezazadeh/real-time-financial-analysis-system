async function chartComponent (baseUrl = 'data/stock-data/?format=json') {
  const response = await fetch(`http://127.0.0.1:8000/${baseUrl}`)
  const dataRes = await response.json()
  console.log(dataRes);
    const options = {
        series: [{
          name: 'candle',
          data : dataRes.map(item => (
            {
              x : item.timestamp,
              y : [item.opening_price , item.closing_price , item.high , item.low]
            }
          ))
        }],
        chart: {
          height: 600,
          type: 'candlestick',
        },
      
        annotations: {
          xaxis: [
            {
              x: 'Oct 06 14:00',
              borderColor: '#00E396',
              label: {
                borderColor: '#00E396',
                style: {
                  fontSize: '12px',
                  color: '#fff',
                  background: '#00E396'
                },
                orientation: 'horizontal',
                offsetY: 7,
                text: 'Annotation Test'
              }
            }
          ]
        },
        tooltip: {
          enabled: true,
        },
        xaxis: {
          type: 'category',
          labels: {
            formatter: function(val) {
              return dayjs(val).format('MMM DD HH:mm')
            }
          }
        },
        yaxis: {
          tooltip: {
            enabled: true
          }
        }
        };
        document.querySelector('#area-chart').innerHTML =''
      const areaChart = new ApexCharts(document.querySelector('#area-chart'),options);
      areaChart.render();
}

export default chartComponent;