<template>

   <div id="login">
        <p1> {{msg}} </p1>
        <h1>Create Task</h1>
        <input type="text" name="taskName" v-model="input.taskName" placeholder="Task Name" />
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        <input type="text" name="predictionStep"
        v-model="input.predictionStep" placeholder="Prediction Step" />
        <button type="button" v-on:click="createTask()">Register</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateTask',
  data() {
    return {
      input: {
        taskName: '',
        file: '',
        predictionStep: '',
      },
      msg: 'Hallo',
    };
  },
  methods: {
    createTask() {
      this.msg = 'lololo';
      const path = 'http://localhost:5000/createTask';
      if (this.input.taskName !== '' && this.input.predictionStep !== '') {
        const formData = new FormData();
        formData.append('taskname', this.input.taskName);
        formData.append('file', this.input.file);
        formData.append('step', this.input.predictionStep);
        axios.post(path, formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }).then((res) => {
          this.msg = 'posted';
          if (res.data.message === 'added') {
            console.log('added');
          }
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      }
    },
    handleFileUpload() {
      this.input.file = this.$refs.file.files[0];
      console.log(this.input.file);
    },
  },

};
</script>
