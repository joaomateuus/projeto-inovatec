<template>
  <div class="flex flex-col">
    <v-card class="rounded-md h-36 w-fit mt-4"
    @click="$router.push(`foods/${burger.id}`)"
    v-for="burger in hamburgueres" :key="burger.nome">
      <span class="flex flex-row h-fit w-screen p-4 ">
        <div class="w-32">
          <img :src="burger.foto" class="h-28 w-46 rounded-md">
        </div>
        <div class="flex flex-col items-center justify-start p-2">
          <h1 class="text-xl font-bold">{{ burger.nome }}</h1>
          <h1 class="text-xl">{{ burger.nota }}</h1>
          <span class="h-8.5 w-28 mt-2 pl-4 font-mono
          rounded-full bg-red-800 text-white text-md">
            {{ categoria }}
          </span>
        </div>
        <h1 class="text-xl font-bold mt-8 text-green-800">R${{ burger.preco }}</h1>
      </span>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'Lista',
  data: ()=> ({
    categoria: 'Fast-food',
    hamburgueres: [
      {
        id: 1, nome: 'Hamburg', nota: '5/5', preco:'23,00', foto:`hamburg/1.jpg`
      },
      {
        id: 2, nome:'Hamburguer', nota: '4/5', preco:'33,00', foto:`hamburg/3.jpg`
      },
      {
        id:3 ,nome: 'Whopper', nota: '3/5', preco:'23,00', foto:`hamburg/1.jpg`
      },
      {
        id: 4 ,nome: 'PAo', nota: '5/5', preco:'33,00', foto:`hamburg/3.jpg`
      },
      {
        id: 5 ,nome: 'Paozin', nota: '5/5', preco:'23,00', foto:`hamburg/1.jpg`
      }
    ],
  }),
}
</script>

<style />
