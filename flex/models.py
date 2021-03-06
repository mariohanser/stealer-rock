from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import ( FieldPanel, StreamFieldPanel)
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock
from wagtailmedia.edit_handlers import MediaChooserPanel

from streams import blocks

class FlexPage(Page):
    """Flexible page class"""

    template="flex/flex_page.html"

    content = StreamField(
             [
                 ("title_and_text", blocks.TitleAndTextBlock()),
                 ("full_richtext", blocks.RichtextBlock()),
                 ("cards", blocks.CardBlock()),
                 ("cards_link", blocks.CardBlockLink()),
                 ("media", blocks.TestMediaBlock(icon='media')),
             ],
             null=True,
             blank=True,
            )

    subtitle = models.CharField(max_length=100, null=True, blank=True)
    
    content_panels = Page.content_panels + [
            FieldPanel("subtitle"),
            StreamFieldPanel("content"),
        ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
