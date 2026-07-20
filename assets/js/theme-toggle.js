(function () {
  var storageKey = "jj-portfolio-theme";
  var book = document.querySelector(".book");
  var toggle = document.querySelector(".theme-toggle");

  if (!book || !toggle) return;

  function applyTheme(theme) {
    var isDark = theme === "dark";
    book.classList.toggle("theme-dark", isDark);
    book.classList.remove("color-theme-1", "color-theme-2");
    toggle.querySelector("span").textContent = isDark ? "☀" : "☾";
    toggle.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
  }

  var savedTheme = localStorage.getItem(storageKey);
  var initialTheme = savedTheme || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  applyTheme(initialTheme);

  if (window.matchMedia("(max-width: 600px)").matches) {
    window.setTimeout(function () {
      book.classList.remove("with-summary");
    }, 200);
  }

  window.closePortfolioSidebar = function () {
    book.classList.remove("with-summary");
  };

  window.togglePortfolioTheme = function () {
    var nextTheme = book.classList.contains("theme-dark") ? "light" : "dark";
    localStorage.setItem(storageKey, nextTheme);
    applyTheme(nextTheme);
  };
})();
