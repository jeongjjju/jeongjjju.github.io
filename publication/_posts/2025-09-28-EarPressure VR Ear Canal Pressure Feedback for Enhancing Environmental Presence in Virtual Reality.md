---
layout: post
title: EarPressure VR Ear Canal Pressure Feedback for Enhancing Environmental Presence in Virtual Reality
featured: true
description: >
  UIST ’25 (The 38th Annual ACM Symposium on User Interface Software and Technology)
image:
  path: /assets/img/EarPressureVR/Teaser.gif
  srcset:
    1920w: /assets/img/EarPressureVR/Teaser.gif
    960w: /assets/img/EarPressureVR/Teaser.gif
    480w: /assets/img/EarPressureVR/Teaser.gif
accent_image: /assets/img/EarPressureVR/Teaser.gif
excerpt_separator: <!--more-->
sitemap: true
authors: "Kang, S., Kim, G., Gim, B., <strong>Park, J.</strong>, Shin, S., and Kim, S."
conference: "<strong><em>UIST ’25</em></strong>: <em>ACM Symposium on User Interface Software and Technology</em>"
---

## EarPressure VR: Ear Canal Pressure Feedback for Enhancing Environmental Presence in Virtual Reality

**Title**: EarPressure VR: Ear Canal Pressure Feedback for Enhancing Environmental Presence in Virtual Reality  
**Authors**: Kang, S., Kim, G., Gim, B., **Park, J.**, Shin, S., and Kim, S.  
**Conference**: UIST ’25: ACM Symposium on User Interface Software and Technology  
<!--more-->

---

## 🎧 Project Overview

EarPressure VR introduces a **novel haptic channel using ear canal pressure modulation** to simulate atmospheric changes and enhance environmental presence in VR.  
The system uses **stepper motor–driven syringes** and **sealed earbuds** to modulate air pressure within a safe range of **±40 hPa**, creating realistic sensations like ear fullness during underwater descent or altitude change.

The system architecture integrates:
- **Pressure modulation unit** with differential sensor feedback (HX710B) and closed-loop PID control.  
- **Custom silicone sealing interface** to ensure airtight coupling for both inward and outward pressure changes.  
- **Wireless control via Arduino** synchronized with virtual events in Unity3D.  

Two key VR scenarios illustrate its effect:
1. **Jaws Cage Survival** – Gradual underwater descent with steadily increasing inward pressure.  
2. **Sorcerer’s Portal Room** – Instant transitions between high- and low-pressure worlds, creating sharp environmental contrast.  

This research demonstrates how **ear canal feedback** can provide a **physically grounded, non-visual cue** that deepens immersion in virtual environments.

---

## 🔗 Links

- **Full Paper (UIST ’25)**: [https://doi.org/10.1145/3746059.3747618](https://doi.org/10.1145/3746059.3747618)  
- **UIST ’25 Demo Paper**: [https://doi.org/10.1145/3746058.3758999](https://doi.org/10.1145/3746058.3758999)
