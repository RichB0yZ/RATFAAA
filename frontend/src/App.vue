
<template>
  <MyData/>
</template>

<script>
import MyData from './components/show_helloworld.vue'

export default {
  name: 'App',
  components: {
    MyData

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
