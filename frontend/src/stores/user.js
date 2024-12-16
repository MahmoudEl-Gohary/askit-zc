import { defineStore } from "pinia";
import axios from "axios";
import { c } from "vite/dist/node/types.d-aGj9QkWt";
import { ref } from "vue";

export const useUserStore = defineStore('user', {

    // The state of the store
    state: () => ({
        user: {
            id: null,
            first_name: null,
            last_name: null,
            email: null,
            zc_id: null,
            major: null,
            year: null,
            access: null,
            refresh: null,
            isAuthenticated: false,
        }
    }),

    // Actions of the store
    actions: {
        initStore() {
            console.log('initStore with access: ', localStorage.getItem('user.access'))

            if (localStorage.getItem('user.access')) {
                console.log("User has access...")

                this.user.id = localStorage.getItem('user.id')
                this.user.first_name = localStorage.getItem('user.first_name')
                this.user.last_name = localStorage.getItem('user.last_name')
                this.user.email = localStorage.getItem('user.email')
                this.user.zc_id = localStorage.getItem('user.zc_id')
                this.user.major = localStorage.getItem('user.major')
                this.user.year = localStorage.getItem('user.year')
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.isAuthenticated = true

                this.refreshToken()
                console.log('User has been initialized: ', this.user)
            }
        },

        setToken(data) {
            console.log('setToken: ', data)

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

            console.log('user.access: ', localStorage.getItem('user.access'))
        },

        removeToken() {
            console.log('removing Token...')

            this.user.id = null
            this.user.first_name = null
            this.user.last_name = null
            this.user.email = null
            this.user.zc_id = null
            this.user.major = null
            this.user.year = null
            this.user.access = null
            this.user.refresh = null
            this.user.isAuthenticated = false

            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.first_name', '')
            localStorage.setItem('user.last_name', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.zc_id', '')
            localStorage.setItem('user.major', '')
            localStorage.setItem('user.year', '')
        },

        setUserInfo(user) {
            console.log('setting user infor...')

            this.user.id = user.id
            this.user.first_name = user.first_name
            this.user.last_name = user.last_name
            this.user.email = user.email
            this.user.zc_id = user.zc_id
            this.user.major = user.major
            this.user.year = user.year

            localStorage.setItem('user.id', user.id)
            localStorage.setItem('user.first_name', user.first_name)
            localStorage.setItem('user.last_name', user.last_name)
            localStorage.setItem('user.email', user.email)
            localStorage.setItem('user.zc_id', user.zc_id)
            localStorage.setItem('user.major', user.major)
            localStorage.setItem('user.year', user.year)

            console.log('user: ', this.user)
        },

        refreshToken() {
            axios.post('/api/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    localStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)

                    this.removeToken()
                })
        }
    }
});