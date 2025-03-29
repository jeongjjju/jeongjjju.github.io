---
layout: post
title: Proposal of a Framework for Enhancing Teleoperation Experience with Biomechanical Simulation-Based Electrical Muscle Stimulation in Virtual Reality
description: >
  UbiComp Companion 2024
image:
  path: /assets/img/TeleoperationEMS/ems_system.png
  srcset:
    1920w: /assets/img/TeleoperationEMS/ems_system.png
    960w: /assets/img/TeleoperationEMS/ems_system.png
    480w: /assets/img/TeleoperationEMS/ems_system.png
accent_image: /assets/img/TeleoperationEMS/ems_system.png
excerpt_separator: <!--more-->
sitemap: true
authors: Hwang, S., Kang, S., Oh, J., <strong>Park, J.</strong>, Shin, S., Luo, Y., DelPreto, J., Matusik, W., Rus, D., and Kim, S.
conference: "<strong><em>UbiComp Companion 2024</em></strong>: <em>Companion of the 2024 ACM International Joint Conference on Pervasive and Ubiquitous Computing</em>"
---


## Proposal of a Framework for Enhancing Teleoperation Experience with Biomechanical Simulation-Based Electrical Muscle Stimulation in Virtual Reality

**Title**: Proposal of a Framework for Enhancing Teleoperation Experience with Biomechanical Simulation-Based Electrical Muscle Stimulation in Virtual Reality  
**Authors**: Hwang, S., Kang, S., Oh, J., **Park, J.**, Shin, S., Luo, Y., DelPreto, J., Matusik, W., Rus, D., and Kim, S.  
**Conference**: UbiComp Companion 2024

<!--more-->

---

## ⚙️ Project Overview

This paper proposes a haptic feedback framework for VR-based teleoperation by combining biomechanical simulation and electrical muscle stimulation (EMS). The aim is to reduce cognitive load and improve teleoperation efficiency by simulating joint torque through EMS without using heavy mechanical actuators.

The system is divided into two main parts:  
1) **PhySim**: Simulates the user's biomechanics to estimate required joint torques  
2) **EleStim**: Converts torque into personalized EMS intensity for realistic force feedback

The hardware integrates EMS electrodes with real-time motion capture and physical simulation using Unity and Nvidia PhysX. The device stimulates six muscles on the arm, enabling force feedback from remote manipulators.

---

## 🔬 Key Features

- Personalized torque-intensity calibration per user  
- Biomechanical modeling using OpenSim and MoBL-ARMS  
- Real-time stimulation control over Wi-Fi  
- Delay ~45ms from input to muscle contraction  
- Potential for integration with robotic systems including dogs, drones, and surgical robots

---

## 🔗 Link

Click [here](https://doi.org/10.1145/3675094.3678380) for the official ACM publication.
