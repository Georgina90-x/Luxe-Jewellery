

# Testing

Return back to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)

- [Browser Compatibility](#browser-compatibility)

- [Responsiveness](#responsiveness)

- [Accessibility](#accessibility)

- [Defensive Programming](#defensive-programming)

- [Test Driven Development](#test-driven-development)

- [User Story Testing](#user-story-testing)

- [Bugs](#bugs)

</details>

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
The validator picked up the ame error for all pages tested, this is due to using Jinja templating.

| Page | Page URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| add_category | [W3C]() | ![screenshot]() | Notes |
| add_workout| [W3C]() | ![screenshot]() | Notes |
| base | [W3C]() | ![screenshot]() | Notes | Notes |
| edit_category | [W3C]() | ![screenshot]() | Notes |
| edit_workout| [W3C]() | ![screenshot]() | Notes |
| login | [W3C]() | ![screenshot]() | Notes |
| register | [W3C]() | ![screenshot]() | Notes |
| tasks | [W3C]() | ![screenshot]() | Notes |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot]() | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| :---: | :---: | :---: |
| script.js | ![screenshot]() | Notes...|

## Browser Compatibility

I have tested Final Project 4 on the following browsers to check for compatibility issues.

| Browser | Main | Page 1 | Page 2 | Page 3 | Page 4 | Page 5 | Page 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Chrome](https://www.google.com/chrome) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |
| [Firefox](https://www.google.com/firefox) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |
| [Edge](https://www.microsoft.com/en-us/edge/?form=MA13FJ) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |
| [Safari](https://www.apple.com/safari/) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | Works as expected |

## Responsiveness

I have tested my deployed project on multiple devices to check for responsiveness issues.

<details>
<summary>Click for report</summary>

| Device | Main | Page 1 | Page 2 | Page 3 | Page 4 | Page 5 | Page 6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Mobile (iPhone 15 Pro) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No issues |
| Tablet (iPad Air) | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No Issues |
| 13" Macbook Pro| ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No Issues |
| 15" Windows Laptop | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | No Issues |
| Android Phone | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() | ![screenshot]() |  No Issues  |

</details>

## Accessibility

I have tested my deployed project using the [WAVE](https://wave.webaim.org/) web accessibility evaluation tool to check for any accessibility issues.

| Page | Summary | Details | Contrast | Notes |
| :---: | :---: | :---: | :---: | :---: |
| Main | ![screenshot]() | ![screenshot]() | ![screenshot]() | Notes |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

<details>
<summary>Click for report</summary>

| Page | Expectation | Test | Result | Fix | Screenshot |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Main | | | | | |
| | Final Project 4 is expected to have a homepage that shows the workouts added by users that can then be previewed as a dropdown by clicking on them. | Tested this by opening the home page and clicking on the workouts. | The feature behaved as expected.| Test passed. | ![screenshot]() |

</details>

## Test Driven Development

<details>
<summary>Click for report</summary>

| Page | Expectation | Test | Result | Fix | Screenshot |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Main | | | | | |
| | Final Project 4 is expected to have a homepage that shows the workouts added by users that can then be previewed as a dropdown by clicking on them. | Tested this by opening the home page and clicking on the workouts. | The feature behaved as expected.| Test passed. | ![screenshot]() |

</details>

## User Story Testing

| User Story | Screenshot |
| :---: | :---: |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |
| As a new site user, | ![screenshot]() |

## Bugs

The following are bugs that I have come across while creating the Workout site.

- Multiple selection does not autofill. - When editing a workout, the category dropdown should autofill however it did not work.

| Original image | Bug fixed image |
| :---: | :---: |
| ![screenshot]() | ![screenshot]() |

- To fix this...

***

## Unfixed Bugs

| Error | Screenshot | Description |
| :---: | :---: | :---: |
| Error | ![screenshot]() | Description |

There are no remaining bugs that I am aware of.