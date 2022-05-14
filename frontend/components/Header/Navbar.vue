<template>
  <div>
    <v-app-bar height="200" dark src="background.jpg">
      <template v-slot:img="{ props }">
        <v-img v-bind="props" />
      </template>
      <div class="flex flex-col items-start w-screen">
        <div class="flex flex-row items-center justify-between">
          <Sidebar />
          <NuxtLink to="/user">
            <img class="h-12 w-12" src="https://cdn.icon-icons.com/icons2/2643/PNG/512/male_boy_person_people_avatar_icon_159358.png" alt="">
          </NuxtLink>
        </div>
        <div class="w-80">
          <v-text-field rounded=true height="50" solo dense label="Pesquisar" light prepend-inner-icon="mdi-magnify" />
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
