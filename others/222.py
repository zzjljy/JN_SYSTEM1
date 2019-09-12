#coding=utf-8
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
pdfmetrics.registerFont(TTFont('SimKai', 'SimKai.ttf'))

from reportlab.lib import fonts
fonts.addMapping('SimKai', 0, 0, 'SimKai')


import copy

from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
stylesheet=getSampleStyleSheet()
normalStyle = copy.deepcopy(stylesheet['Normal'])
normalStyle.fontName ='SimKai'
normalStyle.fontSize = 20
s=[['阿', '的']]
story = []
story.append(Paragraph(s, normalStyle))
doc = SimpleDocTemplate('hello.pdf')
doc.build(story)
