todoapp.component('picker', {
  delimiters: ['[[', ']]'],

  template: 
  /*html*/`
  <div v-if="details.show" class="popup">
    <div class="popup-inner">
      <form>
          <label for="title">Title</label>
          <input :value="details.data.title" ref="title" type="text" class="form-control" id="title">
          
          <label for="discreption">Discreption</label>
          <textarea :value="details.data.discreption" ref="discreption" class="form-control" id="discreption" rows="6"></textarea>
          <input :checked="details.data.important" ref="important" id="check" type="checkbox"><label for="check">Important</label>
          <br>
          <button class="btn btn-success" @click.prevent="getformdata">Submit</button>
          <button class="btn btn-danger m-2" @click.prevent="close()">Close</button>
      </form>
    </div>
  </div>
  `,
  data() {
      return {
          form: {
              title: undefined,
              discreption: undefined,
              important: undefined,
          },
      }
  },
  props: {
      details: Object,
      close: Function,
      update: Function
  },

  methods: {
      getformdata() {
          if (this.details.data.title !== this.$refs.title.value) {
              this.form.title = this.$refs.title.value
          }
          if (this.details.data.discreption !== this.$refs.discreption.value) {
              this.form.discreption = this.$refs.discreption.value
          }
          if (this.details.data.important !== this.$refs.important.checked) {
              this.form.important = this.$refs.important.checked
          }
          this.update(this.details.data.id, this.form)


      }
  },
})