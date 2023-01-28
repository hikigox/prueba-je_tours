<script lang="ts">
export default {
  data() {
    return {
      numbers: "",
      ordenados: [] as string[],
    };
  },
  methods: {
    ordenar() {
      const data = this.numbers.split(",");
      this.ordenados = data.sort();
    },
  },
};
</script>

<template>
  <div class="container-div">


    <h1>Ordenar Numeros</h1>
    
  <p class="subtitle">
    Ingrese una lista de numeros de la siguiente manera: 1,2,3,5,6.
  </p>
  <div class="container">
    <input v-model="numbers" placeholder="Ingrese la lista de numeros" />
    <button @click="ordenar">Ordenar</button>
  </div>

  <h2>Numeros Ordenados</h2>
  <p>{{ ordenados }}</p>
</div>
</template>

<style scoped>
h1 {
  text-align: center;
  margin: 20px;
}

.subtitle {
  font-weight: bold;
  text-align: center;

  margin: 40px;
}
.container{
  
  display: flex;
  flex-direction: column;
  align-content: center;
  width: 300px;
  margin: 30px;
}
.container-div {

  display: flex;
  flex-direction: column;
  align-items: center;

}

</style>
