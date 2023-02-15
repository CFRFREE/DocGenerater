from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.shared import RGBColor

with open("/home/free/SourceCode/file.list", "r") as f:
	filelist = f.read().split('\n')
f.close()

doc = Document()
doc.styles['Normal'].font.name = u'consolas-with-Yahei'
doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'consolas-with-Yahei')
doc.styles['Normal'].font.size = Pt(7.5)
doc.styles['Normal'].font.color.rgb = RGBColor(0,0,0)

num = 0
for name in filelist:
	with open(name, 'r') as f:
		content = []
		content.append(r"#" * (len(name) + 6))
		content.append(r"###"+name+r"###")
		content.append(r"#" * (len(name) + 6))
		content.extend(f.read().split('\n'))
		for line in content:
			if len(line):
				par=doc.add_paragraph(line)
				par.paragraph_format.line_spacing = 1
				par.paragraph_format.space_before = 0
				par.paragraph_format.space_after = 0
				num += 1
	f.close()
print(num)
doc.save('/home/free/SourceCode/output.docx')
