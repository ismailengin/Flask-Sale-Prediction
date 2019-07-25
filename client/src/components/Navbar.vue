<template>
  <div class="container">
    <b-navbar type="dark" variant="info">
      <b-navbar-brand  disabled>Pizza Sales</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav v-if='!token'>
        <b-navbar-nav>
        <b-nav-item to="/login">Login</b-nav-item>
        <b-nav-item to="/register">Register</b-nav-item>
        
      </b-navbar-nav>
      </b-collapse>

       <b-collapse id="nav-collapse" is-nav v-else>
        <b-navbar-nav>
        <b-nav-item to="/tasks">Tasks</b-nav-item>
        <b-nav-item to="/createTask">Create Task</b-nav-item>
        
      </b-navbar-nav>
      </b-collapse>
      <b-navbar-nav class="ml-auto" v-if='token'>
        <b-nav-item-dropdown right >
          <!-- Using 'button-content' slot -->
          <template slot="button-content"><em>User</em></template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#" v-on:click="logout()">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-navbar>
   
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
