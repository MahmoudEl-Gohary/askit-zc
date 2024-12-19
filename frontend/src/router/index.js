import { createRouter, createWebHistory } from 'vue-router'
import Signin from '../views/Signin.vue'
import SignupView from '../views/Signup.vue'
import profile from '../views/profile.vue'
import contact from '@/views/PagesOfHeader/contact.vue'
import features from '@/views/PagesOfHeader/features.vue'
import feed from '@/views/feed.vue'
import terms from '@/views/footer/terms.vue'
import privacy from '@/views/footer/privacy.vue'
import help from '@/views/footer/help.vue'
import Search from '@/views/Search.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: Signin,
    },
    {
      path: '/signin',
      name: 'signin',
      component: Signin,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: profile
    },
    {
      path: '/contact',
      name: 'contact',
      component: contact
    },
    {
      path: '/features',
      name: 'features',
      component: features
    },
    {
      path: '/feed',
      name: 'feed',
      component: feed
    },
    {
      path: '/terms',
      name: 'terms',
      component: terms
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: privacy
    },
    {
      path: '/help',
      name: 'help',
      component: help
    },
    {
      path: '/Search',
      name: 'Search',
      component: Search
    }
  ],
})

export default router
