<script lang="ts">
export interface FormatData {
  type: string;
  search: string;
}

export default {
  data() {
    return {
      data: {
        type: "",
        search: "",
      } as FormatData,
    };
  },

  methods: {
    fetchData() {
      console.log("Entro al fetch de searchbar");

      this.$emit("update:data", this.data);
    },
  },
};
</script>

<template>
  <div class="container">
    <div class="container-select">
      <select v-model="data.type">
        <option selected hidden value="">Seleccione un tipo de busqueda</option>
        <option value="author">Autor</option>
        <option value="title">Titulo libro</option>
      </select>
      <input v-model="data.search" placeholder="Ingrese palabra clave" />
    </div>
    <button @click="fetchData">Buscar</button>
  </div>
</template>

<style scoped>
.container {
  width: 300px;
  display: flex;
  gap: 10px;
  flex-direction: column;
}
button {
    align-self: center;
    width: 100px;
}
.container-select {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
</style>
