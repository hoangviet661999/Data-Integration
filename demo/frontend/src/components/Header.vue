<template>
  <div id="bannerimage">
    <div id="header">
      <span>
        <a href="/home">DI22 <br> <br>Choose your device</a>
<!--        <h1>TRANG THÔNG TIN BẤT ĐỘNG SẢN</h1>-->
      </span>
    </div>
  </div>

<!--    <router-link class="page-link" to="/">Trang thông tin bất động sản</router-link>-->
</template>

<script>
export default {
  name: 'TopHeader',
  // methods: {
  //   highLight(e) {
  //     const underlines = this.$refs.menu.querySelectorAll('.underline');
  //     underlines.forEach(u => {
  //       u.classList.remove('visible')
  //     });
  //     e.path[1].childNodes[1].classList.add('visible')
  //   }
  // }
}
</script>

<style lang="css" scoped>
.title {
  font-size: 30px;
  font-weight: bold;
  width: 100%;
  display: flex;
  align-items: center;
  padding-left: 10px;
}
#bannerimage {
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('../assets/bg.jpg');
  height: 50%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;

  /*width: 100%;*/
  /*background-image: url('../assets/pngtree-technology-city-banner-background-image_261645.jpg');*/
  /*height: 100%;*/
  /*background-position: center;*/
  /*position: relative;*/
}
#header {
  height: auto;
  padding: 100px 100px;
  margin-top: 0;
  text-align: center;
}
/*h1 {*/
/*  color: white;*/
/*  text-align: center;*/
/*  font-family: Arial;*/
/*}*/
a {
  color: white;
  font-family: Arial;
  font-weight: bold;
  font-size: 30px;
  text-decoration: none;
}
span {

}
</style>