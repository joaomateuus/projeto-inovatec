<template>
  <div class="flex flex-col items-center justify-center bg-gray-200 h-fit pt-4">
    <img src="@/static/logo.png"  class="" alt="">
      <div class="flex-col items-center justify-center h-fit w-fit mt-8">
        <h2>De permisão ao navegador para acessar a camera
          <v-icon>mdi-camera</v-icon>
        </h2>
        <Camera />
      </div>
      <div class="flex flex-col items-center justify-center p-4 bg-blue-300 h-96 mt-4 rounded-sm">
        <h1 class="text-xl font-bold mb-2" >Valores Nutricionais</h1>  
        <v-simple-table height="100" class="rounded-md pt-2 pr-2">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">Valor Energetico</th>
              <th class="text-left">Carboidratos</th>
              <th class="text-left">Gorduras Totais</th>
              <th class="text-left">Gorduras Saturadas</th>
              <th class="text-left">Gorduras Trans</th>
              <th class="text-left">Fibra Alimentar</th>
              <th class="text-left">Sódio</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ infoNutri.valorEnergetico }}</td>
              <td>{{ infoNutri.carboidratos }}</td>
              <td>{{ infoNutri.gordurasTotais }}</td>
              <td>{{ infoNutri.gordurasSaturadas }}</td>
              <td>{{ infoNutri.gordurasTrans }}</td>
              <td>{{ infoNutri.fibraAlimentar }}</td>
              <td>{{ infoNutri.sodio }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>  
      <div class="flex-col items-center justify-center border-2 border-black bg-white h-fit w-74 p-4 mt-4 mb-4 rounded-md ">
        <div class="flex">
          <v-icon>mdi-alert</v-icon>
          <h1 class="text-2xl font-bold ml-4">Aviso</h1>
        </div>
        <p class="text-xl text-red-600">Se voce estiver usando IOS (iphone)<br> A camera não está otimizada para o Safari</p>
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
