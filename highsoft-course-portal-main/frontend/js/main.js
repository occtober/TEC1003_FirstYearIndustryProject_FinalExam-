//Modal box logic for quiz steps

// Get modal elements
var modal = document.getElementById("quiz-modal");
var openBtn = document.getElementById("open-quiz-btn");
var closeBtns = document.getElementsByClassName("quiz-question-card__close");
var quizSteps = [
  document.getElementById("quiz-step-1"),
  document.getElementById("quiz-step-2"),
  document.getElementById("quiz-step-3"),
  document.getElementById("quiz-results")
];

// Function to show a specific quiz step
function showStep(stepId) {
  quizSteps.forEach(function(step) {
    step.classList.remove("active");
  });
  var step = document.getElementById(stepId);
  if (step) {
    step.classList.add("active");
  }
}

// Open modal and show first step
openBtn.onclick = function() {
  modal.style.display = "block";
  showStep("quiz-step-1");
};

// Close modal when clicking close buttons
for (var i = 0; i < closeBtns.length; i++) {
  closeBtns[i].onclick = function() {
    modal.style.display = "none";
  };
}

// Close modal when clicking outside of quiz card
modal.addEventListener("click", function(event) {
  if (!event.target.closest('.quiz-question-card')) {
    modal.style.display = "none";
  }
});

// Handle navigation buttons within quiz steps
modal.querySelectorAll('.quiz-question-card__navigation button').forEach(function(button) {
  button.addEventListener('click', function(event) {
    var action = event.currentTarget.dataset.action;
    if (!action) return;

    if (action === 'next') {
      if (event.currentTarget.closest('#quiz-step-1')) {
        showStep('quiz-step-2');
      } else if (event.currentTarget.closest('#quiz-step-2')) {
        showStep('quiz-step-3');
      }
    }

    if (action === 'back') {
      if (event.currentTarget.closest('#quiz-step-2')) {
        showStep('quiz-step-1');
      } else if (event.currentTarget.closest('#quiz-step-3')) {
        showStep('quiz-step-2');
      }
    }

    if (action === 'complete') {
      showStep('quiz-results');
    }

    if (action === 'retake') {
      showStep('quiz-step-1');
    }
  });
});

// Progress bar logic for course progress
document.addEventListener("DOMContentLoaded", () => {
 if (window.COURSE_PROGRESS) {
    const {current, total} = window.COURSE_PROGRESS;
    const percentage = Math.round((current / total) * 100);
    document.getElementById("progress-bar").style.width = `${percentage}%`;
    }
});
