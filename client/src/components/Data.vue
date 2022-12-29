<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Lifetime App</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Добавить информацию</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Название</th>
              <th scope="col">Описание</th>
              <th scope="col">Окончание гарантийного срока</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data, index) in data" :key="index">
              <td>{{ data.title }}</td>
              <td>{{ data.author }}</td>
              <td>
                <span v-if="data.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Обновить</button>
                <button type="button" class="btn btn-danger btn-sm">Удалить</button>
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
      data: [],
    };
  },
  methods: {
    getData() {
      const path = 'http://localhost:8080/data';
      axios.get(path)
        .then((res) => {
          this.data = res.data.data;
        })
        .catch((error) => {
          // eslint-disable-next-line no-console
          console.error(error);
        });
    },
  },
  created() {
    this.getData();
  },
};
</script>
