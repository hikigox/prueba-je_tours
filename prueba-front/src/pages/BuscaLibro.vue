<!-- eslint-disable no-case-declarations -->
<script>
import TableBook from "../components/TableBooks.vue";
import Search from "../components/SearchBar.vue";
const API_URL = "https://openlibrary.org/search.json";

export default {
  components: {
    TableBook,
    Search,
  },
  data() {
    return {
      fetchData: [],
      data: {},
    };
  },
  methods: {
    async handleFetchData(newData) {
      this.data = newData;
      let resolve;
      switch (this.data?.type) {
        case "author":
          console.log("entro a author");

          resolve = (
            await (await fetch(`${API_URL}?author=${this.data.search}`)).json()
          ).docs;

          this.fetchData = resolve;

          break;
        case "title":
          resolve = (
            await (await fetch(`${API_URL}?title=${this.data.search}`)).json()
          ).docs;
          this.fetchData = resolve;
          break;

        default:
          this.fetchData = [];
          break;
      }
    },
  },
};
</script>

<template>
  <h1>Buscar Libros</h1>
  <div>
    <div>
      <Search v-bind:data="data" @update:data="handleFetchData" />
    </div>
    <div>
      <TableBook :resolve="fetchData" />
    </div>
  </div>
</template>

<style scoped>
h1 {
  text-align: center;
}

div {
  display: flex;
  flex-direction: column;
  align-self: center;
}
</style>
