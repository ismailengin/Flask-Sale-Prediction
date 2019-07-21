<template>
 <form @submit="createTask">
  <div class="form-group" >
    <label for="taskName">Email address</label>
    <input type="email" class="form-control" id="taskName" placeholder="Task Name">
  </div>
  <div class="form-group">
    <label for="taskFile">Password</label>
    <input type="file" class="form-control" id="taskFile" placeholder="Task File">
  </div>
  <div class="form-group">
    <label for="predictionStep">Prediction Step</label>
    <input type="password" class="form-control" id="predictionStep" placeholder="Prediction Step">
  </div>
  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</template>
