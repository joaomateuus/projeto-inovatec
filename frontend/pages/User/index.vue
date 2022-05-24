<template>
    <div class="flex flex-col items-center justify-start">
      <div class="flex flex-col items-center justify-center">
        <div class="flex flex-col w-screen h-56 bg-blue-300 flex items-center justify-center p-4 pt-2">
          <img class="h-32 w-32 border-blue-300" src="https://cdn-icons-png.flaticon.com/512/147/147144.png" alt="">  
          <h2 class="mt-2 text-xl">João Mateus</h2>
          <p class="text-lg">Cliente desde: 12/04/2022</p>
        </div>
        <div class="">
          <v-card class="mx-auto" min-width="400" height="500" tile>
            <v-list flat>
              <v-list-item-group v-model="selectedItem" color="primary">
                <a href="https://sites.google.com/view/modernmenu/p%C3%A1gina-inicial">
                  <v-list-item class="flex">
                    <v-icon>mdi-alert-circle</v-icon>
                    <v-list-item-title class="ml-4">Sobre</v-list-item-title>
                  </v-list-item>
                </a>
                <v-list-item v-for="(item, i) in items" :key="i">
                  <v-list-item-icon>
                    <v-icon v-text="item.icon"></v-icon>
                  </v-list-item-icon>
                  <v-list-item-content class="ml-4">
                    <Nuxt-link :to="item.route">
                      <v-list-item-title v-text="item.text"></v-list-item-title>
                    </Nuxt-link>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: 'index.vue',
    data: () => ({
        selectedItem: 1,
        items: [
          { text: 'Menu', icon: 'mdi-food', route:'/' },
          { text: 'Avaliar', icon: 'mdi-star', route:'/' },
        ],
    }),
}
</script>

<style />
