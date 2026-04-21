## HTML – quick notes for CSS

Just a quick checklist so everything connects nicely 😊 (We hope)

- Remember to link all CSS files in the <head> using <link rel="stylesheet">, for example:
<link rel="stylesheet" href="css/variables.css">
<link rel="stylesheet" href="css/button.css">
Make sure variables.css is loaded first, since the other styles depend on these variables.

- Buttons need both the base class and a variant  
  (example: `button button--primary`, not just `button--primary`)

- Header uses `header__actions`

- Pill buttons use `button button--pill-filter`

- Search should use `.search-bar` with `.input input--search`

- Course cards use `course-card__...` for inner elements

- Avoid inline styles like background--raised, those are already handled in CSS

CSS is built based on the Figma design system (tokens, variables and components) 