<template>
  <div class="flex flex-col items-center justify-center bg-gray-200">
    <h1 class="text-2xl mt-4">Interface realidade aumentada</h1>
      <div class="flex items-center justify-center mt-4 bg-black rounded-md h-72 w-96">
        <Camera />
      </div>
    <div class="h-96 w-screen bg-gray-200 p-6 pt-12">
      <v-simple-table height="130" class="rounded-md pt-2 pr-2">
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
