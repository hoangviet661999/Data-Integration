<template>
  <div id="app">
    <TopHeader/>
    <router-view/>
<!--    <div class="content-wrapper">-->
<!--      <router-view/>-->
<!--    </div>-->
  </div>
</template>

<script>
import TopHeader from './components/Header.vue'

export default {
  name: 'App',
  components: {
    TopHeader,
  }
}
</script>

<style>
</style>