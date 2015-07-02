__author__ = 'Alexey Bright'

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.postprocessors import Postprocessor
from markdown.util import etree
import re

# HTML entities placeholders
DOT = '##183;'
EM_SPACE = '##8195;'
UP_ARROW = '##8593;'
DOWN_ARROW = '##8595;'
DOUBLE_ARROW = '##8644;'
RIGHT_ARROW = '##8594;'
PLACEHOLDERS = (DOT, EM_SPACE, UP_ARROW, DOWN_ARROW, DOUBLE_ARROW, RIGHT_ARROW)

# Regex patterns
ZERO_PATTERN = re.compile(r'(\D)0')
CHARGE_PATTERN = re.compile(r'([a-zA-Z\)\]])(\d*[+-])([^\w\(\[]|$)')
MULTIPLIER_PATTERN = re.compile(r'([a-zA-Z\)\]])(\d+)')
ADDITIONAL_PATTERN = re.compile(r'`(\d*[+-])')

TRANSLATE_TABLE = [
    ('^', UP_ARROW),
    ('*', DOT),
    ('!', DOWN_ARROW),
    ('<=>', EM_SPACE + DOUBLE_ARROW + EM_SPACE),
    ('=>', EM_SPACE + RIGHT_ARROW + EM_SPACE),
    ('=', EM_SPACE + '=' + EM_SPACE)]

class IcedPattern(Pattern):

    def handleMatch(self, m):
        expr = m.group(2)
        for (from_s, to_s) in TRANSLATE_TABLE:
            expr = expr.replace(from_s, to_s)
        expr = ZERO_PATTERN.sub(r'\1<sup>0</sup>', expr)
        expr = CHARGE_PATTERN.sub(r'\1<sup>\2</sup>\3', expr)
        expr = MULTIPLIER_PATTERN.sub(r'\1<sub>\2</sub>', expr)
        expr = ADDITIONAL_PATTERN.sub(r'<sup>\1</sup>', expr)

        return etree.fromstring(
            '<span class="iced">%s</span>' % expr.encode('utf-8'))


class IcedPostprocessor(Postprocessor):

    def run(self, text):
        for placeholder in PLACEHOLDERS:
            text = text.replace(placeholder, '&' + placeholder[1:])
        return text


class IcedReplacer(Extension):

    def __init__(self, marker = '\$\$', *args, **kwargs):
        self.iced_block = marker + r'([^\$]+)' + marker
        super(IcedReplacer, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['iced'] = IcedPattern(self.iced_block, self)
        md.postprocessors['iced'] = IcedPostprocessor(self)


def makeExtension(*args, **kwargs):
    return IcedReplacer(*args, **kwargs)
