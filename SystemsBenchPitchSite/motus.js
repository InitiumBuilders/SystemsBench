/* =====================================================================
   Outlier.Systems — MotusViews live counter  (here.now analytics)
   ---------------------------------------------------------------------
   MotusViews = lifetime views of the SystemsBench site, served LIVE from
   here.now's OWN analytics via a same-origin proxy route:

       .herenow/proxy.json   →   GET /api/views
                             →   here.now /api/v1/publishes/<slug>/analytics
                             →   { totals: { allTimeViews } }

   The account Bearer key is injected server-side by the proxy (from the
   HN_ANALYTICS_KEY service variable) and is NEVER shipped to the browser.

   HONESTY-FIRST (the SenseRun integrity rule):
   - Render order:  live (/api/views → totals.allTimeViews)
                    → dated snapshot fallback
                    → "—".  Never fabricate a live digit.
   - "live" is stamped only when the number truly came off live analytics;
     otherwise the stamp reads "as of <date>".

   The relative path "api/views" resolves correctly whether the site is
   served at  grassy-rafter-9cj4.here.now/  or  august.here.now/systemsbench/.
   ===================================================================== */
(function () {
  "use strict";

  var VIEWS_ENDPOINT = "api/views";          // same-origin here.now proxy route

  // Honest dated fallback if the proxy is ever unreachable.
  var SNAPSHOT = { motus: 9, votus: null, asOf: "2026-06-03" };

  var fmt = function (n) {
    if (n === null || n === undefined || isNaN(n)) return null;
    return Number(n).toLocaleString("en-US");
  };

  // animate a number up to its target (earned motion: fires once, on data)
  function countUp(el, target) {
    if (target === null || target === undefined) { el.textContent = "—"; return; }
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion:reduce)").matches;
    if (reduce) { el.textContent = fmt(target); return; }
    // for large counts, start close so the roll feels alive, not glacial
    var start = target > 300 ? Math.floor(target * 0.85) : 0;
    var dur = 1100, t0 = null;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min(1, (ts - t0) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(Math.round(start + (target - start) * eased));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function paint(motus, votus, live, asOf) {
    document.querySelectorAll("[data-motus]").forEach(function (el) {
      var host = el.closest("[data-counter]");
      if (host) host.classList.add(live ? "counter-live" : "counter-snapshot");
      countUp(el, (motus === undefined ? null : motus));
    });
    document.querySelectorAll("[data-votus]").forEach(function (el) {
      if (votus === null || votus === undefined) {
        el.textContent = "—";
        var host = el.closest("[data-counter]");
        if (host) host.setAttribute("title", "VotusViews activates once click-tracking is wired");
      } else {
        countUp(el, votus);
      }
    });
    document.querySelectorAll("[data-counter-stamp]").forEach(function (s) {
      s.textContent = live ? "live" : ("as of " + (asOf || SNAPSHOT.asOf));
    });
  }

  function load() {
    fetch(VIEWS_ENDPOINT, { headers: { "accept": "application/json" }, cache: "no-store" })
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (d) {
        var v = (d && d.totals && typeof d.totals.allTimeViews === "number")
          ? d.totals.allTimeViews : null;
        if (v === null) throw 0;
        paint(v, null, true, null);                 // LIVE
      })
      .catch(function () {
        paint(SNAPSHOT.motus, SNAPSHOT.votus, false, SNAPSHOT.asOf); // antifragile, dated
      });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", load);
  else load();
})();
