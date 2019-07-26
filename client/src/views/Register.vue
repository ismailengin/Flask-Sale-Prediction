<template>
    <div id="register">
      <navbar></navbar>
      <b-form>
        <h1>Register</h1>
        <b-form-group>
        <b-form-input type="text" name="username" v-model="input.username" placeholder="Username" />
        </b-form-group>
        <b-form-group>
        <b-form-input type="password" name="password" v-model="input.password" placeholder="Password" />
        </b-form-group>
        <button type="button" class="btn btn-warning btn-sm" v-on:click="register()">Register</button>
        <br><br>
        <p1 id="alert" style="color:red;"> {{msg}} </p1>
      </b-form>
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
        //this.msg = this.input.username + this.input.password;
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
  created() {
    if (this.token) {
      router.push({ path: '/tasks' });
    }
  },
};
</script>

<style scoped>
    #register {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
    #alert{
      color: red
    }
</style>
