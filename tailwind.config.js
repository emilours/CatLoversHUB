module.exports = {
  content: [
    "./templates/**/*.html", 
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        customBlue: '#1DA1F2',  // Assurez-vous que cette ligne est présente
      },
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
