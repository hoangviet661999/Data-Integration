<template>
  <div>
  <div class="list" v-for="device in deviceList" v-bind:key="device.name">
  <div class="container">
    <div class="images">
      <img src="https://images-na.ssl-images-amazon.com/images/S/pv-target-images/02ef2b75bf6c39dec48c636c8dc9d0e4252601800eec9e15c8a266fc46150b00._RI_V_TTW_.jpg" />
    </div>
    <div class="product">
      <h1>{{device.name}}</h1>
      <!-- <h2 v-if="device.price">{{device.price}}</h2>-->
      <p class="desc">
        {{device.price}}
      </p>
      <a :href="'http://localhost:8080/device/'+device._id">
        <div class="buttons">
          <button class="add">Xem thêm</button>
        </div>
      </a>

    </div>
  </div>
  </div>
  </div>
</template>

<script>
// import * as axios from 'axios';
// import Item from "./Item";
export default {
  name: 'itemList',
  props: {
    deviceList: null,
  },
  components: {
    // Item,
  },
  computed : {

  },
  mounted() {
  }
}
</script>

<style lang="scss" scoped>

$font: 'Lato', sans-serif;

$white: #F5F5F5;
$light: #DFE7E7;
$tan: #AAD3D3;
$pink: #9ECBCB;
$rose: #89C2C2;
$dark: #4E4E4E;

/* center container in the middle */
html {
  display: grid;
  min-height: 100%;
}

body {
  display: grid;
  background: $light;
  font-family: $font, sans-serif;
  text-transform: uppercase;
}

.list {
  padding: 1em;
}

.container {
  position: relative;
  margin: auto;
  overflow: hidden;
  width: 700px;
  height: 350px;
  background: $white;
  box-shadow: 5px 5px 15px rgba($rose, .5);
  border-radius: 10px;
  padding: 1em;
}

.product {
  position: absolute;
  width: 40%;
  height: 100%;
  top: 10%;
  left: 50%;
}

p {
  font-size: 0.6em;
  color: $rose;
  letter-spacing: 1px;
}

h1 {
  font-size: 1.2em;
  color: $dark;
  margin-top: 1.5em;
  margin-right: 0.1em;
}

h2 {
  color: $dark;
  margin-top: -5px;
}

.desc {
  text-transform: none;
  letter-spacing: 0;
  margin-bottom: 17px;
  color: $dark;
  font-size: 2em;
  line-height: 1.6em;
  margin-right: 25px;
  text-align: justify;
}

img {
  width: 290px;
  height: 200px;
  margin-top: 47px;
  margin-left: 2em;
}

button {
  background: darken(#A3B8CA, 10%);
  padding: 10px;
  display: inline-block;
  outline: 0;
  border: 0;
  margin: -1px;
  border-radius: 2px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: $white;
  cursor: pointer;
  &:hover {
    background: $rose;
    transition: all .4s ease-in-out;
  }
}

.add {
  width: 67%;
}

.like {
  width: 22%;
}

.sizes {
  display: grid;
  color: $pink;
  grid-template-columns: repeat(auto-fill, 30px);
  width: 60%;
  grid-gap: 4px;
  margin-left: 20px;
  margin-top: 5px;
  &:hover {
    cursor: pointer;
  }
}

.pick {
  margin-top: 11px;
  margin-bottom:0;
  margin-left: 20px;
}

.size {
  padding: 9px;
  border: 1px solid $light;
  font-size: 0.7em;
  text-align: center;
  &:hover{
    background: $rose;
    color: $white;
    transition: all .4s ease-in-out;
  }
}

.focus{
  background: $rose;
  color: $white;
}
</style>

