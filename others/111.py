from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import LongTable, TableStyle, BaseDocTemplate, Frame, PageTemplate
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Table, TableStyle


def reprFrame(frame):
    _dict = vars(frame)
    for key in sorted(list(_dict.keys())):
        print(key, ": ", _dict[key])


def test():
    doc = BaseDocTemplate(
        "question.pdf",
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=50,
        bottomMargin=80,
        showBoundary=False)

    elements = []
    data = [['A', 'B', 'C', '天津市西青区南开和平红桥北辰天津站摩天轮', 'D', 'OBJECTID', 'DYBH'],
        ['00', '0dddddddddddddddddddddddddddddddddddd1', '02', 'fff', '04'],
        ['10', '11', '12', 'dfg', '14'],
        ['20', '21', '22', 'ddddddddddddddddddddddddddddddddddddddddddddddddddddddd23', '24'],
        ]



    tableStyle = [
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]


    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    styleN.wordWrap = 'CJK'

    data2 = [[Paragraph(cell, styleN) for cell in row] for row in data]

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')

    reprFrame(frame)

    colwidths = [frame._width/5. for i in range(7)]

    t = LongTable(data2, colWidths=colwidths)
    t.setStyle(TableStyle(tableStyle))
    elements.append(t)

    template = PageTemplate(id='longtable', frames=frame)
    doc.addPageTemplates([template])
    doc.build(elements)


if __name__ == '__main__':
    test()
