<template>
  <div class="flex flex-col items-center justify-center">
    <h1 class="text-2xl mt-2">Interface realidade aumentada</h1>
      <div class="flex items-center justify-center mt-4 bg-blue-300 rounded-md h-72 w-screen">
        <Camera />
      </div>
    <div class="h-80 w-screen bg-gray-300 p-2 rounded-md p-4">
      <div class="flex flex-col items-center justify-center p-2">
        <h1 class="text-2xl">Valor Energetico: {{ infoNutri.valorEnergetico }}</h1>
        <h2 class="text-2xl">Carboidratos: {{ infoNutri.carboidratos }}</h2>
        <h2 class="text-2xl">Gorduras Totais: {{ infoNutri.gordurasTotais }}</h2>
        <h2 class="text-2xl">Gorduras Saturadas:  {{ infoNutri.gordurasSaturadas }}</h2>
        <h2 class="text-2xl">Gorduras Trans:  {{ infoNutri.gordurasTrans }}</h2>
        <h2 class="text-2xl">Fibra Alimentar: {{ infoNutri.fibraAlimentar }}</h2>
        <h2 class="text-2xl">Valor Sódio:  {{ infoNutri.sodio }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import Camera from '../../components/Camera/index.vue'

export default {
  data: () => ({
    infoNutri : [],
    components: {Camera},
  }),
  methods: {
    async gettingNutricionais() {
      try {
        await this.$axios.get(`/pratos/${ this.$route.params.id }`).then((response) => {
          console.log(response);
          this.infoNutri = response.data.nutricional;
        })
      } catch (error) {
        console.log(error);
      }
    }
  },
  mounted() {
    this.gettingNutricionais();
  }
}
</script>

<style>

</style>
