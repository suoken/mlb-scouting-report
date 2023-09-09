/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './core/templates/**/*.html'
  ],
  theme: {
    fontFamily: {
      sans: ['IBM Plex Sans', 'sans-serif']
    },
    extend: {
      colors: {
        'tbj-nav':'#204377',
        'tbj-primary':'#244D87',
        'tbj-secondary':'#3E9FCA',
        'tbj-danger':'#842C2E',
        'tbj-offset':'#F7F7F7'
      }
    },
  },
  plugins: [],
}

