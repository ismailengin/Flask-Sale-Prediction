<template>
    <div class="container text-center">
    <navbar></navbar>
    <br>
        <h1>Hello {{username}} </h1>
        <br>
        <b-form class="col-sm-6" style="margin:auto">
        <p1>Change Password</p1>
        <br>
        <b-form-group >
        <b-form-input type="password" name="old_password"
            v-model="input.old_password" placeholder="Old Password" />
        </b-form-group>
        <b-form-group>
        <b-form-input type="password" name="new_password"
            v-model="input.new_password" placeholder="New Password" />
        </b-form-group>
        <button type="button" class="btn btn-warning btn-sm"
            v-on:click="changePassword()">Change Password</button>
        <br><br>
        <p1 id="alert" style="color:red;"> {{msg}} </p1>
      </b-form>
    </div>
</template>

<script>
import axios from 'axios';
import Navbar from '../components/Navbar.vue';

export default {
  name: 'Profile',
  data() {
    return {
      input: {
        old_password: '',
        new_password: '',

      },
      username: localStorage.username,
      msg: '',
    };
  },
  methods: {
    changePassword() {
      const formData = new FormData();
      if (this.input.pass !== '' && this.input.newpass !== '') {
        const path = 'http://localhost:5000/changePass';
        formData.append('username', this.username);
        formData.append('oldPass', this.input.old_password);
        formData.append('newPass', this.input.new_password);
        console.log(this.username, this.input.old_password, this.input.new_password);
        axios.post(path, formData)
          .then((res) => {
            if (res.data.status === 'success') {
              this.msg = 'Password Changed!';
            }
          }).catch((error) => {
            // eslint-disable-next-line
                    console.log(error);
          });
      } else {
        this.msg = 'All fields must be present';
      }
    },
  },
  components: {
    navbar: Navbar,
  },
};
</script>
