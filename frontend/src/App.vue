<script>
  import { RouterView } from 'vue-router'
  import axios from 'axios'
  import Toast from '@/components/Toast.vue'
  import { useUserStore } from '@/stores/user'

  export default {
    
      setup() {
          const userStore = useUserStore()

          return {
              userStore
          }
      },

      components: {
          Toast,
      },

      beforeCreate() {
          this.userStore.initStore()

          const token = this.userStore.user.access

          if (token) {
              axios.defaults.headers.common["Authorization"] = "Bearer " + token;
          } else {
              axios.defaults.headers.common["Authorization"] = "";
          }
      }
  }
</script>

<template>
    <main> 
      <RouterView />
    </main>
    <Toast />
</template>

