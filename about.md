---
layout: about
image: /assets/img/me4aboutMe.jpg
description: >
  A boutique Jekyll theme for hackers, nerds, and academics,
  with a focus on personal sites that are meant to impress.
hide_description: true
redirect_from:
  - /download/
---
<style>
img[src*="/assets/img/me4aboutMe.jpg"] {
  width: 240px !important;
  height: 240px !important;
  object-fit: cover !important;
  object-position: center !important;
  border-radius: 10% !important;
  display: block;
  margin: 0 auto;
  transform: scale(1.2);
}
</style>

# About Me

<!--author-->

## Selected Publications
{:.lead}

<style>
  .selected-post-preview {
    display: flex;
    gap: 1.25rem;
    margin-bottom: 2rem;
    align-items: flex-start;
  }

  .selected-post-preview img {
    width: 200px;
    height: 120px;
    object-fit: cover;
    border-radius: 6px;
    flex-shrink: 0;
  }

  .highlight-author {
    font-weight: bold;
    color: #ff6600;
  }

  @media (max-width: 768px) {
    .selected-post-preview {
      flex-direction: column;
    }

    .selected-post-preview img {
      width: 100%;
      height: auto;
    }
  }
</style>

<div class="post-list">
  {% assign selected_posts = site.posts | where_exp: "item", "item.categories contains 'publication'" | slice: 0, 3 %}
  {% for post in selected_posts %}
    <div class="selected-post-preview">
      {% if post.image and post.image.path %}
        <img src="{{ post.image.path }}" alt="Thumbnail for {{ post.title }}">
      {% endif %}
      <div style="flex: 1; min-width: 0;">
        <h4 style="margin: 0 0 0.3rem 0;">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </h4>
        {% assign formatted_authors = post.authors | replace: 'Park, J.', '<span class="highlight-author">Park, J.</span>' %}
        <p class="post-meta" style="color: #aaa; font-size: 0.9rem; margin: 0;">
          {{ formatted_authors }}<br>
          {{ post.conference }}
          {% if post.award %}
            <br>
            {% for a in post.award %}
              🏆 {{ a }}<br>
            {% endfor %}
          {% endif %}
        </p>
      </div>
    </div>
  {% endfor %}
</div>


<p style="text-align: right; margin-top: -0.5rem;">
  <a href="/publication/" style="font-weight: bold; font-size: 0.95rem;">See more →</a>
</p>



## Award & Honors
{:.lead}

1. this list will be replaced by the toc  
{:toc .large-only}

- **Outstanding Student Paper Award at the 2022 Summer Annual Conference**, The Institute of Electronics and Information Engineers, Korea (Jul. 2022)  
- **2021 Capstone Design Industry-Academic Cooperation Competition**, Convergence and Open Sharing System, Korea (Dec. 2021)  
- **Oasis Hackathon Special Award**, Oasis Hackathon Business Team, Korea (Aug. 2021)  
- **The 18th 2020 Chonnam National University Startup Item Competition**, Chonnam National University, Korea (Dec. 2020)  
- **2020 Mock Crowdfunding Competition**, Chonnam National University Start-Up Education Center, Korea (Aug. 2020)  
- **2020 Crowdfunding Linked Commercialization Competition**, Chonnam National University Start-Up Education Center, Korea (Jun. 2020)  
- **2020 Student Start-up Promising Team 300 Selection**, The Ministry of Education, Korea (Aug. 2020)  
- **The 4th 2020 Creative Idea Contest**, Chonnam National University Madulmaru Project Group, Korea (Feb. 2020)  



## Experience
{:.lead}

{:toc}

### ![GIST](/assets/img/GIST.png){:style="height:1.5em; vertical-align:middle;"} Gwangju Institute of Science and Technology
**2023 – Present**  
- **Master of Science (M.S.)**  
  Intelligent Robotics, Institute of Integrated Technology  
- Research Intern & M.S at [HCIS LAB](https://sites.google.com/view/gist-hcis-lab) (Human-Centered Intelligent Systems)  
  - M.S: Feb 2024 – Present  
  - Intern: Sep 2023 – Feb 2024  

---

### ![Madulmaru](/assets/img/mandulmaru.png){:style="height:1.5em; vertical-align:middle;"} Maker Space – Staff & Instructor
**2020 – 2023**  
Worked as a professional equipment manager and instructor at [Madulmaru](http://mandulmaru.net)  
- **Managing**  
  CNC, 3D Printer, UV Printer, Laser Cutter, etc.  
- **Instructing**  
  Arduino, 3D Printer, Laser Cutter  

---

### ![CNU](/assets/img/chonnam.svg){:style="height:1.5em; vertical-align:middle;"} Chonnam National University  
**2017 – 2023**  
- **Bachelor of Science (B.S.)**  
  Department of Electronics & Computer Engineering  
  (TGPA 4.08, Major GPA 4.1)  
- Research assistant student at [VIPS LAB](https://jnuvipslab.wixsite.com/vips)  
  (Visual Information Processing & System)   



## Technical Skills
{:.lead}

{:toc}

- **Modeling & Design Tools**: Autodesk Inventor, Fusion 360, SolidWorks, Blender  
- **Adobe Suite**: Illustrator, Photoshop, Premiere Pro  
- **Video Editing**: Final Cut Pro  
- **Software**: Unity, Python  
