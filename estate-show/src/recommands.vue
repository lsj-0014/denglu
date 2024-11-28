<template>
    <div>
      <el-select v-model="job_house" placeholder="请选择租房户型">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-input v-model="job_address" placeholder="请输入房源地"></el-input>
      <el-input v-model="job_price" placeholder="请输入租金"></el-input>
      <el-select v-model="job_way" placeholder="请选择租房方式">
        <el-option
          v-for="item in edus"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>

      <el-button type="success" @click="recommand">租房推荐</el-button>
      <el-table
          :data="jobs"
          height="700"
          border
          style="width: 100%">
        <el-table-column
            prop="job_title"
            label="租房标题"
            width="180">
        </el-table-column>
        <el-table-column
            prop="job_price"
            label="租房租金"
            width="180">
        </el-table-column>
           <el-table-column
            prop="job_area"
            label="租房面积"
            width="180">
        </el-table-column>
        <el-table-column
            prop="job_address"
            label="房源的地址">
        </el-table-column>
        <el-table-column
            prop="job_score"
            label="房源得分">
        </el-table-column>
      </el-table>
    </div>

</template>

<style>
.el-input {
  display: inline-block !important;
  width: auto !important;
  margin-right: 20px;
  margin-bottom: 20px;
}
</style>

<script>
export default {
  data() {
    return {
       options: [{
        value: '1',
        label: '2室1厅'
      }, {
        value: '2',
        label: '2室2厅'
      }, {
        value: '3',
        label: '3室1厅'
      }, {
        value: '4',
        label: '3室2厅'
      }, {
        value: '5',
        label: '4室2厅'
      },{
          value: '0',
          label: '其他'
        }],
      edus: [
        {
          value: '1',
          label: '整租'
        },
        {
          value: '2',
          label: '合租主卧'
        },
        {
          value: '3',
          label: '合租次卧'
        },
        {
          value: '4',
          label: '合租单间'
        },
      ],
      job_house: '',
      job_address: '',
      job_price: "",

      job_way: "",
      jobs: []
    }
  },
  methods: {
    recommand() {
      //携带五个参数请求后端 在后端做推荐算法，然后把推荐回来的数据展示到界面上
      fetch("http://127.0.0.1:5000/recommand?job_house=" + this.job_house + "&job_address=" + this.job_address + "&job_price=" + this.job_price + "&job_way=" + this.job_way).then(res => {
        return res.json()
      }).then(data => {
        this.jobs = data
        console.log(data)
      })
    }
  }
}
</script>