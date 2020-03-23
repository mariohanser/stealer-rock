"""streamfields"""

from django.utils.html import format_html, format_html_join
from django.forms.utils import flatatt

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import URLBlock

from wagtailmedia.blocks import AbstractMediaChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text nothing else"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add yor text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title  & Text"

class RichtextBlock(blocks.RichTextBlock):
    """richtext with all the features"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    class Meta:
        template  = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"

class CardBlock(blocks.StructBlock):
    """Cards with image and text"""
    title = blocks.CharBlock(required=True, help_text="Name")

    cards = blocks.ListBlock(
            blocks.StructBlock(
                [
                    ("image", ImageChooserBlock(required=True)),
                    ("title", blocks.CharBlock(required=True, max_lenght=50)),
                    ("text", blocks.TextBlock(required=True))
                ]
            )
    )

    class Meta:
        template = "streams/card_block.html"
        iocn = "placeholder"
        label = "Staff Cards"

class CardBlockLink(blocks.StructBlock):
    """Cards with image and Links"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock(
            blocks.StructBlock(
                [
                    ("image", ImageChooserBlock(required=True)),
                    ("title", blocks.CharBlock(required=True, max_lenght=50)),
                    ("link", blocks.URLBlock(required=True))
                ]
            )
    )

    class Meta:
        template = "streams/card_block_link.html"
        iocn = "placeholder"
        label = "Link Cards"

class TestMediaBlock(AbstractMediaChooserBlock):
    def render_basic(self, value, context=None):
        if not value:
            return ''

        if value.type == 'video':
            player_code = '''
            <div>
                <video width="320" height="240" controls>
                    {0}
                    Your browser does not support the video tag.
                </video>
            </div>
            '''
        else:
            player_code = '''
            <div>
                <audio controls>
                    {0}
                    Your browser does not support the audio element.
                </audio>
            </div>
            '''

        return format_html(player_code, format_html_join(
            '\n', "<source{0}>",
            [[flatatt(s)] for s in value.sources]
        ))
