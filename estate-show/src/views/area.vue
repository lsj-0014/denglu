EduChart.vue
<template>
  <div>
    <div id="area_bar"></div>
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
    //面积区间饼图
    fetch("http://127.0.0.1:5000/area_bar").then(res => {
      return res.json()
    }).then(data => {
      let container = echarts.init(document.getElementById("area_bar"))
      let option = {
          title: {
            text: '不同区间的房屋面积-数量占比',
            left: 'center'
          },
          tooltip: {
            trigger: 'item'
          },
          legend: {
            orient: 'vertical',
            left: 'left'
          },
          series: [
            {
              name: '面积:',
              type: 'pie',
              radius: '70%',
              data: data,
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        };
        container.setOption(option)
      }
    )
    }
  }
</script>
