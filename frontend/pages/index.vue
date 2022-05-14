<template>
  <div>
    <Navbar @handling-tab1="tab1 = true" />
    <div class="p-2">
      <h1 class="text-4xl mt-4 ml-2">Pratos</h1>
      <div class="mt-4">
        <Pratos v-show="tab1" />
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Header/Navbar.vue'
import Pratos from '../components/Pratos/index.vue'

export default {
  name: 'IndexPage',
  components: { Navbar, Pratos },
  data: () => ({
    tab1: true,
  }),
}
</script>

<style />
