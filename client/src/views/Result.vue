<template>
    <div class="hello">
      <navbar></navbar>
        <h1>Result of {{ name }}</h1>
        <img class="col-sm-12" :src="`http://localhost:5000/show/${id}`">
        <br>
        <a style="cursor: pointer; " class="btn btn-warning btn-sm" v-on:click="goBack()">Go Back</a>
        <button type="button" class="btn btn-warning btn-sm" v-on:click="download()">Export</button>
    </div>

</template>


<script>
import axios from 'axios';
import Navbar from '../components/Navbar.vue'

export default {
  name: 'Result',
  data() {
    return {
      id: 0,
      name: '',
      src: '',
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.name = this.$route.params.name;
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    download() {
      const path = `http://localhost:5000/show/${this.id}`;
      axios({
        url: path,
        method: 'GET',
        responseType: 'blob', // important
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', `${this.id}.png`); // or any other extension
        document.body.appendChild(link);
        link.click();
      });
    },
  },
  components: {
    navbar: Navbar,
  },
};
</script>
