// import details from "./details"

let todoapp = Vue.createApp({
    delimiters: ['[[', ']]'],

    data() {
        return {
            form: {
                title: "",
                discreption: "",
                important: false,
                user: null
            },
            tasks: "",
            details: {
                show: null,
                data: null
            }
        }
    },

    methods: {
        submitForm() {
            axios.post(`http://127.0.0.1:8000/api/todo/user/${this.form.user}`, this.form)
                .then((res) => {
                    this.getUnits();
                    this.form.discreption = "";
                    this.form.title = "";
                    this.form.important = false;

                })
                .catch((error) => {
                    console.log(error)
                })
        },
        getUnits() {
            axios.get(`http://127.0.0.1:8000/api/todo/user/${this.form.user}`)
                .then((res) => {
                    this.tasks = res.data
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        dltbtn(id) {
            axios.delete(`http://127.0.0.1:8000/api/todo/${id}`)
                .then((res) => {
                    this.getUnits()
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        showdetails(id) {
            axios.get(`http://127.0.0.1:8000/api/todo/${id}`)
                .then((res) => {
                    this.details.show = true
                    this.details.data = res.data;
                })
                .catch((error) => {
                    console.log(error);
                    closedetails()
                })

        },
        updatedetails(id, datas) {
            axios.patch(`http://127.0.0.1:8000/api/todo/${id}`, datas)
                .then((res) => {
                    this.getUnits()
                    this.closedetails()
                })
                .catch((error) => {
                    console.log(error);
                })

        },
        closedetails() {
            this.details.show = false
            this.details.data = null

        }
    },
    mounted() {
        this.form.user = this.$refs.userid.value
        this.getUnits();
    },
})


