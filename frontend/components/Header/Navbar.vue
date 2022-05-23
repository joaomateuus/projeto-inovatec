<template>
  <div class="">
    <v-app-bar height="200" dark src="background.jpg">
      <template v-slot:img="{ props }">
        <v-img v-bind="props" />
      </template>
      <div class="flex flex-col items-start justify-center">
        <div class="flex flex-row items-start justify-between w-screen">
          <Sidebar />
          <NuxtLink to="/user">
            <img class="h-12 w-12" src="https://cdn-icons-png.flaticon.com/512/147/147144.png" alt="">
          </NuxtLink>
        </div>
        <div class="ml-2 w-80 mt-6 pt-4">
          <v-text-field rounded="true" height="50" solo dense label="Pesquisar" light prepend-inner-icon="mdi-magnify" />
        </div>
      </div>
      <template v-slot:extension>
        <v-tabs>
          <v-tab @click="$emit('handling-tab1')">Cardapio</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
  </div>
</template>

<script>
import Sidebar from './Sidebar.vue'

export default {
  name: 'Navbar',
  components: { Sidebar },
  emits: ["handling-tab1"],
}
</script>

<style/>
