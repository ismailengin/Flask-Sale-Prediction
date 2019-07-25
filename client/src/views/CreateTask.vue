<template>
  <div id="container">
     <navbar></navbar>
    <div id="createTask" class="col-sm"> 
        <h1>Create Task</h1>
      <b-form>
        <b-form-group>
        <b-form-input type="text" name="taskName" v-model="input.taskName" placeholder="Task Name" />
        </b-form-group>
        <b-form-group>
        <b-form-file type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </b-form-group>
        <b-form-group>
        <b-form-input type="text" name="predictionStep"
        v-model="input.predictionStep" placeholder="Prediction Step" />
        </b-form-group>
        
        <button type="button" class="btn btn-warning btn-sm" v-on:click="createTask()">Add Task</button>
        <br><br>
        <p1> {{msg}} </p1>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Navbar from '../components/Navbar.vue';

export default {
  name: 'CreateTask',
  data() {
    return {
      input: {
        taskName: '',
        file: '',
        predictionStep: '',
      },
      msg: '',
    };
  },
  methods: {
    createTask() {
      const path = 'http://localhost:5000/createTask';
      if (this.input.taskName !== '' && this.input.predictionStep !== '' && this.input.file !== '') {
        const formData = new FormData();
        formData.append('taskowner', localStorage.username);
        formData.append('taskname', this.input.taskName);
        formData.append('file', this.input.file);
        formData.append('step', this.input.predictionStep);
        axios.post(path, formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }).then((res) => {
          if (res.data.message === 'added') {
            console.log('added');
          }
        }).catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      }
      else {
        this.msg = 'All fields must be present'
      }
    },
    handleFileUpload() {
      this.input.file = this.$refs.file.files[0];

      const file_extension = (this.input.file.name).split('.')[1];
      console.log(file_extension);
      if (file_extension !== 'xlsx' && file_extension !== 'csv') {
        this.msg = 'File extension needs to be .csv or .xlsx';
        this.input.file = ''
      } else {
        this.msg = '';
      }
      // console.log(this.input.file.name);
    },
  },
  components: {
    navbar: Navbar,
  },

};
</script>

<style >
  #createTask{
    padding-left:20px;
    padding-right:20px;
  }
    
</style>
