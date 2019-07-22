<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <table class="table table-hover">
          <thead>
          </thead>
          <tbody>
            <tr v-for="(tasks, index) in tasks" :key="index">
              <td>{{ tasks.taskname }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      token: localStorage.userToken,
      tasks: [],
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/getTasks';
      if(this.token){
        const formData = new FormData();
        formData.append('owner', localStorage.username);
        axios.post(path, formData)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      }
    },
  },
  created() {
    this.getTasks();
  },
};
</script>