<template>
  <div class="add_citizen_form mt-0">
    <b-form-row no-gutters>
      <b-col cols="auto">
        <label class="add_citizen_form_label">
            Comments:</label>
      </b-col>
      <b-col>
        <b-textarea id="add_citizen_comment_textarea"
                    ref="commentsref"
                    v-model="comments"
                    :rows="2"
                    size="sm"
                    placeholder="add comments here">

        </b-textarea>
      </b-col>
    </b-form-row>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'Comments',

    mounted() {
      this.$root.$on('focuscomments', () => {
        if (this.$refs && this.$refs.commentsref) {
          this.$refs.commentsref.focus()
        }
      })
    },

    computed: {
      ...mapGetters(['form_data']),

      comments: {
        get() { return this.form_data.comments },
        set(value) {
          this.$store.commit('updateAddModalForm',{type: 'comments', value})
        }
      }
    }
  }
</script>
