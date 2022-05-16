<template>
  <div class="flex">
    <v-app-bar-nav-icon @click.stop="drawer = !drawer" class=""></v-app-bar-nav-icon>
      <v-navigation-drawer v-model="drawer" dark hide-overlay left temporary>
        <div class="">
          <v-list nav dense>
            <v-list-item-group v-model="group"
              v-for="links in linkSidebar" :key="links">
                <v-list-item class="">
                  <v-list-item-title class="">
                    <span class="">
                      <Nuxt-link :to="links.route">
                        {{ links.name }}
                      </Nuxt-link>
                    </span>
                  </v-list-item-title>
                </v-list-item>
                <v-spacer></v-spacer>
              </v-list-item-group>
          </v-list>
        </div>
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
