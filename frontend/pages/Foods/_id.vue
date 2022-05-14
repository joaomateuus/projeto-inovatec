<template>
  <div class="flex flex-col items-center justify-center">
    <h1 class="text-2xl mt-2">Interface realidade aumentada</h1>
    <img class="w-96 h-fit rounded-full mt-2" src="https://st2.depositphotos.com/3957801/5642/i/950/depositphotos_56423065-stock-photo-bacon-burger.jpg" alt="">
    <div class="mt-2">
      <FoodDesc />
    </div>
  </div>
</template>

<script>
import FoodDesc from '../../components/FoodDesc.vue'
export default {
  components: { FoodDesc },
  data: () => ({  
    
  }),
}
</script>

<style>

</style>
