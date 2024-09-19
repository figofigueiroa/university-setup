#!/bin/python3
from courses import Courses
from datetime import date


#ALTERAR PARA FORMATAÇÃO DO TYPST
for course in Courses():
        lectures = course.lectures
        course_title = lectures.course.info["title"]
        lines = [
            r'#import "template.typ": *',
            r'#show: template.with(',
            fr' title: [{course_title}],',
            fr' date: {date.today().strftime('%d/%m/%Y')},',
            r'  authors: ((name: "Thiago Figueiroa")),',
            r'  lof: false,',
            r'  lot: false,',
            r'  lol: false,',
            r'  bibliography_file: "refs.bib",',
            r'  paper_size: "a4",',
            r'  cols: 1,',
            r'  text_font: "XCharter",',
            r'  code_font: "Cascadia Mono",',
            r'  accent: "#DC143C", // blue',
            r')',
            fr'// start lectures',
            fr'// end lectures'
            ]
        lectures.master_file.touch()
        lectures.master_file.write_text('\n'.join(lines))
