---
layout: page
title: Privacy Policy
background: grey
---

<div class="col-lg-12 text-center" style="margin-bottom: 60px;">
	<h2 class="section-heading text-uppercase">Privacy Policy</h2>
</div>

<!-- Image addition -->
<div style="overflow: hidden;">
  <img src="/assets/img/gimmick.png" style="max-width: 30%; height: auto; float: right; margin-left: 20px; margin-bottom: 20px;">
  <div style="line-height: 1.75; margin-bottom: 1.5em;">
    <p>
      This Privacy Policy describes how your personal information is collected, used, and shared when you visit {{ site.title }} (the “Site”).
    </p>

    <p>
      <strong>PERSONAL INFORMATION WE COLLECT</strong>
    </p>

    {% if site.analytics.google %}

    <p>
      <strong>Automatically Collected (Google Analytics):</strong>
    </p>

    <p>
      When you visit the Site, we automatically receive information about your device from your browser, such as your IP address. As you browse the Site, we also collect information about how you interact with the Site. We refer to this automatically-collected information as “Device Information”.
    </p>

    <p>
      We collect Device Information using cookies. “Cookies” are data files that are placed on your device. For more information about cookies and how to disable them, visit <a href="http://www.allaboutcookies.org">http://www.allaboutcookies.org</a>.
    </p>

    <p>
      We do this using Google Analytics: <a href="https://www.google.com/intl/en/policies/privacy/">https://www.google.com/intl/en/policies/privacy/</a>.
    </p>

    <p>
      You can opt-out of Google Analytics here: <a href="https://tools.google.com/dlpage/gaoptout">https://tools.google.com/dlpage/gaoptout</a>.
    </p>

    {% else %}

    <p>
      We do not collect any data about you or use any cookies.
    </p>

    {% endif %}

    <p>
      <strong>CHANGES</strong>
    </p>

    <p>
      We may update this privacy policy from time to time for personal, operational, legal, or regulatory reasons.
    </p>

    <p>
      <strong>CONTACT US</strong>
    </p>

    <p>
      For more information about our privacy practices or if you have questions, please contact us by email at <a href="mailto:{{ site.email }}">{{ site.email }}</a>.
    </p>
  </div>
</div>