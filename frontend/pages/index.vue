<template>
  <v-flex xs12 sm8 md4>
    <v-card class="elevation-12">
      <v-toolbar dark color="primary">
        <v-toolbar-title>Login</v-toolbar-title>
      </v-toolbar>
      <v-form @submit.prevent="submit" novalidate>
        <v-card-text>
          <p class="error" v-if="error">{{ error }}</p>
          <v-text-field prepend-icon="person" name="login" label="Login" type="text" v-model="form.username"></v-text-field>
          <v-text-field id="password" prepend-icon="lock" name="password" label="Password" type="password" v-model="form.password"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn type="submit" color="primary">Login</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  middleware: 'auth',
  data: () => ({
    error: null,
    form: {
      username: '',
      password: ''
    }
  }),
  methods: {
    async submit () {
      try {
        await this.$auth.login({ data: this.form })
        if (this.$auth.hasScope('general')) {
          this.$nuxt.$router.push('/general')
        } else if (this.$auth.hasScope('admin')) {
          this.$nuxt.$router.push('/admin')
        }
      } catch (e) {
        this.error = 'Login failed.'
      }
    }
  }
}
</script>
