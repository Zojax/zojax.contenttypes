##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface
from zope.app.catalog.interfaces import ICatalogIndex
from zojax.product.utils import unregisterUtility

from interfaces import IContentTypesProduct


class ContentTypesProduct(object):
    interface.implements(IContentTypesProduct)

    def uninstall(self):
        unregisterUtility(
            'contenttypes.newsitem.isNews',
            ((ICatalogIndex, 'contenttypes-isNews'),), 'indexes')
        unregisterUtility(
            'contenttypes.newsitem.newsDate',
            ((ICatalogIndex, 'contenttypes-newsDate'),), 'indexes')
        unregisterUtility(
            'contenttypes.event.isEvent',
            ((ICatalogIndex, 'eventIsEvent'),), 'indexes')
        unregisterUtility(
            'contenttypes.event.startDate',
            ((ICatalogIndex, 'eventStartDate'),), 'indexes')
        unregisterUtility(
            'contenttypes.event.endDate',
            ((ICatalogIndex, 'eventEndDate'),), 'indexes')
        super(ContentTypesProduct, self).uninstall()


class temp(object):
    def __init__(self, context, default=None):
        pass
class IsEvent(temp):
    isEvent = None
class EndDate(temp):
    endDate = None
class StartDate(temp):
    startDate = None
class IsNews(temp):
    isNews = None
class NewsDate(temp):
    newsDate = None
