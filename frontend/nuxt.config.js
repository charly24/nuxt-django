module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'sample',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Nuxt Django Sample' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons' }
    ]
  },
  plugins: [
    '~/plugins/vuetify.js',
    '~/plugins/axios'
  ],
  css: [
    '~/assets/style/app.styl'
  ],
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth'
  ],
  axios: {
    baseURL: 'http://django:8000',
    browserBaseURL: 'http://localhost:8000'
  },
  toast: {
    position: 'center',
    theme: 'bubble'
  },
  auth: {
    fetchUserOnLogin: true,
    strategies: {
      local: {
        endpoints: {
          login: { url: '/api/auth/token/create/', method: 'post', propertyName: 'auth_token' },
          logout: { url: '/api/auth/token/destroy/', method: 'post' },
          user: { url: '/api/auth/me/', propertyName: false },
        },
        tokenType: 'Token',
        tokenName: 'Authorization'
      }
    },
    redirect: {
      login: '/',
      home: '/'
    }
  },
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    extractCSS: true,
    /*
    ** Run ESLint on save
    */
    extend (config, ctx) {
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
