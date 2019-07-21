<template>
    <div id="login">
        <p1> {{msg}} </p1>
        <h1>Login</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="register()">Register</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Register',
  data() {
    return {
      input: {
        username: '',
        password: '',
      },
      msg: 'Hallo',
    };
  },
  methods: {
    register() {
      this.msg = 'lololo';

      const path = 'http://localhost:5000/register';
      if (this.input.username !== '' && this.input.password !== '') {
        const payload = {
          username: this.input.username,
          password: this.input.password,
        };
        this.msg = this.input.username + this.input.password;
        axios.post(path, payload).then((res) => {
          this.msg = 'posted';
          if (res.data.message === 'exist') {
            this.msg = 'ilya';
          } else if (res.data.message === 'added') {
            this.msg = 'voila';
          }
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
      }
    },
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
