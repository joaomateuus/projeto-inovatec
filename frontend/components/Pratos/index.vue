<template>
  <div class="flex flex-col">
    <v-card class="rounded-md h-36 w-fit mt-4"
    @click="$router.push(`foods/${burger.id}`)">
      <span class="flex flex-row h-fit w-screen p-4"
      v-for="prato in pratos" :key="prato.id">
        <div class="w-32">
          <img src="" class="h-28 w-46 rounded-md">
        </div>
        <div class="flex flex-col items-center justify-start p-2">
          <h1 class="text-xl font-bold">{{ prato.nome }}</h1>
          <h1 class="text-xl">Teste2</h1>
          <span class="h-8.5 w-28 mt-2 pl-4 font-mono
          rounded-full bg-red-800 text-white text-md">
            teste3
          </span>
        </div>
        <h1 class="text-xl font-bold mt-8 text-green-800">R$teste4</h1>
      </span>
    </v-card>
  </div>
</template>

<script>
import pratosService from '../../services/pratosService';

export default {
  name: 'Lista',
  data: ()=> ({
    categoria: 'Fast-food',
    pratos: [],
  }),
  methods: {
    async gettingPratos() {
     await this.$axios.$get('/cardapio')
     .then((response)=>{
       this.pratos = response.data;
       console.log(this.pratos);
     }).catch((error)=>{
       console.log(error);
     })
    }
  },
  mounted() {
    this.gettingPratos();
  }
}
</script>

<style />
