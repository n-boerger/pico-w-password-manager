/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      backgroundColor: {
        'transparent-200': 'rgba(0, 0, 0, .2)'
      }
    },
  },
  plugins: [],
}
