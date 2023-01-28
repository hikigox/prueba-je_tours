<script lang="ts">
export default {
  props: {
    resolve: [] as any,
  },
};
</script>
<template>
  <table>
    <tr>
      <th>Autor</th>
      <th>Libro</th>
    </tr>
    <tr v-bind:key="item.cover_i" v-for="item of resolve">
      <td>{{ item.author_name[0] }}</td>
      <td>{{ item.title }}</td>
    </tr>
  </table>
</template>

<style scoped>
td {
  text-align: center;
}
</style>
