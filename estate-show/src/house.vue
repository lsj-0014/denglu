<template>
  <div>
    <div id="house_bar"></div>
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
    // 获取数据
    fetch("http://127.0.0.1:5000/house_bar").then(res => {
      return res.json()
    }).then(data => {
      // 初始化echarts实例
      let container = echarts.init(document.getElementById("house_bar"));
      
      // 配置柱状图的option
      let option = {
        title: {
          text: "房屋户型-数量占比",
          left: "center",
          textStyle: {
            fontSize: 18
          }
        },
        tooltip: {
          trigger: 'axis',  // 鼠标悬停时触发的提示框
          axisPointer: {
            type: 'shadow'  // 使用阴影指示器
          }
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        xAxis: {
          type: 'category',
          data: data.map(item => item.name),  // 横坐标使用名称数据
          axisLabel: {
            interval: 0,  // 让标签全部显示
            rotate: 30,   // 让标签有一定角度
            fontSize: 12
          }
        },
        yAxis: {
          type: 'value',  // 纵坐标是数值类型
          name: '数量',
          axisLabel: {
            formatter: '{value}'  // 格式化纵坐标的标签
          }
        },
        series: [
          {
            name: '数量',
            type: 'bar',  // 设置图表类型为柱状图
            data: data.map(item => item.value),  // 获取每个分类的数量
            itemStyle: {
              normal: {
                color: '#4fa3f7',  // 设置柱子的颜色
                borderColor: '#fff',
                borderWidth: 2
              }
            },
            barWidth: '60%',  // 设置柱子的宽度
          }
        ]
      };
      
      // 设置option并渲染图表
      container.setOption(option);
    });
  }
}
</script>