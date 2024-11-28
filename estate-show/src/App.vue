<template>
  <!--编写网页的内容，网页组成：头部 左侧的导航  右侧的控件-->
  <el-container>
    <el-header>
      <h1>租房信息数据爬取展示</h1>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
          <el-menu-item index="1" @click="jumpestate">
            <i class="el-icon-menu"></i>
            <span slot="title">租房信息数据</span>
          </el-menu-item>
          <el-menu-item index="" @click="estateai">
            <i class="el-icon-menu"></i>
            <span slot="title">AI大模型问答系统</span>
          </el-menu-item>
          <el-menu-item index="3" @click="houseEchart">
            <i class="el-icon-apple"></i>
            <span slot="title">户型数量可视化</span>
          </el-menu-item>
          <el-menu-item index="4" @click="orientationEchart">
            <i class="el-icon-bangzhu"></i>
            <span slot="title">朝向数量可视化</span>
          </el-menu-item>
          <el-menu-item index="5" @click="areaEchart">
            <i class="el-icon-document"></i>
            <span slot="title">面积数量可视化</span>
          </el-menu-item>
          <el-menu-item index="6" @click="priceEchart">
            <i class="el-icon-bangzhu"></i>
            <span slot="title">月租金数量可视化</span>
          </el-menu-item>
          <el-menu-item index="7" @click="wayEchart">
            <i class="el-icon-bangzhu"></i>
            <span slot="title">租房方式数量可视化</span>
          </el-menu-item>

          <el-menu-item index="8" @click="recommands">
            <i class="el-icon-bangzhu"></i>
            <span slot="title">租房推荐</span>
          </el-menu-item>
          <el-menu-item index="9" @click="prediction">
            <i class="el-icon-bangzhu"></i>
            <span slot="title">租房租金预测</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <!--是vue提供的一个组件，用来将其他界面在这个位置打开-->
        <router-view/>
      </el-main>
    </el-container>
  </el-container>
</template>
<style>
html, body {
  width: 100%;
  height: 100%;
  margin: 0px;
}

h1 {
  margin: 0px;
}

.el-menu {
  height: 100%;
}

.el-header, .el-footer {
  background-color: #545c64;
  color: white;
  text-align: center;
  line-height: 60px;
  height: 10%;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
  height: 100%;
}

.el-container {
  height: 100%;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: left;
  line-height: 20px;
  height: 100%;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
<script>
export default {
  methods: {
    jumpestate() {
      this.$router.push("/estate")
    },
    estateai() {
      window.open('http://localhost:8501', '_blank');   // 在这里替换为你想要跳转的 URL
    },
    areaEchart() {
      this.$router.push("/area")
    },
    houseEchart() {
      this.$router.push("/house")
    },
    orientationEchart() {
      this.$router.push("/orientation")
    },
    priceEchart() {
      this.$router.push("/price")
    },
    wayEchart() {
      this.$router.push("/way")
    },
    recommands() {
      this.$router.push("/recommands")
    },
    prediction() {
      this.$router.push("/prediction")
    }

  }
}
</script>