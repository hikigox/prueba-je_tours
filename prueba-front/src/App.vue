<script>
import Buscar from "./pages/BuscaLibro.vue";
import OrderNumbers from "./pages/OrderNumbers.vue";
import NotFound from "./pages/404.vue";

const routes = {
  "/": Buscar,
  "/ordenar": OrderNumbers,
};

export default {
  data() {
    return {
      currentPath: window.location.hash,
    };
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || "/"] || NotFound;
    },
  },
  mounted() {
    window.addEventListener("hashchange", () => {
      this.currentPath = window.location.hash;
    });
  },
};
</script>

<template>
  <div class="container">
    <div class="tags">
      <a href="#/">Buscar Libro</a> <a href="#/ordenar">Ordenamiento</a>
    </div>
    <div>
      <component :is="currentView" />
    </div>
  </div>
</template>

<style scoped>
.tags {
  display: flex;
  gap: 10px;
  align-self: space-between;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
