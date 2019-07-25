<template>
    <div id="login">
        <navbar  v-on:logOut="onChildClick" :key="navbarFlag"></navbar>
        <h1>Login</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
        <br><br>
        <p1> {{msg}} </p1>
    </div>
</template>

<script>
import axios from 'axios';
import router from '../router';
import Navbar from '../components/Navbar.vue';

export default {
  name: 'Login',
  data() {
    return {
      token: localStorage.userToken,
      input: {
        username: '',
        password: '',
      },
      msg: '',
    };
  },
  methods: {
    login() {
        const path = 'http://localhost:5000/authenticate';
        if (this.input.username !== '' && this.input.password !== '') {
          const payload = {
            username: this.input.username,
            password: this.input.password,
          };
          this.msg = this.input.username + this.input.password;
          axios.post(path, payload).then((res) => {
            if(!res.data.error)
            {
                this.msg = res.data;
                localStorage.setItem('userToken', res.data);
                localStorage.setItem('username', this.input.username);
                router.push({path: '/tasks'});
            }

            else {
              this.msg = res.data.error;
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

    components:{
      navbar: Navbar,
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
