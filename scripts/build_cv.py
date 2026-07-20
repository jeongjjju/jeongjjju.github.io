from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/pdf/Aboutme/cv.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN_X = 17 * mm
MARGIN_TOP = 15 * mm
MARGIN_BOTTOM = 14 * mm
BLUE = colors.HexColor("#286A9B")
DARK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#5E6B76")
LIGHT = colors.HexColor("#D9E1E7")

styles = getSampleStyleSheet()
body = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.7,
    leading=12.1,
    textColor=DARK,
    spaceAfter=2.5,
)
small = ParagraphStyle(
    "Small",
    parent=body,
    fontSize=7.8,
    leading=10.4,
    textColor=MUTED,
)
name_style = ParagraphStyle(
    "Name",
    parent=body,
    fontName="Helvetica-Bold",
    fontSize=24,
    leading=27,
    textColor=DARK,
    spaceAfter=2,
)
role_style = ParagraphStyle(
    "Role",
    parent=body,
    fontSize=10.5,
    leading=14,
    textColor=BLUE,
)
section_style = ParagraphStyle(
    "Section",
    parent=body,
    fontName="Helvetica-Bold",
    fontSize=12,
    leading=15,
    textColor=BLUE,
    spaceBefore=7,
    spaceAfter=4,
)
item_title = ParagraphStyle(
    "ItemTitle",
    parent=body,
    fontName="Helvetica-Bold",
    fontSize=9.1,
    leading=12.2,
    spaceAfter=1,
)
date_style = ParagraphStyle(
    "Date",
    parent=small,
    alignment=TA_RIGHT,
    fontName="Helvetica-Oblique",
)
publication_style = ParagraphStyle(
    "Publication",
    parent=body,
    fontSize=8.25,
    leading=11.6,
    leftIndent=0,
    spaceAfter=7,
)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.4)
    canvas.line(MARGIN_X, 10 * mm, PAGE_WIDTH - MARGIN_X, 10 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN_X, 6.5 * mm, "Jeongju Park - Curriculum Vitae")
    canvas.drawRightString(PAGE_WIDTH - MARGIN_X, 6.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def section(title):
    return [
        Spacer(1, 2),
        Paragraph(title, section_style),
        HRFlowable(width="100%", thickness=0.6, color=LIGHT, spaceAfter=5),
    ]


def dated_entry(title, date, subtitle=None, detail=None):
    left = [Paragraph(title, item_title)]
    if subtitle:
        left.append(Paragraph(subtitle, body))
    if detail:
        left.append(Paragraph(detail, small))
    table = Table(
        [[left, Paragraph(date, date_style)]],
        colWidths=[PAGE_WIDTH - 2 * MARGIN_X - 37 * mm, 37 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def pub(authors, title, venue, year, url, award=None):
    award_text = f'<br/><font color="#9A6811"><b>Awards:</b> {award}</font>' if award else ""
    return Paragraph(
        f'<b>{title}</b><br/>'
        f'{authors}<br/>'
        f'<i>{venue}</i>, {year} &nbsp; '
        f'<link href="{url}" color="#286A9B">[Paper]</link>{award_text}',
        publication_style,
    )


story = []

header_left = [
    Paragraph("Jeongju Park", name_style),
    Paragraph("Human-Computer Interaction Researcher", role_style),
]
header_right = Paragraph(
    'Research Associate, HCIS Lab<br/>'
    'Gwangju, Republic of Korea<br/>'
    '<link href="mailto:jeongjupark@gm.gist.ac.kr" color="#286A9B">jeongjupark@gm.gist.ac.kr</link><br/>'
    '<link href="https://jeongjupark.com" color="#286A9B">jeongjupark.com</link> &nbsp;|&nbsp; '
    '<link href="https://scholar.google.com/citations?user=JmRPuDcAAAAJ" color="#286A9B">Google Scholar</link>',
    ParagraphStyle("Contact", parent=small, alignment=TA_RIGHT, leading=11),
)
header = Table(
    [[header_left, header_right]],
    colWidths=[98 * mm, PAGE_WIDTH - 2 * MARGIN_X - 98 * mm],
)
header.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]
    )
)
story.extend([header, Spacer(1, 7), HRFlowable(width="100%", thickness=1.2, color=BLUE)])

story.extend(section("Research Profile"))
story.append(
    Paragraph(
        "My research explores haptic interfaces that connect human sensation with digital environments. "
        "I investigate how interactions in spatial computing can be translated into meaningful tactile "
        "experiences through physical, wearable, and multisensory interfaces.",
        body,
    )
)
story.append(Paragraph("Research interests: Human-Computer Interaction, Haptics, Virtual Reality, Spatial Computing, Multisensory Interaction", small))

story.extend(section("Education"))
story.append(
    dated_entry(
        "Gwangju Institute of Science and Technology (GIST)",
        "Feb. 2024 - Feb. 2026",
        "M.S. in Intelligent Robotics",
        "Human-Centered Intelligent Systems Lab | GPA: 4.0 / 4.5",
    )
)
story.append(
    dated_entry(
        "Chonnam National University",
        "Mar. 2017 - Feb. 2023",
        "B.S. in Electronics and Computer Engineering",
        "Total GPA: 4.08 / 4.5 | Major GPA: 4.10 / 4.5 | Cum Laude",
    )
)

story.extend(section("Research Experience"))
story.append(dated_entry("Research Associate, Human-Centered Intelligent Systems Lab", "Mar. 2026 - Present", "GIST, Gwangju, Republic of Korea"))
story.append(dated_entry("Graduate Researcher, Human-Centered Intelligent Systems Lab", "Feb. 2024 - Feb. 2026", "GIST, Gwangju, Republic of Korea"))
story.append(dated_entry("Research Intern, Human-Centered Intelligent Systems Lab", "Sep. 2023 - Feb. 2024", "GIST, Gwangju, Republic of Korea"))
story.append(dated_entry("Undergraduate Researcher, Visual Information Processing & System Lab", "Sep. 2021 - Feb. 2023", "Chonnam National University, Gwangju, Republic of Korea"))

story.extend(section("Publications"))
story.append(pub(
    "S. Kang, G. Kim, B. Gim, <b>J. Park</b>, J. Um, S. Shin, C. Park, and S. Kim,",
    "When Fingers Become Tools: Rendering Virtual Tool Inertia with a Finger-Mounted Extending Rod",
    "ACM CHI Conference on Human Factors in Computing Systems",
    "2026",
    "https://doi.org/10.1145/3772318.3791755",
))
story.append(pub(
    "S. Kang, G. Kim, B. Gim, <b>J. Park</b>, S. Shin, and S. Kim,",
    "EarPressure VR: Ear Canal Pressure Feedback for Enhancing Environmental Presence in Virtual Reality",
    "ACM Symposium on User Interface Software and Technology (UIST)",
    "2025",
    "https://doi.org/10.1145/3746059.3747618",
))
story.append(pub(
    "D. Yeo, G. Kim, M. Oh, <b>J. Park</b>, B. Gim, S. Kang, A. Elsharkawy, and S. Kim,",
    "AttraCar: Multisensory In-Car VR with Thermal, Airflow, and Motion Feedback through Built-In Vehicle Systems",
    "ACM Symposium on User Interface Software and Technology (UIST)",
    "2025",
    "https://doi.org/10.1145/3746059.3747642",
    "Best Demonstration Award (IEEE ISMAR 2025); People's Choice Best Demo Award (ACM UIST 2025); Demo Honorable Mention Award (ACM UIST 2025)",
))
story.append(pub(
    "B. Gim, S. Kang, D. Yeo, G. Kim, J. Um, <b>J. Park</b>, and S. Kim,",
    "Defying Gravity: Towards Gravitoinertial Retargeting of Acceleration for Virtual Vertical Motion in In-Car VR",
    "IEEE International Symposium on Mixed and Augmented Reality (ISMAR)",
    "2025",
    "https://doi.org/10.1109/ISMAR67309.2025.00019",
))
story.append(pub(
    "Y. Kang, <b>J. Park</b>, S. Hwang, M. Seong, G. Kim, and S. Kim,",
    "You're the One Whom I'm Talking To: The Role of Contextual External Human-Machine Interfaces in Multi-Road User Conflict Scenarios",
    "Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies",
    "2025",
    "https://doi.org/10.1145/3749473",
))
story.append(pub(
    "<b>J. Park</b>, S. Shin, S. Kang, G. Kim, and S. Kim,",
    "Magneto: Enabling Multimodal Haptic Feedback on Paper through Magnetic Fields",
    "CHI Conference Extended Abstracts",
    "2025",
    "https://doi.org/10.1145/3706599.3720242",
))
story.append(pub(
    "S. Hwang, S. Kang, J. Oh, <b>J. Park</b>, S. Shin, Y. Luo, J. DelPreto, W. Matusik, D. Rus, and S. Kim,",
    "TelePulse: Enhancing the Teleoperation Experience through Biomechanical Simulation-Based Electrical Muscle Stimulation in Virtual Reality",
    "ACM CHI Conference on Human Factors in Computing Systems",
    "2025",
    "https://doi.org/10.1145/3706598.3713767",
    "Best Paper Award (Top 1%)",
))
story.append(pub(
    "S. Kang, G. Kim, S. Hwang, <b>J. Park</b>, A. Elsharkawy, and S. Kim,",
    "Flip-Pelt: Motor-Driven Peltier Elements for Rapid Thermal Stimulation and Congruent Pressure Feedback in Virtual Reality",
    "ACM Symposium on User Interface Software and Technology (UIST)",
    "2024",
    "https://doi.org/10.1145/3654777.3676363",
))
story.append(pub(
    "S. Hwang, S. Kang, J. Oh, <b>J. Park</b>, S. Shin, Y. Luo, J. DelPreto, W. Matusik, D. Rus, and S. Kim,",
    "Proposal of a Framework for Enhancing Teleoperation Experience with Biomechanical Simulation-Based Electrical Muscle Stimulation in Virtual Reality",
    "UbiComp/ISWC Companion",
    "2024",
    "https://doi.org/10.1145/3675094.3678380",
))
story.append(pub(
    "S. Kang, G. Kim, S. Hwang, <b>J. Park</b>, A. Elsharkawy, and S. Kim,",
    "Dual-sided Peltier Elements for Rapid Thermal Feedback in Wearables",
    "IEEE ICRA Workshop on Wearable",
    "2024",
    "https://arxiv.org/abs/2405.11807",
))
story.append(pub(
    "J. Kim, <b>J. Park</b>, J. Jeong, and D. Kim,",
    "Finger Language Translation Device",
    "IEIE Summer Annual Conference",
    "2022",
    "https://scholar.google.com/citations?view_op=view_citation&user=JmRPuDcAAAAJ&citation_for_view=JmRPuDcAAAAJ:u-x6o8ySG0sC",
    "Outstanding Student Paper Award",
))

story.extend(section("Honors & Awards"))
awards = [
    ("Best Demonstration Award, IEEE ISMAR", "2025", "AttraCar"),
    ("People's Choice Best Demo Award, ACM UIST", "2025", "AttraCar"),
    ("Demo Honorable Mention Award, ACM UIST", "2025", "AttraCar"),
    ("Best Paper Award (Top 1%), ACM CHI", "2025", "TelePulse"),
    ("Outstanding Student Paper Award, IEIE", "Jul. 2022", "Finger Language Translation Device"),
    ("Full Tuition Scholarship, Chonnam National University", "2017 - 2023", None),
    ("Capstone Design Industry-Academic Cooperation Competition Award", "Dec. 2021", None),
    ("Oasis Hackathon Special Award", "Aug. 2021", None),
    ("Chonnam National University Startup Item Competition", "Dec. 2020", None),
    ("Mock Crowdfunding Competition Award", "Aug. 2020", None),
    ("Crowdfunding Linked Commercialization Competition Award", "Jun. 2020", None),
    ("Student Start-up Promising Team 300", "Aug. 2020", None),
    ("Creative Idea Contest Award", "Feb. 2020", None),
]
for title, date, work in awards:
    detail = f"Associated work: {work}" if work else None
    story.append(dated_entry(title, date, detail=detail))

story.extend(section("Technical Skills"))
story.append(Paragraph("<b>Programming:</b> Python, C#, Unity", body))
story.append(Paragraph("<b>Prototyping & Fabrication:</b> Arduino, 3D printing, laser cutting, CNC machining", body))
story.append(Paragraph("<b>3D Modeling:</b> SolidWorks, Autodesk Inventor, Fusion 360, Blender", body))
story.append(Paragraph("<b>Design & Media:</b> Adobe Illustrator, Photoshop, Premiere Pro, Final Cut Pro", body))

doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=MARGIN_X,
    rightMargin=MARGIN_X,
    topMargin=MARGIN_TOP,
    bottomMargin=MARGIN_BOTTOM,
    title="Jeongju Park - Curriculum Vitae",
    author="Jeongju Park",
)
frame = Frame(
    MARGIN_X,
    MARGIN_BOTTOM,
    PAGE_WIDTH - 2 * MARGIN_X,
    PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM,
    id="main",
    leftPadding=0,
    rightPadding=0,
    topPadding=0,
    bottomPadding=0,
)
doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=footer)])
doc.build(story)
print(OUTPUT)
