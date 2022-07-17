<template>
  <div id="bannerimage">
    <div id="header">
      <span>
        <a href="/home"> <h2>DI22</h2> <br>Your device your choice</a>
      </span>
    </div>
  </div>
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
  padding: 50px 50px;
  margin-top: 0;
  text-align: center;
}

h2 {
  font-weight: bolder;
}
/*h1 {*/
/*  color: white;*/
/*  text-align: center;*/
/*  font-family: Arial;*/
/*}*/
a {
  color: white;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-weight: bold;
  font-size: 30px;
  text-decoration: none;
}
span {

}
</style>