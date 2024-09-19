#import "../template.typ": *
#show: template.with(
 title: [AREA1],
 date: 18/09/2024,
  authors: ((name: "Thiago Figueiroa")),
  lof: false,
  lot: false,
  lol: false,
  bibliography_file: "refs.bib",
  paper_size: "a4",
  cols: 1,
  text_font: "XCharter",
  code_font: "Cascadia Mono",
  accent: "#DC143C", // blue
)
// start lectures
    #include "lec_01.typ"
    #include "lec_02.typ"
// end lectures
