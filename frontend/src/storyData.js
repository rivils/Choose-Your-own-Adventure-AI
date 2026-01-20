export const story = {
  start: {
    title: "Splash and Dash: A Water Park Adventure",
    text:
      "It's a sunny summer day, and you've just arrived at the Splash and Dash Water Park. Excitement buzzes through the air as people rush toward towering slides and inviting pools.",
    options: [
      { text: "Head to the towering water slides", next: "slides" },
      { text: "Visit the relaxing lazy river", next: "river" },
      { text: "Explore the kids' adventure pool", next: "kids" },
    ],
  },

  slides: {
    text:
      "You climb the tallest slide. Your heart races as you look down. The lifeguard signals it's safe.",
    options: [
      { text: "Go down the slide", next: "slide_end" },
      { text: "Climb back down", next: "start" },
    ],
  },

  river: {
    text:
      "You float peacefully along the lazy river, soaking in the sun and relaxing.",
    options: [
      { text: "Keep floating", next: "river_end" },
      { text: "Exit the river", next: "start" },
    ],
  },

  kids: {
    text:
      "The adventure pool is full of splashes, fountains, and laughter.",
    options: [
      { text: "Join the fun", next: "kids_end" },
      { text: "Go somewhere else", next: "start" },
    ],
  },

  slide_end: {
    text: "You zoom down the slide screaming with joy. Best ride ever!",
    options: [],
  },

  river_end: {
    text: "You feel completely relaxed. A perfect break from the heat.",
    options: [],
  },

  kids_end: {
    text: "You laugh and splash until you're exhausted. What a day!",
    options: [],
  },
};
