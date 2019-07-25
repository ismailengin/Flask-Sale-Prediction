<template>

    <div id="register">
      <navbar></navbar>
        <h1>Register</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="register()">Register</button>
        <br><br>
        <p1> {{msg}} </p1>
    </div>
</template>

<script>
import axios from 'axios';
import Navbar from '../components/Navbar.vue';

export default {
  name: 'Register',
  data() {
    return {
      input: {
        username: '',
        password: '',
      },
      msg: '',
    };
  },
  methods: {
    register() {
      const path = 'http://localhost:5000/register';
      if (this.input.username !== '' && this.input.password !== '') {
        const payload = {
          username: this.input.username,
          password: this.input.password,
        };
        this.msg = this.input.username + this.input.password;
        axios.post(path, payload).then((res) => {
          if (res.data.message === 'exist') {
            this.msg = 'There username exists. Please choose another one.';
          } else if (res.data.message === 'added') {
            this.msg = 'Registered';
          }
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
      } else {
        this.msg = 'A username and password must be present';
      }
    },
  },
  components: {
    navbar: Navbar,
  },
};
</script>

<style scoped>
    #login {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>
