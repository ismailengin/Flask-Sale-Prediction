<template>
  <div id="app">
    <h1>Pizza Sales </h1>
    <div id="nav1" v-if='!token'>
      <router-link  to="/login">Login</router-link>
      <router-link  to="/register">Register</router-link>
    </div>
    <div id="nav2" v-else>
      <router-link  to="/tasks">Tasks</router-link>
      <router-link  to="/createTask">Create Task</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
import router from './router'
export default {
  name: 'App',
  data() {
    return {
      token: localStorage.userToken,
    }
  },
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
