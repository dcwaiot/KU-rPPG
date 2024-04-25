# Real-time heart rate prediction using facial images from webcam capturing (2023)
> โครงงานนี้มีวัตถุประสงค์เพื่อทำการศึกษาการวัดค่าอัตราการเต้นของหัวใจจากวิโอใบหน้าแบบไม่สัมผัสโดยใช้เทคนิคที่เรียกว่า remote Photoplethysmography (rPPG)  โดยที่เทคนิคนี้กล้องเว็บแคมจะทำการการบันทึกภาพวิดีโอบริเวณหน้าใบหน้าโดยใช้ Dlib มาช่วยในการประมวลผลหาบริเวณที่เป็นใบหน้า เพื่อนำข้อมูลภาพที่เป็นผลลัพธ์จากการประมวลผลใช้ไปวิเคราะห์หาอัตราการเต้นของหัวใจต่อไป
> [_link_here(https://youtu.be/VAt0u9G9iS0)_] 

## Contents
* [Introduced remote Photoplethysmography (rPPG)](#introduced-remote-photoplethysmography-rppg)
* [Tecnologise Used](#tecnologise-used)
* [Flowchart](#flowchart)
* [Setup](#setup)
* [Contact](#contact)
 


## Introduced remote Photoplethysmography (rPPG) 
- Remote Photoplethysmography (rPPG) เป็นเทคโนโลยีที่ใช้กล้องเว็บแคมในการบันทึกภาพวิดีโอบริเวณหน้าใบหน้าเพื่อทำการวิเคราะห์หาสัญญาณชีพจรเช่น อัตราการเต้นของหัวใจ หรือค่าความดันดลหิต เป็นต้น โดยที่เทคโนโลยีนี้จะพิจารณาภาพจากวีดีโอเที่กล้องเว็บแคมได้ทำการบันบัทึกภาพไว้โดยจะแสดงการเปลี่ยนแปลงเล็กน้อยของสีผิวผิที่ตรวจพบจากภาพของวิดิโอมาวัดชีพจรได้โดยไม่ต้องนำอุปกรณ์สัมผัสกับร่างกายโดยตรง


## Tecnologise Used
- Remote Photoplethysmography 
- Face Detection
    - Dlib Algorithm 
- Signal processing
    - Detrending
    - Interpolation
    - Normalization
    - Band-pass filtering
 
## Flowchart
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://github.com/stpsittiporn/KU-rPPG/blob/stp/2023/img/Picture3.png)


## Setup
1.implementation project
```
pip install -r requirements.txt
```
2.Preparing module
```
pip install -r requirements.txt
```

## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
