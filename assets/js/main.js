(function () {
  "use strict";

  /* ---------- Header scroll state ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var solidFromStart = header.dataset.solid === "true";
    var onScroll = function () {
      if (solidFromStart) return;
      if (window.scrollY > 40) {
        header.classList.add("is-scrolled");
        header.classList.remove("is-transparent");
      } else {
        header.classList.remove("is-scrolled");
        header.classList.add("is-transparent");
      }
    };
    if (!solidFromStart) {
      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
    }
  }

  /* ---------- Nav discovery hints (bounce/pulse until the visitor notices) ---------- */
  var navHintSeen = false;
  try {
    navHintSeen = localStorage.getItem("cesa_nav_hint_seen") === "1";
  } catch (e) {}
  var markNavHintSeen = function () {
    if (navHintSeen) return;
    navHintSeen = true;
    try {
      localStorage.setItem("cesa_nav_hint_seen", "1");
    } catch (e) {}
    document.querySelectorAll(".hint-bounce, .hint-pulse").forEach(function (el) {
      el.classList.add("is-done");
    });
  };
  if (navHintSeen) {
    document.querySelectorAll(".hint-bounce, .hint-pulse").forEach(function (el) {
      el.classList.add("is-done");
    });
  }

  /* ---------- Desktop mega menu (click fallback for touch) ---------- */
  document.querySelectorAll(".nav-item").forEach(function (item) {
    var link = item.querySelector(".nav-link");
    if (!link || !item.querySelector(".mega")) return;
    item.addEventListener("mouseenter", markNavHintSeen);
    link.addEventListener("click", function (e) {
      markNavHintSeen();
      if (window.matchMedia("(hover: none)").matches) {
        e.preventDefault();
        document.querySelectorAll(".nav-item.is-open").forEach(function (o) {
          if (o !== item) o.classList.remove("is-open");
        });
        item.classList.toggle("is-open");
      }
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav-item")) {
      document.querySelectorAll(".nav-item.is-open").forEach(function (o) {
        o.classList.remove("is-open");
      });
    }
  });

  /* ---------- Mobile drawer ---------- */
  var burger = document.querySelector(".burger");
  var drawer = document.querySelector(".mobile-drawer");
  if (burger && drawer) {
    var closeBtn = drawer.querySelector(".drawer-close");
    var backdrop = drawer.querySelector(".drawer-backdrop");
    var openDrawer = function () {
      drawer.classList.add("is-open");
      document.body.style.overflow = "hidden";
    };
    var closeDrawer = function () {
      drawer.classList.remove("is-open");
      document.body.style.overflow = "";
    };
    burger.addEventListener("click", function () {
      markNavHintSeen();
      openDrawer();
    });
    if (closeBtn) closeBtn.addEventListener("click", closeDrawer);
    if (backdrop) backdrop.addEventListener("click", closeDrawer);
  }

  /* ---------- Back to top ---------- */
  var topBtn = document.querySelector(".fab-top");
  if (topBtn) {
    window.addEventListener(
      "scroll",
      function () {
        topBtn.classList.toggle("is-visible", window.scrollY > 600);
      },
      { passive: true }
    );
    topBtn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry, i) {
          if (entry.isIntersecting) {
            var delay = entry.target.dataset.revealDelay || i * 60;
            setTimeout(function () {
              entry.target.classList.add("in-view");
            }, delay);
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.14, rootMargin: "0px 0px -60px 0px" }
    );
    revealEls.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("in-view");
    });
  }

  /* ---------- Lightbox gallery ---------- */
  var galleryItems = Array.prototype.slice.call(document.querySelectorAll(".gallery .g-item img"));
  if (galleryItems.length) {
    var lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML =
      '<button class="lightbox-close" aria-label="Fermer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
      '<button class="lightbox-nav prev" aria-label="Précédent"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg></button>' +
      '<img src="" alt="">' +
      '<button class="lightbox-nav next" aria-label="Suivant"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector("img");
    var current = 0;

    var show = function (i) {
      current = (i + galleryItems.length) % galleryItems.length;
      lbImg.src = galleryItems[current].currentSrc || galleryItems[current].src;
      lbImg.alt = galleryItems[current].alt || "";
    };
    galleryItems.forEach(function (img, i) {
      img.closest(".g-item").addEventListener("click", function () {
        show(i);
        lb.classList.add("is-open");
        document.body.style.overflow = "hidden";
      });
    });
    var closeLb = function () {
      lb.classList.remove("is-open");
      document.body.style.overflow = "";
    };
    lb.querySelector(".lightbox-close").addEventListener("click", closeLb);
    lb.addEventListener("click", function (e) {
      if (e.target === lb) closeLb();
    });
    lb.querySelector(".prev").addEventListener("click", function () {
      show(current - 1);
    });
    lb.querySelector(".next").addEventListener("click", function () {
      show(current + 1);
    });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") closeLb();
      if (e.key === "ArrowLeft") show(current - 1);
      if (e.key === "ArrowRight") show(current + 1);
    });
  }

  /* ---------- Hero slideshow (homepage) ---------- */
  var slides = document.querySelectorAll(".hero-slide");
  if (slides.length > 1) {
    var idx = 0;
    slides[0].style.opacity = "1";
    setInterval(function () {
      slides[idx].style.opacity = "0";
      idx = (idx + 1) % slides.length;
      slides[idx].style.opacity = "1";
    }, 5000);
  }

  /* ---------- Simple contact/devis form -> WhatsApp/email handoff ---------- */
  document.querySelectorAll("form[data-lead-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (value, key) {
        if (value) lines.push(key + ": " + value);
      });
      var text = encodeURIComponent("Demande depuis cesaecli.com\n" + lines.join("\n"));
      var waNumber = form.dataset.whatsapp || "";
      if (waNumber) {
        window.open("https://wa.me/" + waNumber + "?text=" + text, "_blank");
      } else {
        window.location.href = "mailto:cesa@rtb.bj?subject=Demande%20de%20devis&body=" + text;
      }
    });
  });
})();
