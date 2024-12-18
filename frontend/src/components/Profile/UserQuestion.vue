<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },



    data() {
        return {
            posts: [],
            user: {
                id: ''
            },
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                    this.can_send_friendship_request = response.data.can_send_friendship_request
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

    }
}
</script>

<template>
  <div class="bg-white rounded-lg shadow p-6">
    <h2 class="text-xl font-bold text-gray-900 mb-4">My Questions</h2>
    <div class="space-y-4">
      <div  v-for="post in posts"
      v-bind:key="post.id
      " class="border-b pb-4 last:border-0">
        <h3 class="text-lg font-semibold text-gray-900">{{ post.title }}</h3>
        <p class="text-gray-600 mt-1">{{ post.body }}</p>
        <div class="flex items-center space-x-4 mt-2 text-sm text-gray-500">
          <span>12 votes</span>
          <span>10 answers</span>
          <span>{{ post.created_at_formated }}</span>
        </div>
      </div>
    </div>
  </div>
</template>