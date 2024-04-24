# rPPG(2023)
> โครงงานนี้มีวัตถุประสงค์เพื่อทำการศึกษาการวัดค่าอัตราการเต้นของหัวใจจากวิโอใบหน้าแบบไม่สัมผัสโดยใช้เทคนิคที่เรียกว่า remote Photoplethysmography (rPPG)  โดยที่เทคนิคนี้กล้องเว็บแคมจะทำการการบันทึกภาพวิดีโอบริเวณหน้าใบหน้าโดยใช้ Dlib มาช่วยในการประมวลผลหาบริเวณที่เป็นใบหน้า เพื่อนำข้อมูลภาพที่เป็นผลลัพธ์จากการประมวลผลใช้ไปวิเคราะห์หาอัตราการเต้นของหัวใจต่อไป
> [_link_here(https://youtu.be/VAt0u9G9iS0)_] 

## Contents
* [Introduced remote Photoplethysmography (rPPG)](#Introduced remote Photoplethysmography (rPPG))
* [Theories Used](#technologies-used)
* [Flowchart](#technologies-used)
* [Setup](#setup)
* [Contact](#contact)



## Introduced remote Photoplethysmography (rPPG) 
- Remote Photoplethysmography (rPPG) เป็นเทคโนโลยีที่ใช้กล้องเว็บแคมในการบันทึกภาพวิดีโอบริเวณหน้าใบหน้าเพื่อทำการวิเคราะห์หาสัญญาณชีพจรเช่น อัตราการเต้นของหัวใจ หรือค่าความดันดลหิต เป็นต้น โดยที่เทคโนโลยีนี้จะพิจารณาภาพจากวีดีโอเที่กล้องเว็บแคมได้ทำการบันบัทึกภาพไว้โดยจะแสดงการเปลี่ยนแปลงเล็กน้อยของสีผิวผิที่ตรวจพบจากภาพของวิดิโอมาวัดชีพจรได้โดยไม่ต้องนำอุปกรณ์สัมผัสกับร่างกายโดยตรง


## Theories Used
- Remote Photoplethysmography 
- Face Detection
- Signal processing
    - Detrending
    - Interpolation
    - Normalization
    - Band-pass filtering

## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
