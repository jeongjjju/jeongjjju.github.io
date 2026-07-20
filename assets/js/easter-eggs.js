(function () {
  var book = document.querySelector(".book");
  var themeToggle = document.querySelector(".theme-toggle");
  var hapticTrigger = document.querySelector(".haptic-easter-egg");
  var toast = document.querySelector(".easter-egg-toast");
  var toastTimer;
  var pressTimer;
  var longPressTriggered = false;
  var hapticClicks = [];

  if (!book || !toast) return;

  function showToast(message) {
    window.clearTimeout(toastTimer);
    toast.textContent = message;
    toast.classList.add("is-visible");
    toastTimer = window.setTimeout(function () {
      toast.classList.remove("is-visible");
    }, 3200);
  }

  function simulateHaptics() {
    book.classList.remove("egg-shake");
    void book.offsetWidth;
    book.classList.add("egg-shake");
    window.setTimeout(function () {
      book.classList.remove("egg-shake");
    }, 450);

    if (navigator.vibrate) {
      navigator.vibrate([35, 45, 75]);
    }

    showToast("Tactile feedback simulated visually.");
  }

  if (themeToggle) {
    function startLongPress(event) {
      if (event.button !== undefined && event.button !== 0) return;
      longPressTriggered = false;
      window.clearTimeout(pressTimer);
      pressTimer = window.setTimeout(function () {
        longPressTriggered = true;
        simulateHaptics();
      }, 1200);
    }

    function cancelLongPress() {
      window.clearTimeout(pressTimer);
    }

    themeToggle.addEventListener("pointerdown", startLongPress);
    themeToggle.addEventListener("pointerup", cancelLongPress);
    themeToggle.addEventListener("pointercancel", cancelLongPress);
    themeToggle.addEventListener("pointerleave", cancelLongPress);
    themeToggle.addEventListener("contextmenu", function (event) {
      if (longPressTriggered) event.preventDefault();
    });
    themeToggle.addEventListener("click", function (event) {
      if (longPressTriggered) {
        event.preventDefault();
        longPressTriggered = false;
        return;
      }
      window.togglePortfolioTheme();
    });
  }

  if (hapticTrigger) {
    hapticTrigger.addEventListener("click", function () {
      var now = Date.now();
      hapticClicks = hapticClicks.filter(function (time) {
        return now - time < 2600;
      });
      hapticClicks.push(now);

      if (hapticClicks.length >= 5) {
        hapticClicks = [];
        if (navigator.vibrate) navigator.vibrate(45);
        showToast("You found the haptic feedback. Unfortunately, your screen cannot feel it yet.");
      }
    });
  }
})();
