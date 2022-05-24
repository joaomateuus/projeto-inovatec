<template>
  <div class="flex flex-col">
    <v-card class="rounded-md h-fit w-fit mt-4"
    v-for="prato in pratos" :key="prato.id"
    @click="$router.push(`foods/${prato.id}`)">
      <span class="flex flex-row h-fit w-screen p-4">
        <img v-bin :src="`${prato.foto }`" class="h-28 w-36 rounded-full">
        <div class="flex flex-col items-start justify-center pr-2 ml-2">
          <h1 class="text-xl font-bold">{{ prato.nome }}</h1>
          <h1 class="text-xl">{{ prato.detalhes }}</h1>
        </div>
        <h1 class="text-xl font-bold mt-8 text-green-800">R${{ prato.valor }}</h1>
      </span>
    </v-card>
  </div>
</template>

<script>

export default {
  name: 'Lista',
  data: ()=> ({
    categoria: 'Fast-food',
    pratos: [],
    sopa: 'https://img.freepik.com/fotos-gratis/peixe-de-rio-frito-com-alho-e-pimenta_5207-657.jpg',
  }),
  methods: {
    async gettingPratos() {
      try {
        await this.$axios.get('/pratos/').then((response) => {
          this.pratos = response.data;
        })
      } catch (error) {
        console.log(error);
      }
    }
  },
  mounted() {
    this.gettingPratos();
  }
}
</script>

<style />
