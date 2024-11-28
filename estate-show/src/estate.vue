<template>
<!--1、输入框  2、按钮  3、表格-->
  <div>
    <el-input v-model="min_price" placeholder="请输入最低月租金"></el-input>
    <spen>—</spen>
    <el-input v-model="max_price" placeholder="请输入最高月租金"></el-input>
    <el-button type="primary" @click="queryJobs">搜索</el-button>
    <el-table :data="jobs" height="650" border style="width: 100%">
      <el-table-column prop="job_title" label="租房标题" ></el-table-column>
      <el-table-column prop="job_way" label="租房方式" ></el-table-column>
      <el-table-column prop="job_house" label="房屋户型" ></el-table-column>
      <el-table-column prop="job_area" label="房屋面积" ></el-table-column>
      <el-table-column prop="job_orientation" label="房屋朝向" ></el-table-column>
      <el-table-column prop="job_address" label="房屋地址" ></el-table-column>
      <el-table-column prop="job_price" label="租房方式" ></el-table-column>
    </el-table>
  </div>
</template>
<style>
.container {
  display: flex;
  flex-direction: column;
}

.search-box {
  display: flex;
  align-items: center; /* 垂直居中对齐 */
  margin-bottom: 20px; /* 输入框和表格之间的间距 */
}

.el-input{
  width: 20% !important;
  margin-right: 5px;
  margin-left: 5px;
  margin-bottom: 10px;
}

</style>
<script>
  export default {
    data() {
      return {
        min_price: '',
        max_price:'',
        jobs:[]
      }
    },
     methods: {
    queryJobs() {
      // 构建查询参数
      let url = "http://127.0.0.1:5000/query_rooms?";
      if (this.min_price) {
        url += `min_price=${this.min_price}&`;
      }
      if (this.max_price) {
        url += `max_price=${this.max_price}&`;
      }

      // 发起请求
      fetch(url).then(res => res.json()).then(data => {
        this.jobs = data; // 更新表格数据
      });
    }
  },
  mounted() {
    // 初始加载时获取所有房间数据
    fetch("http://127.0.0.1:5000/rooms")
      .then(res => res.json())
      .then(data => {
        this.jobs = data;
      });
  }
}
</script>
