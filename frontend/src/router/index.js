import { createRouter, createWebHistory } from 'vue-router'
import Signin from '../views/Signin.vue'
import SignupView from '../views/Signup.vue'
import profile from '../views/profile.vue'
import feed from '@/views/feed.vue'
import search from '@/views/Search.vue'
import help from '@/views/footer/help.vue'
import terms from '@/views/footer/terms.vue'
import privacy from '@/views/footer/privacy.vue'
import QuestionView from '@/views/QuestionView.vue'
import AdminDashboard from '@/views/AdminDashboard.vue'

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
      path: '/feed',
      name: 'feed',
      component: feed
    },
    {
      path: '/search',
      name: 'search',
      component: search
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
      path: '/QuestionView:id',
      name: 'QuestionView',
      component: QuestionView
    },
    {
      path: '/AdminDashboard',
      name: 'AdminDashboard',
      component: AdminDashboard
    }
  ],
})

export default router
