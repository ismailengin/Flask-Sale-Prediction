<template>
    <div id="navs" >
      <div id="nav1" v-if='!token'>
        <router-link  to="/login">Login</router-link>
        <router-link  to="/register">Register</router-link>
      </div>
      <div id="nav2" v-else >
        <router-link  to="/tasks">Tasks</router-link>
        <router-link  to="/createTask">Create Task</router-link>
        <button type="button" v-on:click="logout()">Logout</button>
      </div>
    </div>
</template>

<script>
import router from '../router';

export default {
    name: 'App',
    data() {
        return {
        token: localStorage.userToken,
        }
    },
    methods: {
        logout() {
        localStorage.removeItem('userToken');
        router.push('/login');
        }
    },
};
</script>
