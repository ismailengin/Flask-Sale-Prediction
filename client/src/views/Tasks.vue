<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-sm" id="tasks">
        <h1>Tasks</h1>
        <table class="table table-hover">
          <thead>
          </thead>
          <tbody>
            <tr v-for="(tasks, index) in tasks" :key="index">
              <td>{{ tasks.taskname }}</td>
              <!--<td>{{startTime}}</td>
              <td>{{endTime}}</td> -->
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm"
                    v-on:click="startPrediction(tasks.id)">Start Task</button>
                  <!---<button type="button" v-if='tasks.predicted' class="btn btn-warning btn-sm"
                    v-on:click="showResult(tasks.id)">Show</button>-->
                    <router-link :to="{ name: 'Result', params: { id: tasks.id, name: tasks.taskname } }"
                      v-if='tasks.predicted' class="btn btn-warning btn-sm" >Show</router-link>
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
import Navbar from '../components/Navbar.vue';

export default {
  data() {
    return {
      token: localStorage.userToken,
      tasks: [],
      startTime: '-',
      endTime: '-',
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/getTasks';
      if (this.token) {
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
    startPrediction(taskid) {
      const today = new Date();
      this.startTime = `${today.getHours()}:${today.getMinutes()}:${today.getSeconds()}`;
      const path = `http://localhost:5000/predict/${taskid}`;
      axios.put(path)
        .then(() => {
          this.getTasks();
          const now = new Date();
          this.endTime = `${now.getHours()}:${now.getMinutes()}:${now.getSeconds()}`;
        })
        .catch((error) => {
          // eslint-disable-next-line
      console.error(error);
        });
      console.log(path);
    },
  },

  components: {
    navbar: Navbar,
  },
  created() {
    this.getTasks();
  },
};
</script>

<style >
  #tasks{
    padding-left:26px;
    padding-right:26px;
  }
    
</style>

