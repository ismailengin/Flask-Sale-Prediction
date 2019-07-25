import Vue from 'vue';
import Router from 'vue-router';
import Login from './views/Login.vue';
import Register from './views/Register.vue';
import CreateTask from './views/CreateTask.vue';
import Tasks from './views/Tasks.vue';
import Result from './views/Result.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: '/home',
      component: Login,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/createTask',
      name: 'createTask',
      component: CreateTask,
    },
    {
      path: '/tasks',
      name: 'Tasks',
      component: Tasks,
    },
    {
      path: '/result/:id',
      name: 'Result',
      component: Result,
    },
  ],
});
