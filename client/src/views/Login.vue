<template>
    <div id="login">
        <p1> {{msg}} </p1>
        <h1>Login</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>

<script>
import axios from 'axios';
import router from '../router';

export default {
  name: 'Login',
  data() {
    return {
      token: localStorage.userToken,
      input: {
        username: '',
        password: '',
      },
      msg: 'Hallo',
    };
  },
  methods: {
    login() {
        this.msg = 'lololo';
        const path = 'http://localhost:5000/authenticate';
        if (this.input.username !== '' && this.input.password !== '') {
          const payload = {
            username: this.input.username,
            password: this.input.password,
          };
          this.msg = this.input.username + this.input.password;
          axios.post(path, payload).then((res) => {
            this.msg = 'posted';
            if (res.data) {
              this.msg = res.data;
              localStorage.setItem('userToken', res.data);
              router.push({path: '/tasks'})
            }
            else {
              this.msg = 'no';
            }
          }).catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            this.getBooks();
          });
        } else {
          console.log('A username and password must be present');
        }   
      },
    
    },
    created() {
      if(this.token) {
        router.push({path:'/tasks'})
      }
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
