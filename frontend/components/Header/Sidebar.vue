<template>
  <div class="">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-spacer></v-spacer>
      <v-navigation-drawer v-model="drawer"
      absolute left temporary 
      rounded
      height="200" width="400">
      <v-list nav dense flat>
        <v-list-item-group v-model="group" 
        v-for="links in linkSidebar" :key="links"
        active-class="deep-purple--text text--accent-4">
          <v-list-item>
            <v-list-item-title>
              <Nuxt-link :to="links.route">
                {{ links.name }}
              </Nuxt-link>
            </v-list-item-title>
          </v-list-item>
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
        name:'Menu', route:'/'
      },
      {
        name:'Sobre', route:'/Sobre'
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
