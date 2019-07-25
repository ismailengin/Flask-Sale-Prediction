<template>
    <div class="hello">
        <h1>Sales {{ id }}</h1>
        <img :src="`http://localhost:5000/show/${id}`">
        <a style="cursor: pointer; text-decoration: underline" v-on:click="goBack()">Go Back</a>
        <button type="button" class="btn btn-warning btn-sm" v-on:click="download()">Export</button>
    </div>

</template>


<script>
import axios from 'axios';

export default {
  name: 'Result',
  data() {
    return {
      id: 0,
      src: '',
    };
  },
  created() {
    this.id = this.$route.params.id;
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
};
</script>
