<template>
  <div class="">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-spacer></v-spacer>
      <v-navigation-drawer v-model="drawer"
      absolute left temporary 
      class="rounded-sm"
      height="200" width="450">
      <v-list nav dense flat>
        <a href="https://sites.google.com/view/modernmenu/p%C3%A1gina-inicial">
          <v-list-item class="flex">
            <v-icon>mdi-alert-circle</v-icon>
            <v-list-item-title class="ml-4">Sobre</v-list-item-title>
          </v-list-item>
        </a>
        <v-list-item-group v-model="group" 
        v-for="links in linkSidebar" :key="links"
        active-class="deep-purple--text text--accent-4">
          <Nuxt-link :to="links.route">  
            <v-list-item>
              <v-icon v-text="links.icon" />
              <v-list-item-title class="ml-4">
                  {{ links.name }}
              </v-list-item-title>
            </v-list-item>
          </Nuxt-link>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>  
</template>

<script>
export default {
  name: 'Sidebar',
  data: () => ({
    drawer: false,
    group: null,
    linkSidebar: [
      {
        name:'Menu',icon: 'mdi-food', route:'/'
      },
      {
        name:'Perfil',icon: 'mdi-account', route:'/user'
      },
      {
        name:'Avaliar',icon: 'mdi-star', route:'/'
      },
    ]
  }),
  watch: {
    group() {
      this.drawer = false;
    }
  }

}
</script>

<style />
