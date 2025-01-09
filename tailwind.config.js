module.exports = {
  content: [
    "./templates/**/*.html", 
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        varelaround: ['Varela Round', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ["cupcake"],
  },
}
