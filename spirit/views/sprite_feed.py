#coding:utf-8
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from spirit.models.topic import Topic


class ExtendedRSSFeed(Rss201rev2Feed):
    mime_type = 'application/xml'
    """
    Create a type of RSS feed that has content:encoded elements.
    """
    def root_attributes(self):
        attrs = super(ExtendedRSSFeed, self).root_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        return attrs

    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement(u'content:encoded', item['content_encoded'])


class LatestEntriesFeed(Feed):
    feed_type = ExtendedRSSFeed

    # Elements for the top-level, channel.
    title = u"SwiftChina"
    link = "http://swift.sh"
    author = 'swiftsh'
    description = u"中文Swift社区"

    def items(self):
        return Topic.objects.order_by('-last_active')[:32]

    def item_extra_kwargs(self, item):
        return {'content_encoded': self.item_content_encoded(item)}

    # Elements for each item.
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.comment_set.all()[0].comment

    def item_author_name(self, item):
        if (item.user.get_full_name()):
            return item.user.get_full_name()
        else:
            return item.user

    def item_pubdate(self, item):
        return item.last_active

    def item_content_encoded(self, item):
        return item.comment_set.all()[0].comment_html