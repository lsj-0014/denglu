EduChart.vue
<template>
  <div>
    <div id="price_bar"></div>
  </div>
</template>
<style scoped>
div {
  width: 100%;
  height: 500px;
  margin-top: 70px;
}
</style>
<script>
import * as echarts from 'echarts';

export default {
  name: "chart",
  data() {
    return {}
  },
  mounted() {
    //租金区间饼图
    fetch("http://127.0.0.1:5000/price_bar").then(res => {
      return res.json()
    }).then(data => {
      let container = echarts.init(document.getElementById("price_bar"))
      let option = {
        title: {
          text: "不同区间的房屋月租金-数量占比",
          left: "center",
          textStyle: {
            fontSize: 18
          }
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: '租金',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: data
          }
        ]

      };
      container.setOption(option)
    })
  }
}
</script>